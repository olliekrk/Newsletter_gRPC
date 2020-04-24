from __future__ import print_function

import logging
import threading
import time

import backoff
import grpc

import newsletter_pb2 as news
import newsletter_pb2_grpc as news_grpc

VALID_TYPES = ["FORECAST", "ARTICLE", "DOCUMENTARY"]
SAVED_REQUESTS = []


class GrpcUnavailable(Exception):
    pass


def requests_generator():
    yield from SAVED_REQUESTS
    while True:
        request_type = input("Enter type {}:".format(str(VALID_TYPES))).upper()
        if request_type in VALID_TYPES:
            request_phrase = input("Enter search phrase: ")
            if request_phrase is not "":
                request = news.NewsRequest(type=request_type, searchPhrase=request_phrase)
                SAVED_REQUESTS.append(request)
                yield request
            else:
                print("Blank search phrase is invalid.")
        else:
            print("Unknown type.")


def async_many_news(stub):
    t = threading.Thread(target=subscribe_to_many_news, args=(stub,))
    t.daemon = True
    t.start()


def async_news(stub, request):
    t = threading.Thread(target=subscribe_to_news, args=(stub, request,))
    t.daemon = True
    t.start()


@backoff.on_exception(backoff.fibo, GrpcUnavailable, giveup=lambda e: False)
def subscribe_to_many_news(stub):
    try:
        for singleNews in stub.fetchManyNews(requests_generator()):
            type_name = news.NewsType.Name(singleNews.type)
            print("<%s [MANY]>\n%s" % (type_name, singleNews,))
    except:
        print("Error with bulk subscription.")
        print("Retrying using back-off procedure with: {}".format(str(SAVED_REQUESTS)))
        raise GrpcUnavailable


@backoff.on_exception(backoff.fibo, GrpcUnavailable, giveup=lambda e: False)
def subscribe_to_news(stub, request):
    type_name = news.NewsType.Name(request.type)
    try:
        for singleNews in stub.fetchNews(request):
            print("<%s %s>\n%s" % (type_name, request.searchPhrase, singleNews,))
    except:
        print("Error with for subscription %s %s" % (type_name, request.searchPhrase))
        print("Retrying using back-off procedure.")
        raise GrpcUnavailable


def run():
    mode = None
    while mode not in ["SINGLE", "BULK"]:
        if mode is not None:
            print("Invalid value.")
        mode = input("Select mode:\n"
                     "SINGLE (new subscription per each request)\n"
                     "BULK (single subscription for all "
                     "requests):\n").upper()

    with grpc.insecure_channel('localhost:9002') as channel:
        stub = news_grpc.NewsletterServiceStub(channel)

        if mode == "SINGLE":
            # single subscription
            for request in requests_generator():
                async_news(stub, request)
        elif mode == "BULK":
            # bulk subscription
            async_many_news(stub)

        while True:
            time.sleep(1)


if __name__ == '__main__':
    logging.basicConfig()
    run()

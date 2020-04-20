from __future__ import print_function

import logging
import time
import grpc
import threading

import newsletter_pb2_grpc as news_grpc
import newsletter_pb2 as news

VALID_TYPES = ["FORECAST", "ARTICLE", "DOCUMENTARY"]


def new_task(stub, request):
    t = threading.Thread(target=subscribe_to_news, args=(stub, request,))
    t.start()


def subscribe_to_news(stub, request):
    type_name = news.NewsType.Name(request.type)
    try:
        for singleNews in stub.fetchNews(request):
            print("%s %s: %s" % (type_name, request.searchPhrase, singleNews.content))
    except:
        print("Error with for subscription %s %s" % (type_name, request.searchPhrase))
        print("Retrying after 2 sec")
        time.sleep(2)
        new_task(stub, request)


def run():
    with grpc.insecure_channel('localhost:9002') as channel:
        stub = news_grpc.NewsletterServiceStub(channel)
        while True:
            request_type = input("Enter type: ")
            if request_type in VALID_TYPES:
                request_phrase = input("Search phrase: ")
                request = news.NewsRequest(type=request_type, searchPhrase=request_phrase)
                new_task(stub, request)
            else:
                print("Unknown type.")


if __name__ == '__main__':
    logging.basicConfig()
    run()

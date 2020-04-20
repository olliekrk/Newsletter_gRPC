package com.olliekrk.newsletter;

import com.olliekrk.newsletter.rx.NotifyingSubscriber;
import com.olliekrk.newsletter.rx.RequestObserver;
import io.grpc.stub.ServerCallStreamObserver;
import io.grpc.stub.StreamObserver;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@RequiredArgsConstructor
public class NewsletterService extends NewsletterServiceGrpc.NewsletterServiceImplBase {

    private final NewsGenerator generator;

    @Override
    public void fetchNews(NewsRequest request, StreamObserver<News> responseObserver) {
        log.info("Subscription for news: " + request.toString());
        generator.getNews(request).subscribe(
                responseObserver::onNext,
                responseObserver::onError,
                responseObserver::onCompleted
        );
    }

    @Override
    public StreamObserver<NewsRequest> fetchManyNews(StreamObserver<News> responseObserver) {
        log.info("Bulk subscription");
        var newsObserver = (ServerCallStreamObserver<News>) responseObserver;
        var newsRequestObserver = new RequestObserver<NewsRequest>();
        newsRequestObserver
                .flatMap(generator::getNews)
                .subscribe(new NotifyingSubscriber<>(newsObserver));
        return newsRequestObserver;
    }
}

package com.olliekrk.newsletter;

import io.grpc.stub.StreamObserver;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@RequiredArgsConstructor
public class NewsletterService extends NewsletterServiceGrpc.NewsletterServiceImplBase {

    private final NewsGenerator generator;

    @Override
    public void fetchNews(NewsRequest request, StreamObserver<News> responseObserver) {
        log.info("Subscribing for news: " + request.toString());
        generator.getNews(request).subscribe(
                responseObserver::onNext,
                responseObserver::onError,
                responseObserver::onCompleted
        );
    }
}

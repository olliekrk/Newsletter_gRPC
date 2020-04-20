package com.olliekrk.newsletter.rx;

import io.grpc.stub.ServerCallStreamObserver;
import lombok.RequiredArgsConstructor;
import org.reactivestreams.Subscriber;
import org.reactivestreams.Subscription;

@RequiredArgsConstructor
public class NotifyingSubscriber<T> implements Subscriber<T> {
    private final ServerCallStreamObserver<T> observer;
    private Subscription subscription;

    @Override
    public void onSubscribe(Subscription subscription) {
        this.subscription = subscription;
        observer.setOnCancelHandler(subscription::cancel);
        observer.setOnReadyHandler(() -> subscription.request(1));
    }

    @Override
    public void onNext(T value) {
        observer.onNext(value);
        if (observer.isReady()) {
            subscription.request(1);
        }
    }

    @Override
    public void onError(Throwable t) {
        observer.onError(t);
    }

    @Override
    public void onComplete() {
        observer.onCompleted();
    }
}

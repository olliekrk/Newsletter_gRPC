package com.olliekrk.newsletter.rx;

import io.grpc.stub.StreamObserver;
import io.reactivex.Flowable;
import io.reactivex.processors.FlowableProcessor;
import io.reactivex.processors.PublishProcessor;
import org.reactivestreams.Subscriber;

/**
 * Just a wrapper class to get io.grpc to io.reactivex compatibility.
 */
public class RequestObserver<T> extends Flowable<T> implements StreamObserver<T> {
    private final FlowableProcessor<T> processor = PublishProcessor.create();

    @Override
    protected void subscribeActual(Subscriber<? super T> s) {
        processor.subscribe(s);
    }

    @Override
    public void onNext(T value) {
        processor.onNext(value);
    }

    @Override
    public void onError(Throwable t) {
        processor.onError(t);
    }

    @Override
    public void onCompleted() {
        processor.onComplete();
    }
}

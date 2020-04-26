package com.olliekrk.newsletter.rx;

import io.grpc.stub.StreamObserver;
import io.reactivex.Flowable;
import io.reactivex.exceptions.UndeliverableException;
import io.reactivex.processors.FlowableProcessor;
import io.reactivex.processors.UnicastProcessor;
import lombok.extern.slf4j.Slf4j;
import org.reactivestreams.Subscriber;

/**
 * Just a wrapper class to get io.grpc to io.reactivex compatibility.
 */
@Slf4j
public class RequestObserver<T> extends Flowable<T> implements StreamObserver<T> {
    private final FlowableProcessor<T> processor = UnicastProcessor.create();

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

package com.olliekrk;

import com.olliekrk.newsletter.NewsGenerator;
import com.olliekrk.newsletter.NewsletterService;
import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.StatusRuntimeException;
import io.reactivex.exceptions.UndeliverableException;
import io.reactivex.plugins.RxJavaPlugins;
import lombok.extern.slf4j.Slf4j;

import java.io.IOException;

@Slf4j
public class GRpcServer {
    public static final int SERVER_PORT = 9002;

    public static void main(String[] args) throws InterruptedException, IOException {
        RxJavaPlugins.setErrorHandler(e -> {
            if (e instanceof StatusRuntimeException || e instanceof UndeliverableException)
                log.error("Client must have lost its connection.");
            else
                log.error("Error has occurred: " + e.getMessage());
        });

        var generator = new NewsGenerator();
        Server server = ServerBuilder
                .forPort(SERVER_PORT)
                .addService(new NewsletterService(generator))
                .build();

        server.start();
        log.info("Started gRPC server. Port: " + SERVER_PORT);

        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            log.info("Shutting down gRPC server.");
            server.shutdown();
            log.info("Shutdown completed.");
        }));

        server.awaitTermination();
    }
}

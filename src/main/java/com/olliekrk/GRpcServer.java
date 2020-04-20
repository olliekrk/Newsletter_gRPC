package com.olliekrk;

import com.olliekrk.newsletter.NewsGenerator;
import com.olliekrk.newsletter.NewsletterService;
import io.grpc.Server;
import io.grpc.ServerBuilder;
import lombok.extern.slf4j.Slf4j;

import java.io.IOException;

@Slf4j
public class GRpcServer {
    public static final int SERVER_PORT = 9002;

    public static void main(String[] args) throws InterruptedException, IOException {
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

package com.olliekrk.newsletter;

import com.github.javafaker.Faker;
import io.reactivex.Observable;
import io.reactivex.subjects.PublishSubject;
import lombok.extern.slf4j.Slf4j;

import java.util.Random;
import java.util.concurrent.TimeUnit;
import java.util.stream.Stream;

@Slf4j
public class NewsGenerator {
    private static final int COMMENTS_PER_NEWS = 3;
    private static final Faker faker = Faker.instance();
    private static final Random random = new Random();
    private final PublishSubject<News> newsSubject;

    public NewsGenerator() {
        newsSubject = Observable.interval(500, TimeUnit.MILLISECONDS)
                .map(__ -> randomNews())
                .doOnEach(news -> log.info("Generated " + news.getValue().getType() + ": " + news.getValue().getContent()))
                .subscribeWith(PublishSubject.create());
    }

    public Observable<News> getNews(NewsRequest request) {
        return newsSubject
                .filter(news -> news.getType().equals(request.getType()))
                .filter(news -> news.getContent().contains(request.getSearchPhrase()));
    }

    public static News randomNews() {
        return News.newBuilder()
                .setType(randomType())
                .setCommentSection(randomComments())
                .setContent(faker.friends().quote())
                .setViews(random.nextLong())
                .build();
    }

    private static NewsType randomType() {
        var values = new NewsType[]{NewsType.FORECAST, NewsType.ARTICLE, NewsType.DOCUMENTARY};
        return values[random.nextInt(values.length)];
    }

    private static CommentSection randomComments() {
        var commentsSection = CommentSection.newBuilder();
        Stream.generate(NewsGenerator::randomComment)
                .limit(COMMENTS_PER_NEWS)
                .forEach(commentsSection::addComments);
        return commentsSection.build();
    }

    private static Comment randomComment() {
        return Comment.newBuilder()
                .setAuthor(faker.superhero().name())
                .setRating(random.nextInt())
                .build();
    }

}

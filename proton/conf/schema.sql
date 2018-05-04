drop table if exists feed;
create table feed (
    id integer primary key autoincrement,
    name varchar(128) NOT NULL,
    feedlink varchar(128) NOT NULL,
    sitelink varchar(128)
);
INSERT INTO "feed" VALUES(1,'xkcd.com','https://xkcd.com/rss.xml','https://xkcd.com');
INSERT INTO "feed" VALUES(3,'NYT > Home Page','http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml','http://www.nytimes.com/pages/index.html?partner=rss&emc=rss');
INSERT INTO "feed" VALUES(4,'Reuters: Top News','http://feeds.reuters.com/reuters/topNews','https://www.reuters.com');
INSERT INTO "feed" VALUES(6,'Hacker News','https://news.ycombinator.com/rss','https://news.ycombinator.com/');

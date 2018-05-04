drop table if exists feed;
create table feed (
    id integer primary key autoincrement,
    name varchar(128) NOT NULL,
    feedlink varchar(128) NOT NULL,
    sitelink varchar(128)
);
INSERT INTO feed(name, feedlink, sitelink) VALUES
    ('testsite1', 'testsite1-feedlink.com', 'testsite1-sitelink.com'),
    ('testsite2', 'testsite2-feedlink.com', 'testsite2-sitelink.com'),
    ('testsite3', 'testsite3-feedlink.com', 'testsite3-sitelink.com');

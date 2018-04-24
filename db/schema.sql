drop table if exists feed;
create table feed (
	id integer primary key autoincrement,
	name varchar(128) NOT NULL,
	feedlink varchar(128) NOT NULL,
	sitelink varchar(128)
);

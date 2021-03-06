drop table if exists posts;
drop table if exists tags;
drop table if exists post_tags;

create table posts (
  id integer primary key autoincrement,
  title text not null,
  content text not null,
  created_at datetime not null,
  updated_at datetime not null
);

create table tags (
  id integer primary key autoincrement,
  tag text not null,
  created_at datetime not null,
  updated_at datetime not null
);

create table post_tags (
  id integer primary key autoincrement,
  post_id integer not null,
  tag_id integer not null,
  foreign key (post_id) references posts(id),
  foreign key (tag_id) references tags(id)
);

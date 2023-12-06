drop schema if exists `iterator-db`;
create schema if not exists `iterator-db`;
use `iterator-db`;

drop table if exists interator;

create table interator (
    state int DEFAULT 0
);

insert into interator (state) values (0);

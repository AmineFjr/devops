drop schema if exists `iterator-db`;
create schema if not exists `iterator-db`;
use `iterator-db`;

drop table if exists interator;

create table iterator (
    state int DEFAULT 0
);

insert into iterator (state) values (0);

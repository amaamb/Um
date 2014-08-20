drop table if exists entries;
create table entries (
    id integer primary key not null,
    title text not null,
    text text not null
    );

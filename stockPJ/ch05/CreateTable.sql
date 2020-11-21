create table if not exists company_info(
    code varchar(20),
    company varchar(40),
    last_update date,
    primary key (code)
);

create table if not exists daily_price(
    code varchar(20),
    date DATE,
    open bigint(20),
    high bigint(20),
    low bigint(20),
    close bigint(20),
    diff bigint(20),
    volume bigint(20),
    primary key (code, date)
);
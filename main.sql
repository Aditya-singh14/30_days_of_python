-- create a table
CREATE TABLE student(
    id integer primary key,
    name varchar(30),
    gender char(1),
    age integer not null
);

-- Add value
insert into student values (1,"aditya","m",20);
insert into student values (2,"Pratyush","m",22);
insert into student values (3,"Rajnish","m",23);
insert into student values (4,"Pallavi","f",25);
insert into student values (5,"Vijiya","f",12);
insert into student values (6,"Khusi","f",17);

-- fetch
 select * from student;

-- truncate table student;
-- select * from student;

-- drop table student;
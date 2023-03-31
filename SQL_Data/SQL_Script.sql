# create, show, use  database
create database aneri;
show databases;
use aneri;

# create table student
create table student(
id int,
username varchar(100));


select * from student;

create table person(
pid int,
pfirstname varchar(100),
plastname varchar(100),
address varchar(100), 
country varchar(30),
mobileno int,
dob date
);

insert into person values (1, 'abc', 'def', 'hjdch', 'Germany', 23564464, '1996-02-22');
insert into person values (2, 'cbc', 'vzf', 'mnop', 'India', 85656564, '1998-05-29');
insert into person values (3, 'dbc', 'eef', 'qrstv', 'Italy', 23964464, '1995-09-12');



drop table person;
select * from person;

create table employee(
eid int,
efirstname varchar(50),
elastname varchar(50),
edepartment varchar(100),
egender varchar(30),
edob date,
esalary int,
ejoiningdate date,
emobileno int,
ecountry varchar(200),
eaddress varchar(200),
emailid varchar(100));

select * from employee;

# create table student
insert into student values (1, 'aneri');
insert into student (username) values ('Mia');

select * from student;
insert into student (id) values (2);

update student set id=2 where username='Mia';

insert into student values(4, 'vera'), (5, ' mars');

select * from student;
update student set username= 'mars' where id=4;

create table student1 (
s_id int,
s_name varchar(100),
primary key(s_id) );

describe student1;
insert into student1 values (1, 'ann');

insert into student1 values (1, 'dse');

alter table student add primary key (id);

describe employee;

update student set username='miaaa' where s_id=2;

select * from student;

create table student1 (
s_id int,
s_name varchar(100),
gender char(1) character set ascii,
primary key(s_id) );

insert into student1 values (1, 'ann', 'f');

select * from student1;

insert into student1 values (1, 'ann', 'ff');

insert into student1 values (2, 'cef', 'm');

show character set;
show character set like 'ascii%';

# 20/02/2023
select '123' * 2;

create table student2 (
s_id int,
s_name varchar(100),
gender char(1) character set ascii,
dob date,
login datetime,
register timestamp
 );

insert into student2 values (1, 'cef', 'm', '1999-04-14', '2022-04-22 11:34:53.44', '2020-03-15 07:31:42.23');
insert into student2 values (2, 'gef', 'f', '1999-04-14', now(), now() );
insert into student2 values (3, 'efg', 'f', '1994-06-11', now(), now() );
insert into student2 values (4, 'hoj', 'm', '1993-06-11', now(), now() );

insert into student2 values (5, 'cee', 'm', '1999-04-14', '2022-04-22 11:34:53.44', '2020-03-15 07:31:42');
insert into student2 values (6, 'fff', 'f', '1999-04-14', now(), now() );

select * from student2;
update student2 set register= '2020-03-15 07:31:42'  where s_id=1;  

# Between Operator
select * from student2 where dob between cast('1990-02-20' as date) and cast('1995-03-15' as date);

select * from student2 where register between '2020-02-25 00:00:00' and '2022-01-15 00:00:00';



SELECT CURRENT_DATE - interval 1 DAY;
SELECT CURRENT_DATE + interval 1 DAY;

create table student3 (
s_id int,
s_name varchar(100),
fees decimal(8,2)
);

insert into student3 values (1, 'ann', 14522.23);
insert into student3 values (2, 'bnn', 14522.234);
insert into student3 values (2, 'bnn', 94862.24);
insert into student3 values (3, 'Mira', 15000.24),
(4, 'Aneri', 15000.24),
(5, 'Joel', 15000.24),
(6, 'Joe', 15000.24),
(7, 'Zoe', 15000.24);

select * from student3;

delete from student3 where s_name= 'bnn';

/* User Commands 
To create user
grant privileges
select user from  mysql user
show grants
*/

# To create a user in database
create user aneritest@localhost identified by 'aneri';

# Grant command is used to access the privileges to the created host
grant all privileges on *.* to aneritest@localhost;

select user from mysql.user;

show grants for aneritest@localhost;

select user,host,account_locked,password_Expired from mysql.user;

select user,host,db,command from information_schema.processlist;

# command is not running needs to research on it
/* update user SET authentication_string = password(aneripatel) where user='aneritest'and host='localhost';
UPDATE user SET authentication_string='Aneri' WHERE user='aneritest@localhost'; 
UPDATE user SET password=password('Aneri1') WHERE user='aneritest'; */


# Creating table from the existing table using create command 
select * from student4;

create table student4 select s_id, s_name from student3;

# Between command 
Select * from student2 
where dob between '1999-04-14' and '1994-06-11';

Select * from student3 
where s_name between 'Aneri' and 'Joe';

Select * from student3 
where s_name not between 'Aneri' and 'Joe';

/* Like command 
'a%' - starts with a,
'%a' - ends with a,
'_n%' - the second letter of name is n,
'a_%_%' - starts with a and atleast 3 character in length,
'a%i' - starts with a and ends with i
% - wild card character any number
_ - only on charcter which I don't know 
*/
Select * from student3 
where s_name like 'a%';


# 21/02/2023

/* Creat table name vehicle 
and inserted values in it */
 create table vehicle(
vehicle_no varchar(20) primary key,
model_name varchar(45),
price decimal(10,2),
sell_price decimal(10,2));


insert into vehicle(vehicle_no,model_name,price,sell_price)
values('ssajd314231','mercedes',276473,18797),
('ssajd3142328438','mercedes1',47647,48797),
('ssajd31423341','mercedes2',67647,98797);

select  * from vehicle;

# the command  is used to see all the types of engine
show engines;

use mysql;
 
select table_name,engine from information_schema.tables
where table_name='vehicle';

use aneri;

# command to change the the type of 'ENGINE' for better performance
alter table vehicle ENGINE='MyISAM';

# we can reverse it back to whicever 'ENGINE' it was before
alter table vehicle ENGINE='InnoDB';

repair table vehicle;
# when there are n number of table we can use quick extended key word for the quicker repair
repair table vehicle quick extended;

show table status;
 
 
 # command is use to add column after particular column
 alter table vehicle 
 add column description varchar(200) not null after vehicle_no;
 
 describe vehicle;
 
 # command is use to add column at starting 
 
 alter table vehicle 
 add column vehicle_lr_no varchar(200) not null first;
 
 alter table vehicle alter description set default 'Car is superb'; 
 
 # to see full column description 
 # collation :- Collation means assigning some order to the characters in an Alphabet, say, ASCII or Unicode etc.
 show full columns from vehicle like 'v%o';
 
 show full columns from vehicle;
 
### rename, change and modify column name and datatype
# Syntax
/*ALTER TABLE table_name
RENAME COLUMN old_name to new_name; */

alter table vehicle 
rename column price to actual_price;

alter table vehicle
modify actual_price decimal(9,2);

# drop command is used to drop the particular column in combination of alter command
alter table vehicle 
drop column description;

### Create view 
create view merci as select vehicle_no, actual_price from vehicle where model_name='mercedes';

select * from merci;

# to lock the actual table we can only view the data cannot update
lock tables vehicle read;

/* In research time unlock */
unlock tables;

alter table vehicle 
modify actual_price decimal(10,2);

# To check the connection_id (It is virtual name of the particular user)
select connection_id();


use aneri;
select * from vehicle;

# 22/02/2023

#Boolean Datatype
# How to check which boolean format it has
select true, false, TRUE, FALSE;

create table student5( s_id int, name varchar(250), pass boolean); 

insert into student5 values(1, 'aneri', true);
insert into student5 values(1, 'Mira', true);
insert into student5 values(3, 'mia', false);

select * from student5;


select * from student5 where pass is true;
select * from student5 where pass != true;

# Use of Any Operator
create table table1(num_value int);
insert into table1(num_value) values (10),(20),(25);
create table table2(num_val int);
insert into table2(num_val) values (20),(7),(10);

select num_val from table2 where num_val = ANY(select num_value from table1);
select num_val from table2 where num_val < ANY(select num_value from table1);



# Exist Operator 
use aneri;
create table employee1 (e_id int not null, name varchar(50));
insert into employee1 values(1, 'Mia'),
(2, 'John'),
(3, 'Victor');
insert into employee1 (e_id) values(4);

UPDATE employee1 SET name = 'Michel' WHERE name = 'John';

create table department (dep_id int not null, dep_name varchar(50), e_id int);
insert into department values(1, 'Calculation', 1),
(2, 'IT', 3);

select name from employee1 where exists (select * from department where employee1.e_id= department.e_id );

/* IN and NOT IN operator use */
select * from employee1 
where e_id not in (select e_id from department);

# IS NULL / IS NOT NULL Operator
select * from employee1 
where name is NOT NULL;

/* STRING COMPARISION STRCMP() 
If string1 = string2, this function returns 0
If string1 < string2, this function returns -1
If string1 > string2, this function returns 1 
 */
select strcmp('aneri', 'dkdkjgk');
select strcmp('aneri', 'AAAAA');

# if 
select if(200>350, 'yes', 'no');
select if(200=200, 'yes', 'no');

# ifnull
select ifnull(null, 5);
select ifnull(null, "sql");

# nullif
select nullif("hello", "helloowww");
select nullif("hello", "hello");


# 23/2/2023

# query using Case
select case 1 when 1 then 'one 'when 2 then 'two' else 'more' end;

select case binary 'B' when 'a' then 1 when 'B' then 2 else 'enjoy' end;

create table result(s_id int not null, name varchar(100), score int);

insert into result values(1, 'aneri', '85'),
(2, 'mark', 39),
(3, 'john', 99),
(4, 'jenny', 79),
(5, 'liza', 55),
(6, 'anna', 56),
(7, 'callum', 69),
(8, 'ivan', 90);

SELECT *,
  CASE
    WHEN score >= 94 THEN "A"
    WHEN score >= 85 THEN "A-"
    WHEN score >= 75 THEN "B+"
    WHEN score >= 70 THEN "B"
    WHEN score >= 65 THEN "B-"
    WHEN score >= 60 THEN "C+"
    WHEN score >= 55 THEN "C"
    WHEN score >= 50 THEN "C-"
    WHEN score >= 45 THEN "D+"
    WHEN score >= 35 THEN "D"
    ELSE "F"
  END AS grade
FROM result;

# Order By with desc
SELECT name,
  CASE
   WHEN score >= 94 THEN "A"
    WHEN score >= 85 THEN "A-"
    WHEN score >= 75 THEN "B+"
    WHEN score >= 70 THEN "B"
    WHEN score >= 65 THEN "B-"
    WHEN score >= 60 THEN "C+"
    WHEN score >= 55 THEN "C"
    WHEN score >= 50 THEN "C-"
    WHEN score >= 45 THEN "D+"
    WHEN score >= 35 THEN "D"
    ELSE "F"
  END AS grade
FROM result
ORDER BY score DESC;


/* Example by mates
select case  when 2<1 then 1 when 3>2 then 2 else 'enjoy' end; 

 SELECT CASE, CASE X is evaluated
 SELECT 
 CASE 3
  WHEN 1 THEN 'one'
  WHEN 2 THEN 'two'
  WHEN 3 THEN 'three'
  ELSE 'more' END;

create table salary(id int primary key, name varchar(255), sex enum("m","f"),salary int);
insert into salary values(1,"A","m",2500),(2,"B","f",1500),(3,"C","m",5500),(4,"D","f",500);
select * from salary;
###SWAP m with F 
#1 possibility
UPDATE salary set sex = if(sex="f","m","f");
#2 possibility
UPDATE salary
    SET sex  = (CASE WHEN sex = 'm' 
        THEN  'f' 
        ELSE 'm' 
        END);
*/

select * from employee1;
select * from department;

/* Joins Query by Jinesh
select distinct o.order_id as OrderNumber, c.customer_name as CustomerName
from order_new o
left outer join customer_new c
on c.customer_id = o.customer_id

select o.order_id as OrderNumber, c.customer_name as CustomerName
from order_new o
left join customer_new c
using (customer_id);

select o.order_id as OrderNumber, c.customer_name as CustomerName
from order_new o
left outer join customer_new c
on c.customer_id = o.customer_id
union
select o.order_id as OrderNumber, c.customer_name as CustomerName
from order_new o
right join customer_new c
using (customer_id);

select  o.order_id as OrderNumber, c.customer_name as CustomerName
from order_new o inner join customer_new c
on c.customer_id = o.customer_id;

select  o.order_id as OrderNumber, c.customer_name as CustomerName
from order_new o cross join customer_new c
on c.customer_id = o.customer_id;
*/
 
# Inner Join

select d.dep_name as DepName, e.name as EmpName
from department d
inner join employee1 e
on e.e_id = d.e_id;

# Inner Join with using keyword
select d.dep_name as DepName, e.name as EmpName
from department d
inner join employee1 e
using (e_id);

# Use of Distinct keyword to retrive distinct values 
select distinct d.dep_name as DepName, e.name as EmpName
from department d
inner join employee1 e
on e.e_id = d.e_id;

# Left join or left outer join
select d.dep_name as DepName, e.name as EmpName
from department d
left outer join employee1 e
using (e_id);

# Right join or Right outer join
select d.dep_name as DepName, e.name as EmpName
from department d
right join employee1 e
using (e_id);

# Cross join
select d.dep_name as DepName, e.name as EmpName
from department d
cross join employee1 e;

# Full outer join IT IS NOT SUPPORTED IN SQL 
select department.dep_name as DepName,  employee1.name as EmpName
from department 
FULL  JOIN employee1 
on  employee1.e_id = department.e_id;

use aneri;

# multi join query
create table student16(id int, name varchar(50),branch varchar(50));
create table marks(id int, marks int);
create table attendance(id int, attendance int);

insert into student16 values(1,'anu','cse');
insert into student16 values(2,'mia','ece');
insert into student16 values(3,'sam','ece');
insert into student16 values(4,'kae','cse');

insert into marks values(1,95);
insert into marks values(2,85);
insert into marks values(3,80);
insert into marks values(4,65);

insert into attendance values(1,75);
insert into attendance values(2,65);
insert into attendance values(3,80);
insert into attendance values(4,80);

select s.id, name, marks, attendance
from student16 as s
inner join
marks as m
on s.id=m.id
inner join
attendance as a
on m.id=a.id
where a.attendance>=75;

# delete the record example
/*delete o,c
from order_new o
inner join customer_new c
on o.customer_id=c.customer_id
where o.order_id is NULL;
*/

# UNION and UNION ALL Condition

create table student14(s_id int not null, s_name varchar(100), age int);
create table teacher(t_id int not null, t_name varchar(100), age int);

insert into student14 values(1, 'anna', 16),
(2, 'bnna', 17),
(3, 'cnna', 15),
(4, 'dnna', 19);

insert into teacher values(1, 'avca', 35),
(2, 'hjma', 45),
(3, 'zyna', 26),
(4, 'dina', 36);


select age
from teacher
union
select age
from student14;

select age
from teacher
union all
select age
from student14;



# Ascending descending example by jinesh
select * from customer_new order by customer_id asc, customer_name desc;

/* Query by Jinesh
	create table employee(eid int, emp_name varchar(250),  income int)
create table employee1(eid int, emp_name varchar(250),  income int, city varchar(236))
insert into employee1 values(1,'asjhdskj',7163,'a'),
(2,'asjhdskj',2734163,'a'),
(3,'asjhdskj',73,'b'),
(4,'asjhdskj',7161233,'a'),
(10,'asjhdskj',716332,'b')

select city,min(income) as "Minimum income"
from employee1
group by city
having min(income)>73 */

create table product (p_id int not null, p_name varchar(200), sup_id int, p_unit int, price decimal(10,2));
insert into product values(1, 'book', 34, 80, 65789.95),
(2, 'sketch', 42, 69, 896789.95),
(3, 'stationary', 38, 90, 965789.95),
(4, 'schoolbag', 64, 100, 321235.55),
(5, 'lunchbox', 98, 200, 569389.95);

# Use of min()
select min(price) as SmallestPrice
from product;

# Use of max()
select p_name, max(p_unit) as No_of_Products
from product;



/* create table emp_business (e_id int, e_name varchar(250), occupation varchar(250),working_date date, working_hours int) 

insert into emp_business values(1,'aksjdhgkjsad','IT_DB',null, 5),
(2,'aksdjdhgkjsad','IT_Com',null, 7),
(3,'aksjdhgkjsad','IT_tech',null, 3),
(4,'aksjdhgkjsad','IT_HR',null, 7),
(5,'aksjdhgkjsad','IT_innovat',null, 6),
(6,'aksjdhgkjsad','IT_resarch',null, 4)

select occupation ,sum(working_hours) as "total working hours" from emp_business group by occupation having sum(working_hours)>6;
select occupation ,avg(working_hours) as "total working hours" from emp_business group by occupation having avg(working_hours)>6;
*/

select p_name, sum(price) as 'TotalAmount' from product group by p_name having sum(price)>65789.95;
select p_name, avg(price) as 'TotalAmount' from product group by p_name having sum(price)>65789.95;

# 24/02/23

select * from employee1;

select * from employee1 where name regexp '^[MV]';

select * from employee1 where name regexp '[an]$';
select * from employee1 where name regexp 'a$';

select * from employee1 where name regexp '^.{3}$';

select * from employee1 where name regexp 'c';

select * from employee1 where name regexp '^[^mv]' and '^[^m^v]';





## Match and check 

select ('B' REGEXP '[A-Z]' ) AND  ('M' REGEXP '[D-Z]' )  AS MATCH_;

select REGEXP_LIKE('a', '[A-Z]', 'i') as CHECK_;


SELECT REGEXP_SUBSTR('Cat Cut Cot', 'C.t', 2) Result;
SELECT REGEXP_SUBSTR('Cat Cut Cot', 'C.t', 1) Result;
SELECT REGEXP_SUBSTR('Cat Cut Cot', 'C.t', 1, 3) Result;

#REGEXP_REPLACE(expr, pat, repl[, pos[, occurrence[, match_type]]])

SELECT REGEXP_REPLACE('abc def ghi jk mn abc def', 'def', 'X', 2, 2);

# Select the price which have 1,2,3 in the figure
select * from product where price regexp '[1-3]';
select * from product where price regexp '^[8]|^[9]';

# INDEX

select * from employee1;

create index name_index on employee1(name);

show index from employee1 where column_name = 'name';

select * from employee1 where name='Mia';


/* code by Jinesh for auto increment
 create table example_temp(id int auto_increment primary key,
name varchar(250) not null,
age int not null)


insert into example_temp(name, age) values('John',25)
insert into example_temp(name, age) values('Jane',30);

# To get the last value inserted 
select last_insert_id()
*/

/* Code by Jinesh on  Partition
create table sales(id int not null auto_increment,
sale_date date not null,
amount DECIMAL(10,2) not null,
PRIMARY KEY(id,sale_date))
partition by range(year(sale_date))
(
partition p0 values less than (2010),
partition p1 values less than (2011),
partition p2 values less than (2012),
partition p3 values less than (2013),
partition p4 values less than (2014),
partition p5 values less than (2015),
partition p6 values less than (2016),
partition p7 values less than (2017),
partition p8 values less than (2018),
partition p9 values less than (2019),
partition p10 values less than MAXVALUE
)
*/

# Copy from one table to another table
insert into sales (id,sale_date,amount)
select id, sale_date,amount from sales_party;

/* Code by Jinesh using Partition with over()
select *, row_number() over (partition by sale_date) as row_num from sales 

create table person (name varchar(45) not null,
product varchar(45),
country varchar(45),
year int)

insert into person(Name,product,country,year)
values('as','asdasd','asdasd',2015),
('as','asdasd','asdasd',2016),
('as','asdasd','asdasd',2017),
('as','asdasd','asdasd',2015),
('as','asdasd','asdasd',2018)
select *, row_number() over (partition by year) as row_num from person
*/

/* Example by mate on Partiotion with over()
CREATE TABLE sales2(
id INT NOT NULL AUTO_INCREMENT,
sale_date DATE NOT NULL,
amount DECIMAL(10,2) NOT NULL,
PRIMARY KEY(id,sale_date));
INSERT INTO sales2 (id, sale_date, amount) VALUES
(1, '2014-11-03', 54353),
(2, '2017-01-04', 2576727),
(3, '2016-08-08', 757654),
(4, '2014-04-06', 324235),
(5, '2023-05-03', 23334),
(6, '2019-12-01', 2342134),
(7, '2020-05-03', 24351534),
(7, '2020-07-12', 2153574),
(7, '2020-09-17', 1121534);
SELECT * from sales2;

SELECT * , ROW_NUMBER() OVER (PARTITION BY YEAR(sale_date)) AS row_num FROM sales2;
*/

 
create table student_score(name varchar(50),score int);

insert into student_score
values ('Alice',90),
('Bob',85),
('carl',75),
('Dave',80),
('eric',90);

select Name, score, rank() OVER (ORDER BY SCORE DESC) AS SCHOOL_RANK from student_score; 

select Name, score, DENSE_rank() OVER (ORDER BY SCORE DESC) AS SCHOOL_RANK from student_score;

select name, score, SCHOOL_RANK, (select name, score, DENSE_rank() OVER (ORDER BY SCORE DESC) AS SCHOOL_RANK from  student_score) from  student_score; # not working

SELECT NAME , SCORE , SCHOOL_RANK FROM (
select Name, score, rank() OVER (ORDER BY SCORE DESC) AS SCHOOL_RANK from student_score ) AS RANKED_SUDENTS WHERE SCHOOL_RANK=3;

use aneri;
SELECT brand_name, COUNT(DISTINCT customer_name)
FROM depositor, account
WHERE depositor.account_number = account.account_number
GROUP BY branch_id



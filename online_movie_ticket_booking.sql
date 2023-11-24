-- Table Creation
create table pes1ug21cs268_289_screens(screen_id int not null primary key,class varchar(10) not null,no_of_seats int);
create table pes1ug21cs268_289_movies(movie_id int not null primary key,movie_name varchar(50) not null,language varchar(20),length int,show_start date,show_end date);
create table pes1ug21cs268_289_price_list(price_id int not null primary key, type int,day varchar(10),price int);
create table pes1ug21cs268_289_shows(show_id int not null primary key, type int,time varchar(10),date date,screen_id int, movie_id int, price_id int,foreign key(movie_id) references pes1ug21cs268_289_movies(movie_id), foreign key(screen_id) references pes1ug21cs268_289_screens(screen_id),foreign key(price_id) references pes1ug21cs268_289_price_list(price_id) on update cascade);
create table pes1ug21cs268_289_booked_tickets(ticket_no int not null, seat_no int not null,show_id int not null,primary key(ticket_no,show_id),foreign key(show_id) references pes1ug21cs268_289_shows(show_id) on delete cascade);
create table pes1ug21cs268_289_user(uname varchar(30),uid int not null primary key,email varchar(20));
create table pes1ug21cs268_289_admin(aid int not null primary key, aname varchar(30),password varchar(30));
create table pes1ug21cs268_289_has_booked(ticket_no int not null,uid int not null.primary key(ticket_no,uid),foreign key(ticket_no) references pes1ug21cs268_289_booked_tickets(ticket_no),foreign key(uid) references pes1ug21cs268_289_user(uid));
create table pes1ug21cs268_289_manages(aid int not null,show_id int not null,primary key(aid,show_id),foreign key(aid) references pes1ug21cs268_289_admin(aid),foreign key(show_id) references pes1ug21cs268_289_shows(show_id));

-- Populating table
insert into pes1ug21cs268_289_screens values(1,'Platinum',100);
insert into pes1ug21cs268_289_screens values(2,'standard',150);
insert into pes1ug21cs268_289_screens values(3,'gold',120);
insert into pes1ug21cs268_289_screens values(4,'platinum',50);
insert into pes1ug21cs268_289_screens values(5,'gold',100);

insert into pes1ug21cs268_289_movies values(101,'Black Panther 2','English',161,'2023-11-11','2023-12-11');
insert into pes1ug21cs268_289_movies values(102,'Ram Setu','Hindi',143,'2023-10-25','2023-11-28');
insert into pes1ug21cs268_289_movies values(103,'Kantara','Kannada',150,'2023-09-30','2023-12-10');
insert into pes1ug21cs268_289_movies values(104,'Avatar-2','English',195,'2023-12-16','2023-01-29');
insert into pes1ug21cs268_289_movies values(105,'Bhediya','Hindi',156,'2023-11-25','2023-12-25');

insert into pes1ug21cs268_289_price_list values(1,3,'Friday',500);
insert into pes1ug21cs268_289_price_list values(2,3,'Saturday',500);
insert into pes1ug21cs268_289_price_list values(3,2,'Friday',350);
insert into pes1ug21cs268_289_price_list values(4,2,'Saturday',350);
insert into pes1ug21cs268_289_price_list values(5,1,'Sunday',450);


insert into pes1ug21cs268_289_shows values(001,3,'12:00:00','2023-11-17',1,101,1);
insert into pes1ug21cs268_289_shows values(002,2,'11:30:00','2023-11-17',3,103,2);
insert into pes1ug21cs268_289_shows values(003,3,'12:00:00','2023-11-18',1,101,1);
insert into pes1ug21cs268_289_shows values(004,2,'11:30:00','2023-11-19',2,102,3);
insert into pes1ug21cs268_289_shows values(005,1,'21:30:00','2023-11-20',4,101,5);

insert into pes1ug21cs268_289_booked_tickets values(0170,115,001);
insert into pes1ug21cs268_289_booked_tickets values(0064,85,002);
insert into pes1ug21cs268_289_booked_tickets values(0010,90,002);
insert into pes1ug21cs268_289_booked_tickets values(0022,54,003);
insert into pes1ug21cs268_289_booked_tickets values(0035,100,001);

insert into pes1ug21cs268_289_user values('Varun HR',700,'varunhr@gmail.com');
insert into pes1ug21cs268_289_user values('Neeraj',018,'neeraj@gmail.com');
insert into pes1ug21cs268_289_user values('Rohit',007,'rohit34@gmail.com');
insert into pes1ug21cs268_289_user values('Manoj',010,'manojk12@gmail.com');
insert into pes1ug21cs268_289_user values('Rahul',065,'rahul223@gmail.com');

insert into pes1ug21cs268_289_admin values(001,'Karan','karan001');
insert into pes1ug21cs268_289_admin values(002,'mohan','mohan002');
insert into pes1ug21cs268_289_admin values(003,'Krishna','krishna003');
insert into pes1ug21cs268_289_admin values(004,'Avanish','avanish004');
insert into pes1ug21cs268_289_admin values(005,'Arun','arun005');

insert into pes1ug21cs268_289_has_booked values(0170,018);
insert into pes1ug21cs268_289_has_booked values(0064,700);
insert into pes1ug21cs268_289_has_booked values(0010,007);
insert into pes1ug21cs268_289_has_booked values(0035,065);
insert into pes1ug21cs268_289_has_booked values(0022,010);

insert into pes1ug21cs268_289_manages values(001,001);
insert into pes1ug21cs268_289_manages values(001,002);
insert into pes1ug21cs268_289_manages values(002,002);
insert into pes1ug21cs268_289_manages values(003,003);
insert into pes1ug21cs268_289_manages values(004,004);
insert into pes1ug21cs268_289_manages values(005,005);

-- -- Join 
-- select show_id from pes1ug21cs268_289_shows natural join pes1ug21cs268_289_booked_tickets;
-- select * from pes1ug21cs268_289_shows left join pes1ug21cs268_289_movies on pes1ug21cs268_289_shows.movie_id = pes1ug21cs268_289_movies.movie_id;
-- select * from pes1ug21cs268_289_shows natural join pes1ug21cs268_289_screens;

-- -- Aggregate
-- select day,count(*) from pes1ug21cs268_289_price_list group by day;
-- select language,count(*) from pes1ug21cs268_289_movies group by language;
-- select movie_name,count(*) from pes1ug21cs268_289_movies natural join pes1ug21cs268_289_shows group by movie_name;
-- select class,count(*) from pes1ug21cs268_289_screens natural join pes1ug21cs268_289_shows group by class;
-- select day,max(price),min(price) from pes1ug21cs268_289_price_list group by day;

-- -- Set
-- select screen_id,class from pes1ug21cs268_289_screens union select movie_id,movie_name from pes1ug21cs268_289_movies;
-- select movie_id from pes1ug21cs268_289_movies where movie_id  in (select movie_id from pes1ug21cs268_289_shows);
-- select screen_id from pes1ug21cs268_289_screens where screen_id not in (select screen_id from pes1ug21cs268_289_shows);
-- select show_id from pes1ug21cs268_289_shows where show_id not in (select show_id from pes1ug21cs268_289_booked_tickets);

-- -- function
-- CREATE FUNCTION no_of_freeseats(screen_id int,sh_date date, sh_time varchar(10))
-- RETURNS int
-- DETERMINISTIC
-- BEGIN
-- DECLARE non_free int;
-- DECLARE shid int;
-- DECLARE total int;
-- set shid = (select show_id from v1 where screen_id = screen_id and date = sh_date and time = sh_time);
-- set total = (select no_of_seats  from v1 where screen_id = screen_id and date = sh_date and time = sh_time);
-- set non_free = (select count(*) from pes1ug21cs268_289_booked_tickets where show_id = shid);
-- RETURN total-non_free;
-- END $$

-- --Trigger
-- DELIMITER $$
-- CREATE TRIGGER capacity
-- BEFORE INSERT ON pes1ug21cs268_289_booked_tickets
-- FOR EACH ROW
-- BEGIN
--     DECLARE coun int;
--     DECLARE max1 int;
--     DECLARE id int;
--     DECLARE err_Msg varchar(50);
--     SET err_Msg="Incorrect Seat No!!";
--     set id = (select screen_id from pes1ug21cs268_289_shows where show_id = new.show_id);
--     set coun = new.seat_no;
--     set max1 = (select no_of_seats from pes1ug21cs268_289_screens where screen_id = id);
--     IF coun>max1 or coun<1 then
--         Signal sqlstate '45000'
--         SET MESSAGE_TEXT=err_Msg;
--     END IF;
-- END $$ 

-- --Procedure
-- DELIMITER $$
-- CREATE PROCEDURE get_tickets()
-- 	BEGIN
-- 		INSERT INTO count_tickets SELECT uname,count(*) from pes1ug21cs268_289_user natural join pes1ug21cs268_289_has_booked group by uname;
-- 	END;$$
-- DELIMITER;

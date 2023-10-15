show databases;


use students_info;
create database students_info;

select * from student_details;

CREATE TABLE student_details (
    id int PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    roll_no VARCHAR(100),
    fathers_name VARCHAR(100),
    branch VARCHAR(100),
    phone_number VARCHAR(100),
    address TEXT(200),
    secondary_phone_number VARCHAR(100)
);
DROP TABLE student_details;
INSERT INTO student_details(id,name,roll_no,fathers_name,branch,phone_number,address,secondary_phone_number) VALUES (100,'Himanshu',null,null,null,null,null,null);

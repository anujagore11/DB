create table CONTACT (
Contact_id int AUTO_INCREMENT,
Fname varchar(20),
Mname varchar(20),
Lname varchar(20),
PRIMARY KEY (Contact_id)
);

create table ADDRESS (
Address_id int AUTO_INCREMENT,
Contact_id int,
Address_type varchar(10),
Address varchar(80),
City varchar(20),
State varchar(20),
Zip varchar(10),
PRIMARY KEY (Address_id),
FOREIGN KEY (Contact_id) REFERENCES  CONTACT(Contact_id)
);

create table PHONE (
Phone_id int AUTO_INCREMENT=1,
Contact_id int,
Phone_type varchar(10),
Area_code varchar(10),
PNumber varchar(20),
PRIMARY KEY (Address_id),
FOREIGN KEY (Contact_id) REFERENCES  CONTACT(Contact_id)
);

create table DATE (
Date_id int AUTO_INCREMENT=1,
Contact_id int,
Date_type varchar(10),
Date_v DATE,
PRIMARY KEY (Date_id),
FOREIGN KEY (Contact_id) REFERENCES  CONTACT(Contact_id)
);


LOAD DATA INFILE '/home/hp/Desktop/Contacts.csv'
INTO TABLE CONTACT
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
(Contact_id, Fname, Mname, Lname);

LOAD DATA INFILE '/var/lib/mysql-files/contact_table.csv' 
INTO TABLE CONTACT
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

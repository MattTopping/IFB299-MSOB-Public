 
--
-- DATABASE
--
SHOW databases; 

CREATE DATABASE car_rentals;

USE car_rentals;

-- 
--	USERS 
--	
CREATE TABLE IF NOT EXISTS users (
	id INT(5) NOT NULL
   ,name VARCHAR(50) NOT NULL
   ,phone INT(9) NOT NULL
   ,address VARCHAR(150) NOT NULL
   ,birthday DATE NOT NULL
   ,occupation VARCHAR(100) NOT NULL
   ,gender ENUM('M','F')
   ,PRIMARY KEY(id)
);

--
-- CENTRAL DATABASE
--

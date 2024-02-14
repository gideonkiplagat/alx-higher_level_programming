-- Creates the table hbtn_0d_usa with table states.
-- id INT unique, auto generated, can’t be null and is a primary key

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
    PRIMARY KEY(`id`),
    `id`   INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL
);
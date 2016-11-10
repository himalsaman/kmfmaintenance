-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.5.45-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             9.1.0.4867
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping database structure for maintenancedb
DROP DATABASE IF EXISTS `maintenancedb`;
CREATE DATABASE IF NOT EXISTS `maintenancedb` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `maintenancedb`;


-- Dumping structure for table maintenancedb.bill_of_material
DROP TABLE IF EXISTS `bill_of_material`;
CREATE TABLE IF NOT EXISTS `bill_of_material` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `maintenance_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `maintenance_id` (`maintenance_id`),
  CONSTRAINT `bill_of_material_ibfk_1` FOREIGN KEY (`maintenance_id`) REFERENCES `maintenance` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table maintenancedb.bill_of_material_item
DROP TABLE IF EXISTS `bill_of_material_item`;
CREATE TABLE IF NOT EXISTS `bill_of_material_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `raw_material_id` int(11) DEFAULT NULL,
  `spare_part_id` int(11) DEFAULT NULL,
  `bill_of_material_id` int(11) DEFAULT NULL,
  `cost_of_material` float DEFAULT NULL,
  `qty_of_material` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `raw_material_id` (`raw_material_id`),
  KEY `spare_part_id` (`spare_part_id`),
  KEY `bill_of_material_id` (`bill_of_material_id`),
  CONSTRAINT `bill_of_material_item_ibfk_1` FOREIGN KEY (`raw_material_id`) REFERENCES `raw_material` (`id`),
  CONSTRAINT `bill_of_material_item_ibfk_2` FOREIGN KEY (`spare_part_id`) REFERENCES `spare_parts` (`id`),
  CONSTRAINT `bill_of_material_item_ibfk_3` FOREIGN KEY (`bill_of_material_id`) REFERENCES `bill_of_material` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table maintenancedb.city
DROP TABLE IF EXISTS `city`;
CREATE TABLE IF NOT EXISTS `city` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table maintenancedb.customers
DROP TABLE IF EXISTS `customers`;
CREATE TABLE IF NOT EXISTS `customers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `mobile_number` varchar(13) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `city_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mobile_number` (`mobile_number`),
  KEY `city_id` (`city_id`),
  CONSTRAINT `customers_ibfk_1` FOREIGN KEY (`city_id`) REFERENCES `city` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table maintenancedb.maintenance
DROP TABLE IF EXISTS `maintenance`;
CREATE TABLE IF NOT EXISTS `maintenance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customers_id` int(11) DEFAULT NULL,
  `cost_of_bill_of_material` float DEFAULT NULL,
  `cost_of_spare_parts` float DEFAULT NULL,
  `cost_of_raw_material` float DEFAULT NULL,
  `cost_of_labor` float DEFAULT NULL,
  `cost_of_another` float DEFAULT NULL,
  `cost_of_another_description` varchar(1000) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `close_at` timestamp NULL DEFAULT NULL,
  `product_of_maintenance` varchar(200) DEFAULT NULL,
  `maintenance_description` text,
  PRIMARY KEY (`id`),
  KEY `customers_id` (`customers_id`),
  CONSTRAINT `maintenance_ibfk_1` FOREIGN KEY (`customers_id`) REFERENCES `customers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table maintenancedb.raw_material
DROP TABLE IF EXISTS `raw_material`;
CREATE TABLE IF NOT EXISTS `raw_material` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `default_size` int(11) DEFAULT NULL,
  `string_size` varchar(50) DEFAULT NULL,
  `unit` varchar(50) DEFAULT NULL,
  `cost_per_default_size` float DEFAULT NULL,
  `inv_qty` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table maintenancedb.spare_parts
DROP TABLE IF EXISTS `spare_parts`;
CREATE TABLE IF NOT EXISTS `spare_parts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `code` varchar(20) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `inv_qty` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table maintenancedb.users
DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `role` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;

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
CREATE DATABASE IF NOT EXISTS `maintenancedb` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `maintenancedb`;


-- Dumping structure for table maintenancedb.bill_of_material
CREATE TABLE IF NOT EXISTS `bill_of_material` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `maintenance_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `cost_of_spare_parts` float DEFAULT NULL,
  `cost_of_raw_material` float DEFAULT NULL,
  `total_cost` float DEFAULT NULL,
  `gen_code` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `maintenance_id` (`maintenance_id`),
  CONSTRAINT `bill_of_material_ibfk_1` FOREIGN KEY (`maintenance_id`) REFERENCES `maintenance` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table maintenancedb.bill_of_material_item
CREATE TABLE IF NOT EXISTS `bill_of_material_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `raw_material_id` int(11) DEFAULT NULL,
  `spare_part_id` int(11) DEFAULT NULL,
  `bill_of_material_id` int(11) DEFAULT NULL,
  `cost_of_material` float DEFAULT NULL,
  `qty_of_material` float DEFAULT NULL,
  `gen_code` varchar(100) DEFAULT NULL,
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
CREATE TABLE IF NOT EXISTS `city` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table maintenancedb.customers
CREATE TABLE IF NOT EXISTS `customers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `mobile_number` varchar(13) NOT NULL,
  `mobile_number_1` varchar(13) DEFAULT NULL,
  `mobile_number_2` varchar(13) DEFAULT NULL,
  `mobile_number_3` varchar(13) DEFAULT NULL,
  `mobile_number_4` varchar(13) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `city_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mobile_number` (`mobile_number`),
  KEY `city_id` (`city_id`),
  CONSTRAINT `customers_ibfk_1` FOREIGN KEY (`city_id`) REFERENCES `city` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table maintenancedb.employee
CREATE TABLE IF NOT EXISTS `employee` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `mobile_number` varchar(13) NOT NULL,
  `job_title` varchar(100) DEFAULT NULL,
  `nationality` varchar(100) DEFAULT NULL,
  `nat_id` varchar(100) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mobile_number` (`mobile_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table maintenancedb.finish_products
CREATE TABLE IF NOT EXISTS `finish_products` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `code` varchar(50) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `inv_qty` int(11) DEFAULT NULL,
  `source` varchar(50) DEFAULT NULL,
  `gen_code` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table maintenancedb.maintenance
CREATE TABLE IF NOT EXISTS `maintenance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customers_id` int(11) DEFAULT NULL,
  `cost_of_bill_of_material` float DEFAULT NULL,
  `cost_of_labor` float DEFAULT NULL,
  `cost_of_another` float DEFAULT NULL,
  `cost_of_another_description` varchar(1000) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `close_at` timestamp NULL DEFAULT NULL,
  `product_of_maintenance` varchar(200) DEFAULT NULL,
  `maintenance_description` varchar(20000) DEFAULT NULL,
  `start_date` timestamp NULL DEFAULT NULL,
  `done_date` timestamp NULL DEFAULT NULL,
  `m_code` varchar(100) DEFAULT NULL,
  `hidden` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `customers_id` (`customers_id`),
  CONSTRAINT `maintenance_ibfk_1` FOREIGN KEY (`customers_id`) REFERENCES `customers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table maintenancedb.manufacting
CREATE TABLE IF NOT EXISTS `manufacting` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cost_of_bill_of_material` float DEFAULT NULL,
  `cost_of_labor` float DEFAULT NULL,
  `sales_price` float DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `product_of_manufact` int(11) DEFAULT NULL,
  `start_date` timestamp NULL DEFAULT NULL,
  `done_date` timestamp NULL DEFAULT NULL,
  `m_code` varchar(100) DEFAULT NULL,
  `hidden` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `product_of_manufact` (`product_of_manufact`),
  CONSTRAINT `manufacting_ibfk_1` FOREIGN KEY (`product_of_manufact`) REFERENCES `finish_products` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table maintenancedb.man_bom
CREATE TABLE IF NOT EXISTS `man_bom` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `manufact_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `cost_of_spare_parts` float DEFAULT NULL,
  `cost_of_raw_material` float DEFAULT NULL,
  `total_cost` float DEFAULT NULL,
  `gen_code` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `manufact_id` (`manufact_id`),
  CONSTRAINT `man_bom_ibfk_1` FOREIGN KEY (`manufact_id`) REFERENCES `manufacting` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table maintenancedb.man_bom_item
CREATE TABLE IF NOT EXISTS `man_bom_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `raw_material_id` int(11) DEFAULT NULL,
  `spare_part_id` int(11) DEFAULT NULL,
  `man_bom_id` int(11) DEFAULT NULL,
  `cost_of_material` float DEFAULT NULL,
  `qty_of_material` float DEFAULT NULL,
  `gen_code` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `raw_material_id` (`raw_material_id`),
  KEY `spare_part_id` (`spare_part_id`),
  KEY `man_bom_id` (`man_bom_id`),
  CONSTRAINT `man_bom_item_ibfk_1` FOREIGN KEY (`raw_material_id`) REFERENCES `raw_material` (`id`),
  CONSTRAINT `man_bom_item_ibfk_2` FOREIGN KEY (`spare_part_id`) REFERENCES `spare_parts` (`id`),
  CONSTRAINT `man_bom_item_ibfk_3` FOREIGN KEY (`man_bom_id`) REFERENCES `man_bom` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table maintenancedb.outbound
CREATE TABLE IF NOT EXISTS `outbound` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(50) DEFAULT NULL,
  `out_date` timestamp NULL DEFAULT NULL,
  `reason` varchar(100) DEFAULT NULL,
  `customers_id` int(11) DEFAULT NULL,
  `employee_id` int(11) DEFAULT NULL,
  `raw_material_id` int(11) DEFAULT NULL,
  `spare_part_id` int(11) DEFAULT NULL,
  `tools_id` int(11) DEFAULT NULL,
  `finish_product_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `customers_id` (`customers_id`),
  KEY `employee_id` (`employee_id`),
  KEY `raw_material_id` (`raw_material_id`),
  KEY `spare_part_id` (`spare_part_id`),
  KEY `tools_id` (`tools_id`),
  KEY `finish_product_id` (`finish_product_id`),
  CONSTRAINT `outbound_ibfk_1` FOREIGN KEY (`customers_id`) REFERENCES `customers` (`id`),
  CONSTRAINT `outbound_ibfk_2` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`id`),
  CONSTRAINT `outbound_ibfk_3` FOREIGN KEY (`raw_material_id`) REFERENCES `raw_material` (`id`),
  CONSTRAINT `outbound_ibfk_4` FOREIGN KEY (`spare_part_id`) REFERENCES `spare_parts` (`id`),
  CONSTRAINT `outbound_ibfk_5` FOREIGN KEY (`tools_id`) REFERENCES `tools` (`id`),
  CONSTRAINT `outbound_ibfk_6` FOREIGN KEY (`finish_product_id`) REFERENCES `finish_products` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table maintenancedb.raw_material
CREATE TABLE IF NOT EXISTS `raw_material` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `code` varchar(100) DEFAULT NULL,
  `default_size` float NOT NULL,
  `string_size` varchar(50) DEFAULT NULL,
  `unit` varchar(50) NOT NULL,
  `cost_per_default_size` float NOT NULL,
  `inv_qty` float NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table maintenancedb.spare_parts
CREATE TABLE IF NOT EXISTS `spare_parts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `code` varchar(20) NOT NULL,
  `gen_code` varchar(100) NOT NULL,
  `price` float NOT NULL,
  `inv_qty` int(11) NOT NULL,
  `unit` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table maintenancedb.tools
CREATE TABLE IF NOT EXISTS `tools` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `code` varchar(50) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `inv_qty` int(11) DEFAULT NULL,
  `unit` varchar(50) DEFAULT NULL,
  `gen_code` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table maintenancedb.users
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `role` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;

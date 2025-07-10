-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jul 10, 2025 at 04:43 PM
-- Server version: 9.1.0
-- PHP Version: 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `synex_industries`
--

-- --------------------------------------------------------

--
-- Table structure for table `app_user`
--

DROP TABLE IF EXISTS `app_user`;
CREATE TABLE IF NOT EXISTS `app_user` (
  `Username` varchar(20) NOT NULL,
  `Password` varchar(30) NOT NULL,
  `user_type` varchar(10) NOT NULL,
  PRIMARY KEY (`Username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app_user`
--

INSERT INTO `app_user` (`Username`, `Password`, `user_type`) VALUES
('dumi', '1010', 'owner'),
('tedy', '1111', 'admin'),
('teddy', 'zlsa12', 'admin'),
('dum', 'ygxql$', 'admin'),
('buddy', 'hcnpm123', 'admin'),
('ass', 'ass123', 'admin'),
('aaaa', 'aaaaaa', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
CREATE TABLE IF NOT EXISTS `employee` (
  `Emp_code` varchar(20) NOT NULL,
  `Emp_name` varchar(50) DEFAULT NULL,
  `emp_professon_code` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`Emp_code`),
  KEY `emp_professon_code` (`emp_professon_code`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`Emp_code`, `Emp_name`, `emp_professon_code`) VALUES
('synex0', 'D Perera', '1'),
('synex1', 'KUSUM KANCHANA', '3'),
('synex2', 'J Mish', '2'),
('synex3', 'P PINASH', '4'),
('synex4', 'D Dimoki', '5');

-- --------------------------------------------------------

--
-- Table structure for table `profession`
--

DROP TABLE IF EXISTS `profession`;
CREATE TABLE IF NOT EXISTS `profession` (
  `profession_code` varchar(10) NOT NULL,
  `profession_name` varchar(20) DEFAULT NULL,
  `daily_salary` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`profession_code`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `profession`
--

INSERT INTO `profession` (`profession_code`, `profession_name`, `daily_salary`) VALUES
('1', 'Director', '3000'),
('2', 'Scientist', '2371'),
('3', 'Engineer', '1500'),
('5', 'Driver', '600.0'),
('4', 'Cleane2', '12.0');

-- --------------------------------------------------------

--
-- Table structure for table `work_data`
--

DROP TABLE IF EXISTS `work_data`;
CREATE TABLE IF NOT EXISTS `work_data` (
  `emp_code` varchar(20) DEFAULT NULL,
  `months` varchar(30) DEFAULT NULL,
  `days` int DEFAULT NULL,
  KEY `emp_code` (`emp_code`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `work_data`
--

INSERT INTO `work_data` (`emp_code`, `months`, `days`) VALUES
('synex0', 'January', 10),
('synex0', 'February', 19),
('synex0', 'March', 12),
('synex0', 'April', 26),
('synex0', 'May', 28),
('synex0', 'June', 11),
('synex0', 'July', 25),
('synex0', 'August', 8),
('synex0', 'September', 29),
('synex0', 'October', 12),
('synex0', 'November', 13),
('synex0', 'December', 16),
('synex1', 'January', 13),
('synex1', 'February', 27),
('synex1', 'March', 19),
('synex1', 'April', 11),
('synex1', 'May', 10),
('synex1', 'June', 26),
('synex1', 'July', 20),
('synex1', 'August', 22),
('synex1', 'September', 7),
('synex1', 'October', 26),
('synex1', 'November', 28),
('synex1', 'December', 16),
('synex2', 'January', 22),
('synex2', 'February', 26),
('synex2', 'March', 20),
('synex2', 'April', 20),
('synex2', 'May', 15),
('synex2', 'June', 28),
('synex2', 'July', 29),
('synex2', 'August', 25),
('synex2', 'September', 29),
('synex2', 'October', 18),
('synex2', 'November', 22),
('synex2', 'December', 20),
('synex3', 'January', 28),
('synex3', 'February', 11),
('synex3', 'March', 20),
('synex3', 'April', 20),
('synex3', 'May', 18),
('synex3', 'June', 30),
('synex3', 'July', 26),
('synex3', 'August', 22),
('synex3', 'September', 24),
('synex3', 'October', 15),
('synex3', 'November', 25),
('synex3', 'December', 27),
('synex4', 'January', 12),
('synex4', 'February', 7),
('synex4', 'March', 10),
('synex4', 'April', 26),
('synex4', 'May', 15),
('synex4', 'June', 30),
('synex4', 'July', 13),
('synex4', 'August', 14),
('synex4', 'September', 8),
('synex4', 'October', 20),
('synex4', 'November', 21),
('synex4', 'December', 2);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

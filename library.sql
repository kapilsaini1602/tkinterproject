-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 22, 2021 at 06:55 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library`
--

-- --------------------------------------------------------

--
-- Table structure for table `addbook`
--

CREATE TABLE `addbook` (
  `bookid` int(11) NOT NULL,
  `bookname` varchar(100) DEFAULT NULL,
  `bookauthor` varchar(50) DEFAULT NULL,
  `bookstock` int(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `addbook`
--

INSERT INTO `addbook` (`bookid`, `bookname`, `bookauthor`, `bookstock`) VALUES
(1, 'Programing with C', 'Anurag Sharma', 2),
(2, 'Computer Fundamentals', 'PK sinha', 2);

-- --------------------------------------------------------

--
-- Table structure for table `issuebook`
--

CREATE TABLE `issuebook` (
  `bookid` int(11) DEFAULT NULL,
  `studentid` int(11) NOT NULL,
  `start` int(11) DEFAULT NULL,
  `end` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `issuebook`
--

INSERT INTO `issuebook` (`bookid`, `studentid`, `start`, `end`) VALUES
(2, 4, 4, 4);

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `user` varchar(100) DEFAULT NULL,
  `pass` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`user`, `pass`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`username`, `password`) VALUES
('kunal', '123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `addbook`
--
ALTER TABLE `addbook`
  ADD PRIMARY KEY (`bookid`);

--
-- Indexes for table `issuebook`
--
ALTER TABLE `issuebook`
  ADD PRIMARY KEY (`studentid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 4.6.6deb4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 21, 2017 at 10:28 AM
-- Server version: 5.7.18-0ubuntu0.17.04.1
-- PHP Version: 7.0.18-0ubuntu0.17.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `instabot`
--
CREATE DATABASE IF NOT EXISTS `instabot` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE `instabot`;

-- --------------------------------------------------------

--
-- Table structure for table `bots`
--

CREATE TABLE `bots` (
  `bot_id` int(11) NOT NULL,
  `pid` int(11) DEFAULT NULL,
  `login` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `start_time` datetime DEFAULT NULL,
  `like_per_day` int(11) NOT NULL DEFAULT '1000',
  `comments_per_day` int(11) NOT NULL DEFAULT '0',
  `tag_list` text COLLATE utf8_unicode_ci,
  `tag_blacklist` text COLLATE utf8_unicode_ci,
  `max_like_for_one_tag` int(11) NOT NULL DEFAULT '50',
  `follow_per_day` int(11) NOT NULL DEFAULT '300',
  `follow_time` int(11) NOT NULL DEFAULT '60',
  `unfollow_per_day` int(11) NOT NULL DEFAULT '300',
  `unfollow_break_min` int(11) NOT NULL DEFAULT '15',
  `unfollow_break_max` int(11) NOT NULL DEFAULT '30',
  `log_mod` int(11) NOT NULL DEFAULT '2',
  `proxy` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `comment_list` text COLLATE utf8_unicode_ci,
  `user_blacklist` text COLLATE utf8_unicode_ci,
  `unfollow_whitelist` text COLLATE utf8_unicode_ci,
  `entry_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bots`
--
ALTER TABLE `bots`
  ADD PRIMARY KEY (`bot_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bots`
--
ALTER TABLE `bots`
  MODIFY `bot_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

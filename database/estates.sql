-- phpMyAdmin SQL Dump
-- version 3.4.10.1deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 04, 2014 at 09:22 PM
-- Server version: 5.5.38
-- PHP Version: 5.3.10-1ubuntu3.14

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `estates`
--

-- --------------------------------------------------------

--
-- Table structure for table `estateban`
--

CREATE TABLE IF NOT EXISTS `estateban` (
  `EstateID` int(10) unsigned NOT NULL,
  `bannedUUID` varchar(36) NOT NULL,
  `bannedIp` varchar(16) NOT NULL,
  `bannedIpHostMask` varchar(16) NOT NULL,
  `bannedNameMask` varchar(64) DEFAULT NULL,
  `EstateBanID` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`EstateBanID`),
  KEY `estateban_EstateID` (`EstateID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `estate_groups`
--

CREATE TABLE IF NOT EXISTS `estate_groups` (
  `EstateID` int(10) unsigned NOT NULL,
  `uuid` char(36) NOT NULL,
  `EstateGroupID` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`EstateGroupID`),
  KEY `EstateID` (`EstateID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `estate_managers`
--

CREATE TABLE IF NOT EXISTS `estate_managers` (
  `EstateID` int(10) unsigned NOT NULL,
  `uuid` char(36) NOT NULL,
  `EstateManagerID` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`EstateManagerID`),
  KEY `EstateID` (`EstateID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `estate_managers`
--

INSERT INTO `estate_managers` (`EstateID`, `uuid`, `EstateManagerID`) VALUES
(100, '77164e00-0c0c-4e12-ba27-3df3afb4a333', 1),
(103, '77164e00-0c0c-4e12-ba27-3df3afb4a333', 2),
(102, '9ec9f834-093b-4319-898e-8f12ed81b035', 3),
(102, '77164e00-0c0c-4e12-ba27-3df3afb4a333', 4),
(101, '9ec9f834-093b-4319-898e-8f12ed81b035', 5),
(101, '77164e00-0c0c-4e12-ba27-3df3afb4a333', 6);

-- --------------------------------------------------------

--
-- Table structure for table `estate_map`
--

CREATE TABLE IF NOT EXISTS `estate_map` (
  `RegionID` char(36) NOT NULL DEFAULT '00000000-0000-0000-0000-000000000000',
  `EstateID` int(11) NOT NULL,
  PRIMARY KEY (`RegionID`),
  KEY `EstateID` (`EstateID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `estate_map`
--

INSERT INTO `estate_map` (`RegionID`, `EstateID`) VALUES
('8b438df2-9f7a-48a6-b2c7-58f398793f7d', 100),
('0c02ea17-8e77-4110-b06f-6a3a51582187', 101),
('0d3882eb-da9c-41c8-bbfc-702f580d6e97', 101),
('183248d7-5e98-427a-b806-aaf354f4d72f', 101),
('202cb3c7-2eac-42b4-af3e-dc04c950fff1', 101),
('2140e457-345d-4fd4-8798-f0ec6fcd60b3', 101),
('26ad2f6e-74a5-45e2-b144-68eb9b706b5a', 101),
('2a9ab6c4-79b5-4c95-a5ca-3999815e5956', 101),
('2de9e842-6381-4e25-a9d1-93a35c07769f', 101),
('31a72f45-7719-4c86-b426-edcefe18b8a9', 101),
('34642229-f4a0-4f51-b64f-6cd9a19ccbb5', 101),
('391b6dea-aed1-4804-b12d-de8c51c178a2', 101),
('4137f6c2-3e65-4a2e-b7e2-201f2ff19466', 101),
('41557b54-5ab0-4499-b47a-63c7471d3784', 101),
('42a063da-77ac-4341-834e-144b53628ca2', 101),
('4d813bac-2131-47c6-89a8-b702d74635eb', 101),
('51c88178-032b-4974-a29c-f7e99880ba8c', 101),
('58d9e5e9-d95d-489b-9169-a76bf32ce322', 101),
('5d500b03-2099-41da-bcb5-fbe1ca27ca32', 101),
('61976738-6182-4cef-85b9-5de7b1ca97a0', 101),
('639490a9-8bf6-4d50-9408-19de7ca967b4', 101),
('68f8de9c-867b-4bfe-8bc9-44e3834f8c76', 101),
('6a289bfd-dd66-4680-9fd5-28958c5d1765', 101),
('732b01a6-9c1d-45b2-8a95-43f209460aff', 101),
('861be450-8a63-432e-aaaf-153b02f9b5f1', 101),
('8c3df8aa-e15b-42ce-b728-bfaaa0e334b2', 101),
('8dcaea6d-1793-48da-b1ba-919f11321f34', 101),
('ae687d85-1e8d-4400-a3a7-72b238a1d8ef', 101),
('b3b7198e-e779-4639-8957-297d88626676', 101),
('b566b110-2989-45c9-b7d3-c7f1111fe8b8', 101),
('c36cf1a9-727d-4b35-9e17-3b4382e7f25c', 101),
('c70fab48-8f80-4617-8a44-eee22a8feefb', 101),
('ceaf770e-ad1d-44c4-bdb4-98a2b09c0a86', 101),
('d563a7c2-1e2b-43bc-ac8e-c3b09929a1a7', 101),
('d636e6a1-c410-47a3-abd4-47f2c09a1237', 101),
('e3447c20-60fc-4024-9bb5-8daad04c7824', 101),
('e4143aff-4bfe-4a8d-8215-05e62094eb20', 101),
('e49a971b-4b6d-48b0-9da2-a5fb9da72ed2', 101),
('f79903ee-e365-4b98-89aa-2bb41a141a50', 101),
('fab7eeab-f6c1-4ed5-9370-1dcff5b03e2a', 101),
('0bf2f346-c264-4b84-8faa-f62e523d0619', 102),
('2ad86f99-cde2-4a42-9bf8-f9c2c55645f6', 102),
('2c241658-8dfa-4374-b7b2-b16ae0cba3a5', 102),
('3023e807-cde1-4ea1-bb6a-355c8478dc2b', 102),
('37aeaaba-0b9a-4316-b4c5-66b93f4cac52', 102),
('3c5b63ef-5308-44e3-9d21-4a4c1d2711f9', 102),
('3ff55b57-6f83-4681-9d55-cf3f55edd3a1', 102),
('58952f78-0d13-4625-85e5-b474c49bae41', 102),
('71a7efa8-4ee8-4ba4-bda1-a778fd7ce4ba', 102),
('8157f31d-3943-45dd-ac23-38b586ffb602', 102),
('99212391-96a4-4f58-8f98-56b7ec47ac17', 102),
('a3b8425c-db6f-4b68-a402-15b1097a7e52', 102),
('c03ffead-cc1d-490a-a72c-cc4e87b04f10', 102),
('db1ffbb8-dab9-40e4-a332-94ee40b51735', 102),
('de2a34ef-ca62-46e5-8390-e13ecedd72e8', 102),
('e4777493-f9d2-4767-851f-54bfe09fd8a1', 102),
('e6814abb-45ca-45ce-8ebb-9fa7139d2967', 102),
('21a72f45-7719-4c86-b426-edcefe18b8a9', 104);

-- --------------------------------------------------------

--
-- Table structure for table `estate_settings`
--

CREATE TABLE IF NOT EXISTS `estate_settings` (
  `EstateID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `EstateName` varchar(64) DEFAULT NULL,
  `AbuseEmailToEstateOwner` tinyint(4) NOT NULL,
  `DenyAnonymous` tinyint(4) NOT NULL,
  `ResetHomeOnTeleport` tinyint(4) NOT NULL,
  `FixedSun` tinyint(4) NOT NULL,
  `DenyTransacted` tinyint(4) NOT NULL,
  `BlockDwell` tinyint(4) NOT NULL,
  `DenyIdentified` tinyint(4) NOT NULL,
  `AllowVoice` tinyint(4) NOT NULL,
  `UseGlobalTime` tinyint(4) NOT NULL,
  `PricePerMeter` int(11) NOT NULL,
  `TaxFree` tinyint(4) NOT NULL,
  `AllowDirectTeleport` tinyint(4) NOT NULL,
  `RedirectGridX` int(11) NOT NULL,
  `RedirectGridY` int(11) NOT NULL,
  `ParentEstateID` int(10) unsigned NOT NULL,
  `SunPosition` double NOT NULL,
  `EstateSkipScripts` tinyint(4) NOT NULL,
  `BillableFactor` float NOT NULL,
  `PublicAccess` tinyint(4) NOT NULL,
  `AbuseEmail` varchar(255) NOT NULL,
  `EstateOwner` varchar(36) NOT NULL,
  `DenyMinors` tinyint(4) NOT NULL,
  `AllowLandmark` tinyint(4) NOT NULL DEFAULT '1',
  `AllowParcelChanges` tinyint(4) NOT NULL DEFAULT '1',
  `AllowSetHome` tinyint(4) NOT NULL DEFAULT '1',
  PRIMARY KEY (`EstateID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=105 ;

--
-- Dumping data for table `estate_settings`
--

INSERT INTO `estate_settings` (`EstateID`, `EstateName`, `AbuseEmailToEstateOwner`, `DenyAnonymous`, `ResetHomeOnTeleport`, `FixedSun`, `DenyTransacted`, `BlockDwell`, `DenyIdentified`, `AllowVoice`, `UseGlobalTime`, `PricePerMeter`, `TaxFree`, `AllowDirectTeleport`, `RedirectGridX`, `RedirectGridY`, `ParentEstateID`, `SunPosition`, `EstateSkipScripts`, `BillableFactor`, `PublicAccess`, `AbuseEmail`, `EstateOwner`, `DenyMinors`, `AllowLandmark`, `AllowParcelChanges`, `AllowSetHome`) VALUES
(100, 'My Estate', 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, '', '3d6181b0-6a4b-97ef-18d8-722652995cf1', 0, 1, 1, 1),
(101, 'Mainland', 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 6.833984375, 0, 0, 1, '', '3d6181b0-6a4b-97ef-18d8-722652995cf1', 0, 1, 1, 1),
(102, 'LinkinU Labs Research', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, '', '3d6181b0-6a4b-97ef-18d8-722652995cf1', 0, 1, 1, 1),
(103, 'My Estate', 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, '', '3d6181b0-6a4b-97ef-18d8-722652995cf1', 0, 1, 1, 1),
(104, 'shadi toxx', 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, '', '8cd7162f-5646-46d5-af55-4fd95bafc5fc', 0, 1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `estate_users`
--

CREATE TABLE IF NOT EXISTS `estate_users` (
  `EstateID` int(10) unsigned NOT NULL,
  `uuid` char(36) NOT NULL,
  `EstateUserID` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`EstateUserID`),
  KEY `EstateID` (`EstateID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `migrations`
--

CREATE TABLE IF NOT EXISTS `migrations` (
  `name` varchar(100) DEFAULT NULL,
  `version` int(11) DEFAULT NULL,
  `migrationid` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`migrationid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `migrations`
--

INSERT INTO `migrations` (`name`, `version`, `migrationid`) VALUES
('migrations', 1, 1),
('EstateStore', 33, 2);

-- --------------------------------------------------------

--
-- Table structure for table `south_migrationhistory`
--

CREATE TABLE IF NOT EXISTS `south_migrationhistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) NOT NULL,
  `migration` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `south_migrationhistory`
--

INSERT INTO `south_migrationhistory` (`id`, `app_name`, `migration`, `applied`) VALUES
(10, 'grid_estates', '0001_initial', '2014-09-03 13:16:20'),
(11, 'grid_estates', '0002_auto__del_field_estategroups_id__add_field_estategroups_estategroupid', '2014-09-03 13:16:34'),
(12, 'grid_estates', '0003_auto__del_field_migrations_id__add_field_migrations_migrationid__del_f', '2014-09-03 13:16:35');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

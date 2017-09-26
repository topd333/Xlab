-- phpMyAdmin SQL Dump
-- version 3.4.10.1deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 04, 2014 at 09:21 PM
-- Server version: 5.5.38
-- PHP Version: 5.3.10-1ubuntu3.14

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `oxdata`
--

-- --------------------------------------------------------

--
-- Table structure for table `migrations`
--

CREATE TABLE IF NOT EXISTS `migrations` (
  `name` varchar(100) DEFAULT NULL,
  `version` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `migrations`
--

INSERT INTO `migrations` (`name`, `version`) VALUES
('migrations', 1),
('TransactionUserAccountData', 1),
('TransactionDataScript', 1);

-- --------------------------------------------------------

--
-- Table structure for table `TransactionData`
--

CREATE TABLE IF NOT EXISTS `TransactionData` (
  `SourceAccount` varchar(36) NOT NULL,
  `SourceIP` varchar(64) NOT NULL,
  `DestinationAccount` varchar(36) NOT NULL,
  `DestinationIP` varchar(64) NOT NULL,
  `TransactionAmount` char(40) NOT NULL,
  `TransactionDate` int(11) NOT NULL,
  `TransactionFlags` int(11) DEFAULT NULL,
  `TransactionType` int(11) DEFAULT NULL,
  `Description` varchar(128) DEFAULT NULL,
  `SerialNumber` mediumint(9) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`SerialNumber`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=248 ;

--
-- Dumping data for table `TransactionData`
--

INSERT INTO `TransactionData` (`SourceAccount`, `SourceIP`, `DestinationAccount`, `DestinationIP`, `TransactionAmount`, `TransactionDate`, `TransactionFlags`, `TransactionType`, `Description`, `SerialNumber`) VALUES
('00000000-0000-0000-0000-000000000000', '', '77164e00-0c0c-4e12-ba27-3df3afb4a333', '', '4000000', 0, NULL, NULL, NULL, 56),
('00000000-0000-0000-0000-000000000000', '', '77164e00-0c0c-4e12-ba27-3df3afb4a333', '', '4000000', 0, NULL, NULL, NULL, 57),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '77164e00-0c0c-4e12-ba27-3df3afb4a333', '0.0.0.0', '-4000000', 2014, NULL, NULL, 'BlueWall Slade Pays linked inyou 4000000', 58),
('77164e00-0c0c-4e12-ba27-3df3afb4a333', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '4000000', 2014, NULL, NULL, 'BlueWall Slade Pays linked inyou 4000000', 59),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '77164e00-0c0c-4e12-ba27-3df3afb4a333', '0.0.0.0', '-4000000', 2014, NULL, NULL, 'BlueWall Slade Pays linked inyou 4000000', 60),
('77164e00-0c0c-4e12-ba27-3df3afb4a333', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '4000000', 2014, NULL, NULL, 'BlueWall Slade Pays linked inyou 4000000', 61),
('00000000-0000-0000-0000-000000000000', '', '77164e00-0c0c-4e12-ba27-3df3afb4a333', '', '8000000', 0, NULL, NULL, NULL, 62),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '77164e00-0c0c-4e12-ba27-3df3afb4a333', '0.0.0.0', '-4000000', 2014, NULL, NULL, 'BlueWall Slade Pays linked inyou 4000000', 63),
('77164e00-0c0c-4e12-ba27-3df3afb4a333', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '4000000', 2014, NULL, NULL, 'BlueWall Slade Pays linked inyou 4000000', 64),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '77164e00-0c0c-4e12-ba27-3df3afb4a333', '0.0.0.0', '-2000000', 2014, NULL, NULL, 'BlueWall Slade Pays linked inyou 2000000', 65),
('77164e00-0c0c-4e12-ba27-3df3afb4a333', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '2000000', 2014, NULL, NULL, 'BlueWall Slade Pays linked inyou 2000000', 66),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '77164e00-0c0c-4e12-ba27-3df3afb4a333', '0.0.0.0', '-2000000', 2014, NULL, NULL, 'BlueWall Slade Pays linked inyou 2000000', 67),
('77164e00-0c0c-4e12-ba27-3df3afb4a333', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '2000000', 2014, NULL, NULL, 'BlueWall Slade Pays linked inyou 2000000', 68),
('00000000-0000-0000-0000-000000000000', '', '77164e00-0c0c-4e12-ba27-3df3afb4a333', '', '10000000', 0, NULL, NULL, NULL, 69),
('21e49698-f7a5-4ce9-94c7-392e78bee6fb', '0.0.0.0', '77164e00-0c0c-4e12-ba27-3df3afb4a333', '0.0.0.0', '-1000', 2014, NULL, NULL, 'BlueWall Slade Pays James Hughes 1000', 70),
('77164e00-0c0c-4e12-ba27-3df3afb4a333', '0.0.0.0', '21e49698-f7a5-4ce9-94c7-392e78bee6fb', '0.0.0.0', '1000', 2014, NULL, NULL, 'BlueWall Slade Pays James Hughes 1000', 71),
('21e49698-f7a5-4ce9-94c7-392e78bee6fb', '0.0.0.0', '77164e00-0c0c-4e12-ba27-3df3afb4a333', '0.0.0.0', '-1000', 2014, NULL, NULL, 'BlueWall Slade Pays James Hughes 1000', 72),
('77164e00-0c0c-4e12-ba27-3df3afb4a333', '0.0.0.0', '21e49698-f7a5-4ce9-94c7-392e78bee6fb', '0.0.0.0', '1000', 2014, NULL, NULL, 'BlueWall Slade Pays James Hughes 1000', 73),
('21e49698-f7a5-4ce9-94c7-392e78bee6fb', '0.0.0.0', '77164e00-0c0c-4e12-ba27-3df3afb4a333', '0.0.0.0', '-2000', 2014, NULL, NULL, 'BlueWall Slade Pays James Hughes 2000', 74),
('77164e00-0c0c-4e12-ba27-3df3afb4a333', '0.0.0.0', '21e49698-f7a5-4ce9-94c7-392e78bee6fb', '0.0.0.0', '2000', 2014, NULL, NULL, 'BlueWall Slade Pays James Hughes 2000', 75),
('2da10b31-3128-4262-8771-4d6b455dccdb', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-1000', 2014, NULL, NULL, 'linked inyou Pays one two 1000', 76),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '2da10b31-3128-4262-8771-4d6b455dccdb', '0.0.0.0', '1000', 2014, NULL, NULL, 'linked inyou Pays one two 1000', 77),
('dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-1000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 1000', 78),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', 'dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '1000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 1000', 79),
('dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-2000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 2000', 80),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', 'dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '2000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 2000', 81),
('dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-20000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 20000', 82),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', 'dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '20000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 20000', 83),
('dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-3000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 3000', 84),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', 'dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '3000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 3000', 85),
('dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-1000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 1000', 86),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', 'dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '1000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 1000', 87),
('dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-4000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 4000', 88),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', 'dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '4000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 4000', 89),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', 'dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '-5000', 2014, NULL, NULL, 'Game Developer Pays linked inyou 5000', 90),
('dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '5000', 2014, NULL, NULL, 'Game Developer Pays linked inyou 5000', 91),
('695685a2-4071-48d0-900e-46a04d64d497', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-1000', 2014, NULL, NULL, 'linked inyou Pays Saad Zarf 1000', 92),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '695685a2-4071-48d0-900e-46a04d64d497', '0.0.0.0', '1000', 2014, NULL, NULL, 'linked inyou Pays Saad Zarf 1000', 93),
('695685a2-4071-48d0-900e-46a04d64d497', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-1000', 2014, NULL, NULL, 'linked inyou Pays Saad Zarf 1000', 94),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '695685a2-4071-48d0-900e-46a04d64d497', '0.0.0.0', '1000', 2014, NULL, NULL, 'linked inyou Pays Saad Zarf 1000', 95),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '695685a2-4071-48d0-900e-46a04d64d497', '0.0.0.0', '-10', 2014, NULL, NULL, 'Object sLinkDisplayRow3 owned by linked inyou paid 10 by Saad Zarf', 96),
('695685a2-4071-48d0-900e-46a04d64d497', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '10', 2014, NULL, NULL, 'Object sLinkDisplayRow3 owned by linked inyou paid 10 by Saad Zarf', 97),
('695685a2-4071-48d0-900e-46a04d64d497', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-20', 2014, NULL, NULL, 'You received 20 from an object,  Linkoo v7.0  OPEN, owned by linked inyou', 98),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '695685a2-4071-48d0-900e-46a04d64d497', '0.0.0.0', '20', 2014, NULL, NULL, 'You received 20 from an object,  Linkoo v7.0  OPEN, owned by linked inyou', 99),
('e672f547-30c1-4f63-8ddf-2c66e6777dc4', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-1000', 2014, NULL, NULL, 'linked inyou Pays gogo koy 1000', 100),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', 'e672f547-30c1-4f63-8ddf-2c66e6777dc4', '0.0.0.0', '1000', 2014, NULL, NULL, 'linked inyou Pays gogo koy 1000', 101),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', 'e672f547-30c1-4f63-8ddf-2c66e6777dc4', '0.0.0.0', '-10', 2014, NULL, NULL, 'Object sLinkDisplayRow3 owned by linked inyou paid 10 by gogo koy', 102),
('e672f547-30c1-4f63-8ddf-2c66e6777dc4', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '10', 2014, NULL, NULL, 'Object sLinkDisplayRow3 owned by linked inyou paid 10 by gogo koy', 103),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', 'e672f547-30c1-4f63-8ddf-2c66e6777dc4', '0.0.0.0', '-10', 2014, NULL, NULL, 'Object sLinkDisplayRow5 owned by linked inyou paid 10 by gogo koy', 104),
('e672f547-30c1-4f63-8ddf-2c66e6777dc4', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '10', 2014, NULL, NULL, 'Object sLinkDisplayRow5 owned by linked inyou paid 10 by gogo koy', 105),
('480e6e96-c5f7-4a71-beb8-3fd8805c4cb3', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-1000', 2014, NULL, NULL, 'linked inyou Pays Ahmad Q8 1000', 106),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '480e6e96-c5f7-4a71-beb8-3fd8805c4cb3', '0.0.0.0', '1000', 2014, NULL, NULL, 'linked inyou Pays Ahmad Q8 1000', 107),
('39578dd4-3d58-4106-a6eb-5124aa514fed', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-1000', 2014, NULL, NULL, 'linked inyou Pays 5morh ksa 1000', 108),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '39578dd4-3d58-4106-a6eb-5124aa514fed', '0.0.0.0', '1000', 2014, NULL, NULL, 'linked inyou Pays 5morh ksa 1000', 109),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '39578dd4-3d58-4106-a6eb-5124aa514fed', '0.0.0.0', '-10', 2014, NULL, NULL, 'Object sLinkDisplayRow2 owned by linked inyou paid 10 by 5morh ksa', 110),
('39578dd4-3d58-4106-a6eb-5124aa514fed', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '10', 2014, NULL, NULL, 'Object sLinkDisplayRow2 owned by linked inyou paid 10 by 5morh ksa', 111),
('80e25e1f-0782-430d-a84a-4e5f05a9ec7c', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-1000', 2014, NULL, NULL, 'linked inyou Pays Tunidev Free 1000', 112),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '80e25e1f-0782-430d-a84a-4e5f05a9ec7c', '0.0.0.0', '1000', 2014, NULL, NULL, 'linked inyou Pays Tunidev Free 1000', 113),
('3e92a2e8-0cf0-45f9-b94e-0f6c85eb6eaf', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-1000', 2014, NULL, NULL, 'linked inyou Pays cariolane resident 1000', 114),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '3e92a2e8-0cf0-45f9-b94e-0f6c85eb6eaf', '0.0.0.0', '1000', 2014, NULL, NULL, 'linked inyou Pays cariolane resident 1000', 115),
('3ad6bff1-3d9c-4c72-b419-2059d06ad971', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-1000', 2014, NULL, NULL, 'linked inyou Pays amwaj Ellisson 1000', 116),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '3ad6bff1-3d9c-4c72-b419-2059d06ad971', '0.0.0.0', '1000', 2014, NULL, NULL, 'linked inyou Pays amwaj Ellisson 1000', 117),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '3ad6bff1-3d9c-4c72-b419-2059d06ad971', '0.0.0.0', '-1000', 2014, NULL, NULL, 'amwaj Ellisson Pays linked inyou 1000', 118),
('3ad6bff1-3d9c-4c72-b419-2059d06ad971', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '1000', 2014, NULL, NULL, 'amwaj Ellisson Pays linked inyou 1000', 119),
('3ad6bff1-3d9c-4c72-b419-2059d06ad971', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-2000', 2014, NULL, NULL, 'linked inyou Pays amwaj Ellisson 2000', 120),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '3ad6bff1-3d9c-4c72-b419-2059d06ad971', '0.0.0.0', '2000', 2014, NULL, NULL, 'linked inyou Pays amwaj Ellisson 2000', 121),
('6baed7c5-a7a3-4031-803c-0e41704ab519', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-100', 2014, NULL, NULL, 'linked inyou Pays om ar 100', 122),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '6baed7c5-a7a3-4031-803c-0e41704ab519', '0.0.0.0', '100', 2014, NULL, NULL, 'linked inyou Pays om ar 100', 123),
('7b56ea8b-3596-4e08-a680-e38adb5fc3bb', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-1000', 2014, NULL, NULL, 'linked inyou Pays Kiss Me 1000', 124),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '7b56ea8b-3596-4e08-a680-e38adb5fc3bb', '0.0.0.0', '1000', 2014, NULL, NULL, 'linked inyou Pays Kiss Me 1000', 125),
('41d7372e-4303-4dac-b89b-3aacfdd257b0', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-2000', 2014, NULL, NULL, 'linked inyou Pays Scon Crill 2000', 126),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '41d7372e-4303-4dac-b89b-3aacfdd257b0', '0.0.0.0', '2000', 2014, NULL, NULL, 'linked inyou Pays Scon Crill 2000', 127),
('6a688332-f3f9-46cb-b1c9-41ad6c811ccf', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-1000', 2014, NULL, NULL, 'linked inyou Pays miss ranoo 1000', 128),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '6a688332-f3f9-46cb-b1c9-41ad6c811ccf', '0.0.0.0', '1000', 2014, NULL, NULL, 'linked inyou Pays miss ranoo 1000', 129),
('cb58867c-ab55-425d-a0f5-5e340ffae5fd', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-1000', 2014, NULL, NULL, 'linked inyou Pays Q8 Kuwait 1000', 130),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', 'cb58867c-ab55-425d-a0f5-5e340ffae5fd', '0.0.0.0', '1000', 2014, NULL, NULL, 'linked inyou Pays Q8 Kuwait 1000', 131),
('e672f547-30c1-4f63-8ddf-2c66e6777dc4', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-1000', 2014, NULL, NULL, 'linked inyou Pays gogo koy 1000', 132),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', 'e672f547-30c1-4f63-8ddf-2c66e6777dc4', '0.0.0.0', '1000', 2014, NULL, NULL, 'linked inyou Pays gogo koy 1000', 133),
('82cae55e-6534-49ba-8a1e-f240d2a43e94', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-1100000', 2014, NULL, NULL, 'linked inyou Pays Lbn Resident 1100000', 134),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '82cae55e-6534-49ba-8a1e-f240d2a43e94', '0.0.0.0', '1100000', 2014, NULL, NULL, 'linked inyou Pays Lbn Resident 1100000', 135),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '82cae55e-6534-49ba-8a1e-f240d2a43e94', '0.0.0.0', '-100', 2014, NULL, NULL, 'Object Sale', 136),
('82cae55e-6534-49ba-8a1e-f240d2a43e94', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '100', 2014, NULL, NULL, 'Object Sale', 137),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '82cae55e-6534-49ba-8a1e-f240d2a43e94', '0.0.0.0', '-100', 2014, NULL, NULL, 'Object Sale', 138),
('82cae55e-6534-49ba-8a1e-f240d2a43e94', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '100', 2014, NULL, NULL, 'Object Sale', 139),
('82cae55e-6534-49ba-8a1e-f240d2a43e94', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-200', 2014, NULL, NULL, 'linked inyou Pays Lbn Resident 200', 140),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '82cae55e-6534-49ba-8a1e-f240d2a43e94', '0.0.0.0', '200', 2014, NULL, NULL, 'linked inyou Pays Lbn Resident 200', 141),
('13fa6a6e-8d72-44d4-8e3b-9c7fdaa98b45', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-10000', 2014, NULL, NULL, 'linked inyou Pays Cloth Me 10000', 142),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '13fa6a6e-8d72-44d4-8e3b-9c7fdaa98b45', '0.0.0.0', '10000', 2014, NULL, NULL, 'linked inyou Pays Cloth Me 10000', 143),
('429b061e-c719-4523-887c-08f1b6203da6', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-10000', 2014, NULL, NULL, 'linked inyou Pays DjS Remix 10000', 144),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '429b061e-c719-4523-887c-08f1b6203da6', '0.0.0.0', '10000', 2014, NULL, NULL, 'linked inyou Pays DjS Remix 10000', 145),
('13fa6a6e-8d72-44d4-8e3b-9c7fdaa98b45', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-20000', 2014, NULL, NULL, 'linked inyou Pays Cloth Me 20000', 146),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '13fa6a6e-8d72-44d4-8e3b-9c7fdaa98b45', '0.0.0.0', '20000', 2014, NULL, NULL, 'linked inyou Pays Cloth Me 20000', 147),
('77164e00-0c0c-4e12-ba27-3df3afb4a333', '0.0.0.0', '77164e00-0c0c-4e12-ba27-3df3afb4a333', '0.0.0.0', '-12', 2014, NULL, NULL, 'Object Sale', 148),
('77164e00-0c0c-4e12-ba27-3df3afb4a333', '0.0.0.0', '77164e00-0c0c-4e12-ba27-3df3afb4a333', '0.0.0.0', '12', 2014, NULL, NULL, 'Object Sale', 149),
('ade7f0a0-cc38-4a46-8bc8-0763e712f62f', '0.0.0.0', '82cae55e-6534-49ba-8a1e-f240d2a43e94', '0.0.0.0', '-5000', 2014, NULL, NULL, 'Lbn Resident Pays G H 5000', 150),
('82cae55e-6534-49ba-8a1e-f240d2a43e94', '0.0.0.0', 'ade7f0a0-cc38-4a46-8bc8-0763e712f62f', '0.0.0.0', '5000', 2014, NULL, NULL, 'Lbn Resident Pays G H 5000', 151),
('82cae55e-6534-49ba-8a1e-f240d2a43e94', '0.0.0.0', 'ade7f0a0-cc38-4a46-8bc8-0763e712f62f', '0.0.0.0', '-20', 2014, NULL, NULL, 'Object Sale', 152),
('ade7f0a0-cc38-4a46-8bc8-0763e712f62f', '0.0.0.0', '82cae55e-6534-49ba-8a1e-f240d2a43e94', '0.0.0.0', '20', 2014, NULL, NULL, 'Object Sale', 153),
('ade7f0a0-cc38-4a46-8bc8-0763e712f62f', '0.0.0.0', '82cae55e-6534-49ba-8a1e-f240d2a43e94', '0.0.0.0', '-20', 2014, NULL, NULL, 'Lbn Resident Pays G H 20', 154),
('82cae55e-6534-49ba-8a1e-f240d2a43e94', '0.0.0.0', 'ade7f0a0-cc38-4a46-8bc8-0763e712f62f', '0.0.0.0', '20', 2014, NULL, NULL, 'Lbn Resident Pays G H 20', 155),
('d085cb56-660e-4cd2-992d-e9fd5d64cfac', '0.0.0.0', '82cae55e-6534-49ba-8a1e-f240d2a43e94', '0.0.0.0', '-10000', 2014, NULL, NULL, 'Lbn Resident Pays sweet moon 10000', 156),
('82cae55e-6534-49ba-8a1e-f240d2a43e94', '0.0.0.0', 'd085cb56-660e-4cd2-992d-e9fd5d64cfac', '0.0.0.0', '10000', 2014, NULL, NULL, 'Lbn Resident Pays sweet moon 10000', 157),
('a6b772cc-14cb-4759-885b-cbf0e66cf7cc', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-1000', 2014, NULL, NULL, 'linked inyou Pays rainbow colors 1000', 158),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', 'a6b772cc-14cb-4759-885b-cbf0e66cf7cc', '0.0.0.0', '1000', 2014, NULL, NULL, 'linked inyou Pays rainbow colors 1000', 159),
('743c087b-8516-4c7b-adb8-d9d8ff6c2e30', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-50000', 2014, NULL, NULL, 'linked inyou Pays a z 50000', 160),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '743c087b-8516-4c7b-adb8-d9d8ff6c2e30', '0.0.0.0', '50000', 2014, NULL, NULL, 'linked inyou Pays a z 50000', 161),
('7b56ea8b-3596-4e08-a680-e38adb5fc3bb', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-50000', 2014, NULL, NULL, 'linked inyou Pays Kiss Me 50000', 162),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '7b56ea8b-3596-4e08-a680-e38adb5fc3bb', '0.0.0.0', '50000', 2014, NULL, NULL, 'linked inyou Pays Kiss Me 50000', 163),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-2000000', 2014, NULL, NULL, 'linked inyou Pays R A 2000000', 164),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '2000000', 2014, NULL, NULL, 'linked inyou Pays R A 2000000', 165),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '-100', 2014, NULL, NULL, 'Object MoneyChessyV2.6 owned by R A paid 100 by R A', 166),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '100', 2014, NULL, NULL, 'Object MoneyChessyV2.6 owned by R A paid 100 by R A', 167),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-400', 2014, NULL, NULL, 'Object MoneyChessyV2.6 owned by R A paid 400 by linked inyou', 168),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '400', 2014, NULL, NULL, 'Object MoneyChessyV2.6 owned by R A paid 400 by linked inyou', 169),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '-400', 2014, NULL, NULL, 'Object MoneyChessyV2.6 owned by R A paid 400 by R A', 170),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '400', 2014, NULL, NULL, 'Object MoneyChessyV2.6 owned by R A paid 400 by R A', 171),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-1400', 2014, NULL, NULL, 'linked inyou Pays R A 1400', 172),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '1400', 2014, NULL, NULL, 'linked inyou Pays R A 1400', 173),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-400', 2014, NULL, NULL, 'Object Player0 owned by R A paid 400 by linked inyou', 174),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '400', 2014, NULL, NULL, 'Object Player0 owned by R A paid 400 by linked inyou', 175),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '-100', 2014, NULL, NULL, 'Object MoneyChessyV2.6 owned by R A paid 100 by R A', 176),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '100', 2014, NULL, NULL, 'Object MoneyChessyV2.6 owned by R A paid 100 by R A', 177),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '-100', 2014, NULL, NULL, 'Object BeloteV2.9 owned by R A paid 100 by R A', 178),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '100', 2014, NULL, NULL, 'Object BeloteV2.9 owned by R A paid 100 by R A', 179),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '-100', 2014, NULL, NULL, 'Object BeloteV2.9 owned by R A paid 100 by R A', 180),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '100', 2014, NULL, NULL, 'Object BeloteV2.9 owned by R A paid 100 by R A', 181),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '-400', 2014, NULL, NULL, 'Object MoneyChessyV2.6 owned by R A paid 400 by R A', 182),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '400', 2014, NULL, NULL, 'Object MoneyChessyV2.6 owned by R A paid 400 by R A', 183),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-400', 2014, NULL, NULL, 'Object MoneyChessyV2.6 owned by R A paid 400 by linked inyou', 184),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '400', 2014, NULL, NULL, 'Object MoneyChessyV2.6 owned by R A paid 400 by linked inyou', 185),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-400', 2014, NULL, NULL, 'Object Caisse owned by R A paid 400 by linked inyou', 186),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '400', 2014, NULL, NULL, 'Object Caisse owned by R A paid 400 by linked inyou', 187),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '-100', 2014, NULL, NULL, 'Object MoneyChessyV2.6 owned by R A paid 100 by R A', 188),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '100', 2014, NULL, NULL, 'Object MoneyChessyV2.6 owned by R A paid 100 by R A', 189),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-100', 2014, NULL, NULL, 'Object MoneyChessyV2.6 owned by R A paid 100 by linked inyou', 190),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '100', 2014, NULL, NULL, 'Object MoneyChessyV2.6 owned by R A paid 100 by linked inyou', 191),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '-100', 2014, NULL, NULL, 'Object MoneyChessyV2.6 owned by R A paid 100 by R A', 192),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '100', 2014, NULL, NULL, 'Object MoneyChessyV2.6 owned by R A paid 100 by R A', 193),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-100', 2014, NULL, NULL, 'Object MoneyChessyV2.6 owned by R A paid 100 by linked inyou', 194),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '100', 2014, NULL, NULL, 'Object MoneyChessyV2.6 owned by R A paid 100 by linked inyou', 195),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '-100', 2014, NULL, NULL, 'Object BeloteV2.9 owned by R A paid 100 by R A', 196),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '100', 2014, NULL, NULL, 'Object BeloteV2.9 owned by R A paid 100 by R A', 197),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '-400', 2014, NULL, NULL, 'Object Home29 owned by R A paid 400 by R A', 198),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '400', 2014, NULL, NULL, 'Object Home29 owned by R A paid 400 by R A', 199),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '-100', 2014, NULL, NULL, 'Object Buy owned by R A paid 100 by R A', 200),
('5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '5644d887-8ec5-48d1-8664-bcb583163145', '0.0.0.0', '100', 2014, NULL, NULL, 'Object Buy owned by R A paid 100 by R A', 201),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-30', 2014, NULL, NULL, 'Object sLinkDisplayRow1 owned by linked inyou paid 30 by linked inyou', 202),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '30', 2014, NULL, NULL, 'Object sLinkDisplayRow1 owned by linked inyou paid 30 by linked inyou', 203),
('3bd37e2d-7f9b-4f08-ad0d-55438a2e7ee0', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-2000', 2014, NULL, NULL, 'linked inyou Pays A R 2000', 204),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '3bd37e2d-7f9b-4f08-ad0d-55438a2e7ee0', '0.0.0.0', '2000', 2014, NULL, NULL, 'linked inyou Pays A R 2000', 205),
('3bd37e2d-7f9b-4f08-ad0d-55438a2e7ee0', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-2000', 2014, NULL, NULL, 'linked inyou Pays A R 2000', 206),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '3bd37e2d-7f9b-4f08-ad0d-55438a2e7ee0', '0.0.0.0', '2000', 2014, NULL, NULL, 'linked inyou Pays A R 2000', 207),
('3bd37e2d-7f9b-4f08-ad0d-55438a2e7ee0', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-2000', 2014, NULL, NULL, 'linked inyou Pays A R 2000', 208),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '3bd37e2d-7f9b-4f08-ad0d-55438a2e7ee0', '0.0.0.0', '2000', 2014, NULL, NULL, 'linked inyou Pays A R 2000', 209),
('3bd37e2d-7f9b-4f08-ad0d-55438a2e7ee0', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-2000', 2014, NULL, NULL, 'linked inyou Pays A R 2000', 210),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '3bd37e2d-7f9b-4f08-ad0d-55438a2e7ee0', '0.0.0.0', '2000', 2014, NULL, NULL, 'linked inyou Pays A R 2000', 211),
('3bd37e2d-7f9b-4f08-ad0d-55438a2e7ee0', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-3000', 2014, NULL, NULL, 'linked inyou Pays A R 3000', 212),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '3bd37e2d-7f9b-4f08-ad0d-55438a2e7ee0', '0.0.0.0', '3000', 2014, NULL, NULL, 'linked inyou Pays A R 3000', 213),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '3bd37e2d-7f9b-4f08-ad0d-55438a2e7ee0', '0.0.0.0', '-2000', 2014, NULL, NULL, 'A R Pays linked inyou 2000', 214),
('3bd37e2d-7f9b-4f08-ad0d-55438a2e7ee0', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '2000', 2014, NULL, NULL, 'A R Pays linked inyou 2000', 215),
('3bd37e2d-7f9b-4f08-ad0d-55438a2e7ee0', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-7000', 2014, NULL, NULL, 'linked inyou Pays A R 7000', 216),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '3bd37e2d-7f9b-4f08-ad0d-55438a2e7ee0', '0.0.0.0', '7000', 2014, NULL, NULL, 'linked inyou Pays A R 7000', 217),
('3bd37e2d-7f9b-4f08-ad0d-55438a2e7ee0', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-7000', 2014, NULL, NULL, 'linked inyou Pays A R 7000', 218),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '3bd37e2d-7f9b-4f08-ad0d-55438a2e7ee0', '0.0.0.0', '7000', 2014, NULL, NULL, 'linked inyou Pays A R 7000', 219),
('3bd37e2d-7f9b-4f08-ad0d-55438a2e7ee0', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-7000', 2014, NULL, NULL, 'linked inyou Pays A R 7000', 220),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '3bd37e2d-7f9b-4f08-ad0d-55438a2e7ee0', '0.0.0.0', '7000', 2014, NULL, NULL, 'linked inyou Pays A R 7000', 221),
('3bd37e2d-7f9b-4f08-ad0d-55438a2e7ee0', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-7000', 2014, NULL, NULL, 'linked inyou Pays A R 7000', 222),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '3bd37e2d-7f9b-4f08-ad0d-55438a2e7ee0', '0.0.0.0', '7000', 2014, NULL, NULL, 'linked inyou Pays A R 7000', 223),
('3bd37e2d-7f9b-4f08-ad0d-55438a2e7ee0', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-7000', 2014, NULL, NULL, 'linked inyou Pays A R 7000', 224),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '3bd37e2d-7f9b-4f08-ad0d-55438a2e7ee0', '0.0.0.0', '7000', 2014, NULL, NULL, 'linked inyou Pays A R 7000', 225),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '3bd37e2d-7f9b-4f08-ad0d-55438a2e7ee0', '0.0.0.0', '-7000', 2014, NULL, NULL, 'A R Pays linked inyou 7000', 226),
('3bd37e2d-7f9b-4f08-ad0d-55438a2e7ee0', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '7000', 2014, NULL, NULL, 'A R Pays linked inyou 7000', 227),
('dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-4000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 4000', 228),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', 'dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '4000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 4000', 229),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', 'dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '-1000', 2014, NULL, NULL, 'Game Developer Pays linked inyou 1000', 230),
('dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '1000', 2014, NULL, NULL, 'Game Developer Pays linked inyou 1000', 231),
('dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-4000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 4000', 232),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', 'dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '4000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 4000', 233),
('dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-4000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 4000', 234),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', 'dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '4000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 4000', 235),
('dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-4000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 4000', 236),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', 'dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '4000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 4000', 237),
('dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-7000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 7000', 238),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', 'dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '7000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 7000', 239),
('dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-10000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 10000', 240),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', 'dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '10000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 10000', 241),
('bf536b7a-249b-427c-99bf-38e99cdcb9ec', '0.0.0.0', 'dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '-4000', 2014, NULL, NULL, 'Game Developer Pays T C 4000', 242),
('dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', 'bf536b7a-249b-427c-99bf-38e99cdcb9ec', '0.0.0.0', '4000', 2014, NULL, NULL, 'Game Developer Pays T C 4000', 243),
('dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-8000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 8000', 244),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', 'dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '8000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 8000', 245),
('dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', '-8000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 8000', 246),
('9ec9f834-093b-4319-898e-8f12ed81b035', '0.0.0.0', 'dd5c0f5e-2a97-4a53-84fd-e12ac7d92953', '0.0.0.0', '8000', 2014, NULL, NULL, 'linked inyou Pays Game Developer 8000', 247);

-- --------------------------------------------------------

--
-- Table structure for table `TransactionUserAccountData`
--

CREATE TABLE IF NOT EXISTS `TransactionUserAccountData` (
  `UserId` varchar(36) NOT NULL,
  `AccountId` varchar(36) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `TransactionUserAccountData`
--

INSERT INTO `TransactionUserAccountData` (`UserId`, `AccountId`) VALUES
('77164e00-0c0c-4e12-ba27-3df3afb4a333', '77164e00-0c0c-4e12-ba27-3df3afb4a333'),
('9ec9f834-093b-4319-898e-8f12ed81b035', '9ec9f834-093b-4319-898e-8f12ed81b035'),
('21e49698-f7a5-4ce9-94c7-392e78bee6fb', '21e49698-f7a5-4ce9-94c7-392e78bee6fb');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

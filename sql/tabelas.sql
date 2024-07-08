DROP DATABASE IF EXISTS airCrashes;

CREATE DATABASE IF NOT EXISTS airCrashes;

USE airCrashes;

--
-- Table structure for table `COUNTRY`
--

DROP TABLE IF EXISTS `COUNTRY`;

CREATE TABLE `COUNTRY` (
  `CountryID` varchar(2) NOT NULL,
  `CountryName` varchar(60) NOT NULL,
  PRIMARY KEY (`CountryID`),
  UNIQUE KEY `CountryName` (`CountryName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Table structure for table `MANUFACTURER`
--

DROP TABLE IF EXISTS `MANUFACTURER`;

CREATE TABLE `MANUFACTURER` (
  `ManufacturerID` int(11) NOT NULL AUTO_INCREMENT,
  `ManufacturerName` varchar(35) NOT NULL,
  `Active` enum('S', 'N') NOT NULL, -- S sim, N não
  PRIMARY KEY (`ManufacturerID`),
  UNIQUE KEY `ManufacturerName` (`ManufacturerName`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Table structure for table `MODEL`
--

DROP TABLE IF EXISTS `MODEL`;

CREATE TABLE `MODEL` (
  `ModelID` varchar(45) NOT NULL,
  `ManufacturerID` int(11) NOT NULL,
  PRIMARY KEY (`ModelID`),
  CONSTRAINT `model_ibfk_1` FOREIGN KEY (`ManufacturerID`) REFERENCES `MANUFACTURER` (`ManufacturerID`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Table structure for table `CITY`
--

DROP TABLE IF EXISTS `CITY`;

CREATE TABLE `CITY` (
  `CityID` int(11) NOT NULL AUTO_INCREMENT,
  `CityName` varchar(50) NOT NULL,  
  `CountryID` varchar(2) NOT NULL,
  PRIMARY KEY (`CityID`),
  CONSTRAINT `city_ibfk_1` FOREIGN KEY (`CountryID`) REFERENCES `COUNTRY` (`CountryID`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Table structure for table `PLANE`
--

DROP TABLE IF EXISTS `PLANE`;

CREATE TABLE `PLANE` (
  `PlaneID` varchar(30) NOT NULL,
  `ModelID` varchar(60) NOT NULL,  
  `CNLN` varchar(30) NOT NULL,
  PRIMARY KEY (`PlaneID`),
  CONSTRAINT `plane_ibfk_1` FOREIGN KEY (`ModelID`) REFERENCES `MODEL` (`ModelID`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Table structure for table `CARRIER`
--

DROP TABLE IF EXISTS `CARRIER`;

CREATE TABLE `CARRIER` (
  `CarrierID` int(11) NOT NULL AUTO_INCREMENT,
  `CarrierName` varchar(60) NOT NULL,  
  `Active` enum('S', 'N', '-') NOT NULL, -- **REMOVER o '-' quando os dados estiverem todos preenchidos
  PRIMARY KEY (`CarrierID`),
  UNIQUE KEY `CarrierName` (`CarrierName`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Table structure for table `LOCATION`
--

DROP TABLE IF EXISTS `LOCATION`;

CREATE TABLE `LOCATION` (
  `LocationID` int(11) NOT NULL AUTO_INCREMENT,
  `CityID` int(11) DEFAULT NULL,  
  `CountryID` varchar(2) NOT NULL,
  `Description` text DEFAULT NULL,
  PRIMARY KEY (`LocationID`),
  CONSTRAINT `location_ibfk_1` FOREIGN KEY (`CityID`) REFERENCES `CITY` (`CityID`) ON UPDATE CASCADE,
  CONSTRAINT `location_ibfk_2` FOREIGN KEY (`CountryID`) REFERENCES `COUNTRY` (`CountryID`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Table structure for table `FLIGHT`
--

DROP TABLE IF EXISTS `FLIGHT`;

CREATE TABLE `FLIGHT` (
  `PlaneID` varchar(30) NOT NULL,
  `FlightNumber` varchar(10) DEFAULT NULL,
  `Date` date NOT NULL,
  `Time` time DEFAULT NULL,  
  `LocationID` int(11) NOT NULL,
  `Type` enum('C', 'M', 'P') NOT NULL, -- C comercial, M militar, P privado
  `CarrierID` int(11) NOT NULL,
  `AboardPassenger` int(4) NOT NULL,
  `AboardCrew` int(4) NOT NULL,
  `FatalityCrew` int(4) NOT NULL,
  `FatalityPassenger` int(4) NOT NULL,
  `Ground` int(4) NOT NULL,
  `Route` text NOT NULL,
  `Summary` text NOT NULL,
  PRIMARY KEY (`PlaneID`),
  CONSTRAINT `flight_ibfk_1` FOREIGN KEY (`PlaneID`) REFERENCES `PLANE` (`PlaneID`) ON UPDATE CASCADE,
  CONSTRAINT `flight_ibfk_2` FOREIGN KEY (`LocationID`) REFERENCES `LOCATION` (`LocationID`) ON UPDATE CASCADE,
  CONSTRAINT `flight_ibfk_3` FOREIGN KEY (`CarrierID`) REFERENCES `CARRIER` (`CarrierID`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Table structure for table `STOP`
--

DROP TABLE IF EXISTS `STOP`;

CREATE TABLE `STOP` (
  `PlaneID` varchar(30) NOT NULL,
  `StopOrder` int(2) NOT NULL,
  `CityID` int(11) NOT NULL,  
  PRIMARY KEY (`PlaneID`,`StopOrder`),
  KEY `StopOrder` (`StopOrder`),
  CONSTRAINT `stop_ibfk_1` FOREIGN KEY (`PlaneID`) REFERENCES `FLIGHT` (`PlaneID`) ON UPDATE CASCADE,
  CONSTRAINT `stop_ibfk_2` FOREIGN KEY (`CityID`) REFERENCES `CITY` (`CityID`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

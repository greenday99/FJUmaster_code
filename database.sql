-- MySQL dump 10.13  Distrib 5.7.17, for Linux (x86_64)
--
-- Host: localhost    Database: myThesisDatabase
-- ------------------------------------------------------
-- Server version	5.7.18-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `candidates`
--

DROP TABLE IF EXISTS `candidates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `candidates` (
  `itemID` varchar(10) NOT NULL,
  `itemType` int(11) DEFAULT NULL,
  `openPrice` float DEFAULT NULL,
  `closePrice` float DEFAULT NULL,
  `itemPrice` float DEFAULT NULL,
  `attr_1` float DEFAULT NULL,
  `attr_2` float DEFAULT NULL,
  `attr_3` float DEFAULT NULL,
  `attr_4` float DEFAULT NULL,
  `attr_5` float DEFAULT NULL,
  `attr_6` float DEFAULT NULL,
  `attr_7` float DEFAULT NULL,
  `attr_8` float DEFAULT NULL,
  `attr_9` float DEFAULT NULL,
  `attr_10` float DEFAULT NULL,
  `attr_11` float DEFAULT NULL,
  PRIMARY KEY (`itemID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `candidates`
--

LOCK TABLES `candidates` WRITE;
/*!40000 ALTER TABLE `candidates` DISABLE KEYS */;
/*!40000 ALTER TABLE `candidates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cluster_four`
--

DROP TABLE IF EXISTS `cluster_four`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cluster_four` (
  `itemID` varchar(10) NOT NULL,
  `itemName` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`itemID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cluster_four`
--

LOCK TABLES `cluster_four` WRITE;
/*!40000 ALTER TABLE `cluster_four` DISABLE KEYS */;
/*!40000 ALTER TABLE `cluster_four` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cluster_one`
--

DROP TABLE IF EXISTS `cluster_one`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cluster_one` (
  `itemID` varchar(10) NOT NULL,
  `itemName` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`itemID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cluster_one`
--

LOCK TABLES `cluster_one` WRITE;
/*!40000 ALTER TABLE `cluster_one` DISABLE KEYS */;
/*!40000 ALTER TABLE `cluster_one` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cluster_three`
--

DROP TABLE IF EXISTS `cluster_three`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cluster_three` (
  `itemID` varchar(10) NOT NULL,
  `itemName` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`itemID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cluster_three`
--

LOCK TABLES `cluster_three` WRITE;
/*!40000 ALTER TABLE `cluster_three` DISABLE KEYS */;
/*!40000 ALTER TABLE `cluster_three` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cluster_two`
--

DROP TABLE IF EXISTS `cluster_two`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cluster_two` (
  `itemID` varchar(10) NOT NULL,
  `itemName` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`itemID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cluster_two`
--

LOCK TABLES `cluster_two` WRITE;
/*!40000 ALTER TABLE `cluster_two` DISABLE KEYS */;
/*!40000 ALTER TABLE `cluster_two` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `evaluation_data`
--

DROP TABLE IF EXISTS `evaluation_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `evaluation_data` (
  `itemID` varchar(10) NOT NULL,
  `itemType` int(11) DEFAULT NULL,
  `itemPrice` float DEFAULT NULL,
  `start_info` float DEFAULT NULL,
  `end_info` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`itemID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `evaluation_data`
--

LOCK TABLES `evaluation_data` WRITE;
/*!40000 ALTER TABLE `evaluation_data` DISABLE KEYS */;
/*!40000 ALTER TABLE `evaluation_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-08-22 14:36:04

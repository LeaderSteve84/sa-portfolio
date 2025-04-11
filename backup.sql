-- MySQL dump 10.13  Distrib 8.0.41, for Linux (x86_64)
--
-- Host: icopoghru9oezxh8.cbetxkdyhwsb.us-east-1.rds.amazonaws.com    Database: tzlyru4u5xvhjqm0
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `id` varchar(36) NOT NULL,
  `username` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `phone` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES ('31bc0c33-e061-489c-9639-05e700bd6761','LeaderSteve','steveadahson@gmail.com','pbkdf2:sha256:600000$679Zgm8tyE6QH2rH$0f2db079b640aa38d64201e8305b80accfed070149d1f5507c155926fcd528e9','+2349011446215');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contactMessage`
--

DROP TABLE IF EXISTS `contactMessage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contactMessage` (
  `message_id` varchar(36) NOT NULL,
  `date_submitted` datetime NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(120) NOT NULL,
  `subject` varchar(120) NOT NULL,
  `message` text NOT NULL,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`message_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contactMessage`
--

LOCK TABLES `contactMessage` WRITE;
/*!40000 ALTER TABLE `contactMessage` DISABLE KEYS */;
INSERT INTO `contactMessage` VALUES ('8b36a1d9-a2e6-4f84-8169-6b2b30d08816','2025-02-14 18:07:31','Smart shaker','smartshaker@gmail.com','I want us to collaborate ','Hi,\r\nI did love the both of us to collaborate in a project. \r\nKindly chat me up as soon as possible.\r\nThanks','Attend');
/*!40000 ALTER TABLE `contactMessage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `featuredProjects`
--

DROP TABLE IF EXISTS `featuredProjects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `featuredProjects` (
  `featured_project_id` varchar(36) NOT NULL,
  `date_created` datetime NOT NULL,
  `date_updated` datetime NOT NULL,
  `title` varchar(1024) NOT NULL,
  `description` text NOT NULL,
  `image_link` varchar(2083) DEFAULT NULL,
  `stacks` varchar(1024) NOT NULL,
  `role` text,
  `challenges` text,
  `date_cmptd` varchar(1024) DEFAULT NULL,
  `domain_link` varchar(2083) DEFAULT NULL,
  `github_link` varchar(2083) DEFAULT NULL,
  `video_link` varchar(2083) DEFAULT NULL,
  PRIMARY KEY (`featured_project_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `featuredProjects`
--

LOCK TABLES `featuredProjects` WRITE;
/*!40000 ALTER TABLE `featuredProjects` DISABLE KEYS */;
INSERT INTO `featuredProjects` VALUES ('89969526-e4d1-4487-a95f-8947111b869e','2025-02-15 16:05:27','2025-02-15 16:31:27','Personal Professional Portfolio Web App','My personal portfolio web application to showcase my professional skills and experiences to potential clients, with featured and projects done.','https://i.postimg.cc/v8tQtDGG/portfolio-stephen-me3.jpg','Python - Flask framework, Jinja2 templating engine, HTML, Bootstrap5.0, CSS, MySQL, Tools - PostImages, Flask-JWT extended, etc','Full-stack developer','Authentication and authorization','22/10/2024','https://portfolio-stephen.me','','');
/*!40000 ALTER TABLE `featuredProjects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projectsDone`
--

DROP TABLE IF EXISTS `projectsDone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projectsDone` (
  `project_done_id` varchar(36) NOT NULL,
  `date_created` datetime NOT NULL,
  `date_updated` datetime NOT NULL,
  `title` varchar(1024) NOT NULL,
  `project_type` varchar(1024) NOT NULL,
  `description` text NOT NULL,
  `stacks` varchar(1024) NOT NULL,
  `role` varchar(1024) NOT NULL,
  `date_cmptd` varchar(1024) NOT NULL,
  `video_link` varchar(2083) DEFAULT NULL,
  PRIMARY KEY (`project_done_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projectsDone`
--

LOCK TABLES `projectsDone` WRITE;
/*!40000 ALTER TABLE `projectsDone` DISABLE KEYS */;
/*!40000 ALTER TABLE `projectsDone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reference`
--

DROP TABLE IF EXISTS `reference`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reference` (
  `reference_id` varchar(36) NOT NULL,
  `date_created` datetime NOT NULL,
  `date_updated` datetime NOT NULL,
  `reference_type` varchar(50) NOT NULL,
  `message` text NOT NULL,
  `reference_link` varchar(255) DEFAULT NULL,
  `contact` varchar(100) DEFAULT NULL,
  `name` varchar(100) NOT NULL,
  `designation` varchar(50) NOT NULL,
  PRIMARY KEY (`reference_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reference`
--

LOCK TABLES `reference` WRITE;
/*!40000 ALTER TABLE `reference` DISABLE KEYS */;
INSERT INTO `reference` VALUES ('0e775717-d2de-4543-ad32-2d39aa7dfbeb','2025-03-15 16:14:57','2025-03-15 16:14:57','testimony','So overwhelmed with this great mind filled with innovative and progressive acts, a solution provider and a visionary','','+2347065877616','Jefferson Chang Kisha','collaborator'),('ba8b46b0-4805-46b9-b3c1-791cc3d35189','2025-02-13 17:02:59','2025-02-13 17:02:59','testimony','I love this guy. An example of hard work.','','','Gladys Akudo','colleague');
/*!40000 ALTER TABLE `reference` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resume`
--

DROP TABLE IF EXISTS `resume`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resume` (
  `resume_id` varchar(36) NOT NULL,
  `date_created` datetime NOT NULL,
  `date_updated` datetime NOT NULL,
  `resume_image1_link` varchar(255) DEFAULT NULL,
  `resume_image2_link` varchar(255) DEFAULT NULL,
  `resume_image3_link` varchar(255) DEFAULT NULL,
  `resume_image4_link` varchar(255) DEFAULT NULL,
  `resume_download_link` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`resume_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resume`
--

LOCK TABLES `resume` WRITE;
/*!40000 ALTER TABLE `resume` DISABLE KEYS */;
INSERT INTO `resume` VALUES ('9523274c-1606-42ad-8161-0f5894394ff6','2025-03-04 11:42:37','2025-03-04 12:18:17','https://i.postimg.cc/5NshtHfv/stephen-resume-page1.png','https://i.postimg.cc/tTGfcWz0/stephen-resume-page2.png','','','https://drive.google.com/uc?export=download&id=1kuB9H4qG2uRHtgENxSiwseleVUqsT5XH');
/*!40000 ALTER TABLE `resume` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `writings`
--

DROP TABLE IF EXISTS `writings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `writings` (
  `writing_id` varchar(36) NOT NULL,
  `date_created` datetime NOT NULL,
  `date_updated` datetime NOT NULL,
  `title` varchar(1024) NOT NULL,
  `image_link` varchar(2083) DEFAULT NULL,
  `description` text NOT NULL,
  `published_link` varchar(2083) DEFAULT NULL,
  PRIMARY KEY (`writing_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `writings`
--

LOCK TABLES `writings` WRITE;
/*!40000 ALTER TABLE `writings` DISABLE KEYS */;
/*!40000 ALTER TABLE `writings` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-10 21:50:03

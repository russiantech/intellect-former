-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 25, 2024 at 06:26 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `russiant`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('7cc25bbc6373');

-- --------------------------------------------------------

--
-- Table structure for table `badge`
--

CREATE TABLE `badge` (
  `id` int(11) NOT NULL,
  `level` int(11) DEFAULT NULL,
  `icon` varchar(100) DEFAULT NULL,
  `user` int(11) NOT NULL,
  `course` int(11) NOT NULL,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `brand`
--

CREATE TABLE `brand` (
  `id` int(11) NOT NULL,
  `type` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `logo` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `lang` varchar(100) DEFAULT NULL,
  `us` varchar(1000) DEFAULT NULL,
  `ceo` varchar(500) DEFAULT NULL,
  `hype` varchar(10000) DEFAULT NULL,
  `socials` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`socials`)),
  `tutors` int(11) DEFAULT NULL,
  `ratings` int(11) DEFAULT NULL,
  `reviews` int(11) DEFAULT NULL,
  `bank` varchar(100) DEFAULT NULL,
  `acct` int(11) DEFAULT NULL,
  `verified` tinyint(1) DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `image` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `id` int(11) NOT NULL,
  `title` varchar(45) NOT NULL,
  `desc` varchar(100) DEFAULT NULL,
  `slug` varchar(130) DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `image` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`id`, `title`, `desc`, `slug`, `created`, `updated`, `deleted`, `active`, `image`) VALUES
(13, 'All', 'Explore a wide range of courses covering various topics from programming to design.', NULL, '2024-02-05 16:16:57', '2024-02-05 16:16:57', 0, 1, NULL),
(14, 'Trending', 'Discover the hottest and most popular courses trending in the e-learning community.', NULL, '2024-02-05 16:16:57', '2024-02-05 16:16:57', 0, 1, NULL),
(15, 'New Courses', 'Stay updated with the latest additions to our ever-growing course catalog.', NULL, '2024-02-05 16:16:57', '2024-02-05 16:16:57', 0, 1, NULL),
(16, 'Data & Data Science', 'Dive into the world of data, analytics, and data science with our specialized courses.', NULL, '2024-02-05 16:16:57', '2024-02-05 16:16:57', 0, 1, NULL),
(17, 'Free Courses', 'Access a collection of high-quality courses available for free to enhance your skills.', NULL, '2024-02-05 16:16:57', '2024-02-05 16:16:57', 0, 1, NULL),
(18, 'Analytics', 'Master the art of data analysis and gain insights with our analytics-focused courses.', NULL, '2024-02-05 16:16:57', '2024-02-05 16:16:57', 0, 1, NULL),
(19, 'Mobile Development', 'Learn to build innovative mobile applications with our comprehensive mobile development courses.', NULL, '2024-02-05 16:16:57', '2024-02-05 16:16:57', 0, 1, NULL),
(20, 'Hacking', 'Explore the exciting world of ethical hacking and cybersecurity to protect digital systems.', NULL, '2024-02-05 16:16:57', '2024-02-05 16:16:57', 0, 1, NULL),
(21, 'Cyber Security', 'Enhance your cybersecurity skills and stay ahead in the constantly evolving digital landscape.', NULL, '2024-02-05 16:16:57', '2024-02-05 16:16:57', 0, 1, NULL),
(22, 'Programming', 'Build a solid foundation in programming languages and become a proficient coder.', NULL, '2024-02-05 16:16:57', '2024-02-05 16:16:57', 0, 1, NULL),
(23, 'Web Development', 'Become a web development expert with our courses covering front-end and back-end technologies.', NULL, '2024-02-05 16:16:57', '2024-02-05 16:16:57', 0, 1, NULL),
(24, 'Machine Learning', 'Delve into the realm of machine learning and artificial intelligence with our specialized courses.', NULL, '2024-02-05 16:16:57', '2024-02-05 16:16:57', 0, 1, NULL),
(25, 'Software Development', 'Master the software development life cycle and refine your coding skills.', NULL, '2024-02-05 16:16:57', '2024-02-05 16:16:57', 0, 1, NULL),
(26, 'Javascript', 'Explore the versatile world of JavaScript and create dynamic and interactive web pages.', NULL, '2024-02-05 16:16:57', '2024-02-05 16:16:57', 0, 1, NULL),
(27, 'Beginner', 'Perfect for beginners, these courses provide a gentle introduction to various subjects.', NULL, '2024-02-05 16:16:57', '2024-02-05 16:16:57', 0, 1, NULL),
(28, 'Advanced', 'Challenge yourself with advanced courses designed for experienced learners.', NULL, '2024-02-05 16:16:57', '2024-02-05 16:16:57', 0, 1, NULL),
(29, 'UI/UX Designs', 'Learn the principles of user interface and user experience design for creating visually appealing ap', NULL, '2024-02-05 16:16:57', '2024-02-05 16:16:57', 0, 1, NULL),
(30, 'Digital Marketing', 'Unlock the secrets of digital advertising and enhance your online presence.', NULL, '2024-02-05 16:16:57', '2024-02-05 16:16:57', 0, 1, NULL),
(31, 'Internet Of Things', 'Discover the fascinating world of IoT and build connected devices for the future.', NULL, '2024-02-05 16:16:57', '2024-02-05 16:16:57', 0, 1, NULL),
(32, 'Full Stack Development', 'Become a full-stack developer by mastering both front-end and back-end technologies.', NULL, '2024-02-05 16:16:57', '2024-02-05 16:16:57', 0, 1, NULL),
(33, 'Artificial Intelligence', 'Dive deep into the world of AI and explore its applications in various domains.', NULL, '2024-02-05 16:16:57', '2024-02-05 16:16:57', 0, 1, NULL),
(34, 'Python', 'Learn the popular programming language Python and its versatile applications.', NULL, '2024-02-05 16:16:57', '2024-02-05 16:16:57', 0, 1, NULL),
(35, 'Game Development', 'Create your own interactive games with our game development courses.', NULL, '2024-02-05 16:16:57', '2024-02-05 16:16:57', 0, 1, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `category_course_association`
--

CREATE TABLE `category_course_association` (
  `course_id` int(11) DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `category_course_association`
--

INSERT INTO `category_course_association` (`course_id`, `category_id`) VALUES
(30, 25),
(31, 25),
(32, 27),
(33, 20),
(34, 20),
(35, 33),
(36, 33),
(37, 13),
(38, 23),
(39, 30),
(40, 29),
(41, 20),
(42, 20),
(43, 20),
(44, 20),
(45, 23),
(46, 13),
(47, 30),
(48, 27),
(49, 22),
(50, 22),
(51, 25),
(52, 25),
(53, 28),
(54, 28),
(55, 28),
(56, 25),
(57, 25),
(58, 22),
(59, 26),
(60, 13),
(61, 18),
(62, 18),
(63, 18),
(64, 18),
(65, 25),
(66, 25),
(67, 25),
(68, 25),
(69, 25),
(70, 25),
(71, 25),
(72, 25),
(73, 25),
(74, 25),
(75, 25),
(76, 25),
(77, 25),
(78, 25),
(79, 25),
(80, 25),
(81, 25),
(82, 25),
(83, 25),
(84, 25),
(85, 25),
(86, 25),
(87, 25),
(88, 25),
(89, 25),
(90, 25),
(91, 25),
(92, 25),
(93, 25),
(94, 25),
(95, 25),
(96, 25),
(97, 25),
(98, 19),
(99, 19),
(100, 19),
(101, 13);

-- --------------------------------------------------------

--
-- Table structure for table `chat`
--

CREATE TABLE `chat` (
  `id` int(11) NOT NULL,
  `_from` int(11) NOT NULL,
  `_to` int(11) NOT NULL,
  `_text` varchar(140) DEFAULT NULL,
  `_media` varchar(140) DEFAULT NULL,
  `_sticker` varchar(140) DEFAULT NULL,
  `_from_del` tinyint(1) NOT NULL,
  `_to_del` tinyint(1) NOT NULL,
  `_seen` tinyint(1) NOT NULL,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `content`
--

CREATE TABLE `content` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `body` text NOT NULL,
  `image` varchar(255) DEFAULT NULL,
  `descr` text DEFAULT NULL,
  `completed` tinyint(1) DEFAULT NULL,
  `topic_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `id` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `desc` text DEFAULT NULL,
  `video` varchar(1000) DEFAULT NULL,
  `material` varchar(100) DEFAULT NULL,
  `fee` int(11) DEFAULT NULL,
  `lang` varchar(50) DEFAULT NULL,
  `duration` varchar(50) DEFAULT NULL,
  `level` varchar(50) DEFAULT NULL,
  `views` int(11) DEFAULT NULL,
  `comment` int(11) DEFAULT NULL,
  `rating` int(11) DEFAULT NULL,
  `completedby` int(11) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `slug` varchar(50) DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `image` varchar(20) NOT NULL,
  `category_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`id`, `title`, `desc`, `video`, `material`, `fee`, `lang`, `duration`, `level`, `views`, `comment`, `rating`, `completedby`, `status`, `slug`, `created`, `updated`, `deleted`, `active`, `image`, `category_id`) VALUES
(30, 'React Native', '\"[\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"What Will I Learn?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"React Native is an open-source mobile application framework created by Facebook, Inc\\\",\\r\\n            \\\"This course will get you started with the fundamentals of React Native and will make you up and running with cross-platform app development\\\",\\r\\n            \\\"Creating your first application in React Native and understanding the concept of components\\\",\\r\\n            \\\"Understanding the design process and styling the components\\\",\\r\\n            \\\"Working with Images in React Native and understanding how to render an image in the app and related concepts\\\",\\r\\n            \\\"Working with various layouts such as ScrollView and ListView in React Native\\\",\\r\\n            \\\"Handling user interaction and work with buttons, events, animations, and much more\\\",\\r\\n            \\\"Understanding the concept of navigation and getting familiar with something called the router\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Who is the target audience?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Students and industry professionals who wish to get hands-on an amazing cross-platform app development framework - React Native\\\",\\r\\n            \\\"Users who wish to learn cross-platform application development and get into the field of mobile application development\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Benefits\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"React Native is Community-driven\\\",\\r\\n            \\\"Maximum code reuse & cost saving\\\",\\r\\n            \\\"Live reload\\\",\\r\\n            \\\"Strong performance for mobile environments\\\",\\r\\n            \\\"Modular and intuitive architecture similar to React\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Salary\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Average Salary: $117,277 per year\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Requirements\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"Previous experience with mobile application development will be beneficial\\\",\\r\\n            \\\"Familiarity with React JS, ES6, and Modern JavaScript is a must\\\"\\r\\n        ]\\r\\n    }\\r\\n    \\r\\n]\\r\\n\"', NULL, NULL, 2300, 'en', 'weeks', 'pro', 76, NULL, NULL, NULL, 'published', 'react-native', '2024-02-09 14:45:06', '2024-02-09 14:45:06', 0, 1, 'react_native.png', 25),
(31, 'Flutter', '\"[\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"flutter.png\\\",\\r\\n        \\\"title\\\": \\\"What Will I Learn?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Flutter is Google\'s UI toolkit for crafting beautiful, natively compiled applications for mobile, web, and desktop from a single codebase.\\\",\\r\\n            \\\"This course will get you started with Flutter and help you understand the basic concepts and architecture of Flutter\\\",\\r\\n            \\\"Working with Flutter widgets, layouts, dialogs, images, and so much more\\\",\\r\\n            \\\"Understanding the Flutter state management and related concepts\\\",\\r\\n            \\\"Getting started with Flutter animations\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"flutter.png\\\",\\r\\n        \\\"title\\\": \\\"Who is the target audience?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Students and industry professionals who wish to add the latest app development skills in the pockets\\\",\\r\\n            \\\"Students who wish to get hands-on mobile application development using Dart and Flutter\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"flutter.png\\\",\\r\\n        \\\"title\\\": \\\"Benefits\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Same UI and Business Logic in All Platforms\\\",\\r\\n            \\\"Reduced Code Development Time\\\",\\r\\n            \\\"Increased Time-to-Market Speed\\\",\\r\\n            \\\"Similar to Native App Performance\\\",\\r\\n            \\\"Custom, Animated UI of Any Complexity Available\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"flutter.png\\\",\\r\\n        \\\"title\\\": \\\"Salary\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Average Salary : $87,820 USD per year\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"flutter.png\\\",\\r\\n        \\\"title\\\": \\\"Requirements\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"Basic understanding of mobile application development and how it works\\\",\\r\\n            \\\"Familiarity with Dart programming is a must\\\"\\r\\n        ]\\r\\n    }\\r\\n    \\r\\n]\\r\\n\"', NULL, NULL, 20, 'en', 'weeks', 'pro', 57, NULL, NULL, NULL, 'published', 'flutter-x8', '2024-02-13 09:37:19', '2024-02-13 09:37:19', 0, 1, 'default.webp', 19),
(32, 'Computer Fundamentals', '\"[\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"What Will I Learn?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"How do we communicate with the computer.\\\",\\r\\n            \\\"How to give instructions to a Computer to perform a task.\\\",\\r\\n            \\\"How to help a computer make decisions.\\\",\\r\\n            \\\"Common mistakes made by a programmer.\\\",\\r\\n            \\\"What is a programming language.\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Who is the target audience?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Those who want to start a career in Computer programming.\\\",\\r\\n            \\\"This is the best suitable course for those who want to know how a computer performs a task in a simple and easy way.\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Benefits\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Get a clear understanding of how a computer performs a task.\\\",\\r\\n            \\\"The course is made so simple that after doing this course you won\'t find it difficult to start with any programming language.\\\",\\r\\n            \\\"Live reload\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Salary\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"25,000 USD per year\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Requirements\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"A strong work ethic, willingness to learn, and plenty of excitement about the awesome new programs you\\u2019re about to build\\\",\\r\\n            \\\"Nothing else! It\\u2019s just you, your phone/laptop and your hunger to get started today\\\"\\r\\n          ]\\r\\n    }\\r\\n    \\r\\n]\\r\\n\"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 34, NULL, NULL, NULL, 'published', 'computer-fundamentals', '2024-02-15 13:30:53', '2024-02-15 13:30:53', 0, 1, 'default.webp', 27),
(33, 'Ethical Hacking', '\"[\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"What Will I Learn?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Start from scratch and learn all basic concepts used in hacking upto intermediate level.\\\",\\r\\n            \\\"Learn what is ethical hacking, it\'s fields and different types of hackers\\\",\\r\\n            \\\"Discovering vulnerability in systems & exploit them to hack servers\\\",\\r\\n            \\\"Various hacking tools.\\\",\\r\\n            \\\"Types of hacking techniques.\\\",\\r\\n            \\\"Case studies and getting started with hacking\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Who is the target audience?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Anyone who wants to learn hacking from scratch or brush up his knowledge in hacking\\\",\\r\\n            \\\"If you wish to build a career in cyber security or professional white hat hacking\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Benefits\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Get a clear understanding of hacking & how to stay safe and anonymous.\\\",\\r\\n            \\\"Become job ready in the field of hacking.\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Salary\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"72,000 USD per year\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Requirements\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"Anyone with keen interest in learning hacking\\\",\\r\\n            \\\"Having knowledge of basic programming languages and software architecture is a plus point\\\",\\r\\n            \\\"Hunger to learn, practice and you can get started today!\\\"\\r\\n          ]\\r\\n    }\\r\\n    \\r\\n]\\r\\n\"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 16, NULL, NULL, NULL, 'published', 'ethical-hacking', '2024-02-15 14:36:28', '2024-02-15 14:36:28', 0, 1, 'default.webp', 20),
(34, 'Hacking Advanced', '\"[\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ai.png\\\",\\r\\n        \\\"title\\\": \\\"What Will I Learn?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Hacking has been a part of computing for almost five decades and it is a very broad discipline, which covers a wide range of topics.\\\",\\r\\n            \\\"Continuing the basics journey, to taking stuff to intermediate to advanced level\\\",\\r\\n            \\\"In this course, you will come across many practical methods that will enhance your hacking skills.\\\",\\r\\n            \\\"Top hacking skills such as Password breaking, Being anonymous, Art of secret writing and hiding, XSS and much more.\\\",\\r\\n            \\\"In this course, we will take you through the various concepts of Ethical Hacking and explain how you can use them in a real-time environment.\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ai.png\\\",\\r\\n        \\\"title\\\": \\\"Who is the target audience?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"This tutorial has been prepared for professionals aspiring to make a career as an ethical hacker.\\\",\\r\\n            \\\"For both, students and industry experts that want to take their basic hacking skills to a level up.\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ai.png\\\",\\r\\n        \\\"title\\\": \\\"Benefits\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Fighting against terrorism and national security breaches.\\\",\\r\\n            \\\"Having a computer system that prevents malicious hackers from gaining access.\\\",\\r\\n            \\\"Having adequate preventative measures in place to prevent security breaches.\\\",\\r\\n            \\\"Numerous opportunities and a career designation full of exciting challenges.\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ai.png\\\",\\r\\n        \\\"title\\\": \\\"Salary\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Average Salary : $111,502 per year\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ai.png\\\",\\r\\n        \\\"title\\\": \\\"Requirements\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"Before proceeding to this course you should have knowledge of hacking basics.\\\",\\r\\n            \\\"It is highly recommended to go through the Hacking Basic course first which is available on this application.\\\"\\r\\n        ]\\r\\n    }\\r\\n    \\r\\n]\"', NULL, NULL, 0, 'en', 'weeks', 'pro', 53, NULL, NULL, NULL, 'published', 'hacking-advanced', '2024-02-19 14:53:44', '2024-02-19 14:53:44', 0, 1, 'default.webp', 20),
(35, 'Artificial Intelligence', '\"[\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ai.png\\\",\\r\\n        \\\"title\\\": \\\"What Will I Learn?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Get a clear understanding about Artificial Intelligence.\\\",\\r\\n            \\\"How a computer can take a decision on its own.\\\",\\r\\n            \\\"Various types of Artificial Intelligence available.\\\",\\r\\n            \\\"Understanding Agents and Environments.\\\",\\r\\n            \\\"Understanding about the issues with Artificial Intelligence.\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ai.png\\\",\\r\\n        \\\"title\\\": \\\"Who is the target audience?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Who is curious to know how the basics functionality of Google now, Siri, Cortana or other AI.\\\",\\r\\n            \\\"Those who want to start their career in AI, this course can give you a clear idea about the basics of AI.\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ai.png\\\",\\r\\n        \\\"title\\\": \\\"Benefits\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"AI can be applied to any industry, to solve problems, Hence the demand of engineers having a good knowledge of AI is increasing day by day.\\\",\\r\\n            \\\"Automobile companies are moving towards driverless cars to avoid any human error while driving a car.\\\",\\r\\n            \\\"Weather predictions are getting accurate thus helping people to plan their day.\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ai.png\\\",\\r\\n        \\\"title\\\": \\\"Salary\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"100,000 USD per year\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ai.png\\\",\\r\\n        \\\"title\\\": \\\"Requirements\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"Curiosity to know how a computer can think.\\\",\\r\\n            \\\"Nothing else! It\\u2019s just you, your phone and your hunger to get started today\\\"\\r\\n        ]\\r\\n    }\\r\\n    \\r\\n]\\r\\n\"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 12, NULL, NULL, NULL, 'published', 'artificial-intelligence', '2024-02-19 15:32:36', '2024-02-19 15:32:36', 0, 1, 'default.webp', 33),
(36, 'Machine Learning', '\"[\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ml.png\\\",\\r\\n        \\\"title\\\": \\\"What Will I Learn?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"How Machine learning works.\\\",\\r\\n            \\\"What are some simple applications of Machine learning.\\\",\\r\\n            \\\"What are the ethics of Machine learning.\\\",\\r\\n            \\\"How big is the future of Machine learning.\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ml.png\\\",\\r\\n        \\\"title\\\": \\\"Who is the target audience?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"People who are progressing their journey towards machine learning\\\",\\r\\n            \\\"Where there is data and it needs to be analyzed, Machine learning is the best way to do so.\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ml.png\\\",\\r\\n        \\\"title\\\": \\\"Benefits\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Data Science sector is increasing rapidly, so is the demand of people who can write algorithms to analyze that data.\\\",\\r\\n            \\\"With increasing amount of data, the accuracy of the result has to be increased.\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ml.png\\\",\\r\\n        \\\"title\\\": \\\"Salary\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"110,000 USD per year\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ml.png\\\",\\r\\n        \\\"title\\\": \\\"Requirements\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"Curiosity to know how your AI learns about you and gives you suggestions according to your need.\\\",\\r\\n            \\\"Nothing else! It\\u2019s just you, your phone and your hunger to get started today\\\"\\r\\n        ]\\r\\n    }\\r\\n    \\r\\n]\\r\\n\"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 13, NULL, NULL, NULL, 'published', 'machine-learnign-x', '2024-02-19 16:03:57', '2024-02-19 16:03:57', 0, 1, 'default.webp', 33),
(37, 'Data Science', '\"[\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"data_sc.png\\\",\\r\\n        \\\"title\\\": \\\"What Will I Learn?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Develop in depth understanding of the key technologies in data science and business analytics:\\\",\\r\\n            \\\"data mining, machine learning, visualization techniques, predictive modeling, and statistics\\\",\\r\\n            \\\"Practice problem analysis and decision-making\\\",\\r\\n            \\\"Gain practical, hands-on experience with statistics programming languages and big data tools through coursework\\\",\\r\\n            \\\"Employ cutting edge tools and technologies to analyze Big Data\\\",\\r\\n            \\\"Apply algorithms to build machine intelligence\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"data_sc.png\\\",\\r\\n        \\\"title\\\": \\\"Who is the target audience?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Anybody with an interest in Data Science\\\",\\r\\n            \\\"Anybody who wants to improve their data mining skills\\\",\\r\\n            \\\"Anybody who wants to improve their statistical modelling skills\\\",\\r\\n            \\\"Anybody who wants to improve their data preparation skills\\\",\\r\\n            \\\"Anybody who wants to improve their Data Science presentation skills\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"data_sc.png\\\",\\r\\n        \\\"title\\\": \\\"Benefits\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"This course will give you a full overview of the Data Science journey. Upon completing this course you will know:\\\",\\r\\n            \\\"How to clean and prepare your data for analysis\\\",\\r\\n            \\\"How to perform basic visualisation of your data\\\",\\r\\n            \\\"How to model your data\\\",\\r\\n            \\\"How to curve-fit your data\\\",\\r\\n            \\\"And finally, how to present your findings and wow the audience\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"data_sc.png\\\",\\r\\n        \\\"title\\\": \\\"Salary\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"According to Google, A data scientist earns around 1.2M $ per year\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"data_sc.png\\\",\\r\\n        \\\"title\\\": \\\"Requirements\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"Only a passion for success\\\",\\r\\n            \\\"All software used in this course is either available for Free or as a Demo version\\\"\\r\\n        ]\\r\\n    }\\r\\n    \\r\\n]\"', NULL, NULL, 110, 'en', 'weeks', 'pro', 15, NULL, NULL, NULL, 'published', 'data-scien', '2024-02-19 16:48:12', '2024-02-19 16:48:12', 0, 1, 'default.webp', 13),
(38, 'Web Design', '\"[\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"data_sc.png\\\",\\r\\n        \\\"title\\\": \\\"Highlights?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"By the end of this course, you will have a basic & thorough understanding of HTML & CSS\\\",\\r\\n            \\\"Code a useful HTML & CSS examples\\\",\\r\\n            \\\"Focus on building a beautiful, semantic, HTML & CSS web page\\\",\\r\\n            \\\"Start building beautiful websites\\\",\\r\\n            \\\"Get the ball rolling for a career in web design\\\"\\r\\n        ]\\r\\n    }\\r\\n    \\r\\n]\\r\\n\"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 16, NULL, NULL, NULL, 'published', 'web-design', '2024-02-19 17:00:51', '2024-02-19 17:00:51', 0, 1, 'default.webp', 23),
(39, 'Digital Marketing Advanced', '\"[\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"digital_mark.png\\\",\\r\\n        \\\"title\\\": \\\"What Will I Learn?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Understanding Marketing and its transition in this Digital world.\\\",\\r\\n            \\\"Getting hands-on dozens of proven digital marketing strategies.\\\",\\r\\n            \\\"Improving your brand identity and grow your brand\'s audience\\\",\\r\\n            \\\"Understanding how to find the right audience and performing Market Research\\\",\\r\\n            \\\"Getting hands-on A/B Testing\\\",\\r\\n            \\\"Diving into social media marketing using all of the most popular social media platforms to grow your business\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"digital_mark.png\\\",\\r\\n        \\\"title\\\": \\\"Who is the target audience?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Entrepreneurs, business owners, bloggers, YouTubers, social media fans\\\",\\r\\n            \\\"Website owners who want to increase web traffic, conversions, and sales.:\\\",\\r\\n            \\\"Business owners who want to use digital marketing to grow their business.\\\",\\r\\n            \\\"Anyone wanting to do their own marketing\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"digital_mark.png\\\",\\r\\n        \\\"title\\\": \\\"Benefits\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"A well planned digital marketing campaign can reach thousands of people at a much lower cost than traditional marketing methods.\\\",\\r\\n            \\\"Digitalization has turned the world into a global village.\\\",\\r\\n            \\\"Digital Marketing allows ad campaigns to be visible in any part of the world at any time.\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"digital_mark.png\\\",\\r\\n        \\\"title\\\": \\\"Salary\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Average salary : $64,500 USD per year\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"digital_mark.png\\\",\\r\\n        \\\"title\\\": \\\"Requirements\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"No prior marketing knowledge required, just sound knowledge of how businesses run and being friendly with computers is added advantage.\\\",\\r\\n            \\\"Check out our Digital Marketing Advanced Course\\\",\\r\\n            \\\"You should be ready to take action and see real results!n\\\"\\r\\n        ]\\r\\n    }\\r\\n    \\r\\n]\\r\\n\"', NULL, NULL, 39, 'en', 'weeks', 'pro', 27, NULL, NULL, NULL, 'published', 'digital-ma', '2024-02-19 17:30:55', '2024-02-19 17:30:55', 0, 1, 'default.webp', 30),
(40, 'UI/UX', '\"[\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ui_ux.png\\\",\\r\\n        \\\"title\\\": \\\"What Will I Learn?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Brief introduction to User interface and User experience Design\\\",\\r\\n            \\\"Fundamentals and principles of UI/UX Design\\\",\\r\\n            \\\"Tips and techniques for a better real world design\\\",\\r\\n            \\\"Some real life examples and cases to make the concept of UI/UX clear\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ui_ux.png\\\",\\r\\n        \\\"title\\\": \\\"Who is the target audience?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"User who want to make a career in user interface or user experience design\\\",\\r\\n            \\\"Both students and industry professionals who want to expand their skill set\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ui_ux.png\\\",\\r\\n        \\\"title\\\": \\\"Benefits\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Digital products at all stages of maturity benefit from User Interface (UI) Design\\\",\\r\\n            \\\"User disappointment and costly, time consuming redesigns are avoided as usability, presentation and behaviour are fully addressed in the design process\\\",\\r\\n            \\\"Style Guides communicate key design information to the Product Management and Development team regardless of previous experience with the project or User Interface (UI)\\\",\\r\\n            \\\"Increasing the usability of product\\\",\\r\\n            \\\"Meeting the level of customer/user satisfaction\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ui_ux.png\\\",\\r\\n        \\\"title\\\": \\\"Salary\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Average Salary : $128,000 per year\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ui_ux.png\\\",\\r\\n        \\\"title\\\": \\\"Requirements\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"Not much, but a little front end design/development knowledge is beneficial\\\",\\r\\n            \\\"Little knowledge of human psychology\\\",\\r\\n            \\\"One most important thing - Patience and Hardwork\\\"\\r\\n        ]\\r\\n    }\\r\\n    \\r\\n]\\r\\n\"', NULL, NULL, 45, 'en', 'weeks', 'pro', 13, NULL, NULL, NULL, 'published', 'ui-ux-buah', '2024-02-20 10:19:16', '2024-02-20 10:19:16', 0, 1, 'default.webp', 29),
(41, 'Cyber Security', '\"[\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ai.png\\\",\\r\\n        \\\"title\\\": \\\"What Will I Learn?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Understanding the Basics of Cyber Security\\\",\\r\\n            \\\"Understanding Physical Security concepts\\\",\\r\\n            \\\"How cyber security applies in today\\u2019s digital world\\\",\\r\\n            \\\"Cyber attacks and Laws\\\",\\r\\n            \\\"Will go through with digital forensics\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ai.png\\\",\\r\\n        \\\"title\\\": \\\"Who is the target audience?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Beginners who want to learn something new other than programming\\\",\\r\\n            \\\"Those who are interested in hacking, security\\\",\\r\\n            \\\"People who want to learn fundamentals, laws, attacks and move into core Cybersecurity and more\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ai.png\\\",\\r\\n        \\\"title\\\": \\\"Benefits\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Increased security\\\",\\r\\n            \\\"A job that never gets Boring!\\\",\\r\\n            \\\"Travel the World with Cybersecurity\\\",\\r\\n            \\\"No Math, No Coding!\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ai.png\\\",\\r\\n        \\\"title\\\": \\\"Salary\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Average Salary : $125,000 per Year\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ai.png\\\",\\r\\n        \\\"title\\\": \\\"Requirements\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"A willingness to learn Hacking skills\\\",\\r\\n            \\\"No programming experience is required\\\"\\r\\n        ]\\r\\n    }\\r\\n    \\r\\n]\"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 17, NULL, NULL, NULL, 'published', 'cyber-secu', '2024-02-20 15:40:22', '2024-02-20 15:40:22', 0, 1, 'default.webp', 20),
(42, 'Cloud Computing', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'cloud-comp', '2024-02-20 15:40:53', '2024-02-20 15:40:53', 0, 1, 'default.webp', 20),
(43, 'React Development', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 10, NULL, NULL, NULL, 'published', 'react-deve', '2024-02-20 15:41:32', '2024-02-20 15:41:32', 0, 1, 'react_js.webp', 26),
(44, 'GIT', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'git-srkj5e', '2024-02-20 15:41:56', '2024-02-20 15:41:56', 0, 1, 'default.webp', 20),
(45, 'Foundation framework', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'foundation', '2024-02-20 15:44:02', '2024-02-20 15:44:02', 0, 1, 'default.webp', 23),
(46, 'Programming.', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'programmin', '2024-02-20 15:45:55', '2024-02-20 15:45:55', 0, 1, 'default.webp', 13),
(47, 'SEO', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'seo-bggrps', '2024-02-20 15:47:09', '2024-02-20 15:47:09', 0, 1, 'default.webp', 30),
(48, 'IT Basics', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'it-basics-', '2024-02-20 15:47:47', '2024-02-20 15:47:47', 0, 1, 'default.webp', 27),
(49, 'Linux', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'linux-d50o', '2024-02-20 15:48:05', '2024-02-20 15:48:05', 0, 1, 'default.webp', 22),
(50, 'Shell Scripting', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 2, NULL, NULL, NULL, 'published', 'shell-scri', '2024-02-20 15:48:29', '2024-02-20 15:48:29', 0, 1, 'default.webp', 22),
(51, 'Devops Engineering', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 2, NULL, NULL, NULL, 'published', 'devops-eng', '2024-02-20 15:50:43', '2024-02-20 15:50:43', 0, 1, 'default.webp', 25),
(52, 'Cryptography', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'cryptograp', '2024-02-20 15:51:28', '2024-02-20 15:51:28', 0, 1, 'default.webp', 25),
(53, 'AWS Cloud Computing', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'aws-cloud-', '2024-02-20 15:55:28', '2024-02-20 15:55:28', 0, 1, 'default.webp', 28),
(54, 'IPV4 & Networking', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'ipv4---net', '2024-02-20 15:55:47', '2024-02-20 15:55:47', 0, 1, 'default.webp', 28),
(55, 'Computer Networks', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'computer-n', '2024-02-20 15:56:08', '2024-02-20 15:56:08', 0, 1, 'default.webp', 28),
(56, 'Software Testing', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'software-t', '2024-02-20 15:56:43', '2024-02-20 15:56:43', 0, 1, 'default.webp', 25),
(57, 'Software Engineering', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'software-e', '2024-02-20 15:56:55', '2024-02-20 15:56:55', 0, 1, 'default.webp', 25),
(58, 'Object Oriented Programming(OOPS).', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'object-ori', '2024-02-20 15:57:29', '2024-02-20 15:57:29', 0, 1, 'default.webp', 22),
(59, 'JavaScript Advanced', '\"[\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"js.png\\\",\\r\\n        \\\"title\\\": \\\"What Will I Learn?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"To Play with Strings\\\",\\r\\n            \\\"Objects in JS\\\",\\r\\n            \\\"Document Object Model (DOM)\\\",\\r\\n            \\\"Manipulating HTML Elements\\\",\\r\\n            \\\"Manipulating CSS Elements\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"js.png\\\",\\r\\n        \\\"title\\\": \\\"Who is the target audience?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Interested in improving your web development skills.\\\",\\r\\n            \\\"If you want to make some advanced and dynamic websites, this course is for you.\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"js.png\\\",\\r\\n        \\\"title\\\": \\\"Benefits\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"There are a lot of platforms available for Javascript like Node JS, Angular JS etc, you can advanced to any platform after completing this course.\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"js.png\\\",\\r\\n        \\\"title\\\": \\\"Salary\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"58,000 USD per year\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"js.png\\\",\\r\\n        \\\"title\\\": \\\"Requirements\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"Basic concepts of Javascript, HTML, and CSS should be clear.\\\",\\r\\n            \\\"A strong work ethic, willingness to learn, and plenty of excitement about the awesome new programs you\\u2019re about to build\\\"\\r\\n        ]\\r\\n    }\\r\\n    \\r\\n]\\r\\n\"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 8, NULL, NULL, NULL, 'published', 'javascript', '2024-02-20 16:29:34', '2024-02-20 16:29:34', 0, 1, 'default.webp', 26),
(60, 'Growth Hacking', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 1, NULL, NULL, NULL, 'published', 'growth-hac', '2024-02-21 22:52:47', '2024-02-21 22:52:47', 0, 1, 'default.webp', 13),
(61, 'Big Data Analysis', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'big-data-a', '2024-02-21 22:53:32', '2024-02-21 22:53:32', 0, 1, 'default.webp', 18),
(62, 'Unity', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'unity-qcto', '2024-02-21 22:53:48', '2024-02-21 22:53:48', 0, 1, 'default.webp', 18),
(63, 'Social Media Marketing', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'social-med', '2024-02-21 22:54:13', '2024-02-21 22:54:13', 0, 1, 'default.webp', 18),
(64, 'Statistical Analysis', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'statistica', '2024-02-21 22:54:47', '2024-02-21 22:54:47', 0, 1, 'default.webp', 18),
(65, 'Blockchain', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 1, NULL, NULL, NULL, 'published', 'blockchain', '2024-02-21 22:55:11', '2024-02-21 22:55:11', 0, 1, 'default.webp', 25),
(66, 'Firebase', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'firebase-c', '2024-02-21 22:56:37', '2024-02-21 22:56:37', 0, 1, 'default.webp', 25),
(67, 'RDBMS', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'rdbms-smnm', '2024-02-21 22:56:51', '2024-02-21 22:56:51', 0, 1, 'default.webp', 25),
(68, 'Mongo DB', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'mongo-db-5', '2024-02-21 22:57:02', '2024-02-21 22:57:02', 0, 1, 'default.webp', 25),
(69, 'Postgress', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'postgress-', '2024-02-21 22:57:14', '2024-02-21 22:57:14', 0, 1, 'default.webp', 25),
(70, 'GraphQL', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'graphql-ig', '2024-02-21 22:57:28', '2024-02-21 22:57:28', 0, 1, 'default.webp', 25),
(71, 'SQL', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'sql-294ji1', '2024-02-21 22:57:37', '2024-02-21 22:57:37', 0, 1, 'default.webp', 25),
(72, 'PHP', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'php-7bwtly', '2024-02-21 22:58:18', '2024-02-21 22:58:18', 0, 1, 'default.webp', 25),
(73, 'Laravel', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'laravel-to', '2024-02-21 22:58:24', '2024-02-21 22:58:24', 0, 1, 'default.webp', 25),
(74, 'Dart', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'dart-uzrit', '2024-02-21 22:58:29', '2024-02-21 22:58:29', 0, 1, 'default.webp', 25),
(75, 'Node JS', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'node-js-u8', '2024-02-21 22:58:43', '2024-02-21 22:58:43', 0, 1, 'default.webp', 25),
(76, 'Html 5 Advanced', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 11, NULL, NULL, NULL, 'published', 'html-5-adv', '2024-02-21 22:59:02', '2024-02-21 22:59:02', 0, 1, 'html_5.webp', 25),
(77, 'CSS 3', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'css-3-z9un', '2024-02-21 22:59:14', '2024-02-21 22:59:14', 0, 1, 'default.webp', 25),
(78, 'SASS', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'sass-zr1rx', '2024-02-21 22:59:19', '2024-02-21 22:59:19', 0, 1, 'sass.webp', 25),
(79, 'ReactJS', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'reactjs-vw', '2024-02-21 23:00:25', '2024-02-21 23:00:25', 0, 1, 'react.webp', 25),
(80, 'jQuery', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'jquery-bys', '2024-02-21 23:00:34', '2024-02-21 23:00:34', 0, 1, 'default.webp', 25),
(81, 'Next JS', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'next-js-ud', '2024-02-21 23:00:56', '2024-02-21 23:00:56', 0, 1, 'default.webp', 25),
(82, 'Typescript', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 2, NULL, NULL, NULL, 'published', 'typescript', '2024-02-21 23:01:00', '2024-02-21 23:01:00', 0, 1, 'default.webp', 25),
(83, 'Vue JS', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'vue-js-3ft', '2024-02-21 23:01:13', '2024-02-21 23:01:13', 0, 1, 'default.webp', 25),
(84, 'Express JS', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'express-js', '2024-02-21 23:01:21', '2024-02-21 23:01:21', 0, 1, 'default.webp', 25),
(85, 'Angular JS', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'angular-js', '2024-02-21 23:01:33', '2024-02-21 23:01:33', 0, 1, 'default.webp', 25),
(86, 'Boostrap', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'boostrap-r', '2024-02-21 23:01:39', '2024-02-21 23:01:39', 0, 1, 'default.webp', 25),
(87, 'Material Design', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'material-d', '2024-02-21 23:01:51', '2024-02-21 23:01:51', 0, 1, 'default.webp', 25),
(88, 'JAVA', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'java-lvqzo', '2024-02-21 23:01:57', '2024-02-21 23:01:57', 0, 1, 'default.webp', 25),
(89, 'Python', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 3, NULL, NULL, NULL, 'published', 'python-se2', '2024-02-21 23:02:02', '2024-02-21 23:02:02', 0, 1, 'default.webp', 25),
(90, 'Python Advanced', '\"[\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"python.png\\\",\\r\\n        \\\"title\\\": \\\"What Will I Learn?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Python is one of the top programming languages of the decade which is quite easy to learn and high in demand\\\",\\r\\n            \\\"In this course, we would explore the advanced concepts of Python programming and take your skills one level up\\\",\\r\\n            \\\"Understanding concepts such as File and Exception handling in Python\\\",\\r\\n            \\\"Exploring Python modules and their related topics, getting hands-on the concept of Regular Expressions\\\",\\r\\n            \\\"Getting started with database connection in Python and learning how to connect a Python project to a database and perform CRUD operations\\\",\\r\\n            \\\"Learning one of the most important concepts of programming called object-oriented programming\\\",\\r\\n            \\\"Getting started with GUI development using Python and getting hands-on the concept of multithreading\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"python.png\\\",\\r\\n        \\\"title\\\": \\\"Who is the target audience?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Students and industry professionals who wish to get hands-on one of the most demand programming language - Python\\\",\\r\\n            \\\"Users who wish to dive deep into Python and explore the advanced concepts by taking their skills to next level\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"python.png\\\",\\r\\n        \\\"title\\\": \\\"Benefits\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Easy to learn\\\",\\r\\n            \\\"High in demand\\\",\\r\\n            \\\"General-purpose and diverse use cases\\\",\\r\\n            \\\"Greater job and career opportunities\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"python.png\\\",\\r\\n        \\\"title\\\": \\\"Salary\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Average Salary: $110,840 per year\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"python.png\\\",\\r\\n        \\\"title\\\": \\\"Requirements\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"Previous experience with programming and knowledge of the basics of Python is required\\\",\\r\\n            \\\"Should have completed the Python or Python3 course available on this application\\\"\\r\\n        ]\\r\\n    }\\r\\n    \\r\\n]\"', NULL, NULL, 120, 'en', 'weeks', 'pro', 6, NULL, NULL, NULL, 'published', 'python-3-h', '2024-02-21 23:02:18', '2024-02-21 23:02:18', 0, 1, 'default.webp', 22),
(91, 'Python Django', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'python-dja', '2024-02-21 23:02:25', '2024-02-21 23:02:25', 0, 1, 'default.webp', 25),
(92, 'Python Flask', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 1, NULL, NULL, NULL, 'published', 'python-fla', '2024-02-21 23:02:40', '2024-02-21 23:02:40', 0, 1, 'default.webp', 25),
(93, 'Python For Artificial Intelligence', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'python-for', '2024-02-21 23:03:04', '2024-02-21 23:03:04', 0, 1, 'default.webp', 25),
(94, 'Swift', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'swift-m5lp', '2024-02-21 23:03:33', '2024-02-21 23:03:33', 0, 1, 'default.webp', 25),
(95, 'Ruby', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'ruby-jz2bt', '2024-02-21 23:03:46', '2024-02-21 23:03:46', 0, 1, 'default.webp', 25),
(96, 'C#', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'c-ddsiecub', '2024-02-21 23:03:56', '2024-02-21 23:03:56', 0, 1, 'default.webp', 25),
(97, 'C++', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'c-zu4hq7fg', '2024-02-21 23:04:01', '2024-02-21 23:04:01', 0, 1, 'default.webp', 25),
(98, 'Android Development ', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'android-de', '2024-02-22 00:35:00', '2024-02-22 00:35:00', 0, 1, 'default.webp', 19),
(99, 'IOS Development ', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'ios-develo', '2024-02-22 00:35:09', '2024-02-22 00:35:09', 0, 1, 'default.webp', 19),
(100, 'Computer Vision Using... ', '\"Enter Your Description Here  \"', NULL, NULL, NULL, 'en', 'weeks', 'pro', 0, NULL, NULL, NULL, 'published', 'computer-v', '2024-02-22 00:35:25', '2024-02-22 00:35:25', 0, 1, 'default.webp', 19);

-- --------------------------------------------------------

--
-- Table structure for table `course_tag_association`
--

CREATE TABLE `course_tag_association` (
  `course_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `enrollment`
--

CREATE TABLE `enrollment` (
  `id` int(11) NOT NULL,
  `completed` tinyint(1) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `completed_topics` int(11) DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `enrollment`
--

INSERT INTO `enrollment` (`id`, `completed`, `user_id`, `course_id`, `completed_topics`, `created`, `updated`, `deleted`, `active`) VALUES
(8, 0, 2, 33, 1, '2024-02-26 14:28:23', '2024-02-26 14:28:23', 0, 1),
(9, 0, 2, 30, 6, '2024-02-26 14:30:55', '2024-02-26 14:30:55', 0, 1),
(10, 0, 2, 37, 0, '2024-02-26 15:59:53', '2024-02-26 15:59:53', 0, 1),
(13, 0, 2, 36, 0, '2024-03-11 13:00:35', '2024-03-11 13:00:35', 0, 1),
(15, 0, 2, 41, 0, '2024-03-12 13:28:21', '2024-03-12 13:28:21', 0, 1),
(16, 0, 2, 38, 0, '2024-03-12 13:30:05', '2024-03-12 13:30:05', 0, 1),
(17, 0, 2, 34, 4, '2024-03-12 13:39:41', '2024-03-12 13:39:41', 0, 1),
(18, 0, 2, 40, 0, '2024-03-12 13:42:10', '2024-03-12 13:42:10', 0, 1),
(19, 0, 2, 34, 0, '2024-03-20 04:35:43', '2024-03-20 04:35:43', 0, 1),
(20, 0, 2, 76, 0, '2024-03-20 05:15:30', '2024-03-20 05:15:30', 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `id` int(11) NOT NULL,
  `rating` int(11) DEFAULT NULL,
  `comment` text DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `interaction`
--

CREATE TABLE `interaction` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `rating` float DEFAULT NULL,
  `views` int(11) DEFAULT NULL,
  `purchase` tinyint(1) DEFAULT NULL,
  `like` tinyint(1) DEFAULT NULL,
  `comment` text DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  `is_enrolled` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `interaction`
--

INSERT INTO `interaction` (`id`, `user_id`, `course_id`, `rating`, `views`, `purchase`, `like`, `comment`, `timestamp`, `is_enrolled`) VALUES
(1, 2, 1, 2, 5, 1, 1, 'It\'s cool', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `lesson`
--

CREATE TABLE `lesson` (
  `id` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `desc` text DEFAULT NULL,
  `video` varchar(1000) DEFAULT NULL,
  `material` varchar(100) DEFAULT NULL,
  `fee` int(11) DEFAULT NULL,
  `lang` varchar(100) DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  `slug` varchar(130) DEFAULT NULL,
  `user` int(11) DEFAULT NULL,
  `course_id` int(11) NOT NULL,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `image` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `lesson`
--

INSERT INTO `lesson` (`id`, `title`, `desc`, `video`, `material`, `fee`, `lang`, `duration`, `slug`, `user`, `course_id`, `created`, `updated`, `deleted`, `active`, `image`) VALUES
(69, 'Let\'s Get Started', '\" \"', NULL, NULL, NULL, 'en', NULL, 'let-s-get-started-drk8aav2', NULL, 32, '2024-02-15 13:33:28', '2024-02-15 13:33:28', 0, 1, 'default.png'),
(70, 'Storage', '\" \"', NULL, NULL, NULL, 'en', NULL, 'storage-3kkuyib0', NULL, 32, '2024-02-15 13:33:39', '2024-02-15 13:33:39', 0, 1, 'default.png'),
(71, 'Repeating Things', '\" \"', NULL, NULL, NULL, 'en', NULL, 'repeating-things-euepyza7', NULL, 32, '2024-02-15 13:33:50', '2024-02-15 13:33:50', 0, 1, 'default.png'),
(72, 'Making Decisions', '\" \"', NULL, NULL, NULL, 'en', NULL, 'making-decisions-ifnltnh3', NULL, 32, '2024-02-15 13:34:13', '2024-02-15 13:34:13', 0, 1, 'default.png'),
(73, 'Creating Lists', '\" \"', NULL, NULL, NULL, 'en', NULL, 'creating-lists-rc4livf9', NULL, 32, '2024-02-15 13:34:28', '2024-02-15 13:34:28', 0, 1, 'default.png'),
(74, 'Grouping Instructions', '\" \"', NULL, NULL, NULL, 'en', NULL, 'grouping-instructions-lepngxhl', NULL, 32, '2024-02-15 13:34:46', '2024-02-15 13:34:46', 0, 1, 'default.png'),
(75, 'Avoiding Mistakes', '\" \"', NULL, NULL, NULL, 'en', NULL, 'avoiding-mistakes-lg403ryy', NULL, 32, '2024-02-15 13:35:03', '2024-02-15 13:35:03', 0, 1, 'default.png'),
(76, 'Using Computer Language', '\" \"', NULL, NULL, NULL, 'en', NULL, 'using-computer-language-mvcihpkn', NULL, 32, '2024-02-15 13:35:26', '2024-02-15 13:35:26', 0, 1, 'default.png'),
(78, 'Introduction To Hacking', '\" \"', NULL, NULL, NULL, 'en', NULL, 'introduction-to-hacking-oiuh8npr', NULL, 33, '2024-02-19 15:07:46', '2024-02-19 15:07:46', 0, 1, 'default.png'),
(79, 'Introduction To Security', '\" \"', NULL, NULL, NULL, 'en', NULL, 'introduction-to-security-bllnru60', NULL, 33, '2024-02-19 15:08:00', '2024-02-19 15:08:00', 0, 1, 'default.png'),
(80, 'Motivations', '\" \"', NULL, NULL, NULL, 'en', NULL, 'motivations-bai5gj9y', NULL, 33, '2024-02-19 15:08:16', '2024-02-19 15:08:16', 0, 1, 'default.png'),
(81, 'Types Of Hackers', '\" \"', NULL, NULL, NULL, 'en', NULL, 'types-of-hackers-hwgdz6uy', NULL, 33, '2024-02-19 15:08:32', '2024-02-19 15:08:32', 0, 1, 'default.png'),
(82, 'Malware', '\" \"', NULL, NULL, NULL, 'en', NULL, 'malware-kjwnt2ez', NULL, 33, '2024-02-19 15:08:44', '2024-02-19 15:08:44', 0, 1, 'default.png'),
(83, 'Virus', '\" \"', NULL, NULL, NULL, 'en', NULL, 'virus-i9ot7kdi', NULL, 33, '2024-02-19 15:08:56', '2024-02-19 15:08:56', 0, 1, 'default.png'),
(84, 'Worms & Trojans', '\" \"', NULL, NULL, NULL, 'en', NULL, 'worms---trojans-eorfgid6', NULL, 33, '2024-02-19 15:09:04', '2024-02-19 15:09:04', 0, 1, 'default.png'),
(85, 'Information Gathering', '\" \"', NULL, NULL, NULL, 'en', NULL, 'information-gathering-swwfyvdq', NULL, 33, '2024-02-19 15:09:22', '2024-02-19 15:09:22', 0, 1, 'default.png'),
(86, 'System Hacking', '\" \"', NULL, NULL, NULL, 'en', NULL, 'system-hacking-zgjshjvh', NULL, 33, '2024-02-19 15:09:34', '2024-02-19 15:09:34', 0, 1, 'default.png'),
(87, 'website Hacking', '\" \"', NULL, NULL, NULL, 'en', NULL, 'website-hacking-ohq10mkb', NULL, 33, '2024-02-19 15:09:47', '2024-02-19 15:09:47', 0, 1, 'default.png'),
(90, 'AI Basics', '\" \"', NULL, NULL, NULL, 'en', NULL, 'ai-basics-7whq9feh', NULL, 35, '2024-02-19 15:33:48', '2024-02-19 15:33:48', 0, 1, 'default.png'),
(91, 'Talking About Natural Intelligence', '\" \"', NULL, NULL, NULL, 'en', NULL, 'talking-about-natural-intellig-gsmq3tge', NULL, 35, '2024-02-19 15:34:05', '2024-02-19 15:34:05', 0, 1, 'default.png'),
(92, 'Reasoning', '\" \"', NULL, NULL, NULL, 'en', NULL, 'reasoning-afptu2c2', NULL, 35, '2024-02-19 15:34:23', '2024-02-19 15:34:23', 0, 1, 'default.png'),
(93, 'Learning', '\" \"', NULL, NULL, NULL, 'en', NULL, 'learning-qqop9kqc', NULL, 35, '2024-02-19 15:34:29', '2024-02-19 15:34:29', 0, 1, 'default.png'),
(94, 'Decision Making', '\" \"', NULL, NULL, NULL, 'en', NULL, 'decision-making-jludlh1y', NULL, 35, '2024-02-19 15:35:02', '2024-02-19 15:35:02', 0, 1, 'default.png'),
(95, 'Types of AI', '\" \"', NULL, NULL, NULL, 'en', NULL, 'types-of-ai-o51r8vns', NULL, 35, '2024-02-19 15:35:17', '2024-02-19 15:35:17', 0, 1, 'default.png'),
(96, 'Understanding Agents & Environments In AI', '\" \"', NULL, NULL, NULL, 'en', NULL, 'understanding-agents---environ-pscfqewz', NULL, 35, '2024-02-19 15:35:44', '2024-02-19 15:35:44', 0, 1, 'default.png'),
(97, 'Environments', '\" \"', NULL, NULL, NULL, 'en', NULL, 'environments-4fidxcnr', NULL, 35, '2024-02-19 15:35:50', '2024-02-19 15:35:50', 0, 1, 'default.png'),
(98, 'Related Technologies To AI', '\" \"', NULL, NULL, NULL, 'en', NULL, 'related-technologies-to-ai-f4dknur7', NULL, 35, '2024-02-19 15:36:09', '2024-02-19 15:36:09', 0, 1, 'default.png'),
(99, 'Issues With AI', '\" \"', NULL, NULL, NULL, 'en', NULL, 'issues-with-ai-ki9aaupv', NULL, 35, '2024-02-19 15:36:22', '2024-02-19 15:36:22', 0, 1, 'default.png'),
(100, 'Applications Of AI', '\" \"', NULL, NULL, NULL, 'en', NULL, 'applications-of-ai-llnmhgke', NULL, 35, '2024-02-19 15:36:32', '2024-02-19 15:36:32', 0, 1, 'default.png'),
(101, 'Introduction To Machine Learning', '\" \"', NULL, NULL, NULL, 'en', NULL, 'introduction-to-machine-learni-cylzfjmw', NULL, 36, '2024-02-19 16:04:46', '2024-02-19 16:04:46', 0, 1, 'default.png'),
(102, 'How Does It Work', '\" \"', NULL, NULL, NULL, 'en', NULL, 'how-does-it-work-bjfqdx9f', NULL, 36, '2024-02-19 16:05:46', '2024-02-19 16:05:46', 0, 1, 'default.png'),
(103, 'Useful Or Not', '\" \"', NULL, NULL, NULL, 'en', NULL, 'useful-or-not-km5ircmz', NULL, 36, '2024-02-19 16:06:06', '2024-02-19 16:06:06', 0, 1, 'default.png'),
(104, 'Simple Applications', '\" \"', NULL, NULL, NULL, 'en', NULL, 'simple-applications-5ntl7va8', NULL, 36, '2024-02-19 16:06:24', '2024-02-19 16:06:24', 0, 1, 'default.png'),
(105, 'Back In Time ', '\" \"', NULL, NULL, NULL, 'en', NULL, 'back-in-time-th6dyws0', NULL, 36, '2024-02-19 16:06:39', '2024-02-19 16:06:39', 0, 1, 'default.png'),
(106, 'The Working Details', '\" \"', NULL, NULL, NULL, 'en', NULL, 'the-working-details-dcugnytn', NULL, 36, '2024-02-19 16:06:55', '2024-02-19 16:06:55', 0, 1, 'default.png'),
(107, 'Approaches', '\" \"', NULL, NULL, NULL, 'en', NULL, 'approaches-ycwcgtib', NULL, 36, '2024-02-19 16:07:15', '2024-02-19 16:07:15', 0, 1, 'default.png'),
(108, 'The Real Deal', '\" \"', NULL, NULL, NULL, 'en', NULL, 'the-real-deal-6fiv9dwa', NULL, 36, '2024-02-19 16:07:23', '2024-02-19 16:07:23', 0, 1, 'default.png'),
(109, 'Ethics In ML', '\" \"', NULL, NULL, NULL, 'en', NULL, 'ethics-in-ml-ktcvgxdt', NULL, 36, '2024-02-19 16:07:38', '2024-02-19 16:07:38', 0, 1, 'default.png'),
(110, 'The Future Of ML', '\" \"', NULL, NULL, NULL, 'en', NULL, 'the-future-of-ml-p0184jqh', NULL, 36, '2024-02-19 16:07:59', '2024-02-19 16:07:59', 0, 1, 'default.png'),
(111, 'Introduction', '\" \"', NULL, NULL, NULL, 'en', NULL, 'introduction-xxloxome', NULL, 38, '2024-02-19 17:01:38', '2024-02-19 17:01:38', 0, 1, 'default.png'),
(112, 'Exploring The Result', '\" \"', NULL, NULL, NULL, 'en', NULL, 'exploring-the-result-x1mnkfvb', NULL, 38, '2024-02-19 17:02:44', '2024-02-19 17:02:44', 0, 1, 'default.png'),
(113, 'Structuring The Project', '\" \"', NULL, NULL, NULL, 'en', NULL, 'structuring-the-project-haqoec95', NULL, 38, '2024-02-19 17:03:02', '2024-02-19 17:03:02', 0, 1, 'default.png'),
(114, 'Creating The Home Page', '\" \"', NULL, NULL, NULL, 'en', NULL, 'creating-the-home-page-zc0rujqh', NULL, 38, '2024-02-19 17:03:19', '2024-02-19 17:03:19', 0, 1, 'default.png'),
(115, 'The About Page', '\" \"', NULL, NULL, NULL, 'en', NULL, 'the-about-page-nulrtk6h', NULL, 38, '2024-02-19 17:03:46', '2024-02-19 17:03:46', 0, 1, 'default.png'),
(116, 'The Services Page', '\" \"', NULL, NULL, NULL, 'en', NULL, 'the-services-page-gujgrsbd', NULL, 38, '2024-02-19 17:03:52', '2024-02-19 17:03:52', 0, 1, 'default.png'),
(117, 'The Contact Page', '\" \"', NULL, NULL, NULL, 'en', NULL, 'the-contact-page-b0qpqwkv', NULL, 38, '2024-02-19 17:04:12', '2024-02-19 17:04:12', 0, 1, 'default.png'),
(118, 'The Meta Tags', '\" \"', NULL, NULL, NULL, 'en', NULL, 'the-meta-tags-t5mo1g21', NULL, 38, '2024-02-19 17:04:26', '2024-02-19 17:04:26', 0, 1, 'default.png'),
(119, 'Uploading The Website On a Server', '\" \"', NULL, NULL, NULL, 'en', NULL, 'uploading-the-website-on-a-ser-m56gfi4i', NULL, 38, '2024-02-19 17:05:00', '2024-02-19 17:05:00', 0, 1, 'default.png'),
(120, 'Frameworks, Responsiveness & Buzz', '\" \"', NULL, NULL, NULL, 'en', NULL, 'frameworks--responsiveness---b-15arxvjw', NULL, 38, '2024-02-19 17:05:27', '2024-02-19 17:05:27', 0, 1, 'default.png'),
(121, 'Getting Started', '\" \"', NULL, NULL, NULL, 'en', NULL, 'getting-started-m19her3q', NULL, 39, '2024-02-19 17:31:39', '2024-02-19 17:31:39', 0, 1, 'default.png'),
(122, 'Market Research', '\" \"', NULL, NULL, NULL, 'en', NULL, 'market-research-ccud1glm', NULL, 39, '2024-02-19 17:31:50', '2024-02-19 17:31:50', 0, 1, 'default.png'),
(123, 'Website Development & A/B Testing', '\" \"', NULL, NULL, NULL, 'en', NULL, 'website-development---a-b-test-gpucitj3', NULL, 39, '2024-02-19 17:32:22', '2024-02-19 17:32:22', 0, 1, 'default.png'),
(124, 'Web Analytics', '\" \"', NULL, NULL, NULL, 'en', NULL, 'web-analytics-kstznhl8', NULL, 39, '2024-02-19 17:32:35', '2024-02-19 17:32:35', 0, 1, 'default.png'),
(125, 'Conversation Rate Optimization', '\" \"', NULL, NULL, NULL, 'en', NULL, 'conversation-rate-optimization-t1jk2fy6', NULL, 39, '2024-02-19 17:33:00', '2024-02-19 17:33:00', 0, 1, 'default.png'),
(126, 'Some Fundamentals', '\" \"', NULL, NULL, NULL, 'en', NULL, 'some-fundamentals-sobesbzc', NULL, 39, '2024-02-19 17:33:15', '2024-02-19 17:33:15', 0, 1, 'default.png'),
(128, 'Getting Started With UI/UX', '\" \"', NULL, NULL, NULL, 'en', NULL, 'getting-started-with-ui-ux-3asdrpk4', NULL, 40, '2024-02-20 10:19:59', '2024-02-20 10:19:59', 0, 1, 'default.png'),
(129, 'Consistency & Standards In UI/UX', '\" \"', NULL, NULL, NULL, 'en', NULL, 'consistency---standards-in-ui-a0cvesn7', NULL, 40, '2024-02-20 10:20:19', '2024-02-20 10:20:19', 0, 1, 'default.png'),
(130, 'A Few More Principles', '\" \"', NULL, NULL, NULL, 'en', NULL, 'a-few-more-principles-gsfyjyxr', NULL, 40, '2024-02-20 10:20:40', '2024-02-20 10:20:40', 0, 1, 'default.png'),
(131, 'It\'s All About Colors', '\" \"', NULL, NULL, NULL, 'en', NULL, 'it-s-all-about-colors-sddidmqt', NULL, 40, '2024-02-20 10:21:44', '2024-02-20 10:21:44', 0, 1, 'default.png'),
(132, 'Size Matters In UI/UX', '\" \"', NULL, NULL, NULL, 'en', NULL, 'size-matters-in-ui-ux-4wggny2q', NULL, 40, '2024-02-20 10:22:04', '2024-02-20 10:22:04', 0, 1, 'default.png'),
(133, 'Typography & Icons In UI/UX', '\" \"', NULL, NULL, NULL, 'en', NULL, 'typography---icons-in-ui-ux-dy94umcc', NULL, 40, '2024-02-20 10:22:31', '2024-02-20 10:22:31', 0, 1, 'default.png'),
(134, 'User Flow In UX', '\" \"', NULL, NULL, NULL, 'en', NULL, 'user-flow-in-ux-lpnewvii', NULL, 40, '2024-02-20 10:22:47', '2024-02-20 10:22:47', 0, 1, 'default.png'),
(135, 'The Final Steps', '\" \"', NULL, NULL, NULL, 'en', NULL, 'the-final-steps-fbggh9pt', NULL, 40, '2024-02-20 10:23:00', '2024-02-20 10:23:00', 0, 1, 'default.png'),
(136, 'How Much Do You KNow?', '\" \"', NULL, NULL, NULL, 'en', NULL, 'how-much-do-you-know-sk1v3myt', NULL, 40, '2024-02-20 10:23:18', '2024-02-20 10:23:18', 0, 1, 'default.png'),
(137, 'React Native - The Native Touch', '\" \"', NULL, NULL, NULL, 'en', NULL, 'react-native---the-native-touc-bl8zpkkh', NULL, 30, '2024-02-20 11:31:48', '2024-02-20 11:31:48', 0, 1, 'default.png'),
(138, 'Environment Set-Up', '\" \"', NULL, NULL, NULL, 'en', NULL, 'environment-set-up-wrcozd05', NULL, 30, '2024-02-20 11:32:10', '2024-02-20 11:32:10', 0, 1, 'default.png'),
(139, 'Our First Application', '\" \"', NULL, NULL, NULL, 'en', NULL, 'our-first-application-ikn5gaz0', NULL, 30, '2024-02-20 11:32:27', '2024-02-20 11:32:27', 0, 1, 'default.png'),
(140, 'The Design Process', '\" \"', NULL, NULL, NULL, 'en', NULL, 'the-design-process-0xt4mjlk', NULL, 30, '2024-02-20 11:32:51', '2024-02-20 11:32:51', 0, 1, 'default.png'),
(141, 'Images In React Native', '\" \"', NULL, NULL, NULL, 'en', NULL, 'images-in-react-native-znltcivi', NULL, 30, '2024-02-20 11:33:14', '2024-02-20 11:33:14', 0, 1, 'default.png'),
(142, 'The Component Library', '\" \"', NULL, NULL, NULL, 'en', NULL, 'the-component-library-9y9r3ubm', NULL, 30, '2024-02-20 11:33:32', '2024-02-20 11:33:32', 0, 1, 'default.png'),
(143, 'User Interactions', '\" \"', NULL, NULL, NULL, 'en', NULL, 'user-interactions-w6sda9ef', NULL, 30, '2024-02-20 11:33:46', '2024-02-20 11:33:46', 0, 1, 'default.png'),
(144, 'Understanding Navigation', '\" \"', NULL, NULL, NULL, 'en', NULL, 'understanding-navigation-abpvzd4h', NULL, 30, '2024-02-20 11:34:05', '2024-02-20 11:34:05', 0, 1, 'default.png'),
(145, 'Introduction To Flutter', '\" \"', NULL, NULL, NULL, 'en', NULL, 'introduction-to-flutter-m8ask2te', NULL, 31, '2024-02-20 12:09:32', '2024-02-20 12:09:32', 0, 1, 'default.png'),
(146, 'Creating A Simple Application', '\" \"', NULL, NULL, NULL, 'en', NULL, 'creating-a-simple-application-6dnmkzni', NULL, 31, '2024-02-20 12:09:59', '2024-02-20 12:09:59', 0, 1, 'default.png'),
(147, 'Architecture & Behind The Screen', '\" \"', NULL, NULL, NULL, 'en', NULL, 'architecture---behind-the-scre-gmh5d8j2', NULL, 31, '2024-02-20 12:10:28', '2024-02-20 12:10:28', 0, 1, 'default.png'),
(148, 'Build With Flutter - Widgets', '\" \"', NULL, NULL, NULL, 'en', NULL, 'build-with-flutter---widgets-pmq38qia', NULL, 31, '2024-02-20 12:10:54', '2024-02-20 12:10:54', 0, 1, 'default.png'),
(149, 'Build With Flutter - Layouts & Gestures', '\" \"', NULL, NULL, NULL, 'en', NULL, 'build-with-flutter---layouts-ilsd48kk', NULL, 31, '2024-02-20 12:35:41', '2024-02-20 12:35:41', 0, 1, 'default.png'),
(150, 'Build With Flutter - Alert Dialogs & Images', '\" \"', NULL, NULL, NULL, 'en', NULL, 'build-with-flutter---alert-dia-xpsz2o1h', NULL, 31, '2024-02-20 12:36:13', '2024-02-20 12:36:13', 0, 1, 'default.png'),
(151, 'Build With Flutter - Drawers & Tab Bars', '\" \"', NULL, NULL, NULL, 'en', NULL, 'build-with-flutter---drawers-xz316vai', NULL, 31, '2024-02-20 12:40:59', '2024-02-20 12:40:59', 0, 1, 'default.png'),
(152, 'Flutter State Management', '\" \"', NULL, NULL, NULL, 'en', NULL, 'flutter-state-management-d7svqall', NULL, 31, '2024-02-20 12:41:12', '2024-02-20 12:41:12', 0, 1, 'default.png'),
(153, 'Animations In Flutter', ' ', NULL, NULL, NULL, 'en', NULL, 'animations-in-flutter-mkmm4ugz', NULL, 31, '2024-02-20 12:41:39', '2024-02-20 12:41:39', 0, 1, 'default.png'),
(154, 'Let\'s Conclude Our Learning', '\" \"', NULL, NULL, NULL, 'en', NULL, 'let-s-conclude-xl7kktef', NULL, 31, '2024-02-20 12:41:51', '2024-02-20 12:41:51', 0, 1, 'default.webp'),
(155, 'Fundamentals Of Information Security', '\" \"', NULL, NULL, NULL, 'en', NULL, 'fundamentals-of-information-se-snqyfl6p', NULL, 41, '2024-02-20 16:06:06', '2024-02-20 16:06:06', 0, 1, 'default.png'),
(156, 'Concepts Of Physical Security', '\" \"', NULL, NULL, NULL, 'en', NULL, 'concepts-of-physical-security-ntzfbszw', NULL, 41, '2024-02-20 16:06:30', '2024-02-20 16:06:30', 0, 1, 'default.png'),
(157, 'Cyber Attacks & Laws', '\" \"', NULL, NULL, NULL, 'en', NULL, 'cyber-attacks---laws-vyoumlmh', NULL, 41, '2024-02-20 16:06:51', '2024-02-20 16:06:51', 0, 1, 'default.png'),
(158, 'Basics Of Cyber Security', '\" \"', NULL, NULL, NULL, 'en', NULL, 'basics-of-cyber-security-m09dec5a', NULL, 41, '2024-02-20 16:07:08', '2024-02-20 16:07:08', 0, 1, 'default.png'),
(159, 'Layers Of Security', '\" \"', NULL, NULL, NULL, 'en', NULL, 'layers-of-security-admwy6tw', NULL, 41, '2024-02-20 16:07:37', '2024-02-20 16:07:37', 0, 1, 'default.png'),
(160, 'Digital Forensics', '\" \"', NULL, NULL, NULL, 'en', NULL, 'digital-forensics-kny2viix', NULL, 41, '2024-02-20 16:08:20', '2024-02-20 16:08:20', 0, 1, 'default.png'),
(161, 'Myths & Conclusion', '\" \"', NULL, NULL, NULL, 'en', NULL, 'myths---conclusion-evwvzllg', NULL, 41, '2024-02-20 16:08:40', '2024-02-20 16:08:40', 0, 1, 'default.png'),
(162, 'Final Recap', '\" \"', NULL, NULL, NULL, 'en', NULL, 'final-recap-qkxnqhsz', NULL, 41, '2024-02-20 16:08:56', '2024-02-20 16:08:56', 0, 1, 'default.png'),
(163, 'Scope', '\" \"', NULL, NULL, NULL, 'en', NULL, 'scope-2cc2ghha', NULL, 59, '2024-02-20 17:13:05', '2024-02-20 17:13:05', 0, 1, 'default.png'),
(164, 'Playing With Strings', '\" \"', NULL, NULL, NULL, 'en', NULL, 'playing-with-strings-mfwlplzm', NULL, 59, '2024-02-20 17:13:26', '2024-02-20 17:13:26', 0, 1, 'default.png'),
(165, 'Numbers & Booleans', '\" \"', NULL, NULL, NULL, 'en', NULL, 'numbers---booleans-pxe8phrs', NULL, 59, '2024-02-20 17:18:19', '2024-02-20 17:18:19', 0, 1, 'default.png'),
(166, 'Objetcs In JavaScript', '\" \"', NULL, NULL, NULL, 'en', NULL, 'objetcs-in-javascript-bwzeje1s', NULL, 59, '2024-02-20 17:20:26', '2024-02-20 17:20:26', 0, 1, 'default.png'),
(167, 'Dates In JavaScript', '\" \"', NULL, NULL, NULL, 'en', NULL, 'dates-in-javascript-t2xjhmrp', NULL, 59, '2024-02-20 17:20:55', '2024-02-20 17:20:55', 0, 1, 'default.png'),
(168, 'Document Object Model(DOM)', '\" \"', NULL, NULL, NULL, 'en', NULL, 'document-object-model-0bfq2o9m', NULL, 59, '2024-02-20 17:21:14', '2024-02-20 17:21:14', 0, 1, 'default.webp'),
(169, 'Accessing HTML Elements Using JavaScript', '\" \"', NULL, NULL, NULL, 'en', NULL, 'accessing-html-elements-using-1gqmthz9', NULL, 59, '2024-02-20 17:22:32', '2024-02-20 17:22:32', 0, 1, 'default.png'),
(170, 'Manipulating HTML Elements Using JavaScript', '\" \"', NULL, NULL, NULL, 'en', NULL, 'manipulating-html-elements-usi-ym6vtjqv', NULL, 59, '2024-02-20 17:22:57', '2024-02-20 17:22:57', 0, 1, 'default.png'),
(171, 'Manipulating CSS Using JavaScript', '\" \"', NULL, NULL, NULL, 'en', NULL, 'manipulating-css-using-javascr-fkqwqbid', NULL, 59, '2024-02-20 17:23:13', '2024-02-20 17:23:13', 0, 1, 'default.png'),
(172, 'Events In JavaScript', '\" \"', NULL, NULL, NULL, 'en', NULL, 'events-in-javascript-zrswx85b', NULL, 59, '2024-02-20 17:23:29', '2024-02-20 17:23:29', 0, 1, 'default.png'),
(173, 'Browser Object Model(BOM)', '\" \"', NULL, NULL, NULL, 'en', NULL, 'browser-object-model-bom-uzah5wxw', NULL, 59, '2024-02-20 17:23:52', '2024-02-20 17:23:52', 0, 1, 'default.png'),
(174, 'Cookies', '\" \"', NULL, NULL, NULL, 'en', NULL, 'cookies-4wkqpxho', NULL, 59, '2024-02-20 17:24:08', '2024-02-20 17:24:08', 0, 1, 'default.png'),
(175, 'Getting Started With ES6', '\" \"', NULL, NULL, NULL, 'en', NULL, 'getting-started-with-es6-tvje5tip', NULL, 59, '2024-02-20 17:24:35', '2024-02-20 17:24:35', 0, 1, 'default.png'),
(176, 'Classes In ES6', '\" \"', NULL, NULL, NULL, 'en', NULL, 'classes-in-es6-niwoev9n', NULL, 59, '2024-02-20 17:24:51', '2024-02-20 17:24:51', 0, 1, 'default.png'),
(177, 'Continuation Of The Journey', '\" \"', NULL, NULL, NULL, 'en', NULL, 'continuation-of-the-journey-scq6ethf', NULL, 34, '2024-03-11 14:50:04', '2024-03-11 14:50:04', 0, 1, 'default.png'),
(178, 'Networking Basics', '\" \"', NULL, NULL, NULL, 'en', NULL, 'networking-basics-qprx7bb1', NULL, 34, '2024-03-11 14:50:21', '2024-03-11 14:50:21', 0, 1, 'default.png'),
(180, 'Let\'s Go Anonymous', '\" \"', NULL, NULL, NULL, 'en', NULL, 'let-s-go-anonymous-qcdqwehu', NULL, 34, '2024-03-11 14:50:45', '2024-03-11 14:50:45', 0, 1, 'default.png'),
(181, 'VAPT - What Is It?', '\" \"', NULL, NULL, NULL, 'en', NULL, 'vapt---what-is-it-2yjwzlgz', NULL, 34, '2024-03-11 14:51:09', '2024-03-11 14:51:09', 0, 1, 'default.png'),
(182, 'The Art Of Secret Writing', '\" \"', NULL, NULL, NULL, 'en', NULL, 'the-art-of-secret-writing-n1m5rq9a', NULL, 34, '2024-03-11 14:51:27', '2024-03-11 14:51:27', 0, 1, 'default.png'),
(183, 'Let\'s Break Passwords', '\" \"', NULL, NULL, NULL, 'en', NULL, 'let-s-break-passwords-zr2m0prw', NULL, 34, '2024-03-11 14:51:48', '2024-03-11 14:51:48', 0, 1, 'default.png'),
(184, 'Man In The Middle Attack', '\" \"', NULL, NULL, NULL, 'en', NULL, 'man-in-the-middle-attack-sw1zzrj8', NULL, 34, '2024-03-11 14:52:01', '2024-03-11 14:52:01', 0, 1, 'default.png'),
(185, 'Denial Of service(DOS) Attack', '\" \"', NULL, NULL, NULL, 'en', NULL, 'denial-of-service-dos--attack-38cju3fa', NULL, 34, '2024-03-11 14:52:28', '2024-03-11 14:52:28', 0, 1, 'default.png'),
(186, 'Some Interesting Concepts', '\" \"', NULL, NULL, NULL, 'en', NULL, 'some-interesting-concepts-vmavtwjz', NULL, 34, '2024-03-11 14:52:39', '2024-03-11 14:52:39', 0, 1, 'default.png'),
(187, 'More On Web Hacking', '\" \"', NULL, NULL, NULL, 'en', NULL, 'more-on-web-hacking-kip0px8n', NULL, 34, '2024-03-11 14:52:57', '2024-03-11 14:52:57', 0, 1, 'default.png'),
(188, 'Introduction To Data Science', '\" \"', NULL, NULL, NULL, 'en', NULL, 'introduction-to-data-science-7umdngbe', NULL, 37, '2024-03-12 13:12:03', '2024-03-12 13:12:03', 0, 1, 'default.png'),
(189, 'Data Wrangling', '\" \"', NULL, NULL, NULL, 'en', NULL, 'data-wrangling-e6bfgilo', NULL, 37, '2024-03-12 13:12:29', '2024-03-12 13:12:29', 0, 1, 'default.png'),
(190, 'Data Analysis', '\" \"', NULL, NULL, NULL, 'en', NULL, 'data-analysis-useyjcpo', NULL, 37, '2024-03-12 13:12:38', '2024-03-12 13:12:38', 0, 1, 'default.png'),
(191, 'Data Visualization', '\" \"', NULL, NULL, NULL, 'en', NULL, 'data-visualization-kulng3io', NULL, 37, '2024-03-12 13:12:48', '2024-03-12 13:12:48', 0, 1, 'default.png'),
(192, 'Tools Used In Data Science', '\" \"', NULL, NULL, NULL, 'en', NULL, 'tools-used-in-data-science-mrp82zzr', NULL, 37, '2024-03-12 13:13:18', '2024-03-12 13:13:18', 0, 1, 'default.png'),
(193, 'Machine Learning Basics', '\" \"', NULL, NULL, NULL, 'en', NULL, 'machine-learning-basics-uifsimug', NULL, 37, '2024-03-12 13:13:32', '2024-03-12 13:13:32', 0, 1, 'default.png'),
(194, 'Machine Learning & Data Science', '\" \"', NULL, NULL, NULL, 'en', NULL, 'machine-learning---data-scienc-lwmzskxz', NULL, 37, '2024-03-12 13:13:50', '2024-03-12 13:13:50', 0, 1, 'default.png'),
(195, 'Data Science Application', '\" \"', NULL, NULL, NULL, 'en', NULL, 'data-science-application-mum7tkfh', NULL, 37, '2024-03-12 13:14:05', '2024-03-12 13:14:05', 0, 1, 'default.png'),
(196, 'Getting started Again', '\" \"', NULL, NULL, NULL, 'en', NULL, 'getting-started-again-rv8oqyjs', NULL, 90, '2024-03-12 15:20:12', '2024-03-12 15:20:12', 0, 1, 'default.png'),
(197, 'File Handling In Python', '\" \"', NULL, NULL, NULL, 'en', NULL, 'file-handling-in-python-guutndas', NULL, 90, '2024-03-12 15:20:30', '2024-03-12 15:20:30', 0, 1, 'default.png'),
(198, 'Modules: Let\'s Re-use', '\" \"', NULL, NULL, NULL, 'en', NULL, 'modules--let-s-re-use-0xdruawm', NULL, 90, '2024-03-12 15:20:51', '2024-03-12 15:20:51', 0, 1, 'default.png'),
(199, 'Exceptions In Python', '\" \"', NULL, NULL, NULL, 'en', NULL, 'exceptions-in-python-omjrqimp', NULL, 90, '2024-03-12 15:21:03', '2024-03-12 15:21:03', 0, 1, 'default.png'),
(200, 'Regular Expressions', '\" \"', NULL, NULL, NULL, 'en', NULL, 'regular-expressions-rqnubcqw', NULL, 90, '2024-03-12 15:21:15', '2024-03-12 15:21:15', 0, 1, 'default.png'),
(201, 'Database Connection', '\" \"', NULL, NULL, NULL, 'en', NULL, 'database-connection-xtrgmm3x', NULL, 90, '2024-03-12 15:21:43', '2024-03-12 15:21:43', 0, 1, 'default.png'),
(202, 'GUI Development', '\" \"', NULL, NULL, NULL, 'en', NULL, 'gui-development-femruvuu', NULL, 90, '2024-03-12 15:21:53', '2024-03-12 15:21:53', 0, 1, 'default.png'),
(203, 'Object Oriented Programming', '\" \"', NULL, NULL, NULL, 'en', NULL, 'object-oriented-programming-ypy9dnxo', NULL, 90, '2024-03-12 15:22:16', '2024-03-12 15:22:16', 0, 1, 'default.png'),
(204, 'Multi-threading In Python', '\" \"', NULL, NULL, NULL, 'en', NULL, 'multi-threading-in-python-mhmoesyy', NULL, 90, '2024-03-12 15:22:34', '2024-03-12 15:22:34', 0, 1, 'default.png'),
(205, 'What\'s Next', '\" \"', NULL, NULL, NULL, 'en', NULL, 'what-s-next-agsanmeq', NULL, 90, '2024-03-12 15:22:42', '2024-03-12 15:22:42', 0, 1, 'default.png');

-- --------------------------------------------------------

--
-- Table structure for table `message`
--

CREATE TABLE `message` (
  `id` int(11) NOT NULL,
  `sender_id` int(11) DEFAULT NULL,
  `recipient_id` int(11) DEFAULT NULL,
  `body` varchar(140) DEFAULT NULL,
  `is_seen` tinyint(1) DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `notification`
--

CREATE TABLE `notification` (
  `id` int(11) NOT NULL,
  `name` varchar(128) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `payload_json` text DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `notification`
--

INSERT INTO `notification` (`id`, `name`, `user_id`, `payload_json`, `created`, `updated`, `deleted`, `active`) VALUES
(1, 'unread', 1, '\"Recent Signin -> just now\"', '2024-02-10 00:48:28', '2024-02-10 00:48:28', 0, 1),
(6, 'unread', 1, '\"Recent Signin ->  less than a second ago\"', '2024-02-06 08:16:30', '2024-02-06 08:16:30', 0, 1),
(7, 'count_unread', 2, '0', '2024-02-15 04:19:42', '2024-02-15 04:19:42', 0, 1),
(25, 'unread', 2, '\"Recent Signin -> just now\"', '2024-03-24 20:50:44', '2024-03-24 20:50:44', 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `id` int(11) NOT NULL,
  `currency` varchar(100) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `provider` varchar(100) DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `tx_id` varchar(100) DEFAULT NULL,
  `tx_status` varchar(100) DEFAULT NULL,
  `tx_ref` varchar(100) DEFAULT NULL,
  `tx_amount` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`id`, `currency`, `user_id`, `course_id`, `provider`, `created`, `updated`, `deleted`, `tx_id`, `tx_status`, `tx_ref`, `tx_amount`) VALUES
(30, 'USD', 2, 33, 'FlutterWave', '2024-02-26 14:27:36', '2024-02-26 14:27:36', 0, '4934382', 'successful', '-tx-techa-rqf83', 100),
(31, 'USD', 2, 30, 'FlutterWave', '2024-02-26 14:30:01', '2024-02-26 14:30:01', 0, '4934384', 'successful', '-tx-techa-gn6wy', 100),
(32, 'USD', 2, 50, 'FlutterWave', '2024-02-26 14:45:24', '2024-02-26 14:45:24', 0, NULL, 'cancelled', '-tx-techa-kxixk', 100),
(33, 'USD', 2, 30, 'FlutterWave', '2024-02-26 15:42:04', '2024-02-26 15:42:04', 0, NULL, 'pending', '-tx-techa-wlwhp', 2300),
(34, 'USD', 2, 37, 'FlutterWave', '2024-02-26 15:57:56', '2024-02-26 15:57:56', 0, '4934566', 'successful', '-tx-techa-sqpnd', 120),
(35, 'USD', 2, 39, 'FlutterWave', '2024-02-26 16:57:18', '2024-02-26 16:57:18', 0, NULL, 'pending', '-tx-techa-gii7c', 39),
(36, 'USD', 2, 40, 'FlutterWave', '2024-02-26 17:42:17', '2024-02-26 17:42:17', 0, NULL, 'pending', '-tx-techa-erwzw', 45),
(37, 'USD', 2, 40, 'FlutterWave', '2024-02-26 17:45:11', '2024-02-26 17:45:11', 0, NULL, 'pending', '-tx-techa-zcn9l', 45),
(38, 'USD', 2, 30, 'FlutterWave', '2024-02-26 17:46:31', '2024-02-26 17:46:31', 0, NULL, 'pending', '-tx-techa-j470n', 2300),
(39, 'USD', 2, 31, 'FlutterWave', '2024-03-06 08:50:28', '2024-03-06 08:50:28', 0, NULL, 'pending', '-tx-techa-hqzep', 20),
(40, 'USD', 2, 76, 'FlutterWave', '2024-03-06 14:46:19', '2024-03-06 14:46:19', 0, NULL, 'pending', '-tx-techa-ckuyd', 100),
(41, 'USD', 2, 76, 'FlutterWave', '2024-03-06 14:50:38', '2024-03-06 14:50:38', 0, NULL, 'pending', '-tx-techa-sm6r6', 100),
(42, 'USD', 2, 32, 'FlutterWave', '2024-03-06 15:08:00', '2024-03-06 15:08:00', 0, NULL, 'pending', '-tx-techa-6sdub', 100),
(43, 'USD', 2, 76, 'FlutterWave', '2024-03-06 17:16:11', '2024-03-06 17:16:11', 0, '4951745', 'successful', '-tx-techa-mssh5', 100),
(44, 'USD', 2, 76, 'FlutterWave', '2024-03-06 17:18:21', '2024-03-06 17:18:21', 0, NULL, 'pending', '-tx-techa-fw8xi', 100),
(45, 'USD', 2, 35, 'FlutterWave', '2024-03-06 17:20:46', '2024-03-06 17:20:46', 0, NULL, 'pending', '-tx-techa-kcq8t', 100),
(46, 'USD', 2, 32, 'FlutterWave', '2024-03-06 17:29:43', '2024-03-06 17:29:43', 0, NULL, 'pending', '-tx-techa-5bkw9', 100),
(47, 'USD', 2, 31, 'FlutterWave', '2024-03-08 09:39:43', '2024-03-08 09:39:43', 0, NULL, 'pending', '-tx-techa-6qysr', 20),
(50, 'USD', 2, 65, 'FlutterWave', '2024-03-11 12:31:18', '2024-03-11 12:31:18', 0, NULL, 'pending', '-tx-techa-d7qyl', 100),
(54, 'USD', 2, 36, 'FlutterWave', '2024-03-11 13:02:30', '2024-03-11 13:02:30', 0, '4959509', 'successful', '-tx-techa-yxczm', 100),
(55, 'USD', 2, 34, 'FlutterWave', '2024-03-11 17:16:48', '2024-03-11 17:16:48', 0, NULL, 'pending', '-tx-techa-lclmd', 100),
(56, 'USD', 2, 34, 'FlutterWave', '2024-03-11 17:18:30', '2024-03-11 17:18:30', 0, NULL, 'pending', '-tx-techa-oqccv', 100),
(57, 'USD', 2, 41, 'FlutterWave', '2024-03-12 13:26:34', '2024-03-12 13:26:34', 0, '4961746', 'successful', '-tx-techa-1xpds', 100),
(58, 'USD', 2, 38, 'FlutterWave', '2024-03-12 13:29:20', '2024-03-12 13:29:20', 0, '4961749', 'successful', '-tx-techa-wnqal', 100),
(59, 'USD', 2, 34, 'FlutterWave', '2024-03-12 13:35:26', '2024-03-12 13:35:26', 0, '4961769', 'successful', '-tx-techa-jt8pr', 100),
(60, 'USD', 2, 40, 'FlutterWave', '2024-03-12 13:40:52', '2024-03-12 13:40:52', 0, '4961775', 'successful', '-tx-techa-5vlmg', 45),
(61, 'USD', 2, 90, 'FlutterWave', '2024-03-12 15:38:53', '2024-03-12 15:38:53', 0, NULL, 'pending', '-tx-techa-5bs8r', 120),
(62, 'USD', 2, 34, 'FlutterWave', '2024-03-20 04:31:05', '2024-03-20 04:31:05', 0, '4977144', 'successful', '-tx-techa-cjh3l', 100),
(63, 'USD', 2, 76, 'FlutterWave', '2024-03-20 05:11:43', '2024-03-20 05:11:43', 0, NULL, 'pending', '-tx-techa-risjb', 100),
(64, 'USD', 2, 76, 'FlutterWave', '2024-03-20 05:12:54', '2024-03-20 05:12:54', 0, NULL, 'pending', '-tx-techa-f21l3', 100),
(65, 'USD', 2, 76, 'FlutterWave', '2024-03-20 05:15:02', '2024-03-20 05:15:02', 0, '4977194', 'successful', '-tx-techa-lzftz', 100);

-- --------------------------------------------------------

--
-- Table structure for table `post`
--

CREATE TABLE `post` (
  `id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `content` text NOT NULL,
  `user_id` int(11) NOT NULL,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

CREATE TABLE `role` (
  `id` int(11) NOT NULL,
  `type` varchar(100) DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tag`
--

CREATE TABLE `tag` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `topic`
--

CREATE TABLE `topic` (
  `id` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `desc` text NOT NULL,
  `video` varchar(1000) DEFAULT NULL,
  `material` varchar(100) DEFAULT NULL,
  `duration` datetime DEFAULT NULL,
  `slug` varchar(130) DEFAULT NULL,
  `course_id` int(11) NOT NULL,
  `lesson_id` int(11) NOT NULL,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `image` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `topic`
--

INSERT INTO `topic` (`id`, `title`, `desc`, `video`, `material`, `duration`, `slug`, `course_id`, `lesson_id`, `created`, `updated`, `deleted`, `active`, `image`) VALUES
(127, 'Introduction', '\"[\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ai.png\\\",\\r\\n        \\\"title\\\": \\\"What Will I Learn?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Get a clear understanding about Artificial Intelligence.\\\",\\r\\n            \\\"How a computer can take a decision on its own.\\\",\\r\\n            \\\"Various types of Artificial Intelligence available.\\\",\\r\\n            \\\"Understanding Agents and Environments.\\\",\\r\\n            \\\"Understanding about the issues with Artificial Intelligence.\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ai.png\\\",\\r\\n        \\\"title\\\": \\\"Who is the target audience?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Who is curious to know how the basics functionality of Google now, Siri, Cortana or other AI.\\\",\\r\\n            \\\"Those who want to start their career in AI, this course can give you a clear idea about the basics of AI.\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ai.png\\\",\\r\\n        \\\"title\\\": \\\"Benefits\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"AI can be applied to any industry, to solve problems, Hence the demand of engineers having a good knowledge of AI is increasing day by day.\\\",\\r\\n            \\\"Automobile companies are moving towards driverless cars to avoid any human error while driving a car.\\\",\\r\\n            \\\"Weather predictions are getting accurate thus helping people to plan their day.\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ai.png\\\",\\r\\n        \\\"title\\\": \\\"Salary\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"100,000 USD per year\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"ai.png\\\",\\r\\n        \\\"title\\\": \\\"Requirements\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"Curiosity to know how a computer can think.\\\",\\r\\n            \\\"Nothing else! It\\u2019s just you, your phone and your hunger to get started today\\\"\\r\\n        ]\\r\\n    }\\r\\n    \\r\\n]\\r\\n\"', NULL, NULL, NULL, 'introduction-ulcimeja', 32, 69, '2024-02-19 14:37:48', '2024-02-19 14:37:48', 0, 1, 'default.webp'),
(128, 'Problem Solving Test', '\"[\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"data_sc.png\\\",\\r\\n        \\\"title\\\": \\\"What Will I Learn?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Develop in depth understanding of the key technologies in data science and business analytics:\\\",\\r\\n            \\\"data mining, machine learning, visualization techniques, predictive modeling, and statistics\\\",\\r\\n            \\\"Practice problem analysis and decision-making\\\",\\r\\n            \\\"Gain practical, hands-on experience with statistics programming languages and big data tools through coursework\\\",\\r\\n            \\\"Employ cutting edge tools and technologies to analyze Big Data\\\",\\r\\n            \\\"Apply algorithms to build machine intelligence\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"data_sc.png\\\",\\r\\n        \\\"title\\\": \\\"Who is the target audience?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Anybody with an interest in Data Science\\\",\\r\\n            \\\"Anybody who wants to improve their data mining skills\\\",\\r\\n            \\\"Anybody who wants to improve their statistical modelling skills\\\",\\r\\n            \\\"Anybody who wants to improve their data preparation skills\\\",\\r\\n            \\\"Anybody who wants to improve their Data Science presentation skills\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"data_sc.png\\\",\\r\\n        \\\"title\\\": \\\"Benefits\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"This course will give you a full overview of the Data Science journey. Upon completing this course you will know:\\\",\\r\\n            \\\"How to clean and prepare your data for analysis\\\",\\r\\n            \\\"How to perform basic visualisation of your data\\\",\\r\\n            \\\"How to model your data\\\",\\r\\n            \\\"How to curve-fit your data\\\",\\r\\n            \\\"And finally, how to present your findings and wow the audience\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"data_sc.png\\\",\\r\\n        \\\"title\\\": \\\"Salary\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"According to Google, A data scientist earns around 1.2M $ per year\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"data_sc.png\\\",\\r\\n        \\\"title\\\": \\\"Requirements\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"Only a passion for success\\\",\\r\\n            \\\"All software used in this course is either available for Free or as a Demo version\\\"\\r\\n        ]\\r\\n    }\\r\\n    \\r\\n]\\r\\n\"', NULL, NULL, NULL, 'problem-solving-test-mrapxigk', 32, 69, '2024-02-19 14:38:04', '2024-02-19 14:38:04', 0, 1, 'default.webp'),
(129, 'Programs', '\" \"', NULL, NULL, NULL, 'programs-8lemf3xw', 32, 69, '2024-02-19 14:38:17', '2024-02-19 14:38:17', 0, 1, 'default.png'),
(130, 'Summary', '\" \"', NULL, NULL, NULL, 'summary-dxsquqt0', 32, 69, '2024-02-19 14:38:27', '2024-02-19 14:38:27', 0, 1, 'default.png'),
(131, 'Introduction', '\" \"', NULL, NULL, NULL, 'introduction-usjvjkmu', 32, 70, '2024-02-19 14:38:55', '2024-02-19 14:38:55', 0, 1, 'default.png'),
(132, 'Asking the computer to remember', '\" \"', NULL, NULL, NULL, 'asking-the-computer-to-remembe-hbabwncg', 32, 70, '2024-02-19 14:39:04', '2024-02-19 14:39:04', 0, 1, 'default.png'),
(133, 'Variables', '\" \"', NULL, NULL, NULL, 'variables-q34vezyu', 32, 70, '2024-02-19 14:39:14', '2024-02-19 14:39:14', 0, 1, 'default.webp'),
(134, 'Changing values', '\" \"', NULL, NULL, NULL, 'changing-values-1xmfcjdt', 32, 70, '2024-02-19 14:39:24', '2024-02-19 14:39:24', 0, 1, 'default.png'),
(135, 'Using variables', '\" \"', NULL, NULL, NULL, 'using-variables-akt19bwo', 32, 70, '2024-02-19 14:39:32', '2024-02-19 14:39:32', 0, 1, 'default.png'),
(136, 'Storing Text', '\" \"', NULL, NULL, NULL, 'storing-text-pfdu8gxh', 32, 70, '2024-02-19 14:39:41', '2024-02-19 14:39:41', 0, 1, 'default.png'),
(137, 'Lists', '\" \"', NULL, NULL, NULL, 'lists-jt7o7spb', 32, 70, '2024-02-19 14:39:50', '2024-02-19 14:39:50', 0, 1, 'default.png'),
(138, 'Summary', '\" \"', NULL, NULL, NULL, 'summary-6xfyeq22', 32, 70, '2024-02-19 14:40:01', '2024-02-19 14:40:01', 0, 1, 'default.png'),
(139, 'Introduction', '\" \"', NULL, NULL, NULL, 'introduction-hyg8qpom', 32, 71, '2024-02-19 14:40:28', '2024-02-19 14:40:28', 0, 1, 'default.png'),
(140, ' Where to use repeat?', '\" \"', NULL, NULL, NULL, 'where-to-use-repeat-tu1uxfln', 32, 71, '2024-02-19 14:40:32', '2024-02-19 14:40:32', 0, 1, 'default.png'),
(141, 'Loops', '\" \"', NULL, NULL, NULL, 'loops-31vznyfo', 32, 71, '2024-02-19 14:40:44', '2024-02-19 14:40:44', 0, 1, 'default.png'),
(142, 'While Loop', '\" \"', NULL, NULL, NULL, 'while-loop-eljx95vg', 32, 71, '2024-02-19 14:40:48', '2024-02-19 14:40:48', 0, 1, 'default.png'),
(143, 'Summary', '\" \"', NULL, NULL, NULL, 'summary-2ymty5sr', 32, 71, '2024-02-19 14:41:03', '2024-02-19 14:41:03', 0, 1, 'default.png'),
(144, 'Introduction', '\" \"', NULL, NULL, NULL, 'introduction-ajy1uduj', 32, 71, '2024-02-19 14:41:42', '2024-02-19 14:41:42', 0, 1, 'default.png'),
(145, 'Introduction', '\" \"', NULL, NULL, NULL, 'introduction-yh5k5ubh', 32, 72, '2024-02-19 14:42:01', '2024-02-19 14:42:01', 0, 1, 'default.png'),
(146, 'Using If..Then..Else', '\" \"', NULL, NULL, NULL, 'using-if--then--else-tkqhd93a', 32, 72, '2024-02-19 14:42:05', '2024-02-19 14:42:05', 0, 1, 'default.png'),
(147, 'Using Else If', '\" \"', NULL, NULL, NULL, 'using-else-if-qfmtzmjt', 32, 72, '2024-02-19 14:42:22', '2024-02-19 14:42:22', 0, 1, 'default.png'),
(148, 'Summary', '\" \"', NULL, NULL, NULL, 'summary-zxk5wcj2', 32, 72, '2024-02-19 14:42:31', '2024-02-19 14:42:31', 0, 1, 'default.png'),
(149, 'How to store multiple values', '\" \"', NULL, NULL, NULL, 'how-to-store-multiple-values-uw9rtlim', 32, 73, '2024-02-19 14:42:45', '2024-02-19 14:42:45', 0, 1, 'default.png'),
(150, 'Summary', '\" \"', NULL, NULL, NULL, 'summary-pyqg1rfb', 32, 73, '2024-02-19 14:42:48', '2024-02-19 14:42:48', 0, 1, 'default.png'),
(151, 'Similar instructions', '\" \"', NULL, NULL, NULL, 'similar-instructions-2u34auwd', 32, 74, '2024-02-19 14:43:11', '2024-02-19 14:43:11', 0, 1, 'default.png'),
(152, 'Create group of instructions', '\" \"', NULL, NULL, NULL, 'create-group-of-instructions-qdtfi9se', 32, 74, '2024-02-19 14:43:26', '2024-02-19 14:43:26', 0, 1, 'default.png'),
(153, 'Procedures & Functions', '\" \"', NULL, NULL, NULL, 'procedures---functions-hhx0dadj', 32, 74, '2024-02-19 14:43:34', '2024-02-19 14:43:34', 0, 1, 'default.png'),
(154, 'Let\'s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-jpwi4hsn', 32, 74, '2024-02-19 14:43:59', '2024-02-19 14:43:59', 0, 1, 'default.png'),
(155, 'What are mistakes?', '\" \"', NULL, NULL, NULL, 'what-are-mistakes-md3rioa2', 32, 75, '2024-02-19 14:44:20', '2024-02-19 14:44:20', 0, 1, 'default.png'),
(156, 'What is debugging?', '\" \"', NULL, NULL, NULL, 'what-is-debugging-vlmimprl', 32, 75, '2024-02-19 14:44:30', '2024-02-19 14:44:30', 0, 1, 'default.png'),
(157, 'Logic bug', '\" \"', NULL, NULL, NULL, 'logic-bug-v2ihf4yu', 32, 75, '2024-02-19 14:44:39', '2024-02-19 14:44:39', 0, 1, 'default.png'),
(158, 'Avoiding bug', '\" \"', NULL, NULL, NULL, 'avoiding-bug-xoldesgp', 32, 75, '2024-02-19 14:44:48', '2024-02-19 14:44:48', 0, 1, 'default.png'),
(159, 'Summary', '\" \"', NULL, NULL, NULL, 'summary-pd2h2zsw', 32, 75, '2024-02-19 14:44:57', '2024-02-19 14:44:57', 0, 1, 'default.png'),
(160, 'What is a computer language?', '\" \"', NULL, NULL, NULL, 'what-is-a-computer-language-d688t9l7', 32, 76, '2024-02-19 14:45:19', '2024-02-19 14:45:19', 0, 1, 'default.png'),
(161, 'Converting code to 0s and 1s', '\" \"', NULL, NULL, NULL, 'converting-code-to-0s-and-1s-nnp0teht', 32, 76, '2024-02-19 14:45:29', '2024-02-19 14:45:29', 0, 1, 'default.png'),
(162, 'Understanding code', '\" \"', NULL, NULL, NULL, 'understanding-code-dyymat9f', 32, 76, '2024-02-19 14:45:37', '2024-02-19 14:45:37', 0, 1, 'default.png'),
(163, 'Let’s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-hnkvs1cl', 32, 76, '2024-02-19 14:45:46', '2024-02-19 14:45:46', 0, 1, 'default.png'),
(164, 'Meeting Kuro Kage', '\" \"', NULL, NULL, NULL, 'meeting-kuro-kage-khtcnodn', 33, 78, '2024-02-19 15:12:55', '2024-02-19 15:12:55', 0, 1, 'default.png'),
(165, 'Information & Data', '\" \"', NULL, NULL, NULL, 'information---data-voafejql', 33, 78, '2024-02-19 15:13:14', '2024-02-19 15:13:14', 0, 1, 'default.png'),
(166, 'Vulnerability v/s Threat', '\" \"', NULL, NULL, NULL, 'vulnerability-v-s-threat-vh9om2pw', 33, 79, '2024-02-19 15:13:54', '2024-02-19 15:13:54', 0, 1, 'default.png'),
(167, 'Why Secure Data?', '\" \"', NULL, NULL, NULL, 'why-secure-data-pnu5spzm', 33, 79, '2024-02-19 15:14:16', '2024-02-19 15:14:16', 0, 1, 'default.png'),
(168, 'Let’s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-hrapx8uf', 33, 79, '2024-02-19 15:14:26', '2024-02-19 15:14:26', 0, 1, 'default.png'),
(169, 'Describing Motivations', '\" \"', NULL, NULL, NULL, 'describing-motivations-soarowky', 33, 80, '2024-02-19 15:14:46', '2024-02-19 15:14:46', 0, 1, 'default.png'),
(170, 'Political Motivations', '\" \"', NULL, NULL, NULL, 'political-motivations-yssz6ttv', 33, 80, '2024-02-19 15:14:56', '2024-02-19 15:14:56', 0, 1, 'default.png'),
(171, 'Economical Motivations', '\" \"', NULL, NULL, NULL, 'economical-motivations-ijjstkhu', 33, 80, '2024-02-19 15:15:08', '2024-02-19 15:15:08', 0, 1, 'default.png'),
(172, 'Personal Motivation', '\" \"', NULL, NULL, NULL, 'personal-motivation-eq41zrqd', 33, 80, '2024-02-19 15:15:17', '2024-02-19 15:15:17', 0, 1, 'default.png'),
(173, 'Let’s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-yqsl9rhy', 33, 80, '2024-02-19 15:15:26', '2024-02-19 15:15:26', 0, 1, 'default.png'),
(174, 'Black Hat Hacker', '\" \"', NULL, NULL, NULL, 'black-hat-hacker-sed72wvj', 33, 81, '2024-02-19 15:15:44', '2024-02-19 15:15:44', 0, 1, 'default.png'),
(175, 'White Hat Hacker', '\" \"', NULL, NULL, NULL, 'white-hat-hacker-cn7iw3q2', 33, 81, '2024-02-19 15:16:08', '2024-02-19 15:16:08', 0, 1, 'default.png'),
(176, 'Grey Hat Hacker', '\" \"', NULL, NULL, NULL, 'grey-hat-hacker-bstegzf2', 33, 81, '2024-02-19 15:16:18', '2024-02-19 15:16:18', 0, 1, 'default.png'),
(177, 'Let’s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-nvg5qs28', 33, 81, '2024-02-19 15:16:26', '2024-02-19 15:16:26', 0, 1, 'default.png'),
(178, 'What is a Malware?', '\" \"', NULL, NULL, NULL, 'what-is-a-malware-3baanvul', 33, 82, '2024-02-19 15:17:16', '2024-02-19 15:17:16', 0, 1, 'default.png'),
(179, 'Classifying Malware', '\" \"', NULL, NULL, NULL, 'classifying-malware-oodjufqj', 33, 82, '2024-02-19 15:17:27', '2024-02-19 15:17:27', 0, 1, 'default.png'),
(180, 'Categorizing Malware', '\" \"', NULL, NULL, NULL, 'categorizing-malware-4cbi6q1m', 33, 82, '2024-02-19 15:17:36', '2024-02-19 15:17:36', 0, 1, 'default.png'),
(181, 'Let’s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-gsln3nvt', 33, 82, '2024-02-19 15:17:44', '2024-02-19 15:17:44', 0, 1, 'default.png'),
(182, 'What is a Virus?', '\" \"', NULL, NULL, NULL, 'what-is-a-virus-rjzrwq2e', 33, 83, '2024-02-19 15:17:58', '2024-02-19 15:17:58', 0, 1, 'default.png'),
(183, 'Components of Virus', '\" \"', NULL, NULL, NULL, 'components-of-virus-hzg05nkf', 33, 83, '2024-02-19 15:18:07', '2024-02-19 15:18:07', 0, 1, 'default.png'),
(184, 'Life Cycle of Virus', '\" \"', NULL, NULL, NULL, 'life-cycle-of-virus-nizea0zh', 33, 83, '2024-02-19 15:18:16', '2024-02-19 15:18:16', 0, 1, 'default.png'),
(185, 'Let’s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-jzbutiae', 33, 83, '2024-02-19 15:18:24', '2024-02-19 15:18:24', 0, 1, 'default.png'),
(186, 'Can of Worms', '\" \"', NULL, NULL, NULL, 'can-of-worms-8wmbl7cc', 33, 84, '2024-02-19 15:18:39', '2024-02-19 15:18:39', 0, 1, 'default.png'),
(187, 'Horse called Trojan', '\" \"', NULL, NULL, NULL, 'horse-called-trojan-jlsczbtw', 33, 84, '2024-02-19 15:18:46', '2024-02-19 15:18:46', 0, 1, 'default.png'),
(188, 'ILOVEYOU', '\" \"', NULL, NULL, NULL, 'iloveyou-ikulog12', 33, 84, '2024-02-19 15:18:55', '2024-02-19 15:18:55', 0, 1, 'default.png'),
(189, 'Let’s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-lsnqzsbe', 33, 84, '2024-02-19 15:19:02', '2024-02-19 15:19:02', 0, 1, 'default.png'),
(190, 'What is Information Gathering?', '\" \"', NULL, NULL, NULL, 'what-is-information-gathering-vehk2bbr', 33, 85, '2024-02-19 15:19:17', '2024-02-19 15:19:17', 0, 1, 'default.png'),
(191, 'Masking Identity', '\" \"', NULL, NULL, NULL, 'masking-identity-r4kn0nvx', 33, 85, '2024-02-19 15:19:56', '2024-02-19 15:19:56', 0, 1, 'default.png'),
(192, 'Profiling of the Target', '\" \"', NULL, NULL, NULL, 'profiling-of-the-target-klyjkcax', 33, 85, '2024-02-19 15:20:07', '2024-02-19 15:20:07', 0, 1, 'default.png'),
(193, 'Let’s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-wgmfuoei', 33, 85, '2024-02-19 15:20:14', '2024-02-19 15:20:14', 0, 1, 'default.png'),
(194, 'Importance of System Hacking', '\" \"', NULL, NULL, NULL, 'importance-of-system-hacking-oww8zwfj', 33, 86, '2024-02-19 15:20:33', '2024-02-19 15:20:33', 0, 1, 'default.png'),
(195, 'Non-Technical Password Attack', '\" \"', NULL, NULL, NULL, 'non-technical-password-attack-8dnxm5cb', 33, 86, '2024-02-19 15:20:44', '2024-02-19 15:20:44', 0, 1, 'default.png'),
(196, 'Technical Password Attack', '\" \"', NULL, NULL, NULL, 'technical-password-attack-xelss2q2', 33, 86, '2024-02-19 15:20:52', '2024-02-19 15:20:52', 0, 1, 'default.png'),
(197, 'Let’s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-ynddjs5a', 33, 86, '2024-02-19 15:21:02', '2024-02-19 15:21:02', 0, 1, 'default.png'),
(198, 'Websites and more', '\" \"', NULL, NULL, NULL, 'websites-and-more-sjbnz0ro', 33, 87, '2024-02-19 15:21:22', '2024-02-19 15:21:22', 0, 1, 'default.png'),
(199, 'Phishing', '\" \"', NULL, NULL, NULL, 'phishing-48nanxit', 33, 87, '2024-02-19 15:21:32', '2024-02-19 15:21:32', 0, 1, 'default.png'),
(200, 'SQL Injection', '\" \"', NULL, NULL, NULL, 'sql-injection-sl8ddfqn', 33, 87, '2024-02-19 15:21:40', '2024-02-19 15:21:40', 0, 1, 'default.png'),
(201, 'Let’s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-lmjtczxx', 33, 87, '2024-02-19 15:21:50', '2024-02-19 15:21:50', 0, 1, 'default.png'),
(202, 'Introduction to AI', '\" \"', NULL, NULL, NULL, 'introduction-to-ai-stdtimmp', 35, 90, '2024-02-19 15:37:49', '2024-02-19 15:37:49', 0, 1, 'default.png'),
(203, 'How AI was started', '\" \"', NULL, NULL, NULL, 'how-ai-was-started-sxhu22ba', 35, 90, '2024-02-19 15:37:58', '2024-02-19 15:37:58', 0, 1, 'default.png'),
(204, 'Let\'s recap', '\" \"', NULL, NULL, NULL, 'let-s-recap-ien6uqdf', 35, 90, '2024-02-19 15:38:06', '2024-02-19 15:38:06', 0, 1, 'default.png'),
(205, 'What makes Humans smart', '\" \"', NULL, NULL, NULL, 'what-makes-humans-smart-9gsedfjo', 35, 91, '2024-02-19 15:38:36', '2024-02-19 15:38:36', 0, 1, 'default.png'),
(206, 'Natural v/s Machine Intelligence', '\" \"', NULL, NULL, NULL, 'natural-v-s-machine-intelligen-8i7arwen', 35, 91, '2024-02-19 15:38:54', '2024-02-19 15:38:54', 0, 1, 'default.png'),
(207, 'Let’s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-hgmovl2x', 35, 91, '2024-02-19 15:39:01', '2024-02-19 15:39:01', 0, 1, 'default.png'),
(208, 'Introduction to Reasoning', '\" \"', NULL, NULL, NULL, 'introduction-to-reasoning-xe72cjrx', 35, 92, '2024-02-19 15:39:19', '2024-02-19 15:39:19', 0, 1, 'default.png'),
(209, 'Inductive and Deductive Reasoning', '\" \"', NULL, NULL, NULL, 'inductive-and-deductive-reason-4zz1jkzm', 35, 92, '2024-02-19 15:39:31', '2024-02-19 15:39:31', 0, 1, 'default.png'),
(210, 'A comparative example', '\" \"', NULL, NULL, NULL, 'a-comparative-example-trasm1bi', 35, 92, '2024-02-19 15:39:40', '2024-02-19 15:39:40', 0, 1, 'default.png'),
(211, 'Let’s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-ayywy1yy', 35, 92, '2024-02-19 15:39:48', '2024-02-19 15:39:48', 0, 1, 'default.png'),
(212, 'Introduction to Learning', '\" \"', NULL, NULL, NULL, 'introduction-to-learning-valqbobx', 35, 93, '2024-02-19 15:40:07', '2024-02-19 15:40:07', 0, 1, 'default.png'),
(213, 'Types of Learning', '\" \"', NULL, NULL, NULL, 'types-of-learning-eincxruz', 35, 93, '2024-02-19 15:40:15', '2024-02-19 15:40:15', 0, 1, 'default.png'),
(214, 'Methods of Learning', '\" \"', NULL, NULL, NULL, 'methods-of-learning-fezu8l3m', 35, 93, '2024-02-19 15:40:24', '2024-02-19 15:40:24', 0, 1, 'default.png'),
(215, 'Let’s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-rdnnap3m', 35, 93, '2024-02-19 15:40:30', '2024-02-19 15:40:30', 0, 1, 'default.png'),
(216, 'Introduction to Decision-Making', '\" \"', NULL, NULL, NULL, 'introduction-to-decision-makin-h92uuelu', 35, 94, '2024-02-19 15:40:46', '2024-02-19 15:40:46', 0, 1, 'default.png'),
(217, 'Prediction and Judgement', '\" \"', NULL, NULL, NULL, 'prediction-and-judgement-h4tzih3g', 35, 94, '2024-02-19 15:40:57', '2024-02-19 15:40:57', 0, 1, 'default.png'),
(218, 'Human Capabilities and Limitations', '\" \"', NULL, NULL, NULL, 'human-capabilities-and-limitat-obpja7b4', 35, 94, '2024-02-19 15:41:06', '2024-02-19 15:41:06', 0, 1, 'default.png'),
(219, 'Let’s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-ecghrmql', 35, 94, '2024-02-19 15:41:13', '2024-02-19 15:41:13', 0, 1, 'default.png'),
(220, 'Strong AI', '\" \"', NULL, NULL, NULL, 'strong-ai-ise2ywod', 35, 95, '2024-02-19 15:41:34', '2024-02-19 15:41:34', 0, 1, 'default.png'),
(221, 'Weak AI', '\" \"', NULL, NULL, NULL, 'weak-ai-5ykk83ip', 35, 95, '2024-02-19 15:41:43', '2024-02-19 15:41:43', 0, 1, 'default.png'),
(222, 'Plan AI', '\" \"', NULL, NULL, NULL, 'plan-ai-39csqgue', 35, 95, '2024-02-19 15:41:52', '2024-02-19 15:41:52', 0, 1, 'default.png'),
(223, 'Let’s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-ogr61ozi', 35, 95, '2024-02-19 15:42:02', '2024-02-19 15:42:02', 0, 1, 'default.png'),
(224, 'Introduction', '\" \"', NULL, NULL, NULL, 'introduction-gqlfq9lu', 35, 96, '2024-02-19 15:42:31', '2024-02-19 15:42:31', 0, 1, 'default.png'),
(225, 'Agents', '\" \"', NULL, NULL, NULL, 'agents-0nsggnry', 35, 96, '2024-02-19 15:42:40', '2024-02-19 15:42:40', 0, 1, 'default.png'),
(226, 'Let’s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-wue1goob', 35, 96, '2024-02-19 15:42:48', '2024-02-19 15:42:48', 0, 1, 'default.png'),
(227, 'Environments', '\" \"', NULL, NULL, NULL, 'environments-xevdxcmc', 35, 97, '2024-02-19 15:43:19', '2024-02-19 15:43:19', 0, 1, 'default.png'),
(228, 'Different research fields', '\" \"', NULL, NULL, NULL, 'different-research-fields-flfbjsxj', 35, 98, '2024-02-19 15:43:39', '2024-02-19 15:43:39', 0, 1, 'default.png'),
(229, 'Machine Learning and Symbolic Approach', '\" \"', NULL, NULL, NULL, 'machine-learning-and-symbolic-hu8eqzrh', 35, 98, '2024-02-19 15:43:49', '2024-02-19 15:43:49', 0, 1, 'default.png'),
(230, 'Related Technologies', '\" \"', NULL, NULL, NULL, 'related-technologies-3b2wvvfs', 35, 98, '2024-02-19 15:44:00', '2024-02-19 15:44:00', 0, 1, 'default.png'),
(231, 'Let’s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-xnjhbeap', 35, 98, '2024-02-19 15:44:09', '2024-02-19 15:44:09', 0, 1, 'default.png'),
(232, 'Ethical Issues', '\" \"', NULL, NULL, NULL, 'ethical-issues-vczwqovz', 35, 99, '2024-02-19 15:44:29', '2024-02-19 15:44:29', 0, 1, 'default.png'),
(233, 'Technological Issues', '\" \"', NULL, NULL, NULL, 'technological-issues-qerilm6m', 35, 99, '2024-02-19 15:44:37', '2024-02-19 15:44:37', 0, 1, 'default.png'),
(234, 'Let’s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-erpizlrr', 35, 99, '2024-02-19 15:44:45', '2024-02-19 15:44:45', 0, 1, 'default.png'),
(235, 'Data Science & Big Data', '\" \"', NULL, NULL, NULL, 'data-science---big-data-qnyhglom', 35, 100, '2024-02-19 15:45:04', '2024-02-19 15:45:04', 0, 1, 'default.png'),
(236, 'Other Applications', '\" \"', NULL, NULL, NULL, 'other-applications-z68zyr6q', 35, 100, '2024-02-19 15:45:18', '2024-02-19 15:45:18', 0, 1, 'default.png'),
(237, 'Let’s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-jvf3xtph', 35, 100, '2024-02-19 15:45:27', '2024-02-19 15:45:27', 0, 1, 'default.png'),
(238, 'Introduction', '\" \"', NULL, NULL, NULL, 'introduction-4nipaobg', 36, 101, '2024-02-19 16:19:40', '2024-02-19 16:19:40', 0, 1, 'default.png'),
(239, 'ML & AI', '\" \"', NULL, NULL, NULL, 'ml---ai-pcecvhrm', 36, 101, '2024-02-19 16:19:48', '2024-02-19 16:19:48', 0, 1, 'default.png'),
(240, 'Let’s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-qgyfgrvg', 36, 101, '2024-02-19 16:19:57', '2024-02-19 16:19:57', 0, 1, 'default.png'),
(241, 'Teaching to machines', '\" \"', NULL, NULL, NULL, 'teaching-to-machines-s3calr63', 36, 102, '2024-02-19 16:20:25', '2024-02-19 16:20:25', 0, 1, 'default.png'),
(242, 'Patterns, patterns, patterns', '\" \"', NULL, NULL, NULL, 'patterns--patterns--patterns-ywug1ggy', 36, 102, '2024-02-19 16:20:39', '2024-02-19 16:20:39', 0, 1, 'default.png'),
(243, 'Let’s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-nfd6zmcb', 36, 102, '2024-02-19 16:20:47', '2024-02-19 16:20:47', 0, 1, 'default.png'),
(244, 'Everything by hand', '\" \"', NULL, NULL, NULL, 'everything-by-hand-jcyllxvh', 36, 103, '2024-02-19 16:21:02', '2024-02-19 16:21:02', 0, 1, 'default.png'),
(245, 'Modern world and Big Data', '\" \"', NULL, NULL, NULL, 'modern-world-and-big-data-h4lfsish', 36, 103, '2024-02-19 16:21:12', '2024-02-19 16:21:12', 0, 1, 'default.png'),
(246, 'Let’s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-owqluvsl', 36, 103, '2024-02-19 16:21:23', '2024-02-19 16:21:23', 0, 1, 'default.png'),
(247, 'Manual approach', '\" \"', NULL, NULL, NULL, 'manual-approach-lfsagkwd', 36, 104, '2024-02-19 16:24:14', '2024-02-19 16:24:14', 0, 1, 'default.png'),
(248, 'ML Approach', '\" \"', NULL, NULL, NULL, 'ml-approach-yuh2jxzu', 36, 104, '2024-02-19 16:24:37', '2024-02-19 16:24:37', 0, 1, 'default.png'),
(249, 'Let’s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-ui4ynfyv', 36, 104, '2024-02-19 16:24:42', '2024-02-19 16:24:42', 0, 1, 'default.png'),
(250, 'Baby steps', '\" \"', NULL, NULL, NULL, 'baby-steps-kcz47oy0', 36, 105, '2024-02-19 16:27:15', '2024-02-19 16:27:15', 0, 1, 'default.png'),
(251, 'The Artificial Intelligence winter', '\" \"', NULL, NULL, NULL, 'the-artificial-intelligence-wi-isljj97d', 36, 105, '2024-02-19 16:27:28', '2024-02-19 16:27:28', 0, 1, 'default.png'),
(252, 'New discoveries', '\" \"', NULL, NULL, NULL, 'new-discoveries-sab12dxr', 36, 105, '2024-02-19 16:27:51', '2024-02-19 16:27:51', 0, 1, 'default.png'),
(253, 'Let’s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-lxclukvz', 36, 105, '2024-02-19 16:28:05', '2024-02-19 16:28:05', 0, 1, 'default.png'),
(254, 'ML in detail', '\" \"', NULL, NULL, NULL, 'ml-in-detail-5qguleux', 36, 106, '2024-02-19 16:28:39', '2024-02-19 16:28:39', 0, 1, 'default.png'),
(255, 'Discovering features', '\" \"', NULL, NULL, NULL, 'discovering-features-b0rpuwr4', 36, 106, '2024-02-19 16:28:51', '2024-02-19 16:28:51', 0, 1, 'default.png'),
(256, 'Black box', '\" \"', NULL, NULL, NULL, 'black-box-egaynt2y', 36, 106, '2024-02-19 16:29:01', '2024-02-19 16:29:01', 0, 1, 'default.png'),
(257, 'Let’s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-ghkpa01f', 36, 106, '2024-02-19 16:29:09', '2024-02-19 16:29:09', 0, 1, 'default.png'),
(258, 'Choosing with trees', '\" \"', NULL, NULL, NULL, 'choosing-with-trees-4rylxllw', 36, 107, '2024-02-19 16:29:33', '2024-02-19 16:29:33', 0, 1, 'default.png'),
(259, 'Regression', '\" \"', NULL, NULL, NULL, 'regression-glsnfazt', 36, 107, '2024-02-19 16:29:47', '2024-02-19 16:29:47', 0, 1, 'default.png'),
(260, 'Clustering', '\" \"', NULL, NULL, NULL, 'clustering-5oescyix', 36, 107, '2024-02-19 16:29:55', '2024-02-19 16:29:55', 0, 1, 'default.png'),
(261, 'Let’s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-bxgkl0wj', 36, 107, '2024-02-19 16:30:06', '2024-02-19 16:30:06', 0, 1, 'default.png'),
(262, 'Deep Learning', '\" \"', NULL, NULL, NULL, 'deep-learning-6th7cuaf', 36, 108, '2024-02-19 16:30:48', '2024-02-19 16:30:48', 0, 1, 'default.png'),
(263, 'Neural Networks', '\" \"', NULL, NULL, NULL, 'neural-networks-cuecg5ha', 36, 108, '2024-02-19 16:31:04', '2024-02-19 16:31:04', 0, 1, 'default.png'),
(264, 'Let’s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-glyzagfc', 36, 108, '2024-02-19 16:31:12', '2024-02-19 16:31:12', 0, 1, 'default.png'),
(265, 'Good vs bad', '\" \"', NULL, NULL, NULL, 'good-vs-bad-wynunklr', 36, 109, '2024-02-19 16:31:29', '2024-02-19 16:31:29', 0, 1, 'default.png'),
(266, 'Can ML be evil?', '\" \"', NULL, NULL, NULL, 'can-ml-be-evil-ooxfdigt', 36, 109, '2024-02-19 16:31:38', '2024-02-19 16:31:38', 0, 1, 'default.png'),
(267, 'Let’s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-ztgyonqx', 36, 109, '2024-02-19 16:31:50', '2024-02-19 16:31:50', 0, 1, 'default.png'),
(268, 'ML on mobile', '\" \"', NULL, NULL, NULL, 'ml-on-mobile-tcq0lgmy', 36, 110, '2024-02-19 16:32:14', '2024-02-19 16:32:14', 0, 1, 'default.png'),
(269, 'Results, right now!', '\" \"', NULL, NULL, NULL, 'results--right-now-kggd4ucf', 36, 110, '2024-02-19 16:32:24', '2024-02-19 16:32:24', 0, 1, 'default.png'),
(270, 'Quantum computing', '\" \"', NULL, NULL, NULL, 'quantum-computing-fwyfzatv', 36, 110, '2024-02-19 16:32:33', '2024-02-19 16:32:33', 0, 1, 'default.png'),
(271, 'What is this course?', '\" \"', NULL, NULL, NULL, 'what-is-this-course-p8zh5uoh', 38, 111, '2024-02-19 17:06:38', '2024-02-19 17:06:38', 0, 1, 'default.png'),
(272, 'Technologies to be used', '\" \"', NULL, NULL, NULL, 'technologies-to-be-used-3dwf819c', 38, 111, '2024-02-19 17:06:59', '2024-02-19 17:06:59', 0, 1, 'default.png'),
(273, 'Prerequisites', '\" \"', NULL, NULL, NULL, 'prerequisites-ce3vx3g6', 38, 111, '2024-02-19 17:07:07', '2024-02-19 17:07:07', 0, 1, 'default.png'),
(274, 'Let’s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-vq1whdpt', 38, 111, '2024-02-19 17:07:17', '2024-02-19 17:07:17', 0, 1, 'default.png'),
(275, 'What we will be building?', '\" \"', NULL, NULL, NULL, 'what-we-will-be-building-awrigyw1', 38, 112, '2024-02-19 17:07:34', '2024-02-19 17:07:34', 0, 1, 'default.png'),
(276, 'How we will proceed?', '\" \"', NULL, NULL, NULL, 'how-we-will-proceed-lv3jtmnw', 38, 112, '2024-02-19 17:07:42', '2024-02-19 17:07:42', 0, 1, 'default.png'),
(277, 'Setting up the project folder', '\" \"', NULL, NULL, NULL, 'setting-up-the-project-folder-fupx28bq', 38, 113, '2024-02-19 17:07:56', '2024-02-19 17:07:56', 0, 1, 'default.png'),
(278, 'Setting up a basic HTML template', '\" \"', NULL, NULL, NULL, 'setting-up-a-basic-html-templa-hwslmzef', 38, 113, '2024-02-19 17:08:07', '2024-02-19 17:08:07', 0, 1, 'default.png'),
(279, 'Including the necessary files', '\" \"', NULL, NULL, NULL, 'including-the-necessary-files-7upmmggf', 38, 113, '2024-02-19 17:08:17', '2024-02-19 17:08:17', 0, 1, 'default.png'),
(280, 'Let’s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-vuc3chr2', 38, 113, '2024-02-19 17:08:26', '2024-02-19 17:08:26', 0, 1, 'default.png'),
(281, 'The Navigation Bar', '\" \"', NULL, NULL, NULL, 'the-navigation-bar-iyrritrv', 38, 114, '2024-02-19 17:09:17', '2024-02-19 17:09:17', 0, 1, 'default.png'),
(282, 'Background image', '\" \"', NULL, NULL, NULL, 'background-image-v5kuwkao', 38, 114, '2024-02-19 17:09:27', '2024-02-19 17:09:27', 0, 1, 'default.png'),
(283, 'Name and tagline', '\" \"', NULL, NULL, NULL, 'name-and-tagline-cux4xvyg', 38, 114, '2024-02-19 17:09:36', '2024-02-19 17:09:36', 0, 1, 'default.png'),
(284, 'Let’s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-wkhjvxk2', 38, 114, '2024-02-19 17:09:47', '2024-02-19 17:09:47', 0, 1, 'default.png'),
(285, 'Writing the content', '\" \"', NULL, NULL, NULL, 'writing-the-content-iyphuuuq', 38, 115, '2024-02-19 17:10:04', '2024-02-19 17:10:04', 0, 1, 'default.png'),
(286, 'Playing with fonts', '\" \"', NULL, NULL, NULL, 'playing-with-fonts-ynw4zyrd', 38, 115, '2024-02-19 17:10:25', '2024-02-19 17:10:25', 0, 1, 'default.png'),
(287, 'Adding colors', '\" \"', NULL, NULL, NULL, 'adding-colors-18kstk0u', 38, 115, '2024-02-19 17:10:34', '2024-02-19 17:10:34', 0, 1, 'default.png'),
(288, 'Let’s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-1apxumcg', 38, 115, '2024-02-19 17:10:43', '2024-02-19 17:10:43', 0, 1, 'default.png'),
(289, 'Listing the services provided', '\" \"', NULL, NULL, NULL, 'listing-the-services-provided-mrhxxf0h', 38, 116, '2024-02-19 17:11:19', '2024-02-19 17:11:19', 0, 1, 'default.png'),
(290, 'Adding fonts and colors', '\" \"', NULL, NULL, NULL, 'adding-fonts-and-colors-g3hnpr9c', 38, 116, '2024-02-19 17:11:30', '2024-02-19 17:11:30', 0, 1, 'default.png'),
(291, 'Let’s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-pu5h6olm', 38, 116, '2024-02-19 17:11:39', '2024-02-19 17:11:39', 0, 1, 'default.png'),
(292, 'Adding the address and contact information', '\" \"', NULL, NULL, NULL, 'adding-the-address-and-contact-1dxypljw', 38, 117, '2024-02-19 17:11:57', '2024-02-19 17:11:57', 0, 1, 'default.png'),
(293, 'Let’s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-a0kmqwmo', 38, 117, '2024-02-19 17:12:11', '2024-02-19 17:12:11', 0, 1, 'default.png'),
(294, 'Introduction', '\" \"', NULL, NULL, NULL, 'introduction-c6zytrpb', 38, 118, '2024-02-19 17:13:59', '2024-02-19 17:13:59', 0, 1, 'default.png'),
(295, 'Writing the meta tags', '\" \"', NULL, NULL, NULL, 'writing-the-meta-tags-mqqwprsf', 38, 118, '2024-02-19 17:14:10', '2024-02-19 17:14:10', 0, 1, 'default.png'),
(296, 'Let’s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-l8e1vj90', 38, 118, '2024-02-19 17:14:20', '2024-02-19 17:14:20', 0, 1, 'default.png'),
(297, 'Buying a domain and hosting.', '\" \"', NULL, NULL, NULL, 'buying-a-domain-and-hosting-bhx6a7re', 38, 119, '2024-02-19 17:14:35', '2024-02-19 17:14:35', 0, 1, 'default.png'),
(298, 'Hosting the website on Netlify.', '\" \"', NULL, NULL, NULL, 'hosting-the-website-on-netlify-y3hwnl2n', 38, 119, '2024-02-19 17:15:03', '2024-02-19 17:15:03', 0, 1, 'default.png'),
(299, 'Let’s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-coxxltny', 38, 119, '2024-02-19 17:15:12', '2024-02-19 17:15:12', 0, 1, 'default.png'),
(300, 'What is a framework?', '\" \"', NULL, NULL, NULL, 'what-is-a-framework-dx6go4sd', 38, 120, '2024-02-19 17:15:29', '2024-02-19 17:15:29', 0, 1, 'default.png'),
(301, 'What are the popular frameworks available?', '\" \"', NULL, NULL, NULL, 'what-are-the-popular-framework-pvjckh7u', 38, 120, '2024-02-19 17:15:44', '2024-02-19 17:15:44', 0, 1, 'default.png'),
(302, 'What is Responsiveness and why it is important?', '\" \"', NULL, NULL, NULL, 'what-is-responsiveness-and-why-hx4y2vj3', 38, 120, '2024-02-19 17:15:53', '2024-02-19 17:15:53', 0, 1, 'default.png'),
(303, 'Let’s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-b0uw0amk', 38, 120, '2024-02-19 17:16:02', '2024-02-19 17:16:02', 0, 1, 'default.png'),
(304, 'Course Overview', '\" \"', NULL, NULL, NULL, 'course-overview-pomidjzu', 39, 121, '2024-02-19 17:35:00', '2024-02-19 17:35:00', 0, 1, 'default.png'),
(305, 'Some free tools to experiment with', '\" \"', NULL, NULL, NULL, 'some-free-tools-to-experiment-nemn6fip', 39, 121, '2024-02-19 17:36:16', '2024-02-19 17:36:16', 0, 1, 'default.png'),
(306, 'Market Research Introduction', '\" \"', NULL, NULL, NULL, 'market-research-introduction-xdwl3i0u', 39, 122, '2024-02-19 17:36:38', '2024-02-19 17:36:38', 0, 1, 'default.png'),
(307, 'How to find the right audience?', '\" \"', NULL, NULL, NULL, 'how-to-find-the-right-audience-pmlekwii', 39, 122, '2024-02-19 17:36:50', '2024-02-19 17:36:50', 0, 1, 'default.png'),
(308, 'How to get responses to your survey?', '\" \"', NULL, NULL, NULL, 'how-to-get-responses-to-your-s-mephmkhb', 39, 122, '2024-02-19 17:37:02', '2024-02-19 17:37:02', 0, 1, 'default.png'),
(309, 'How to Analyze your Survey Results?', '\" \"', NULL, NULL, NULL, 'how-to-analyze-your-survey-res-n5lm8yiu', 39, 122, '2024-02-19 17:37:15', '2024-02-19 17:37:15', 0, 1, 'default.png'),
(310, 'Case Study', '\" \"', NULL, NULL, NULL, 'case-study-dts9bf8w', 39, 122, '2024-02-19 17:37:26', '2024-02-19 17:37:26', 0, 1, 'default.png'),
(311, 'Build website in less than 1hr', '\" \"', NULL, NULL, NULL, 'build-website-in-less-than-1hr-vvkqmazs', 39, 123, '2024-02-19 17:37:47', '2024-02-19 17:37:47', 0, 1, 'default.png'),
(312, 'What is A/B Testing?', '\" \"', NULL, NULL, NULL, 'what-is-a-b-testing-somk7i3z', 39, 123, '2024-02-19 17:37:58', '2024-02-19 17:37:58', 0, 1, 'default.png'),
(313, 'A/B Testing- Process', '\" \"', NULL, NULL, NULL, 'a-b-testing--process-hvzpb0xp', 39, 123, '2024-02-19 17:38:08', '2024-02-19 17:38:08', 0, 1, 'default.png'),
(314, 'A/B Testing- Collect Data', '\" \"', NULL, NULL, NULL, 'a-b-testing--collect-data-qr8cnoho', 39, 123, '2024-02-19 17:38:20', '2024-02-19 17:38:20', 0, 1, 'default.png'),
(315, 'A/B Testing- Create Variations', '\" \"', NULL, NULL, NULL, 'a-b-testing--create-variations-qhaen1bz', 39, 123, '2024-02-19 17:38:30', '2024-02-19 17:38:30', 0, 1, 'default.png'),
(316, 'A/B Testing- Analyze Results', '\" \"', NULL, NULL, NULL, 'a-b-testing--analyze-results-wqcts12y', 39, 123, '2024-02-19 17:38:42', '2024-02-19 17:38:42', 0, 1, 'default.png'),
(317, 'Case Study', '\" \"', NULL, NULL, NULL, 'case-study-yx1qc4ah', 39, 123, '2024-02-19 17:38:51', '2024-02-19 17:38:51', 0, 1, 'default.png'),
(318, 'Introduction', '\" \"', NULL, NULL, NULL, 'introduction-q890ixpy', 39, 124, '2024-02-19 17:39:09', '2024-02-19 17:39:09', 0, 1, 'default.png'),
(319, 'Google Analytics', '\" \"', NULL, NULL, NULL, 'google-analytics-ukvyhrch', 39, 124, '2024-02-19 17:39:17', '2024-02-19 17:39:17', 0, 1, 'default.png'),
(320, 'Key Matrix', '\" \"', NULL, NULL, NULL, 'key-matrix-rir14h4m', 39, 124, '2024-02-19 17:39:26', '2024-02-19 17:39:26', 0, 1, 'default.png'),
(321, 'Segmentation', '\" \"', NULL, NULL, NULL, 'segmentation-4oqwffpz', 39, 124, '2024-02-19 17:39:35', '2024-02-19 17:39:35', 0, 1, 'default.png'),
(322, 'Emerging Analytics', '\" \"', NULL, NULL, NULL, 'emerging-analytics-rbipnupy', 39, 124, '2024-02-19 17:39:44', '2024-02-19 17:39:44', 0, 1, 'default.png'),
(323, 'Case Study', '\" \"', NULL, NULL, NULL, 'case-study-utm7ktff', 39, 124, '2024-02-19 17:39:52', '2024-02-19 17:39:52', 0, 1, 'default.png'),
(324, 'Definition', '\" \"', NULL, NULL, NULL, 'definition-dsqj6gbt', 39, 125, '2024-02-19 17:40:14', '2024-02-19 17:40:14', 0, 1, 'default.png'),
(325, 'Basics', '\" \"', NULL, NULL, NULL, 'basics-kgt56k6h', 39, 125, '2024-02-19 17:40:33', '2024-02-19 17:40:33', 0, 1, 'default.png'),
(326, 'Understanding your customers', '\" \"', NULL, NULL, NULL, 'understanding-your-customers-wljgdctf', 39, 125, '2024-02-19 17:40:37', '2024-02-19 17:40:37', 0, 1, 'default.png'),
(327, 'Goal setting and Planning', '\" \"', NULL, NULL, NULL, 'goal-setting-and-planning-diasqxny', 39, 125, '2024-02-19 17:40:46', '2024-02-19 17:40:46', 0, 1, 'default.png'),
(328, 'UX and Landing Page', '\" \"', NULL, NULL, NULL, 'ux-and-landing-page-dostas2s', 39, 125, '2024-02-19 17:40:55', '2024-02-19 17:40:55', 0, 1, 'default.png'),
(329, 'Measuring Results', '\" \"', NULL, NULL, NULL, 'measuring-results-smqsmjp5', 39, 125, '2024-02-19 17:41:04', '2024-02-19 17:41:04', 0, 1, 'default.png'),
(330, 'Affiliate Marketing', '\" \"', NULL, NULL, NULL, 'affiliate-marketing-xpopj83b', 39, 126, '2024-02-19 17:41:23', '2024-02-19 17:41:23', 0, 1, 'default.png'),
(331, 'Online Reputation Marketing', '\" \"', NULL, NULL, NULL, 'online-reputation-marketing-vxjrxdgb', 39, 126, '2024-02-19 17:41:33', '2024-02-19 17:41:33', 0, 1, 'default.png'),
(332, 'Google Adwords', '\" \"', NULL, NULL, NULL, 'google-adwords-i0qzhwbe', 39, 126, '2024-02-19 17:41:43', '2024-02-19 17:41:43', 0, 1, 'default.png'),
(333, 'Case Study', '\" \"', NULL, NULL, NULL, 'case-study-kojs1cjw', 39, 126, '2024-02-19 17:41:51', '2024-02-19 17:41:51', 0, 1, 'default.png'),
(334, 'Understanding User Interface', '\" \"', NULL, NULL, NULL, 'understanding-user-interface-q0pq4hgt', 40, 128, '2024-02-20 10:24:05', '2024-02-20 10:24:05', 0, 1, 'default.png'),
(335, 'What is User Experience?', '\" \"', NULL, NULL, NULL, 'what-is-user-experience-qhlop2zs', 40, 128, '2024-02-20 10:24:24', '2024-02-20 10:24:24', 0, 1, 'default.png'),
(336, 'Know the differences - UI vs UX', '\" \"', NULL, NULL, NULL, 'know-the-differences---ui-vs-u-otk5zkfr', 40, 128, '2024-02-20 10:24:46', '2024-02-20 10:24:46', 0, 1, 'default.png'),
(337, 'Roles in UI/UX', '\" \"', NULL, NULL, NULL, 'roles-in-ui-ux-sxqpqo7m', 40, 128, '2024-02-20 10:24:55', '2024-02-20 10:24:55', 0, 1, 'default.png'),
(338, 'Let’s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-ix1bkigr', 40, 128, '2024-02-20 10:25:03', '2024-02-20 10:25:03', 0, 1, 'default.png'),
(339, 'Consistency - What is it?', '\" \"', NULL, NULL, NULL, 'consistency---what-is-it-bcbrdmxb', 40, 129, '2024-02-20 10:25:22', '2024-02-20 10:25:22', 0, 1, 'default.png'),
(340, 'Types of Consistency', '\" \"', NULL, NULL, NULL, 'types-of-consistency-swnbff3d', 40, 129, '2024-02-20 10:25:36', '2024-02-20 10:25:36', 0, 1, 'default.png'),
(341, 'Understanding consistency in UI/UX', '\" \"', NULL, NULL, NULL, 'understanding-consistency-in-u-cqlxk9oh', 40, 129, '2024-02-20 10:25:45', '2024-02-20 10:25:45', 0, 1, 'default.png'),
(342, 'Recap', '\" \"', NULL, NULL, NULL, 'recap-pgpndc2f', 40, 129, '2024-02-20 10:25:53', '2024-02-20 10:25:53', 0, 1, 'default.png'),
(343, 'Affordances, Signifiers & Feedbacks', '\" \"', NULL, NULL, NULL, 'affordances--signifiers---feed-b3nmbp7e', 40, 130, '2024-02-20 10:26:14', '2024-02-20 10:26:14', 0, 1, 'default.png'),
(344, 'Diving Deep into Affordances', '\" \"', NULL, NULL, NULL, 'diving-deep-into-affordances-tdiitf4d', 40, 130, '2024-02-20 10:26:25', '2024-02-20 10:26:25', 0, 1, 'default.png'),
(345, 'Signifiers - What are they?', '\" \"', NULL, NULL, NULL, 'signifiers---what-are-they-td3bntqz', 40, 130, '2024-02-20 10:26:34', '2024-02-20 10:26:34', 0, 1, 'default.png'),
(346, 'Feedbacks in UI/UX', '\" \"', NULL, NULL, NULL, 'feedbacks-in-ui-ux-hk2eicjq', 40, 130, '2024-02-20 10:26:44', '2024-02-20 10:26:44', 0, 1, 'default.png'),
(347, 'Recap', '\" \"', NULL, NULL, NULL, 'recap-43niqo8q', 40, 130, '2024-02-20 10:27:00', '2024-02-20 10:27:00', 0, 1, 'default.png'),
(348, 'The Color Theory', '\" \"', NULL, NULL, NULL, 'the-color-theory-e7wcmdy9', 40, 131, '2024-02-20 10:27:24', '2024-02-20 10:27:24', 0, 1, 'default.png'),
(349, 'Color Models', '\" \"', NULL, NULL, NULL, 'color-models-qjslguhr', 40, 131, '2024-02-20 10:27:32', '2024-02-20 10:27:32', 0, 1, 'default.png'),
(350, 'Understanding the color wheel', '\" \"', NULL, NULL, NULL, 'understanding-the-color-wheel-7dhq52wi', 40, 131, '2024-02-20 10:27:47', '2024-02-20 10:27:47', 0, 1, 'default.png'),
(351, 'The color concept', '\" \"', NULL, NULL, NULL, 'the-color-concept-let0q0ry', 40, 131, '2024-02-20 10:27:56', '2024-02-20 10:27:56', 0, 1, 'default.png'),
(352, 'Recap', '\" \"', NULL, NULL, NULL, 'recap-xb641lsl', 40, 131, '2024-02-20 10:28:06', '2024-02-20 10:28:06', 0, 1, 'default.png'),
(353, 'Understanding the aspect of Size', '\" \"', NULL, NULL, NULL, 'understanding-the-aspect-of-si-p1f9sxvb', 40, 132, '2024-02-20 10:28:23', '2024-02-20 10:28:23', 0, 1, 'default.png'),
(354, 'Terms related to size', '\" \"', NULL, NULL, NULL, 'terms-related-to-size-5jcnnlps', 40, 132, '2024-02-20 10:28:38', '2024-02-20 10:28:38', 0, 1, 'default.png'),
(355, 'Let’s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-fckbezz4', 40, 132, '2024-02-20 10:28:46', '2024-02-20 10:28:46', 0, 1, 'default.png'),
(356, 'Understanding Typography', '\" \"', NULL, NULL, NULL, 'understanding-typography-mbrk4gif', 40, 133, '2024-02-20 10:28:59', '2024-02-20 10:28:59', 0, 1, 'default.png'),
(357, 'Using Icons in UI/UX', '\" \"', NULL, NULL, NULL, 'using-icons-in-ui-ux-xcjjjeub', 40, 133, '2024-02-20 10:29:12', '2024-02-20 10:29:12', 0, 1, 'default.png'),
(358, 'Recap', '\" \"', NULL, NULL, NULL, 'recap-37jpflij', 40, 133, '2024-02-20 10:29:21', '2024-02-20 10:29:21', 0, 1, 'default.png'),
(359, 'What is it?', '\" \"', NULL, NULL, NULL, 'what-is-it-w2u2tirx', 40, 134, '2024-02-20 10:29:37', '2024-02-20 10:29:37', 0, 1, 'default.png'),
(360, 'Types of user flows charts', '\" \"', NULL, NULL, NULL, 'types-of-user-flows-charts-gd8tf4zm', 40, 134, '2024-02-20 10:29:48', '2024-02-20 10:29:48', 0, 1, 'default.png'),
(361, 'Elements of Userflows', '\" \"', NULL, NULL, NULL, 'elements-of-userflows-ztor3ibb', 40, 134, '2024-02-20 10:29:56', '2024-02-20 10:29:56', 0, 1, 'default.png'),
(362, 'Let’s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-0kkncq91', 40, 134, '2024-02-20 10:30:03', '2024-02-20 10:30:03', 0, 1, 'default.png'),
(363, 'Wireframes and Prototypes', '\" \"', NULL, NULL, NULL, 'wireframes-and-prototypes-wylhklgz', 40, 135, '2024-02-20 10:31:18', '2024-02-20 10:31:18', 0, 1, 'default.png'),
(364, 'Let’s draw wireframes', '\" \"', NULL, NULL, NULL, 'let-s-draw-wireframes-9vdamz4f', 40, 135, '2024-02-20 10:31:28', '2024-02-20 10:31:28', 0, 1, 'default.png'),
(365, 'Understanding prototyping', '\" \"', NULL, NULL, NULL, 'understanding-prototyping-sqvbbtoo', 40, 135, '2024-02-20 10:31:37', '2024-02-20 10:31:37', 0, 1, 'default.png'),
(366, 'Recap', '\" \"', NULL, NULL, NULL, 'recap-06z4h9og', 40, 135, '2024-02-20 10:31:46', '2024-02-20 10:31:46', 0, 1, 'default.png'),
(367, 'Testing your knowledge', '\" \"', NULL, NULL, NULL, 'testing-your-knowledge-rztg1zom', 40, 136, '2024-02-20 10:32:06', '2024-02-20 10:32:06', 0, 1, 'default.png'),
(368, 'Farewell', '\" \"', NULL, NULL, NULL, 'farewell-yeo9w9az', 40, 136, '2024-02-20 10:32:14', '2024-02-20 10:32:14', 0, 1, 'default.png');
INSERT INTO `topic` (`id`, `title`, `desc`, `video`, `material`, `duration`, `slug`, `course_id`, `lesson_id`, `created`, `updated`, `deleted`, `active`, `image`) VALUES
(369, 'Introduction To React  Native', '\"[\\r\\n    {\\r\\n        \\\"id\\\": 0,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Introduction\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Welcome to the React Native journey!\\\",\\r\\n            \\\"My name is ReactMan, I am here to guide you throughout the course.\\\",\\r\\n            \\\"Let\'s start and get familiar with React Native\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Hot and Trending\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"It is not wrong to say that mobile phones are the half soul of every individual.\\\",\\r\\n            \\\"When it comes to Android development or iOS development, businesses often get confused whether they should offer their consumers, a mobile app with superlative UI and outstanding UX or apps that are compatible with multiple platforms and are faster to develop.\\\",\\r\\n            \\\"Here comes the React Native Development into the picture!\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 2,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"What is React Native?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"React Native is an application development environment developed by Facebook.\\\",\\r\\n            \\\"Native app creation simply means writing apps for a specific operating system. Nowadays on demand mobile application development is done by React Native.\\\",\\r\\n            \\\"React Native is a JavaScript framework for writing real, natively rendering mobile applications for iOS and Android.\\\",\\r\\n            \\\"It\\u2019s based on React, Facebook\\u2019s JavaScript library for building user interfaces, but instead of targeting the browser, it targets mobile platforms.\\\",\\r\\n            \\\"\\u201cLearn once, Write everywhere\\u201d\\\",\\r\\n            \\\"In other words, developers can now write mobile applications that look and feel truly \\u201cnative,\\u201d all from the comfort of a JavaScript library that we already know and love.\\\",\\r\\n            \\\"Plus, because most of the code you write can be shared between platforms, React Native makes it easy to simultaneously develop for both Android and iOS.\\\",\\r\\n            \\\"React Native helps developers reuse code across the web and on mobile.\\\",\\r\\n            \\\"We don\'t need to build the same app for iOS and for Android from scratch, we can reuse the code across each operating system.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 3,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Fill in the blank\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"React Native is a framework for building cross-platform applications using _____ in Facebook\\u2019s own React library.\\\",\\r\\n            \\\"Tap the correct answer to fill in the blanks\\\",\\r\\n            \\\"Javascript  | Typescript | React.js| Next.js\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 4,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"The history of React Native\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"React Native was developed and launched by the Facebook Team in 2015.\\\",\\r\\n            \\\"Not sure they expected to turn the world of mobile development upside down or at least shake it goodly.\\\",\\r\\n            \\\"However, the dynamic of React Native\\u2019s popularity speaks for itself.\\\",\\r\\n            \\\"The React Native idea was developed out of another Facebook\\u2019s innovation - React (a.k.a. ReactJS or React.js).\\\",\\r\\n            \\\"This is a JS framework for creating web user interfaces.\\\",\\r\\n            \\\"It was introduced in 2013, two years before its younger mobile brother was announced.\\\",\\r\\n            \\\"Actually, the whole concept of React Native was greatly influenced by Facebook\\u2019s experience with web development, which they wanted to bring to mobile development as well.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 5,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"React vs. React Native\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"In the simple terms, React Native isn\\u2019t a \\u2018newer\\u2019 version of React, although React Native does use it.\\\",\\r\\n            \\\"Both React and React Native use a mixture of JavaScript and a special markup language, JSX.\\\",\\r\\n            \\\"Meanwhile, React Native \\u2013 which is powered by React \\u2013 lets developers use a set of UI components to quickly compile and launch iOS and Android apps.\\\",\\r\\n            \\\"Hence, while the two frameworks are related to one another, they\\u2019re used for different purposes.\\\",\\r\\n            \\\"Knowledge of React won\\u2019t be enough for iOS and Android mobile app development.\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 5,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"React vs. React Native\\\",\\r\\n        \\\"desc\\\": [\\r\\n            {   \\\"type\\\": \\\"obj\\\",\\r\\n                \\\"question\\\": \\\"React Native was first released by _______ as an open-source project in 2015.\\\",\\r\\n                \\\"options\\\": [\\\"Facebook\\\", \\\"Google\\\", \\\"Apple\\\", \\\"Microsoft\\\"],\\r\\n                \\\"correct_answer\\\": \\\"Facebook\\\"\\r\\n            },\\r\\n            {   \\\"type\\\": \\\"obj\\\",\\r\\n                \\\"question\\\": \\\"Products built with React Native are?\\\",\\r\\n                \\\"options\\\": [\\\"Facebook\\\", \\\"Instagram\\\", \\\"Walmart\\\", \\\"Ola\\\"],\\r\\n                \\\"correct_answer\\\": [\\\"Facebook\\\", \\\"Instagram\\\", \\\"Walmart\\\"]\\r\\n            },\\r\\n            {   \\\"type\\\": \\\"obj\\\",\\r\\n                \\\"question\\\": \\\"React Native development uses _______ to build the app\\u2019s interface.\\\",\\r\\n                \\\"options\\\": [\\\"React.js\\\", \\\"Node.js\\\", \\\"Typescript\\\", \\\"Apache Cordova\\\"],\\r\\n                \\\"correct_answer\\\": \\\"React.js\\\"\\r\\n            },\\r\\n            {   \\\"type\\\": \\\"obj\\\",\\r\\n                \\\"question\\\": \\\"UI elements that differ on iOS and Android include certain fonts, status bar, and GIF images.\\\",\\r\\n                \\\"options\\\": [\\\"True\\\", \\\"False\\\"],\\r\\n                \\\"correct_answer\\\": \\\"True\\\"\\r\\n            }\\r\\n\\r\\n        ]\\r\\n    }\\r\\n]\"', NULL, NULL, NULL, 'introduction-to-react-native-wrgpropg', 30, 137, '2024-02-20 11:35:41', '2024-02-20 11:35:41', 0, 1, 'default.webp'),
(370, 'How Does React Native Work?', '\"[\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Introduction\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Now that we\\u2019ve seen a short introduction on React Native, let\\u2019s take a look at the mechanics of React Native, and how it\\u2019s different from anything we\\u2019ve seen before.\\\",\\r\\n            \\\"Don\\u2019t worry, we will understand it in layman terms.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 2,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"The bridge concept\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"While JavaScript and Native threads are written in completely different languages, it\\u2019s the bridge feature that makes bidirectional communication possible.\\\",\\r\\n            \\\"This means that \\u2013 if you already have a native iOS or Android app \\u2013 you can still use its components or shift to React Native development.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": \\\"2.x\\\",\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"The bridge concept\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"As mentioned earlier, React Native is written with a mixture of JavaScript and JSX, a special markup code resemblant of XML.\\\",\\r\\n            \\\"The framework has the ability to communicate with both realms \\u2013 JavaScript-based threads and existent, native app threads.\\\",\\r\\n            \\\"How does this communication work? React Native uses a so-called \\u201cbridge\\u201d.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 3,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"What makes React Native unique?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"The difference between React Native and other cross-platform development solutions (for example, Cordova and PhoneGap) is that React Native doesn\\u2019t render WebViews in its code.\\\",\\r\\n            \\\"It runs on actual, native views and components. This is one of the reasons for React Native\\u2019s spectacular success.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 4,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Top notch app built with React Native\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Let\\u2019s have a look at the products built with React Native.\\\",\\r\\n            \\\"Facebook, Skype, Instagram, Walmart, UberEats, Pinterest. From startups to Fortune 500 companies, if you\\u2019re considering taking on a new mobile project, consider using React Native \\u2014 You won\\u2019t regret it.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 5,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Question\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"The bridge feature makes bidirectional communication possible..\\\",\\r\\n            \\\"True\\\",\\r\\n            \\\"False\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 6,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Benefits of React Native\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Let\\u2019s move onto the advantages of React Native development and why you should choose it as a solution to build your mobile app.\\\",\\r\\n            \\\"Code reusability. Being able to reuse code is the biggest advantage of React Native, and it indicates that apps can run effectively on multiple platforms \\u2013 which is something that CEOs and Product Owners truly appreciate.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 7,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Benefits of React Native\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Cost efficiency. As mentioned earlier, this is because developers are able to use the same code to build applications for iOS and Android.\\\",\\r\\n            \\\"It means you don\\u2019t have to hire two separate iOS and Android dev teams to finalize your project; a small team is enough to build it.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 8,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Benefits of React Native\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Simple UI. React Native \\u2013 Differences in development for Android and iOS. Coming back to React Native, I\\u2019m sure you\\u2019re also wondering \\u2013 how does React Native development differ for Android and iOS?\\\",\\r\\n            \\\"After all, from a user point of view, both environments have their share of differences (with UI being the most apparent).\\\",\\r\\n            \\\"Let\\u2019s have a look at the key areas where things work a little differently between the platforms.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 9,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Operating system\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"You can run your tests solely for your Android app, and there\\u2019s just one official testing tool \\u2013 Android Studio.\\\",\\r\\n            \\\"The reason for this is that Windows cannot run XCode, a development environment created by Apple for iOS, macOS, tvOS, and watchOS.\\\",\\r\\n            \\\"So, while you can certainly build your React Native app on both operating systems, only macOS gives you a way to check if both of your Android and iOS React Native apps are working properly.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 10,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Native elements\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"As Android and iOS apps look and function differently, they also have different components.\\\",\\r\\n            \\\"This means that \\u2013 when you\\u2019re using your React Native library \\u2013 you might see a different end result for iOS and Android, even though you\\u2019re using the same component.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 11,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Specific styles\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"iOS and Android have different styles for React Native elements.\\\",\\r\\n            \\\"A great example is shadowing.\\\",\\r\\n            \\\"The shadow is styled once with JavaScript, and the elements are automatically displayed in a platform-specific manner.\\\",\\r\\n            \\\"Other UI elements that differ on iOS and Android include certain fonts, status bar, and GIF images (which aren\\u2019t automatically supported on Android).\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 12,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Top takeaways\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Suppose you have a Startup, you probably won\'t be able to afford two separate dev teams and will have to choose between shipping your product first to iOS or Android.\\\",\\r\\n            \\\"With React Native you can build a single codebase that is usually 70-80% reusable for both platforms.\\\",\\r\\n            \\\"If you have a Team of web pros\', switching them to mobile development doesn\'t seem like a perspective idea.\\\",\\r\\n            \\\"However, since React Native is a JS-based framework, putting your Web Team on RN rails is quite an achievable task.\\\"\\r\\n        ]\\r\\n    }\\r\\n]\"', NULL, NULL, NULL, 'how-does-react-native-work-gdyzpouu', 30, 137, '2024-02-20 11:35:44', '2024-02-20 11:35:44', 0, 1, 'default.webp'),
(371, 'Recap', '\"[\\r\\n    {\\r\\n        \\\"question\\\": \\\"Fill in the blank\\\",\\r\\n        \\\"question_content\\\": \\\"React Native was first released by _______ as an open-source project in 2015.\\\",\\r\\n        \\\"options\\\": [\\\"Facebook\\\", \\\"Google\\\", \\\"Apple\\\", \\\"Microsoft\\\"],\\r\\n        \\\"correct_answer\\\": \\\"Facebook\\\"\\r\\n    },\\r\\n    {\\r\\n        \\\"question\\\": \\\"Tap the correct answer to fill in the blanks\\\",\\r\\n        \\\"question_content\\\": \\\"Products built with React Native are?\\\",\\r\\n        \\\"options\\\": [\\\"Facebook\\\", \\\"Instagram\\\", \\\"Walmart\\\", \\\"Ola\\\"],\\r\\n        \\\"correct_answer\\\": [\\\"Facebook\\\", \\\"Instagram\\\", \\\"Walmart\\\"]\\r\\n    },\\r\\n    {\\r\\n        \\\"question\\\": \\\"Choose the correct one\\\",\\r\\n        \\\"question_content\\\": \\\"React Native development uses _______ to build the app\\u2019s interface.\\\",\\r\\n        \\\"options\\\": [\\\"React.js\\\", \\\"Node.js\\\", \\\"Typescript\\\", \\\"Apache Cordova\\\"],\\r\\n        \\\"correct_answer\\\": \\\"React.js\\\"\\r\\n    },\\r\\n    {\\r\\n        \\\"question\\\": \\\"Select the right answer\\\",\\r\\n        \\\"question_content\\\": \\\"UI elements that differ on iOS and Android include certain fonts, status bar, and GIF images.\\\",\\r\\n        \\\"options\\\": [\\\"True\\\", \\\"False\\\"],\\r\\n        \\\"correct_answer\\\": \\\"True\\\"\\r\\n    }\\r\\n]\"', NULL, NULL, NULL, 'recap-rximjito', 30, 137, '2024-02-20 11:35:54', '2024-02-20 11:35:54', 0, 1, 'default.webp'),
(372, 'Installing Dependencies', '\"[\\r\\n    {\\r\\n        \\\"id\\\": 2,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Introduction\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"Hello and welcome to the React Native environment setup.\\\",\\r\\n            \\\"Okay, okay, geez, don\\u2019t be so impatient!\\\",\\r\\n            \\\"We\\u2019ll get to it soon enough, but first, we\\u2019ll need some tools to kick off the development.\\\",\\r\\n            \\\"So, let\\u2019s dive right into it.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 3,\\r\\n        \\\"image\\\": \\\"null.png\\\",\\r\\n        \\\"title\\\": \\\"Prerequisites\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"We will need Node, the React Native command line interface, and Android Studio.\\\",\\r\\n            \\\"While you can use any editor of your choice to develop your app, you will need to install Android Studio in order to set up the necessary tooling to build your React Native app for Android.\\\",\\r\\n            \\\"We will be working with Android studio in the later part of the session.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 4,\\r\\n        \\\"image\\\": \\\"null.png\\\",\\r\\n        \\\"title\\\": \\\"Install React Native App\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"I recommend installing Node via Chocolatey, a popular package manager for Windows.\\\",\\r\\n            \\\"Node comes with npm (Node Package Manager), which lets you install the React Native.\\\",\\r\\n            \\\"After installing NodeJS and NPM successfully in your system you can proceed with installation of create-react-native-app (globally as shown below).\\\",\\r\\n            \\\"npm install -g create-react-native-app\\\",\\r\\n            \\\"Once the above command is executed, a folder with specified name is created with the contents as shown in the image above.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 4.0,\\r\\n        \\\"image\\\": \\\"react_project_folder.png\\\",\\r\\n        \\\"title\\\": \\\"Creating a project\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"Browse through the required folder and create a new react native project as shown here.\\\",\\r\\n            \\\"`create-react-native-app MyReactNative`\\\",\\r\\n            \\\"Once the this command is executed, a folder with specified name is created with the contents as shown in the image above.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 4.1,\\r\\n        \\\"image\\\": \\\"null.png\\\",\\r\\n        \\\"title\\\": \\\"Question\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"The command used to install the React Native app is?\\\",\\r\\n            \\\"create-react-native-app MyReactNative |\\\",\\r\\n            \\\"npm install -g create-react-native-app |\\\",\\r\\n            \\\"create-g-react-native-app |\\\",\\r\\n            \\\"install -g create-react-native-app npm |\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 5,\\r\\n        \\\"image\\\": \\\"install_react_cli.png\\\",\\r\\n        \\\"title\\\": \\\"Let\\u2019s install React Native CLI\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"Make sure you have Python, NodeJS and JDK8 installed in your system.\\\",\\r\\n            \\\"You can install react native command line interface on npm, using the command as shown below.\\\",\\r\\n            \\\"npm install -g react-native-cli\\\",\\r\\n            \\\"In addition to these I recommend installing the latest version of yarn to avoid certain issues.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 6,\\r\\n        \\\"image\\\": \\\"react_qr.png\\\",\\r\\n        \\\"title\\\": \\\"Start React Native\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"To verify the installation, browse through the project folder and try starting the project using the start command.\\\",\\r\\n            \\\"`MyReactNative > npm start` .\\\",\\r\\n            \\\"Fortunately if everything goes well you will get a QR code as shown above.\\\",\\r\\n            \\\"One way to run react native apps on your android device is to use expo.\\\",\\r\\n            \\\"Install the expo client in your android device and scan the above obtained QR code.\\\"\\r\\n        ]\\r\\n    }\\r\\n]\"', NULL, NULL, NULL, 'installing-dependencies-l6sgz6q8', 30, 138, '2024-02-20 11:36:15', '2024-02-20 11:36:15', 0, 1, 'default.webp'),
(373, 'Setting‌ ‌Android‌ ‌SDK‌ ‌Path', '\"[\\r\\n    {\\r\\n        \\\"id\\\": 7,\\r\\n        \\\"image\\\": \\\"android_studio.png\\\",\\r\\n        \\\"title\\\": \\\"Installing Android Studio\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"Visit the official web page and download Android Studio from https://developer.android.com/studio/\\\",\\r\\n            \\\"After downloading the installation file, double click on it and proceed with the installation.\\\",\\r\\n            \\\"After successful installation, the Android Studio home screen will appear.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 8,\\r\\n        \\\"image\\\": \\\"android_studio1.png\\\",\\r\\n        \\\"title\\\": \\\"Configuring Android SDK path\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"Set Android SDK path as `My Computer > Properties > Advanced system settings > Environment Variables > in System variables section`.\\\",\\r\\n            \\\"Click \\\\\\\"New...\\\\\\\" to add Android home and Android SDK as shown in the screen.\\\",\\r\\n            \\\"Now install the required components by going to `Tools > Android > SDK Manager > SDK platforms` and selecting the required components to install.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 9,\\r\\n        \\\"image\\\": \\\"android_studio2.png\\\",\\r\\n        \\\"title\\\": \\\"Android Emulator\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"Create an Android Emulator, a virtual Android Device, by going to Tools > Android > AVD Manager > Create Virtual Device... and selecting the device type.\\\",\\r\\n            \\\"Now select the API level of the Android Emulator.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 10,\\r\\n        \\\"image\\\": \\\"android_studio8.png\\\",\\r\\n        \\\"title\\\": \\\"AVD configuration\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"Finally, click on the Finish button to finish the AVD configuration.\\\",\\r\\n            \\\"After configuring your virtual device, click on the play button under the Actions column to start your Android emulator.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 11,\\r\\n        \\\"image\\\": \\\"android_studio.png\\\",\\r\\n        \\\"title\\\": \\\"Select the right answer\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"An Android Emulator is a virtual Android Device.\\\",\\r\\n            \\\"True\\\",\\r\\n            \\\"False\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 12,\\r\\n        \\\"image\\\": \\\"start_react.png\\\",\\r\\n        \\\"title\\\": \\\"Running Android\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"Open command prompt, browse through your project folder, and execute the `react-native run-android` command.\\\",\\r\\n            \\\"Then, your app execution begins in another prompt and you can see its status.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 13,\\r\\n        \\\"image\\\": \\\"react_native0.png\\\",\\r\\n        \\\"title\\\": \\\"-\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"In your android emulator you can see the execution of the default app as:\\\"\\r\\n        ]\\r\\n    }\\r\\n]\"', NULL, NULL, NULL, 'setting---android---sdk---path-b3mlsonc', 30, 138, '2024-02-20 11:36:29', '2024-02-20 11:36:29', 0, 1, 'default.webp'),
(374, 'Let’s Revise', '\"[\\r\\n    {\\r\\n        \\\"id\\\": 13,\\r\\n        \\\"image\\\": \\\"select_answer.png\\\",\\r\\n        \\\"title\\\": \\\"Select the right answer\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"The command used to install React Native CLI is?\\\",\\r\\n            \\\"`cli install -g react-native-npm`\\\",\\r\\n            \\\"`npm install -g create-react-native-cli\\\",\\r\\n            \\\"`cli install -g create-react-native-npm`\\\",\\r\\n            \\\"`npm install -g react-native-cli`\\\" \\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 14,\\r\\n        \\\"image\\\": \\\"select_answer.png\\\",\\r\\n        \\\"title\\\": \\\"Select the right answer\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"One way to run React Native apps on your Android device is to use Expo.\\\",\\r\\n            \\\"`False`\\\",\\r\\n            \\\"`True`\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 15,\\r\\n        \\\"image\\\": \\\"select_answer.png\\\",\\r\\n        \\\"title\\\": \\\"Choose the correct one\\\",\\r\\n        \\\"desc\\\":[\\r\\n            \\\"To start your Android emulator, click on the what?\\\",\\r\\n            \\\"`Play button`\\\",\\r\\n            \\\"`Action`\\\",\\r\\n            \\\"`New`\\\",\\r\\n            \\\"`Advanced`\\\"\\r\\n        ]\\r\\n    }\\r\\n]\"', NULL, NULL, NULL, 'let-s-revise-8shlsyyp', 30, 138, '2024-02-20 11:36:38', '2024-02-20 11:36:38', 0, 1, 'default.webp'),
(375, 'Hello World', '\"[\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Introduction\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Hey curious one!\\\",\\r\\n            \\\"Ready to follow the tradition?\\\",\\r\\n            \\\"So, let\\u2019s work on our application.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 2,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"First app Hello World\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"In accordance with the ancient traditions of our people, we must first build an app that does nothing except say \\\\\\\"Hello world\\\\\\\". \\\\n\\\",\\r\\n            \\\"import React from \'react\';import { StyleSheet, Text, View } from \'reactnative\'; \\\\n\\\",\\r\\n            \\\"export default class App extends React.Component { \\\",\\r\\n            \\\"render() { return ( <View> <Text>Hello World</Text> </View> ); } } .\\\\n\\\",\\r\\n            \\\"If you are feeling curious, you can play around with the sample code directly in the web simulators.\\\",\\r\\n            \\\"You can also paste it into your App.js file to create a real app on your local machine.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 3,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Making it simple\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"First of all, we need to import React to be able to use JSX, which will then be transformed to the native components of each platform.\\\",\\r\\n            \\\"Next we import the StyleSheet, Text and View components from reactnative.\\\",\\r\\n            \\\"Then there is a default class that defines the classes that extend the React Component.\\\",\\r\\n            \\\"This block of code defines the components that represent the user interface.\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 4,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Fill in the blank\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"We need to --- React to be able to use JSX.?\\\",\\r\\n            \\\"`import`\\\",\\r\\n            \\\"`export`\\\"\\r\\n        ]\\r\\n\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 5,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"Let\\u2019s bring in StyleSheet\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"We can edit the React Native \\\\\\\"Hello World\\\\\\\" application using StyleSheet in the following manner:\\\\n\\\",\\r\\n            \\\"import React, {Component} from \'react\'; \\\\n\\\",\\r\\n            \\\"import {Platform, StyleSheet, Text, View} from `reactnative`; \\\\n\\\",\\r\\n            \\\"export default class App extends Component <Props> { \\\\n\\\",\\r\\n            \\\"render() { return ( <View><Text style={styles.welcome}> Hello World </Text> </View> ); } } .\\\\n\\\",\\r\\n            \\\"const styles = StyleSheet.create({ \\\",\\r\\n            \\\"welcome: { fontSize: 20, textAlign: \'center\', margin: 10, } });\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 6,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"How it works?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Let\\u2019s start with a render() function that returns a React element.\\\",\\r\\n            \\\"return() function returns the result of layout and UI components.\\\",\\r\\n            \\\"View is a container that supports the layout accessibility controls.\\\",\\r\\n            \\\"Text is used for displaying a text.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 7,\\r\\n        \\\"image\\\": \\\"react_native.png\\\",\\r\\n        \\\"title\\\": \\\"More to go!\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"style: a property used for styling the components using StyleSheet.\\\",\\r\\n            \\\"styles: used to design individual components.\\\",\\r\\n            \\\"const styles = StyleSheet.create({}):\\\", \\r\\n            \\\"The StyleSheet class creates the style object that controls the layout and appearance of components.\\\", \\r\\n            \\\"It is similar to Cascading Style Sheets (CSS) used on the Web.\\\"\\r\\n        ]\\r\\n    }\\r\\n]\"', NULL, NULL, NULL, 'hello-world-45lz3puy', 30, 139, '2024-02-20 11:36:56', '2024-02-20 11:36:56', 0, 1, 'default.webp'),
(376, 'Components in React Native', '\"[\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 3,\\r\\n        \\\"title\\\": \\\"Components\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"A component is a very basic element in React-Native that helps use to divide the large application into many small Components.\\\",\\r\\n            \\\"This makes development fast and maintains the code very clear to understand.\\\",\\r\\n            \\\"The components in React Native are defined as functions or classes.\\\",\\r\\n            \\\"To define the React component class, a React.component is extended.\\\",\\r\\n            \\\"Using React Native Props and State, we can control one component.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 4,\\r\\n        \\\"title\\\": \\\"What are Props?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"props\\u2019 stands for \\u2018properties\\u2019. Normally, a parent component passes prop to its child components.\\\",\\r\\n            \\\"The child component uses the values defined in the props. Using props, it becomes easy to write reusable code.\\\",\\r\\n            \\\"In the programming world we call it \\u201cImmutable\\u201d or in simple english \\u201cUnchangeable\\u201d.\\\",\\r\\n            \\\"Props are Unchangeable \\u2014 Immutable!\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 5,\\r\\n        \\\"title\\\": \\\"Using props in components\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"In most system components, we need to use props because these components will look differently for different properties.\\\",\\r\\n            \\\"For example, to add one image in a react-native application, the following \\u2018Image\\u2019 component is required:\\\",\\r\\n            \\\"<Image source={url} style={{width: 100, height: 100}}/>\\\",\\r\\n            \\\"Here, \\u2018source\\u2019 is the props. We can pass different urls and it will show different images.\\\",\\r\\n            \\\"Note that we are using the same component \\u2018Image\\u2019 but the props \\u2018url\\u2019 is different.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 5.1,\\r\\n        \\\"title\\\": \\\"Quick Test\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"In Props, a parent component passes prop to its child components.\\\",\\r\\n            \\\"`True` | `False` \\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 6,\\r\\n        \\\"title\\\": \\\"What is a State?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"State works differently when compared to props. State is internal to a component, while props are passed to a component.\\\",\\r\\n            \\\"State can Change \\u2014 Mutable.\\\",\\r\\n            \\\"In english the \\u2018state of a being\\u2019 refers to the physical condition of a person, and it is a mere state, which changes over time.\\\",\\r\\n            \\\"Well, a similar state in React/React Native is used within components to keep track of information.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 7,\\r\\n        \\\"title\\\": \\\"So when can state be used?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Anytime there is data that is going to change within a component, state can be used.\\\",\\r\\n            \\\"User interaction with components are good examples of how state works.\\\",\\r\\n            \\\"Clicking buttons, checkboxes, filling forms, etc. are examples of user interaction where state can be used within the component.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 8,\\r\\n        \\\"title\\\": \\\"Fill in the blank\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"export default class App extends\\\",\\r\\n            \\\"\\u2018React.Component\\u2019\\\",\\r\\n            \\\"`Render()` | `View.Component` | `Class.Component`\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 9,\\r\\n        \\\"title\\\": \\\"Which function returns a React element?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"`render`\\\",\\r\\n            \\\"`render` | `return` | `style` | `create`\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 10,\\r\\n        \\\"title\\\": \\\"Choose the correct one\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"The -- in React Native are defined as functions or classes.\\\",\\r\\n            \\\"`Components`\\\",\\r\\n            \\\"`Components` | `Interface` | `Props` | `State`\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 11,\\r\\n        \\\"title\\\": \\\"Question\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"React Native is used within components to keep track of information.\\\",\\r\\n            \\\"`True`\\\",\\r\\n            \\\"`True` | `False`\\\"\\r\\n        ]\\r\\n    }\\r\\n]\\r\\n\"', NULL, NULL, NULL, 'components-in-react-native-upnonh8h', 30, 139, '2024-02-20 11:37:09', '2024-02-20 11:37:09', 0, 1, 'default.webp'),
(377, 'Let’s Revise', '\" [\\r\\n    {\\r\\n        \\\"id\\\": 8,\\r\\n        \\\"title\\\": \\\"Fill in the blank\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"export default class App extends\\\",\\r\\n            \\\"\\u2018React.Component\\u2019\\\",\\r\\n            \\\"`React.Component` | `Render()` | `View.Component` | `Class.Component`\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 9,\\r\\n        \\\"title\\\": \\\"Which function returns a React element?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"`render`\\\",\\r\\n            \\\"`render` | `return` | `style` | `create`\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 10,\\r\\n        \\\"title\\\": \\\"Choose the correct one\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"The -- in React Native are defined as functions or classes.\\\",\\r\\n            \\\"`Components`\\\",\\r\\n            \\\"`Components` | `Interface` | `Props` | `State`\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 11,\\r\\n        \\\"title\\\": \\\"Question\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"React Native is used within components to keep track of information.\\\",\\r\\n            \\\"`True`\\\",\\r\\n            \\\"`True` | `False`\\\"\\r\\n        ]\\r\\n    }\\r\\n    \\r\\n]\"', NULL, NULL, NULL, 'let-s-revise-17kmg5zl', 30, 139, '2024-02-20 11:37:18', '2024-02-20 11:37:18', 0, 1, 'default.webp'),
(378, 'Styling the Components', '\"[\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"title\\\": \\\"Introduction\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Hey you! The interactive person.\\\",\\r\\n            \\\"We are here to design!\\\",\\r\\n            \\\"So, let\\u2019s make it simple, but significant.\\\"\\r\\n        ]\\r\\n    },\\r\\n    \\r\\n    {\\r\\n        \\\"id\\\": 2,\\r\\n        \\\"title\\\": \\\"Styling an application is important\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Whether you are a web developer or mobile app developer, you know that without the proper styling of your application, the UI would probably suck.\\\",\\r\\n            \\\"To create a new style object you use StyleSheet.create() method and encapsulate them.\\\",\\r\\n            \\\"Let\\u2019s check it out!\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 3,\\r\\n        \\\"title\\\": \\\"What are Styled Components?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Styled Components is a CSS-in-JS library that enables developers to write each component with their own styles and allows the code to be in a single location.\\\",\\r\\n            \\\"By coupling your styles with the components, it results in optimizing developer experience and output.\\\",\\r\\n            \\\"React Native tends to follow a certain convention when it comes to styling your app.\\\",\\r\\n            \\\"Such as all CSS property names should be in camelCase such as for background-color in React Native is:\\\",\\r\\n            \\\" backgroundColor: \'blue\'\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 4,\\r\\n        \\\"title\\\": \\\"Fill in the blank\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"It is better to use ---  to define several styles in one place...?\\\",\\r\\n            \\\"`StyleSheet.create`\\\",\\r\\n            \\\"`Stylesheet.insert` | `create.stylesheet` | `StyleSheet.create` | `Styled.create`\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 5,\\r\\n        \\\"title\\\": \\\"Using Styled Components\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Let\\u2019s open up the App.js file and make some modifications.\\\",\\r\\n            \\\" import React from \'react\';\\\",\\r\\n            \\\"import { StyleSheet, Text, View } from \'react-native\';\\\",\\r\\n            \\\"export default class App extends React.Component { render() { return ( <View style={styles.container}> \\\",\\r\\n            \\\"<Text>Open up App.js to start working on your app!</Text> </View> ); } }\\\", \\r\\n            \\\"const styles = StyleSheet.create({ container: { flex: 1, backgroundColor: \'#fff\', alignItems: \'center\', justifyContent: \'center\' } });\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 5,\\r\\n        \\\"title\\\": \\\"The latest version of styled-components library\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Let\\u2019s make some changes to it and use our latest library.\\\",\\r\\n            \\\"To get started, import the library like below.\\\",\\r\\n            \\\" import styled from \'styled-components\';\\\",\\r\\n            \\\"Make changes to the component\\u2019s render function like below.\\\",\\r\\n            \\\"Replace both View and Text with Container and Title.\\\",\\r\\n            \\\"These new elements are going to be custom using semantics from styled-components.\\\",\\r\\n            \\\"export default class App extends React.Component { render() { return ( <Container> <Title>React Native with \\ud83d\\udc85 Styled Components</Title> </Container> ); } }\\\"\\r\\n        ]\\r\\n    },\\r\\n\\r\\n    {\\r\\n        \\\"id\\\": 4,\\r\\n        \\\"title\\\": \\\"Container and Title\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"When creating a component in React Native using styled-components, each component is going to have styles attached to it.\\\",\\r\\n            \\\" `const Container = styled.View`{flex: 1; background-color: papayawhip; justify-content: center; align-items: center};\\\",\\r\\n            \\\" const Title = styled.Text`{font-size: 20px; font-weight: 500; tcolor: palevioletred};\\\",\\r\\n            \\\"You can notice here, the Container is a React Native View and has styling attached to it.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 4,\\r\\n        \\\"title\\\": \\\"Completed\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Here is the complete code for App.js file after changes.\\\",\\r\\n            \\\" import React from \'react\'; import styled from \'styled-components\'; export default class App extends React.Component { render() { return ( <Container> <Title>React Native with \\ud83d\\udc85 Styled Components</Title> </Container> ); } }\\\",\\r\\n            \\\" `const Container = styled.View {flex: 1; tbackground-color: papayawhip; justify-content: center; align-items: center}`\\\",\\r\\n            \\\" `const Title = styled.Text{font-size: 24px; font-weight: 500; tcolor: palevioletred};\\\"\\r\\n         ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 4,\\r\\n        \\\"title\\\": \\\"Is there any change?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"In the previous snippet, do take a note that we are not importing React Native core components such as View, Text, or the StyleSheet object.\\\",\\r\\n            \\\"It is that simple.\\\", \\r\\n            \\\"It uses the same flexbox model that works the same way in React Native as it does in CSS on the web.\\\",\\r\\n            \\\"The advantage here is that you get the advantage of using the same understandable syntax that you have been using in web development and standard CSS.\\\"\\r\\n        ]\\r\\n    }\\r\\n]\\r\\n\"', NULL, NULL, NULL, 'styling-the-components-m64ehzpb', 30, 140, '2024-02-20 11:37:49', '2024-02-20 11:37:49', 0, 1, 'default.webp'),
(379, 'Flexbox Layout in React Native', '\" \"', NULL, NULL, NULL, 'flexbox-layout-in-react-native-uszu3gjs', 30, 140, '2024-02-20 11:38:31', '2024-02-20 11:38:31', 0, 1, 'default.png'),
(380, 'Let’s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-by78am4a', 30, 140, '2024-02-20 11:38:40', '2024-02-20 11:38:40', 0, 1, 'default.png'),
(381, 'Working of an Image', '\" \"', NULL, NULL, NULL, 'working-of-an-image-ojowet91', 30, 141, '2024-02-20 11:38:55', '2024-02-20 11:38:55', 0, 1, 'default.png'),
(382, 'Rendering Images with Captions', '\" \"', NULL, NULL, NULL, 'rendering-images-with-captions-jvprv68u', 30, 141, '2024-02-20 11:39:05', '2024-02-20 11:39:05', 0, 1, 'default.png'),
(383, 'Recap', '\" \"', NULL, NULL, NULL, 'recap-17n4dbye', 30, 141, '2024-02-20 11:39:25', '2024-02-20 11:39:25', 0, 1, 'default.png'),
(384, 'ScrollView in React Native', '\" \"', NULL, NULL, NULL, 'scrollview-in-react-native-eaoxodc4', 30, 142, '2024-02-20 11:39:42', '2024-02-20 11:39:42', 0, 1, 'default.png'),
(385, 'Working with the ListView', '\" \"', NULL, NULL, NULL, 'working-with-the-listview-nqesk6vk', 30, 142, '2024-02-20 11:39:56', '2024-02-20 11:39:56', 0, 1, 'default.png'),
(386, 'Let’s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-jtxdhpqh', 30, 142, '2024-02-20 11:40:05', '2024-02-20 11:40:05', 0, 1, 'default.png'),
(387, 'Adding Buttons in React Native', '\" \"', NULL, NULL, NULL, 'adding-buttons-in-react-native-cztubysu', 30, 143, '2024-02-20 11:41:09', '2024-02-20 11:41:09', 0, 1, 'default.png'),
(388, 'Animation in React Native', '\" \"', NULL, NULL, NULL, 'animation-in-react-native-55jze2jc', 30, 143, '2024-02-20 11:41:19', '2024-02-20 11:41:19', 0, 1, 'default.png'),
(389, 'Let’s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-04e0xp52', 30, 143, '2024-02-20 11:41:27', '2024-02-20 11:41:27', 0, 1, 'default.png'),
(390, 'How Navigation works?', '\" \"', NULL, NULL, NULL, 'how-navigation-works-zujuijdk', 30, 144, '2024-02-20 11:42:18', '2024-02-20 11:42:18', 0, 1, 'default.png'),
(391, 'Getting familiar with Router', '\" \"', NULL, NULL, NULL, 'getting-familiar-with-router-iew8df9s', 30, 144, '2024-02-20 11:42:29', '2024-02-20 11:42:29', 0, 1, 'default.png'),
(392, 'Let’s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-vxopghkq', 30, 144, '2024-02-20 11:42:40', '2024-02-20 11:42:40', 0, 1, 'default.png'),
(393, 'Introduction', '\" \"', NULL, NULL, NULL, 'introduction-pfegtdnj', 31, 145, '2024-02-20 12:58:16', '2024-02-20 12:58:16', 0, 1, 'default.png'),
(394, 'Features, Advantages & Disadvantages', '\" \"', NULL, NULL, NULL, 'features--advantages---disadva-bavwdoml', 31, 145, '2024-02-20 12:58:30', '2024-02-20 12:58:30', 0, 1, 'default.png'),
(395, 'Let\'s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-tjjcybgi', 31, 145, '2024-02-20 12:58:46', '2024-02-20 12:58:46', 0, 1, 'default.png'),
(396, 'Let\'s create', '\" \"', NULL, NULL, NULL, 'let-s-create-qp50ndta', 31, 146, '2024-02-20 12:59:13', '2024-02-20 12:59:13', 0, 1, 'default.png'),
(397, 'Structure of the Application', '\" \"', NULL, NULL, NULL, 'structure-of-the-application-5exuy079', 31, 146, '2024-02-20 12:59:26', '2024-02-20 12:59:26', 0, 1, 'default.png'),
(398, 'Analysing the Code', '\" \"', NULL, NULL, NULL, 'analysing-the-code-vnkbwul1', 31, 146, '2024-02-20 12:59:37', '2024-02-20 12:59:37', 0, 1, 'default.png'),
(399, 'Let\'s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-ktp7jrye', 31, 146, '2024-02-20 12:59:46', '2024-02-20 12:59:46', 0, 1, 'default.png'),
(400, 'Introduction to Flutter Architecture', '\" \"', NULL, NULL, NULL, 'introduction-to-flutter-archit-qhamtwd2', 31, 147, '2024-02-20 13:00:08', '2024-02-20 13:00:08', 0, 1, 'default.png'),
(401, 'Behind the Screen', '\" \"', NULL, NULL, NULL, 'behind-the-screen-34cawova', 31, 147, '2024-02-20 13:00:23', '2024-02-20 13:00:23', 0, 1, 'default.png'),
(403, 'Let\'s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-sby7uxjq', 31, 147, '2024-02-20 13:00:56', '2024-02-20 13:00:56', 0, 1, 'default.png'),
(404, 'Introduction to Widgets', '\" \"', NULL, NULL, NULL, 'introduction-to-widgets-pvkgvn9i', 31, 148, '2024-02-20 13:04:10', '2024-02-20 13:04:10', 0, 1, 'default.png'),
(405, 'What are visible widgets?', '\" \"', NULL, NULL, NULL, 'what-are-visible-widgets-xvvkqc6h', 31, 148, '2024-02-20 13:04:27', '2024-02-20 13:04:27', 0, 1, 'default.png'),
(406, 'What are invisible Widgets?', '\" \"', NULL, NULL, NULL, 'what-are-invisible-widgets-ofkcmqjv', 31, 148, '2024-02-20 13:04:41', '2024-02-20 13:04:41', 0, 1, 'default.png'),
(407, 'Let\'s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-sfbllclr', 31, 148, '2024-02-20 13:04:53', '2024-02-20 13:04:53', 0, 1, 'default.png'),
(408, 'What are Layouts? ', '\" \"', NULL, NULL, NULL, 'what-are-layouts-6wgvf4xu', 31, 149, '2024-02-20 13:05:37', '2024-02-20 13:05:37', 0, 1, 'default.png'),
(409, ' What are Gestures?', '\" \"', NULL, NULL, NULL, 'what-are-gestures-aj776ohr', 31, 149, '2024-02-20 13:05:46', '2024-02-20 13:05:46', 0, 1, 'default.png'),
(410, ' Let\'s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-mbi9djfh', 31, 149, '2024-02-20 13:05:50', '2024-02-20 13:05:50', 0, 1, 'default.png'),
(411, 'Alert Dialog Widget .', '\" \"', NULL, NULL, NULL, 'alert-dialog-widget-avxxxtza', 31, 150, '2024-02-20 13:09:38', '2024-02-20 13:09:38', 0, 1, 'default.png'),
(412, 'How to add images?', '\" \"', NULL, NULL, NULL, 'how-to-add-images-ztxw0z8i', 31, 150, '2024-02-20 13:09:47', '2024-02-20 13:09:47', 0, 1, 'default.png'),
(413, 'Let\'s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-wqi7upxk', 31, 150, '2024-02-20 13:09:50', '2024-02-20 13:09:50', 0, 1, 'default.png'),
(414, 'Navigation through tabs: Tabbars', '\" \"', NULL, NULL, NULL, 'navigation-through-tabs-aapuyxkp', 31, 151, '2024-02-20 13:10:16', '2024-02-20 13:10:16', 0, 1, 'default.png'),
(415, 'Navigation through drawers: Drawers', '\" \"', NULL, NULL, NULL, 'tabbars--navigation-through-dr-jfz8vj9l', 31, 151, '2024-02-20 13:10:30', '2024-02-20 13:10:30', 0, 1, 'default.png'),
(416, 'Let\'s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-emgcwego', 31, 151, '2024-02-20 13:11:56', '2024-02-20 13:11:56', 0, 1, 'default.png'),
(417, 'Concept of State', '\" \"', NULL, NULL, NULL, 'concept-of-state-8sqyezms', 31, 152, '2024-02-20 13:12:13', '2024-02-20 13:12:13', 0, 1, 'default.png'),
(418, 'State Management in Flutter', '\" \"', NULL, NULL, NULL, 'state-management-in-flutter-uwc0wemy', 31, 152, '2024-02-20 13:12:26', '2024-02-20 13:12:26', 0, 1, 'default.png'),
(419, 'Let\'s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-yy3yuj0w', 31, 152, '2024-02-20 13:13:41', '2024-02-20 13:13:41', 0, 1, 'default.png'),
(420, 'Animation: The key to Good UI/UX', '\" \"', NULL, NULL, NULL, 'animation--the-key-to-good-ui-twqpvval', 31, 153, '2024-02-20 13:14:11', '2024-02-20 13:14:11', 0, 1, 'default.png');
INSERT INTO `topic` (`id`, `title`, `desc`, `video`, `material`, `duration`, `slug`, `course_id`, `lesson_id`, `created`, `updated`, `deleted`, `active`, `image`) VALUES
(421, 'Three pillars of Animation', '\" \"', NULL, NULL, NULL, 'three-pillars-of-animation-neqsjdal', 31, 153, '2024-02-20 13:14:21', '2024-02-20 13:14:21', 0, 1, 'default.png'),
(422, 'Let\'s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-c4z03vvq', 31, 153, '2024-02-20 13:14:32', '2024-02-20 13:14:32', 0, 1, 'default.png'),
(423, 'Conclusion', '\" \"', NULL, NULL, NULL, 'conclusion-efqk5tfy', 31, 154, '2024-02-20 13:15:55', '2024-02-20 13:15:55', 0, 1, 'default.png'),
(424, 'Today’s digital world', '\" \"', NULL, NULL, NULL, 'today-s-digital-world-shm3czjk', 41, 155, '2024-02-20 16:09:55', '2024-02-20 16:09:55', 0, 1, 'default.png'),
(425, 'The CIA triad', '\" \"', NULL, NULL, NULL, 'the-cia-triad-4njii2oq', 41, 155, '2024-02-20 16:10:04', '2024-02-20 16:10:04', 0, 1, 'default.png'),
(426, 'Let\'s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-vckvwf2j', 41, 155, '2024-02-20 16:10:13', '2024-02-20 16:10:13', 0, 1, 'default.png'),
(427, 'Physical Security & malware .', '\" \"', NULL, NULL, NULL, 'physical-security---malware-r8ggrlks', 41, 156, '2024-02-20 16:10:45', '2024-02-20 16:10:45', 0, 1, 'default.png'),
(428, 'Breaches & Common Cyber Attacks.', '\" \"', NULL, NULL, NULL, 'breaches---common-cyber-attack-gczgb7u0', 41, 156, '2024-02-20 16:10:59', '2024-02-20 16:10:59', 0, 1, 'default.png'),
(429, 'Let\'s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-5rnv82yg', 41, 156, '2024-02-20 16:11:03', '2024-02-20 16:11:03', 0, 1, 'default.png'),
(430, 'Impacts of Cyber Crimes.', '\" \"', NULL, NULL, NULL, 'impacts-of-cyber-crimes-exrd6tkx', 41, 157, '2024-02-20 16:13:33', '2024-02-20 16:13:33', 0, 1, 'default.png'),
(431, ' IT Acts & Cyber Laws .', '\" \"', NULL, NULL, NULL, 'it-acts---cyber-laws-o9t5uogj', 41, 157, '2024-02-20 16:13:53', '2024-02-20 16:13:53', 0, 1, 'default.png'),
(432, 'Let\'s Revise.', '\" \"', NULL, NULL, NULL, 'let-s-revise-ckbfxemr', 41, 157, '2024-02-20 16:14:03', '2024-02-20 16:14:03', 0, 1, 'default.png'),
(433, 'Why Cyber Security?', '\" \"', NULL, NULL, NULL, 'why-cyber-security-fgmlao9n', 41, 158, '2024-02-20 16:14:53', '2024-02-20 16:14:53', 0, 1, 'default.png'),
(434, 'What needs to be secured?', '\" \"', NULL, NULL, NULL, 'what-needs-to-be-secured-ujv8sxhf', 41, 158, '2024-02-20 16:15:19', '2024-02-20 16:15:19', 0, 1, 'default.png'),
(435, 'Terms related to Cyber Security', '\" \"', NULL, NULL, NULL, 'terms-related-to-cyber-securit-aq8uwtxe', 41, 158, '2024-02-20 16:15:30', '2024-02-20 16:15:30', 0, 1, 'default.png'),
(436, 'Let\'s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-opwss76z', 41, 158, '2024-02-20 16:15:54', '2024-02-20 16:15:54', 0, 1, 'default.png'),
(437, 'Network Security', '\" \"', NULL, NULL, NULL, 'network-security-odwkatky', 41, 159, '2024-02-20 16:16:26', '2024-02-20 16:16:26', 0, 1, 'default.png'),
(438, 'Operating System Security', '\" \"', NULL, NULL, NULL, 'operating-system-security-b5lc1hyg', 41, 159, '2024-02-20 16:16:39', '2024-02-20 16:16:39', 0, 1, 'default.png'),
(439, 'Let\'s Revise.', '\" \"', NULL, NULL, NULL, 'let-s-revise-p0godvuh', 41, 159, '2024-02-20 16:16:51', '2024-02-20 16:16:51', 0, 1, 'default.png'),
(440, 'Basics of Digital Forensics', '\" \"', NULL, NULL, NULL, 'basics-of-digital-forensics-iwhyd45h', 41, 160, '2024-02-20 16:17:10', '2024-02-20 16:17:10', 0, 1, 'default.png'),
(441, 'Stages of Forensic', '\" \"', NULL, NULL, NULL, 'stages-of-forensic-5yqtnjp4', 41, 160, '2024-02-20 16:17:32', '2024-02-20 16:17:32', 0, 1, 'default.png'),
(442, 'Let\'s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-mjbz0eum', 41, 160, '2024-02-20 16:17:41', '2024-02-20 16:17:41', 0, 1, 'default.png'),
(443, 'Myth bursting', '\" \"', NULL, NULL, NULL, 'myth-bursting-rktcbwb2', 41, 161, '2024-02-20 16:18:03', '2024-02-20 16:18:03', 0, 1, 'default.png'),
(444, 'Conclusion', '\" \"', NULL, NULL, NULL, 'conclusion-gk6aa6op', 41, 161, '2024-02-20 16:18:13', '2024-02-20 16:18:13', 0, 1, 'default.png'),
(445, 'Let\'s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-gpkt2tyd', 41, 161, '2024-02-20 16:18:22', '2024-02-20 16:18:22', 0, 1, 'default.png'),
(446, 'Quiz', '\" \"', NULL, NULL, NULL, 'quiz-uemgqnvg', 41, 162, '2024-02-20 16:18:46', '2024-02-20 16:18:46', 0, 1, 'default.png'),
(447, 'What is scope?', '\" \"', NULL, NULL, NULL, 'what-is-scope-kgbc3gks', 59, 163, '2024-02-20 17:26:30', '2024-02-20 17:26:30', 0, 1, 'default.png'),
(448, 'Local scope', '\" \"', NULL, NULL, NULL, 'local-scope-ahqrd0pk', 59, 163, '2024-02-20 17:26:40', '2024-02-20 17:26:40', 0, 1, 'default.png'),
(449, 'Global scope', '\" \"', NULL, NULL, NULL, 'global-scope-ffm0bsxq', 59, 163, '2024-02-20 17:26:49', '2024-02-20 17:26:49', 0, 1, 'default.png'),
(450, 'Hoisting', '\" \"', NULL, NULL, NULL, 'hoisting-rrzfdzub', 59, 163, '2024-02-20 17:26:58', '2024-02-20 17:26:58', 0, 1, 'default.png'),
(451, 'Let’s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-zbsuu1pw', 59, 163, '2024-02-20 17:27:07', '2024-02-20 17:27:07', 0, 1, 'default.png'),
(452, 'What is a string? ', '\" \"', NULL, NULL, NULL, 'what-is-a-string-bkxqjh7o', 59, 164, '2024-02-20 17:27:29', '2024-02-20 17:27:29', 0, 1, 'default.png'),
(453, 'Operations on strings .', '\" \"', NULL, NULL, NULL, 'operations-on-strings-arppwcp4', 59, 164, '2024-02-20 17:27:38', '2024-02-20 17:27:38', 0, 1, 'default.png'),
(454, 'Let’s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-arokevou', 59, 164, '2024-02-20 17:27:41', '2024-02-20 17:27:41', 0, 1, 'default.png'),
(455, 'What are Numbers?', '\" \"', NULL, NULL, NULL, 'what-are-numbers-z1s5vs64', 59, 165, '2024-02-20 17:28:08', '2024-02-20 17:28:08', 0, 1, 'default.png'),
(456, 'Operations on numbers', '\" \"', NULL, NULL, NULL, 'operations-on-numbers-y80zzieu', 59, 165, '2024-02-20 17:28:26', '2024-02-20 17:28:26', 0, 1, 'default.png'),
(457, 'What is a boolean?', '\" \"', NULL, NULL, NULL, 'what-is-a-boolean-eyyrdfuk', 59, 165, '2024-02-20 17:28:39', '2024-02-20 17:28:39', 0, 1, 'default.png'),
(458, 'Let’s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-mklln9ie', 59, 165, '2024-02-20 17:28:50', '2024-02-20 17:28:50', 0, 1, 'default.png'),
(459, 'What are objects?', '\" \"', NULL, NULL, NULL, 'what-are-objects-a3cimqi0', 59, 166, '2024-02-20 17:29:13', '2024-02-20 17:29:13', 0, 1, 'default.png'),
(460, 'Defining an object', '\" \"', NULL, NULL, NULL, 'defining-an-object-tge47i7l', 59, 166, '2024-02-20 17:30:26', '2024-02-20 17:30:26', 0, 1, 'default.png'),
(461, 'Accessing object properties', '\" \"', NULL, NULL, NULL, 'accessing-object-properties-mpsfft2y', 59, 166, '2024-02-20 17:30:37', '2024-02-20 17:30:37', 0, 1, 'default.png'),
(462, 'Let’s Revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-dhidel7w', 59, 166, '2024-02-20 17:30:46', '2024-02-20 17:30:46', 0, 1, 'default.png'),
(463, 'The date object.', '\" \"', NULL, NULL, NULL, 'the-date-object-owi9tqpw', 59, 167, '2024-02-20 17:31:11', '2024-02-20 17:31:11', 0, 1, 'default.png'),
(464, 'Operations on date.', '\" \"', NULL, NULL, NULL, 'operations-on-date-acld8zhi', 59, 167, '2024-02-20 17:31:21', '2024-02-20 17:31:21', 0, 1, 'default.png'),
(465, 'Let’s Revise.', '\" \"', NULL, NULL, NULL, 'let-s-revise-52iefd2o', 59, 167, '2024-02-20 17:31:27', '2024-02-20 17:31:27', 0, 1, 'default.png'),
(466, 'What is a DOM? ', '\" \"', NULL, NULL, NULL, 'what-is-a-dom-nookrh9d', 59, 168, '2024-02-20 17:31:50', '2024-02-20 17:31:50', 0, 1, 'default.png'),
(467, 'Accessing Elements in DOM.', '\" \"', NULL, NULL, NULL, 'accessing-elements-in-dom-sxvbwcbo', 59, 168, '2024-02-20 17:32:00', '2024-02-20 17:32:00', 0, 1, 'default.png'),
(468, 'Let’s Revise.', '\" \"', NULL, NULL, NULL, 'let-s-revise-6uljicks', 59, 168, '2024-02-20 17:32:15', '2024-02-20 17:32:15', 0, 1, 'default.png'),
(469, 'Introduction.', '\" \"', NULL, NULL, NULL, 'introduction-j5ybgrqf', 59, 169, '2024-02-20 17:33:08', '2024-02-20 17:33:08', 0, 1, 'default.png'),
(470, 'Accessing HTML elements.', '\" \"', NULL, NULL, NULL, 'accessing-html-elements-zzc8vd4y', 59, 169, '2024-02-20 17:33:17', '2024-02-20 17:33:17', 0, 1, 'default.png'),
(471, 'Let’s Revise.', '\" \"', NULL, NULL, NULL, 'let-s-revise-adh1jynp', 59, 169, '2024-02-20 17:33:23', '2024-02-20 17:33:23', 0, 1, 'default.png'),
(472, 'Introduction.', '\" \"', NULL, NULL, NULL, 'introduction-rebupixi', 59, 170, '2024-02-20 17:33:45', '2024-02-20 17:33:45', 0, 1, 'default.png'),
(473, 'Manipulating HTML elements.', '\" \"', NULL, NULL, NULL, 'manipulating-html-elements-l7da7rim', 59, 170, '2024-02-20 17:33:57', '2024-02-20 17:33:57', 0, 1, 'default.png'),
(474, 'Let’s Revise.', '\" \"', NULL, NULL, NULL, 'let-s-revise-b043rscy', 59, 170, '2024-02-20 17:34:03', '2024-02-20 17:34:03', 0, 1, 'default.png'),
(475, 'Introduction.', '\" \"', NULL, NULL, NULL, 'introduction-a5qaue7u', 59, 171, '2024-02-20 17:35:53', '2024-02-20 17:35:53', 0, 1, 'default.png'),
(476, 'Manipulating CSS.', '\" \"', NULL, NULL, NULL, 'manipulating-css-bo6vgleb', 59, 171, '2024-02-20 17:36:05', '2024-02-20 17:36:05', 0, 1, 'default.png'),
(477, 'Let’s Revise.', '\" \"', NULL, NULL, NULL, 'let-s-revise-xk6d28ac', 59, 171, '2024-02-20 17:36:11', '2024-02-20 17:36:11', 0, 1, 'default.png'),
(478, 'What are Events?', '\" \"', NULL, NULL, NULL, 'what-are-events-xucpaadp', 59, 172, '2024-02-20 17:37:46', '2024-02-20 17:37:46', 0, 1, 'default.png'),
(479, ' Types of Events.', '\" \"', NULL, NULL, NULL, 'types-of-events-q2roglie', 59, 172, '2024-02-20 17:38:04', '2024-02-20 17:38:04', 0, 1, 'default.png'),
(480, ' Attaching events to HTML elements.', '\" \"', NULL, NULL, NULL, 'attaching-events-to-html-elem-ght7eewk', 59, 172, '2024-02-20 17:38:22', '2024-02-20 17:38:22', 0, 1, 'default.png'),
(481, 'Removing events from HTML elements.', '\" \"', NULL, NULL, NULL, 'removing-events-from-html-elem-5bvdrr7x', 59, 172, '2024-02-20 17:38:34', '2024-02-20 17:38:34', 0, 1, 'default.png'),
(482, 'Let’s Revise.', '\" \"', NULL, NULL, NULL, 'let-s-revise-1pzylhyv', 59, 172, '2024-02-20 17:38:39', '2024-02-20 17:38:39', 0, 1, 'default.png'),
(483, 'What is BOM?', '\" \"', NULL, NULL, NULL, 'what-is-bom-zqnqvudc', 59, 173, '2024-02-20 17:39:58', '2024-02-20 17:39:58', 0, 1, 'default.png'),
(484, ' Exploring the window object.', '\" \"', NULL, NULL, NULL, 'exploring-the-window-object-ecar7hcp', 59, 173, '2024-02-20 17:40:08', '2024-02-20 17:40:08', 0, 1, 'default.png'),
(485, 'Let’s Revise.', '\" \"', NULL, NULL, NULL, 'let-s-revise-lvag1gll', 59, 173, '2024-02-20 17:40:13', '2024-02-20 17:40:13', 0, 1, 'default.png'),
(486, 'What are cookies?', '\" \"', NULL, NULL, NULL, 'what-are-cookies-cwblwbbp', 59, 174, '2024-02-20 17:40:57', '2024-02-20 17:40:57', 0, 1, 'default.png'),
(487, 'Playing with cookies.', '\" \"', NULL, NULL, NULL, 'playing-with-cookies-dfpomhzz', 59, 174, '2024-02-20 17:41:09', '2024-02-20 17:41:09', 0, 1, 'default.png'),
(488, 'Let’s Revise.', '\" \"', NULL, NULL, NULL, 'let-s-revise-qotmbgdo', 59, 174, '2024-02-20 17:41:14', '2024-02-20 17:41:14', 0, 1, 'default.png'),
(489, 'What is es6?', '\" \"', NULL, NULL, NULL, 'what-is-es6-mewqpixq', 59, 175, '2024-02-20 17:41:40', '2024-02-20 17:41:40', 0, 1, 'default.png'),
(490, 'Exploring new features of es6.', '\" \"', NULL, NULL, NULL, 'exploring-new-features-of-es6-uu21uzas', 59, 175, '2024-02-20 17:41:51', '2024-02-20 17:41:51', 0, 1, 'default.png'),
(491, 'Let’s Revise.', '\" \"', NULL, NULL, NULL, 'let-s-revise-voqvfhka', 59, 175, '2024-02-20 17:41:57', '2024-02-20 17:41:57', 0, 1, 'default.png'),
(492, 'What is a Class?', '\" \"', NULL, NULL, NULL, 'what-is-a-class-tf1wttmv', 59, 176, '2024-02-20 17:42:19', '2024-02-20 17:42:19', 0, 1, 'default.png'),
(493, ' Writing a Class.', '\" \"', NULL, NULL, NULL, 'writing-a-class-vwkjqn1a', 59, 176, '2024-02-20 17:42:28', '2024-02-20 17:42:28', 0, 1, 'default.png'),
(494, ' Accessing members of the class.', '\" \"', NULL, NULL, NULL, 'accessing-members-of-the-clas-b5whzzvj', 59, 176, '2024-02-20 17:42:41', '2024-02-20 17:42:41', 0, 1, 'default.png'),
(495, ' Let’s Revise.', '\" \"', NULL, NULL, NULL, 'let-s-revise-ui8cwugn', 59, 176, '2024-02-20 17:42:46', '2024-02-20 17:42:46', 0, 1, 'default.png'),
(496, 'Over to you Kevin', '\"[\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"title\\\": \\\"Welcome Back\\\",\\r\\n        \\\"image\\\": \\\"a_hacking.png\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Hey, Welcome back!\\\",\\r\\n            \\\"You remember me right?\\\",\\r\\n            \\\"Ok, let me refresh your memory, I am Kuro Kage.\\\",\\r\\n            \\\"If you don\\u2019t know me, that means we haven\'t met.\\\",\\r\\n            \\\"So before moving ahead, I would highly recommend you going through the basics course first!\\\",\\r\\n            \\\"If you already have, then let\\u2019s not wait and move ahead.\\\",\\r\\n            \\\"Oh no! But sadly, we have to move apart.\\\",\\r\\n            \\\"My Job was to introduce you to the hacking world.\\\",\\r\\n            \\\"From hereon, My hacker mate - Kevin will take over.\\\",\\r\\n            \\\"Want to know who he is? Click here\\\",\\r\\n            \\\"He is one of the greatest hackers of all the time.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 2,\\r\\n        \\\"title\\\": \\\"Hello Script rookie\\\",\\r\\n        \\\"image\\\": \\\"a_hacking.png\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Hey Script rookie!\\\",\\r\\n            \\\"Welcome to the journey that will transform you from a Script rookie to a White Hat Hacker.\\\",\\r\\n            \\\"I am Kevin - An American Hacker.\\\",\\r\\n            \\\"Thus, without any further delays, let\\u2019s start.\\\",\\r\\n            \\\"And remember, \\u201cHacking is more of defending and securing!\\u201d\\\"\\r\\n        ]\\r\\n    }\\r\\n]\"', NULL, NULL, NULL, 'over-to-you-kevin-gdsiysvy', 34, 177, '2024-03-11 15:02:24', '2024-03-11 15:02:24', 0, 1, 'default.webp'),
(497, 'A quick revision', '\"  [\\r\\n    {\\r\\n        \\\"id\\\": 3,\\r\\n        \\\"title\\\": \\\"Revision\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Welcome,\\\",\\r\\n            \\\"Before we move to the advanced topics, Let\'s see what you learned earlier\\\"\\r\\n        ],\\r\\n        \\\"image\\\": \\\"a_hacking.png\\\"\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 4,\\r\\n        \\\"title\\\": \\\"Who is a Hacker?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"A computer hacker is a skilled expert who overcomes a problem using their technical knowledge.\\\"\\r\\n        ],\\r\\n        \\\"image\\\": \\\"a_hacking.png\\\"\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 5,\\r\\n        \\\"title\\\": \\\"Motivations\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Can you recollect?\\\",\\r\\n            \\\"A hacker\'s motivation can be divided into the following 3 categories:\\\",\\r\\n            \\\"Political\\\",\\r\\n            \\\"Economical\\\",\\r\\n            \\\"Personal\\\"\\r\\n        ],\\r\\n        \\\"image\\\": \\\"a_hacking.png\\\"\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 6,\\r\\n        \\\"title\\\": \\\"What can be a hacker\'s motivation?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"All the above\\\",\\r\\n            \\\"Political\\\",\\r\\n            \\\"Economical\\\",\\r\\n            \\\"Personal\\\",\\r\\n            \\\"All the above\\\"\\r\\n        ],\\r\\n        \\\"image\\\": \\\"a_hacking.png\\\"\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 7,\\r\\n        \\\"title\\\": \\\"Types of Hacker\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Kuro taught you this, There are broadly 3 types of hackers :\\\",\\r\\n            \\\"White Hat Hackers : These are the individuals professing hacker skills and using them for defensive purposes.\\\",\\r\\n            \\\"Black Hat Hackers : These are the individuals with extraordinary skills, resorting to malicious or destructive activities.\\\",\\r\\n            \\\"Gray Hat Hackers : These are individuals who work both offensively and defensively at various times.\\\"\\r\\n        ],\\r\\n        \\\"image\\\": \\\"a_hacking.png\\\"\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 8,\\r\\n        \\\"title\\\": \\\"Which type of Hacker do you want to be?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"White Hat\\\",\\r\\n            \\\"White hat\\\",\\r\\n            \\\"Black Hat\\\",\\r\\n            \\\"Gray Hat\\\"\\r\\n        ],\\r\\n        \\\"image\\\": \\\"a_hacking.png\\\"\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 9,\\r\\n        \\\"title\\\": \\\"Do you remember these terms?\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"As a hacker, you will come across the below terms daily,\\\",\\r\\n            \\\"Malware : \'Malware\' is short for \'malicious software\' - computer programs designed to infiltrate and damage computers without the user\'s consent.\\\",\\r\\n            \\\"Virus\\\",\\r\\n            \\\"Virus : A computer virus is a malicious software program loaded onto a user\'s computer that can be self-replicating, inserting itself onto other programs or files, infecting them in the process.\\\",\\r\\n            \\\"Worm\\\",\\r\\n            \\\"Worm : A computer worm is a standalone malware computer program that replicates itself in order to spread to other computers\\\",\\r\\n            \\\"Trojan\\\",\\r\\n            \\\"Trojan : A Trojan horse, or Trojan, is a type of malicious code or software that looks legitimate but can take control of your computer.\\\"\\r\\n        ],\\r\\n        \\\"image\\\": \\\"a_hacking.png\\\"\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 10,\\r\\n        \\\"title\\\": \\\"Quiz time\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"--- is a type of malicious code or software that looks legitimate but can take control of your computer.\\\",\\r\\n            \\\"Trojan\\\",\\r\\n            \\\"Virus\\\",\\r\\n            \\\"Worm\\\"\\r\\n        ],\\r\\n        \\\"image\\\": \\\"a_hacking.png\\\"\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 11,\\r\\n        \\\"title\\\": \\\"Remember the steps\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"The basic steps of hacking,\\\",\\r\\n            \\\"Footprinting\\\",\\r\\n            \\\"Scanning\\\",\\r\\n            \\\"Gaining access\\\",\\r\\n            \\\"Maintaining access\\\",\\r\\n            \\\"Clearing logs\\\"\\r\\n        ],\\r\\n        \\\"image\\\": \\\"a_hacking.png\\\"\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 12,\\r\\n        \\\"title\\\": \\\"Hey, I know you knew all this\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Kuro had done a Good Job.\\\",\\r\\n            \\\"Also, we have revised the fundamentals, Let\'s keep going.\\\"\\r\\n        ],\\r\\n        \\\"image\\\": \\\"a_hacking.png\\\"\\r\\n    }\\r\\n]\"', NULL, NULL, NULL, 'a-quick-revision-tpsdz7t8', 34, 177, '2024-03-11 15:02:58', '2024-03-11 15:02:58', 0, 1, 'default.webp'),
(498, 'Terminologies you should know', '\"[\\r\\n    {\\r\\n        \\\"id\\\": 1,\\r\\n        \\\"title\\\": \\\"Welcome back! Kevin here\\\",\\r\\n        \\\"image\\\": \\\"networking.png\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Let us go through some important networking terminologies in this section\\\",\\r\\n            \\\"It\'s time to take your hacking skills to another level in this course.\\\",\\r\\n            \\\"It\'s time to level up!\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 2,\\r\\n        \\\"title\\\": \\\"What is Data?\\\",\\r\\n        \\\"image\\\": \\\"data.png\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Consider iron ore:\\\",\\r\\n            \\\"It needs to be extracted from mines, transported as freight and smelted into a useful form, which can then be used to make something of value.\\\",\\r\\n            \\\"Replace iron with data.\\\",\\r\\n            \\\"Replace mines with information systems.\\\",\\r\\n            \\\"Replace transportation with data architecture and warehouses.\\\",\\r\\n            \\\"Replace smelting with data mining.\\\",\\r\\n            \\\"Thus, In simple terms, Data is a raw material that needs to be processed to achieve some meaningful insights from it.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 3,\\r\\n        \\\"title\\\": \\\"Network?\\\",\\r\\n        \\\"image\\\": \\\"network.png\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"In simple terms, A network is a collection of computers and devices connected together, often wirelessly, via communications devices and transmission media.\\\",\\r\\n            \\\"When a computer connects to a network, it is online.\\\",\\r\\n            \\\"Networks allow computers to share resources, such as hardware, software, data, and information.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 4,\\r\\n        \\\"title\\\": \\\"Internet - What is it?\\\",\\r\\n        \\\"image\\\": \\\"internet.png\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"You now know what a network is, the next question arises, What is the Internet?\\\",\\r\\n            \\\"Let us break the term Internet,\\\",\\r\\n            \\\"Internet = Interconnected + Network\\\",\\r\\n            \\\"Thus, simply the Internet is various networks connected to each other.\\\",\\r\\n            \\\"Therefore, it is a worldwide collection of networks that connects millions of businesses, government agencies, educational institutions, and individuals.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 5,\\r\\n        \\\"title\\\": \\\"Internet - What is it?\\\",\\r\\n        \\\"image\\\": \\\"internet.png\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"The Internet is various networks connected to each other.\\\",\\r\\n            \\\"True\\\",\\r\\n            \\\"True\\\",\\r\\n            \\\"False\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 6,\\r\\n        \\\"title\\\": \\\"IP Address\\\",\\r\\n        \\\"image\\\": \\\"ip_address.png\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"If a friend of you wants to talk (\'ccommunicate\') to you he/she will call you by your name.\\\",\\r\\n            \\\"In the same way when a computer wants to communicate with another computer or any other communicating device they make use of IP addresses.\\\",\\r\\n            \\\"An IP address is an identifier assigned to a device (computer, smartphone, tablet, printer, router, etc.) connected to a network (more specifically an Ethernet network).\\\",\\r\\n            \\\"Example : Your local address will be, 127.0.0.1\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 7,\\r\\n        \\\"title\\\": \\\"Port Number\\\",\\r\\n        \\\"image\\\": \\\"port_number.png\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"When some random data (packet) comes on your cell phone..\\\",\\r\\n            \\\"How do you think your cellphone knows whether that packet needs to be sent to your Facebook app, your Instagram app or your browser?\\\",\\r\\n            \\\"Every such app will have a number associated with them, those are called \'port numbers\'.\\\",\\r\\n            \\\"So when some data comes it looks at the data (packet), it\'ll contain the port number and your cell phone goes to the app and says: \'Take this, this belongs to you\'\\\",\\r\\n            \\\"Port Numbers help to identify the exact sender and receiver processes.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 8,\\r\\n        \\\"title\\\": \\\"Protocol\\\",\\r\\n        \\\"image\\\": \\\"protocol.png\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Basically, a protocol is a set of rules and procedures that allow communication between computer systems in a network environment.\\\",\\r\\n            \\\"Without the use of an agreed protocol it will be a challenge to design, integrate and implement computer / telecommunication based Networks.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"id\\\": 9,\\r\\n        \\\"title\\\": \\\"Fill in the blank\\\",\\r\\n        \\\"image\\\": \\\"fill_in_blank.png\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"--- help to identify the exact sender and receiver processes.\\\",\\r\\n            \\\"Port Numbers\\\",\\r\\n            \\\"Port Numbers\\\",\\r\\n            \\\"IP Addresses\\\"\\r\\n        ]\\r\\n    }\\r\\n]\"', NULL, NULL, NULL, 'terminologies-you-should-know-f2dwz32c', 34, 178, '2024-03-11 15:05:04', '2024-03-11 15:05:04', 0, 1, 'default.webp'),
(499, 'Understanding the OSI Model', '\" [\\r\\n    {\\r\\n        \\\"title\\\": \\\"The OSI Model\\\",\\r\\n        \\\"image\\\": \\\"osi.png\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Now you are aware of the important networking terms, Remember them till your last breath!\\\" ,\\r\\n            \\\"It\\u2019s time to move ahead and learn about the OSI model in networking that will help you in the future concepts such as VPN, Wireless Hijacking and more.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"title\\\": \\\"The OSI Model\\\",\\r\\n        \\\"image\\\": \\\"osi.png\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"It is a reference model for how applications communicate over a network.\\\",\\r\\n            \\\"The Open Systems Interconnection(OSI) Model is a seven layer architecture with each layer having specific functionality to perform.\\\",\\r\\n            \\\"All these layers work collaboratively to transmit data from one place to another.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"title\\\": \\\"The Layers\\\",\\r\\n        \\\"image\\\": \\\"osi.png\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"The seven layers of the OSI Model are :\\\",\\r\\n            \\\"`Physical Layer`\\\",\\r\\n            \\\"`Data Link Layer`\\\",\\r\\n            \\\"`Network Layer`\\\",\\r\\n            \\\"`Transport Layer`\\\",\\r\\n            \\\"`Session Layer`\\\",\\r\\n            \\\"`Presentation Layer`\\\",\\r\\n            \\\"`Application Layer`\\\",\\r\\n            \\\"Tough to remember so many layers? Don\'t\\u2019 worry just remember the following acronym,\\\",\\r\\n            \\\"Please Do Not Throw Sushi and Pizza Away. (PDNTSPA).\\\",\\r\\n            \\\"Simple right?\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"title\\\": \\\"Which of the following is not a OSI Model layer?\\\",\\r\\n        \\\"image\\\": \\\"osi.png\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"`System layer`\\\",\\r\\n            \\\"`Application layer`\\\",\\r\\n            \\\"`System layer`\\\",\\r\\n            \\\"`Physical layer`\\\",\\r\\n            \\\"`Data Link layer`\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"title\\\": \\\"Physical Layer\\\",\\r\\n        \\\"image\\\": \\\"osi.png\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"This layer contains information in the form of bits.\\\",\\r\\n            \\\"It is responsible for the movement of bits from one node to another.\\\",\\r\\n            \\\"It defines the characteristics of the interface between the devices and the transmission media.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"title\\\": \\\"Data Link Layer\\\",\\r\\n        \\\"image\\\": \\\"osi.png\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"This layer is responsible for the movement of frames from one node to the next.\\\",\\r\\n            \\\"A frame is a stream of bits. These are manageable data units.\\\",\\r\\n            \\\"This layer is also responsible for error control, flow control and access control.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"title\\\": \\\"Network and Transport Layer\\\",\\r\\n        \\\"image\\\": \\\"osi.png\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Network Layer : It ensures the source to destination delivery of each data packet. Routing occurs at the network layer. It uses the physical (MAC) address of networks.\\\",\\r\\n            \\\"Transport Layer: The transport layer is responsible for process to process communication. It provides services to the application layer and takes services from the network layer.\\\",\\r\\n            \\\"Two main transfer layer protocols are UDP and TCP.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"title\\\": \\\"Question Time\\\",\\r\\n        \\\"image\\\": \\\"osi.png\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Which layer is responsible for process to process communication?\\\",\\r\\n            \\\"`Select the right answer`\\\",\\r\\n            \\\"`Transport Layer`\\\",\\r\\n            \\\"`Network Layer`\\\",\\r\\n            \\\"`Transport Layer`\\\",\\r\\n            \\\"`Data Link Layer`\\\",\\r\\n            \\\"`None of the above`\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"title\\\": \\\"Session Layer\\\",\\r\\n        \\\"image\\\": \\\"osi.png\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"This layer is responsible for dialog control and synchronisation.\\\",\\r\\n            \\\"It allows the communicating systems to enter into a dialog.\\\",\\r\\n            \\\"Synchronisation allows systems to add check points.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"title\\\": \\\"Presentation & Application layer\\\",\\r\\n        \\\"image\\\": \\\"osi.png\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"Presentation Layer: This layer is responsible for translation, compression and encryption/decryption of data.\\\",\\r\\n            \\\"Application Layer: Also known as the desktop layer, this layer is responsible for providing services to the user. For example: DNS, Email.\\\"\\r\\n        ]\\r\\n    },\\r\\n    {\\r\\n        \\\"title\\\": \\\"--- layer is responsible for encryption/decryption of data.\\\",\\r\\n        \\\"image\\\": \\\"osi.png\\\",\\r\\n        \\\"desc\\\": [\\r\\n            \\\"`Choose the correct option`\\\",\\r\\n            \\\"`Application`\\\",\\r\\n            \\\"`Application`\\\",\\r\\n            \\\"`Presentation`\\\"\\r\\n        ]\\r\\n    }\\r\\n]\"', NULL, NULL, NULL, 'understanding-the-osi-model-b9rglciu', 34, 178, '2024-03-11 15:05:12', '2024-03-11 15:05:12', 0, 1, 'default.webp'),
(500, 'Recap', '\" \"', NULL, NULL, NULL, 'recap-ttxhhmcn', 34, 178, '2024-03-11 15:05:19', '2024-03-11 15:05:19', 0, 1, 'default.png'),
(501, 'What is VPN?', '\" \"', NULL, NULL, NULL, 'what-is-vpn-vu2jvscc', 34, 180, '2024-03-11 15:05:39', '2024-03-11 15:05:39', 0, 1, 'default.png'),
(502, 'How does it work?', '\" \"', NULL, NULL, NULL, 'how-does-it-work-ubo3ypbb', 34, 180, '2024-03-11 15:05:47', '2024-03-11 15:05:47', 0, 1, 'default.png'),
(503, 'Be anonymous', '\" \"', NULL, NULL, NULL, 'be-anonymous-j5z7cpf9', 34, 180, '2024-03-11 15:05:55', '2024-03-11 15:05:55', 0, 1, 'default.png'),
(504, 'Recap', '\" \"', NULL, NULL, NULL, 'recap-0t8iiue4', 34, 180, '2024-03-11 15:06:02', '2024-03-11 15:06:02', 0, 1, 'default.png'),
(505, 'What is Vulnerability Assessment?', '\" \"', NULL, NULL, NULL, 'what-is-vulnerability-assessme-dx4sh8f5', 34, 181, '2024-03-11 15:48:10', '2024-03-11 15:48:10', 0, 1, 'default.png'),
(506, 'Introduction to Pen Testing', '\" \"', NULL, NULL, NULL, 'introduction-to-pen-testing-77icqcpe', 34, 181, '2024-03-11 15:48:29', '2024-03-11 15:48:29', 0, 1, 'default.png'),
(507, 'Let’s perform network scanning', '\" \"', NULL, NULL, NULL, 'let-s-perform-network-scanning-rfu20acb', 34, 181, '2024-03-11 15:48:46', '2024-03-11 15:48:46', 0, 1, 'default.png'),
(508, 'Some more tools that you can use', '\" \"', NULL, NULL, NULL, 'some-more-tools-that-you-can-u-mfvifa7y', 34, 181, '2024-03-11 15:48:56', '2024-03-11 15:48:56', 0, 1, 'default.png'),
(509, 'Recap', '\" \"', NULL, NULL, NULL, 'recap-rm9fpruy', 34, 181, '2024-03-11 15:49:06', '2024-03-11 15:49:06', 0, 1, 'default.png'),
(510, 'Getting to know Cryptography', '\" \"', NULL, NULL, NULL, 'getting-to-know-cryptography-xntw8gyt', 34, 182, '2024-03-11 15:49:31', '2024-03-11 15:49:31', 0, 1, 'default.png'),
(511, 'Some basic terminologies', '\" \"', NULL, NULL, NULL, 'some-basic-terminologies-a80cxwaq', 34, 182, '2024-03-11 15:49:41', '2024-03-11 15:49:41', 0, 1, 'default.png'),
(512, 'Let’s use this Art', '\" \"', NULL, NULL, NULL, 'let-s-use-this-art-yronayiv', 34, 182, '2024-03-11 15:49:51', '2024-03-11 15:49:51', 0, 1, 'default.png'),
(513, 'Recap', '\" \"', NULL, NULL, NULL, 'recap-nhunoeim', 34, 182, '2024-03-11 15:50:05', '2024-03-11 15:50:05', 0, 1, 'default.png'),
(514, 'What is Password cracking?', '\" \"', NULL, NULL, NULL, 'what-is-password-cracking-bfu30fri', 34, 183, '2024-03-11 15:50:34', '2024-03-11 15:50:34', 0, 1, 'default.png'),
(515, 'How strong is your password?', '\" \"', NULL, NULL, NULL, 'how-strong-is-your-password-cefmvuck', 34, 183, '2024-03-11 15:50:45', '2024-03-11 15:50:45', 0, 1, 'default.png'),
(516, 'Know these techniques', '\" \"', NULL, NULL, NULL, 'know-these-techniques-qj2jbir0', 34, 183, '2024-03-11 15:50:55', '2024-03-11 15:50:55', 0, 1, 'default.png'),
(517, 'Some handy tools', '\" \"', NULL, NULL, NULL, 'some-handy-tools-4ttf8tlx', 34, 183, '2024-03-11 15:51:04', '2024-03-11 15:51:04', 0, 1, 'default.png'),
(518, 'Let’s crack the windows', '\" \"', NULL, NULL, NULL, 'let-s-crack-the-windows-ljzfeddz', 34, 183, '2024-03-11 15:51:12', '2024-03-11 15:51:12', 0, 1, 'default.png'),
(519, 'Recap', '\" \"', NULL, NULL, NULL, 'recap-gumelmec', 34, 183, '2024-03-11 15:51:21', '2024-03-11 15:51:21', 0, 1, 'default.png'),
(520, 'What is MITM?', '\" \"', NULL, NULL, NULL, 'what-is-mitm-q4ikkl8n', 34, 184, '2024-03-11 15:51:50', '2024-03-11 15:51:50', 0, 1, 'default.png'),
(521, 'ARP Poisoning', '\" \"', NULL, NULL, NULL, 'arp-poisoning-3y3d49wn', 34, 184, '2024-03-11 15:52:00', '2024-03-11 15:52:00', 0, 1, 'default.png'),
(522, 'ARP spoofing using MITMf', '\" \"', NULL, NULL, NULL, 'arp-spoofing-using-mitmf-0eva1ogo', 34, 184, '2024-03-11 15:52:17', '2024-03-11 15:52:17', 0, 1, 'default.png'),
(523, 'Recap', '\" \"', NULL, NULL, NULL, 'recap-jgvvsmrd', 34, 184, '2024-03-11 15:52:25', '2024-03-11 15:52:25', 0, 1, 'default.png'),
(524, 'Understanding DOS', '\" \"', NULL, NULL, NULL, 'understanding-dos-fawmwq85', 34, 185, '2024-03-11 15:53:07', '2024-03-11 15:53:07', 0, 1, 'default.png'),
(525, 'Common Dos Attacks', '\" \"', NULL, NULL, NULL, 'common-dos-attacks-j0nfqjz6', 34, 185, '2024-03-11 15:53:20', '2024-03-11 15:53:20', 0, 1, 'default.png'),
(526, 'Dos Attack tools', '\" \"', NULL, NULL, NULL, 'dos-attack-tools-nrjredj5', 34, 185, '2024-03-11 15:53:30', '2024-03-11 15:53:30', 0, 1, 'default.png'),
(527, 'Time for Attack', '\" \"', NULL, NULL, NULL, 'time-for-attack-cfvqitoh', 34, 185, '2024-03-11 15:53:39', '2024-03-11 15:53:39', 0, 1, 'default.png'),
(528, 'Recap', '\" \"', NULL, NULL, NULL, 'recap-gle6jpxm', 34, 185, '2024-03-11 15:53:48', '2024-03-11 15:53:48', 0, 1, 'default.png'),
(529, 'Art of hiding - Steganography', '\" \"', NULL, NULL, NULL, 'art-of-hiding---steganography-18vwjk53', 34, 186, '2024-03-11 15:54:29', '2024-03-11 15:54:29', 0, 1, 'default.png'),
(530, 'Using the art of hiding', '\" \"', NULL, NULL, NULL, 'using-the-art-of-hiding-bvnjqzaq', 34, 186, '2024-03-11 15:54:38', '2024-03-11 15:54:38', 0, 1, 'default.png'),
(531, 'Recap', '\" \"', NULL, NULL, NULL, 'recap-8pj5dvb3', 34, 186, '2024-03-11 15:54:46', '2024-03-11 15:54:46', 0, 1, 'default.png'),
(532, 'How much do you remember?', '\" \"', NULL, NULL, NULL, 'how-much-do-you-remember-nrffi4wb', 34, 187, '2024-03-11 15:55:28', '2024-03-11 15:55:28', 0, 1, 'default.png'),
(533, 'Cross site scripting(XSS)', '\" \"', NULL, NULL, NULL, 'cross-site-scripting-xss-etlxcnvk', 34, 187, '2024-03-11 15:55:42', '2024-03-11 15:55:42', 0, 1, 'default.png'),
(534, 'OWASP Top 10', '\" \"', NULL, NULL, NULL, 'owasp-top-10-vrlayltu', 34, 187, '2024-03-11 15:55:50', '2024-03-11 15:55:50', 0, 1, 'default.png'),
(535, 'Recap', '\" \"', NULL, NULL, NULL, 'recap-wdmcakl8', 34, 187, '2024-03-11 15:56:01', '2024-03-11 15:56:01', 0, 1, 'default.png'),
(536, 'Summarizing our learning', '\" \"', NULL, NULL, NULL, 'summarizing-our-learning-nmgne6f9', 33, 78, '2024-03-11 17:00:51', '2024-03-11 17:00:51', 0, 1, 'default.png'),
(537, 'Let’s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-clujz0lr', 33, 78, '2024-03-11 17:01:42', '2024-03-11 17:01:42', 0, 1, 'default.png'),
(538, 'World & Data', '\" \"', NULL, NULL, NULL, 'world---data-0gkhpig3', 37, 188, '2024-03-12 13:15:13', '2024-03-12 13:15:13', 0, 1, 'default.png'),
(539, 'Problems solved by data science', '\" \"', NULL, NULL, NULL, 'problems-solved-by-data-scienc-6w4z2iya', 37, 188, '2024-03-12 13:15:32', '2024-03-12 13:15:32', 0, 1, 'default.png'),
(540, 'Let\'s recap', '\" \"', NULL, NULL, NULL, 'let-s-recap-lbfoeews', 37, 188, '2024-03-12 13:15:42', '2024-03-12 13:15:42', 0, 1, 'default.png'),
(541, 'Extracting and cleaning data', '\" \"', NULL, NULL, NULL, 'extracting-and-cleaning-data-fbirz4vk', 37, 189, '2024-03-12 13:15:59', '2024-03-12 13:15:59', 0, 1, 'default.png'),
(542, 'Process of data wrangling', '\" \"', NULL, NULL, NULL, 'process-of-data-wrangling-sgwzm9uy', 37, 189, '2024-03-12 13:16:07', '2024-03-12 13:16:07', 0, 1, 'default.png'),
(543, 'Category of data', '\" \"', NULL, NULL, NULL, 'category-of-data-ofy6q4k2', 37, 189, '2024-03-12 13:16:13', '2024-03-12 13:16:13', 0, 1, 'default.png'),
(544, 'Data analysis overview', '\" \"', NULL, NULL, NULL, 'data-analysis-overview-avdi2cvi', 37, 190, '2024-03-12 13:16:27', '2024-03-12 13:16:27', 0, 1, 'default.png'),
(545, 'Flow of data analysis', '\" \"', NULL, NULL, NULL, 'flow-of-data-analysis-dsvu8q7m', 37, 190, '2024-03-12 13:16:36', '2024-03-12 13:16:36', 0, 1, 'default.png'),
(546, 'Let\'s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-tjjanewf', 37, 190, '2024-03-12 13:16:42', '2024-03-12 13:16:42', 0, 1, 'default.png'),
(547, 'Introduction to visualization', '\" \"', NULL, NULL, NULL, 'introduction-to-visualization-rsqxtdul', 37, 191, '2024-03-12 13:17:07', '2024-03-12 13:17:07', 0, 1, 'default.png'),
(548, 'Examples of diagrams used for data visualization', '\" \"', NULL, NULL, NULL, 'examples-of-diagrams-used-for-a2zmgf2x', 37, 191, '2024-03-12 13:17:18', '2024-03-12 13:17:18', 0, 1, 'default.png'),
(549, 'Let\'s revise Data Visualization', '\" \"', NULL, NULL, NULL, 'let-s-revise-data-visualizatio-nwv0ih3k', 37, 191, '2024-03-12 13:17:42', '2024-03-12 13:17:42', 0, 1, 'default.png'),
(550, 'Overview of numpy', '\" \"', NULL, NULL, NULL, 'overview-of-numpy-f3nhv4oo', 37, 192, '2024-03-12 13:17:58', '2024-03-12 13:17:58', 0, 1, 'default.png'),
(551, 'Overview of Pandas', '\" \"', NULL, NULL, NULL, 'overview-of-pandas-ibp4e2xd', 37, 192, '2024-03-12 13:18:06', '2024-03-12 13:18:06', 0, 1, 'default.png'),
(552, 'Overview of Matplotlib', '\" \"', NULL, NULL, NULL, 'overview-of-matplotlib-oo55zklb', 37, 192, '2024-03-12 13:18:14', '2024-03-12 13:18:14', 0, 1, 'default.png'),
(553, 'Let\'s revise', '\" \"', NULL, NULL, NULL, 'let-s-revise-uby0fhng', 37, 192, '2024-03-12 13:18:20', '2024-03-12 13:18:20', 0, 1, 'default.png'),
(554, 'How a machine learns', '\" \"', NULL, NULL, NULL, 'how-a-machine-learns-bt1wib9t', 37, 193, '2024-03-12 13:18:34', '2024-03-12 13:18:34', 0, 1, 'default.png'),
(555, 'Machine Learning Approaches', '\" \"', NULL, NULL, NULL, 'machine-learning-approaches-axh3detu', 37, 193, '2024-03-12 13:18:44', '2024-03-12 13:18:44', 0, 1, 'default.png'),
(556, 'Let\'s revise Machine Learning In Data Science', '\" \"', NULL, NULL, NULL, 'let-s-revise-machine-learning-ki3zjuqo', 37, 193, '2024-03-12 13:19:11', '2024-03-12 13:19:11', 0, 1, 'default.png'),
(557, 'Role of machine learning scientists and data scien', '\" \"', NULL, NULL, NULL, 'role-of-machine-learning-scien-b9yrwych', 37, 194, '2024-03-12 13:19:28', '2024-03-12 13:19:28', 0, 1, 'default.png'),
(558, 'The fields of data science', '\" \"', NULL, NULL, NULL, 'the-fields-of-data-science-dy8jpbd6', 37, 194, '2024-03-12 13:19:47', '2024-03-12 13:19:47', 0, 1, 'default.png'),
(559, 'Data Science Application', '\" \"', NULL, NULL, NULL, 'data-science-application-uche4nls', 37, 195, '2024-03-12 13:20:02', '2024-03-12 13:20:02', 0, 1, 'default.png'),
(560, 'Let\'s Revise Data Science Application', '\" \"', NULL, NULL, NULL, 'let-s-revise-data-science-appl-imrz1zwd', 37, 195, '2024-03-12 13:20:21', '2024-03-12 13:20:21', 0, 1, 'default.png'),
(561, 'Where did we leave?', '\" \"', NULL, NULL, NULL, 'where-did-we-leave-qfqvieha', 90, 196, '2024-03-12 15:24:11', '2024-03-12 15:24:11', 0, 1, 'default.png'),
(562, 'Welcome back', '\" \"', NULL, NULL, NULL, 'welcome-back-480vzbur', 90, 196, '2024-03-12 15:24:32', '2024-03-12 15:24:32', 0, 1, 'default.png'),
(563, 'Prerequisites', '\" \"', NULL, NULL, NULL, 'prerequisites-z98vapx6', 90, 196, '2024-03-12 15:24:41', '2024-03-12 15:24:41', 0, 1, 'default.png'),
(564, 'File and File Handling', '\" \"', NULL, NULL, NULL, 'file-and-file-handling-t8yuz2en', 90, 197, '2024-03-12 15:24:58', '2024-03-12 15:24:58', 0, 1, 'default.png'),
(565, 'Opening and File Modes', '\" \"', NULL, NULL, NULL, 'opening-and-file-modes-uhddxy2m', 90, 197, '2024-03-12 15:25:19', '2024-03-12 15:25:19', 0, 1, 'default.png'),
(566, 'Reading and Writing', '\" \"', NULL, NULL, NULL, 'reading-and-writing-gjpwszhq', 90, 197, '2024-03-12 15:25:28', '2024-03-12 15:25:28', 0, 1, 'default.png'),
(567, 'Closing File', '\" \"', NULL, NULL, NULL, 'closing-file-y5vnfxys', 90, 197, '2024-03-12 15:25:37', '2024-03-12 15:25:37', 0, 1, 'default.png'),
(568, 'Recap - Python File Handling', '\" \"', NULL, NULL, NULL, 'recap---python-file-handling-l21wrcas', 90, 197, '2024-03-12 15:25:56', '2024-03-12 15:25:56', 0, 1, 'default.png'),
(569, 'What are Python Modules?', '\" \"', NULL, NULL, NULL, 'what-are-python-modules-qb8volre', 90, 198, '2024-03-12 15:26:19', '2024-03-12 15:26:19', 0, 1, 'default.png'),
(570, 'Random Module', '\" \"', NULL, NULL, NULL, 'random-module-xtpip3n1', 90, 198, '2024-03-12 15:26:26', '2024-03-12 15:26:26', 0, 1, 'default.png'),
(571, 'Statistics Module', '\" \"', NULL, NULL, NULL, 'statistics-module-bymd3v31', 90, 198, '2024-03-12 15:26:36', '2024-03-12 15:26:36', 0, 1, 'default.png'),
(572, 'Time Module', '\" \"', NULL, NULL, NULL, 'time-module-qsjcbqc3', 90, 198, '2024-03-12 15:26:43', '2024-03-12 15:26:43', 0, 1, 'default.png'),
(573, 'Recap - Python Modules', '\" \"', NULL, NULL, NULL, 'recap---python-modules-3ibxg3oj', 90, 198, '2024-03-12 15:27:04', '2024-03-12 15:27:04', 0, 1, 'default.png'),
(574, 'Errors and Exceptions', '\" \"', NULL, NULL, NULL, 'errors-and-exceptions-4utzutpc', 90, 199, '2024-03-12 15:27:23', '2024-03-12 15:27:23', 0, 1, 'default.png'),
(575, 'Exception Handling in Python', '\" \"', NULL, NULL, NULL, 'exception-handling-in-python-shefxnie', 90, 199, '2024-03-12 15:27:31', '2024-03-12 15:27:31', 0, 1, 'default.png'),
(576, 'Finally and Raise', '\" \"', NULL, NULL, NULL, 'finally-and-raise-dd8ddmh1', 90, 199, '2024-03-12 15:27:38', '2024-03-12 15:27:38', 0, 1, 'default.png'),
(577, 'Recap - Python Exceptions', '\" \"', NULL, NULL, NULL, 'recap---python-exceptions-snkvocbi', 90, 199, '2024-03-12 15:27:54', '2024-03-12 15:27:54', 0, 1, 'default.png'),
(578, 'What is Regular Expression?', '\" \"', NULL, NULL, NULL, 'what-is-regular-expression-wid8elp3', 90, 200, '2024-03-12 15:28:22', '2024-03-12 15:28:22', 0, 1, 'default.png'),
(579, 'Using RE Methods', '\" \"', NULL, NULL, NULL, 'using-re-methods-h4vvpa4v', 90, 200, '2024-03-12 15:28:31', '2024-03-12 15:28:31', 0, 1, 'default.png'),
(580, 'Recap Regex in python', '\" \"', NULL, NULL, NULL, 'recap-regex-in-python-pbliqz2e', 90, 200, '2024-03-12 15:28:51', '2024-03-12 15:28:51', 0, 1, 'default.png'),
(581, 'MySQL Overview', '\" \"', NULL, NULL, NULL, 'mysql-overview-sas8bujv', 90, 201, '2024-03-12 15:29:09', '2024-03-12 15:29:09', 0, 1, 'default.png'),
(582, 'Connecting to Database', '\" \"', NULL, NULL, NULL, 'connecting-to-database-tcseg6tt', 90, 201, '2024-03-12 15:29:20', '2024-03-12 15:29:20', 0, 1, 'default.png'),
(583, 'Creating a Table', '\" \"', NULL, NULL, NULL, 'creating-a-table-vdkvoxxk', 90, 201, '2024-03-12 15:29:27', '2024-03-12 15:29:27', 0, 1, 'default.png'),
(584, 'CRUD Operations', '\" \"', NULL, NULL, NULL, 'crud-operations-6nk235dw', 90, 201, '2024-03-12 15:29:38', '2024-03-12 15:29:38', 0, 1, 'default.png'),
(585, 'Recap - Db Connection Python', '\" \"', NULL, NULL, NULL, 'recap---db-connection-python-iwod44s2', 90, 201, '2024-03-12 15:30:02', '2024-03-12 15:30:02', 0, 1, 'default.png'),
(586, 'What is GUI?', '\" \"', NULL, NULL, NULL, 'what-is-gui-gegsa4mc', 90, 202, '2024-03-12 15:30:21', '2024-03-12 15:30:21', 0, 1, 'default.png'),
(587, 'Introduction to Tkinter', '\" \"', NULL, NULL, NULL, 'introduction-to-tkinter-jsxblybz', 90, 202, '2024-03-12 15:30:31', '2024-03-12 15:30:31', 0, 1, 'default.png'),
(588, 'Working with Tkinter Widgets', '\" \"', NULL, NULL, NULL, 'working-with-tkinter-widgets-hu7xemho', 90, 202, '2024-03-12 15:30:39', '2024-03-12 15:30:39', 0, 1, 'default.png'),
(589, 'Recap - Python GUI Development', '\" \"', NULL, NULL, NULL, 'recap---python-gui-development-1h72bcol', 90, 202, '2024-03-12 15:30:56', '2024-03-12 15:30:56', 0, 1, 'default.png'),
(590, 'OOPS and Related Concepts', '\" \"', NULL, NULL, NULL, 'oops-and-related-concepts-zsxcrr8o', 90, 203, '2024-03-12 15:31:16', '2024-03-12 15:31:16', 0, 1, 'default.png'),
(591, 'Classes and Objects', '\" \"', NULL, NULL, NULL, 'classes-and-objects-tuz5infh', 90, 203, '2024-03-12 15:31:26', '2024-03-12 15:31:26', 0, 1, 'default.png'),
(592, 'Inheritance in Python', '\" \"', NULL, NULL, NULL, 'inheritance-in-python-rq3slu4c', 90, 203, '2024-03-12 15:31:32', '2024-03-12 15:31:32', 0, 1, 'default.png'),
(593, 'Recap - Oops In Python', '\" \"', NULL, NULL, NULL, 'recap---oops-in-python-yev0kqvi', 90, 203, '2024-03-12 15:31:54', '2024-03-12 15:31:54', 0, 1, 'default.png'),
(594, 'Introduction to Multithreading', '\" \\r\\n\"', NULL, NULL, NULL, 'introduction-to-multithreading-ctpkduum', 90, 204, '2024-03-12 15:32:17', '2024-03-12 15:32:17', 0, 1, 'default.png'),
(595, 'Threading Module', '\" \\r\\n\"', NULL, NULL, NULL, 'threading-module-7qhgcx5x', 90, 204, '2024-03-12 15:32:28', '2024-03-12 15:32:28', 0, 1, 'default.png'),
(596, 'Threading Example', '\" \\r\\n\"', NULL, NULL, NULL, 'threading-example-ougxxvd9', 90, 204, '2024-03-12 15:32:37', '2024-03-12 15:32:37', 0, 1, 'default.png'),
(597, 'Recap - Python Multithreading', '\" \\r\\n\"', NULL, NULL, NULL, 'recap---python-multithreading-8ruvm4t0', 90, 204, '2024-03-12 15:33:00', '2024-03-12 15:33:00', 0, 1, 'default.png'),
(598, 'Congratulations', '\" \\r\\n\"', NULL, NULL, NULL, 'congratulations-aqybcqxg', 90, 205, '2024-03-12 15:33:17', '2024-03-12 15:33:17', 0, 1, 'default.png'),
(599, 'Roadmap', '\" \\r\\n\"', NULL, NULL, NULL, 'roadmap-8lo5zgpq', 90, 205, '2024-03-12 15:33:23', '2024-03-12 15:33:23', 0, 1, 'default.png');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `password` varchar(500) NOT NULL,
  `title` varchar(50) DEFAULT NULL,
  `gender` text DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `lang` varchar(100) DEFAULT NULL,
  `about` varchar(5000) DEFAULT NULL,
  `socials` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`socials`)),
  `duration` int(11) DEFAULT NULL,
  `education` varchar(100) DEFAULT NULL,
  `comment_count` int(11) DEFAULT NULL,
  `trainee` int(11) DEFAULT NULL,
  `ratings` int(11) DEFAULT NULL,
  `reviews` int(11) DEFAULT NULL,
  `ip` varchar(50) DEFAULT NULL,
  `verified` tinyint(1) DEFAULT NULL,
  `graduated` tinyint(1) DEFAULT NULL,
  `bank` int(11) DEFAULT NULL,
  `online` tinyint(1) DEFAULT NULL,
  `last_seen` datetime DEFAULT NULL,
  `last_message_read_time` datetime DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `image` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `username`, `email`, `phone`, `password`, `title`, `gender`, `city`, `lang`, `about`, `socials`, `duration`, `education`, `comment_count`, `trainee`, `ratings`, `reviews`, `ip`, `verified`, `graduated`, `bank`, `online`, `last_seen`, `last_message_read_time`, `created`, `updated`, `deleted`, `active`, `image`) VALUES
(1, 'Chris James', 'hacker', 'hacker@yahoo.com', '07026561327', '$2b$12$MgujcNuTC7ELHX54wgCZ6u1/Ufg3rj5KdWRYAzxaLXwveO5q7E10C', NULL, 'm', '', '', 'Elite software developer with special interest in artificial intelligence, business intelligence, data & hacking', NULL, 72, NULL, NULL, NULL, NULL, NULL, '127.0.0.1', 0, 0, NULL, 1, '2024-02-06 08:16:30', NULL, '2024-02-01 17:23:30', '2024-02-01 17:23:30', 0, 1, NULL),
(2, 'Chris Hacker', '@hacka', 'hacker@gmail.com', '07126561327', '$2b$12$7gISVGcDb0KRCbjv8BHGDODDpcpbX53Y3.fAc8OFG8UrTcd5yXKYq', NULL, 'm', '', 'english', 'Elite Software Engr With Special Interest In Artificial Intelligence | Business Intelligence | Data & Hacking', NULL, 72, NULL, NULL, NULL, NULL, NULL, '127.0.0.1', 0, 0, NULL, 1, '2024-03-24 20:50:44', NULL, '2024-02-03 07:25:41', '2024-02-03 07:25:41', 0, 1, 'hacka_chris500c.png');

-- --------------------------------------------------------

--
-- Table structure for table `user_course_association`
--

CREATE TABLE `user_course_association` (
  `user_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user_role_association`
--

CREATE TABLE `user_role_association` (
  `user_id` int(11) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user_topic_progress`
--

CREATE TABLE `user_topic_progress` (
  `user_id` int(11) NOT NULL,
  `topic_id` int(11) NOT NULL,
  `completed` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_topic_progress`
--

INSERT INTO `user_topic_progress` (`user_id`, `topic_id`, `completed`) VALUES
(2, 164, 0),
(2, 369, 0),
(2, 370, 0),
(2, 371, 0),
(2, 372, 0),
(2, 373, 0),
(2, 374, 0),
(2, 375, 0),
(2, 376, 0),
(2, 377, 0),
(2, 378, 0),
(2, 379, 0),
(2, 381, 0),
(2, 382, 0),
(2, 383, 0),
(2, 384, 0),
(2, 385, 0),
(2, 386, 0),
(2, 496, 0),
(2, 497, 0),
(2, 498, 0),
(2, 499, 0),
(2, 500, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `badge`
--
ALTER TABLE `badge`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `user` (`user`),
  ADD KEY `course` (`course`);

--
-- Indexes for table `brand`
--
ALTER TABLE `brand`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD UNIQUE KEY `type` (`type`),
  ADD UNIQUE KEY `name` (`name`),
  ADD UNIQUE KEY `ix_brand_email` (`email`),
  ADD KEY `ix_brand_phone` (`phone`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD UNIQUE KEY `title` (`title`),
  ADD UNIQUE KEY `desc` (`desc`);

--
-- Indexes for table `category_course_association`
--
ALTER TABLE `category_course_association`
  ADD KEY `course_id` (`course_id`),
  ADD KEY `category_id` (`category_id`);

--
-- Indexes for table `chat`
--
ALTER TABLE `chat`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `_from` (`_from`),
  ADD KEY `_to` (`_to`);

--
-- Indexes for table `content`
--
ALTER TABLE `content`
  ADD PRIMARY KEY (`id`),
  ADD KEY `topic_id` (`topic_id`);

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD UNIQUE KEY `title` (`title`),
  ADD KEY `category_id` (`category_id`);

--
-- Indexes for table `course_tag_association`
--
ALTER TABLE `course_tag_association`
  ADD PRIMARY KEY (`course_id`,`tag_id`),
  ADD KEY `tag_id` (`tag_id`);

--
-- Indexes for table `enrollment`
--
ALTER TABLE `enrollment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `course_id` (`course_id`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `course_id` (`course_id`);

--
-- Indexes for table `interaction`
--
ALTER TABLE `interaction`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `lesson`
--
ALTER TABLE `lesson`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `user` (`user`),
  ADD KEY `course_id` (`course_id`);

--
-- Indexes for table `message`
--
ALTER TABLE `message`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `sender_id` (`sender_id`),
  ADD KEY `recipient_id` (`recipient_id`);

--
-- Indexes for table `notification`
--
ALTER TABLE `notification`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `ix_notification_name` (`name`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `course_id` (`course_id`);

--
-- Indexes for table `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `type` (`type`);

--
-- Indexes for table `tag`
--
ALTER TABLE `tag`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `topic`
--
ALTER TABLE `topic`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `course_id` (`course_id`),
  ADD KEY `lesson_id` (`lesson_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD UNIQUE KEY `ix_user_username` (`username`),
  ADD UNIQUE KEY `ix_user_email` (`email`),
  ADD UNIQUE KEY `ix_user_phone` (`phone`),
  ADD KEY `ix_user_password` (`password`),
  ADD KEY `ix_user_name` (`name`);

--
-- Indexes for table `user_course_association`
--
ALTER TABLE `user_course_association`
  ADD PRIMARY KEY (`user_id`,`course_id`),
  ADD KEY `course_id` (`course_id`);

--
-- Indexes for table `user_role_association`
--
ALTER TABLE `user_role_association`
  ADD KEY `user_id` (`user_id`),
  ADD KEY `role_id` (`role_id`);

--
-- Indexes for table `user_topic_progress`
--
ALTER TABLE `user_topic_progress`
  ADD PRIMARY KEY (`user_id`,`topic_id`),
  ADD KEY `topic_id` (`topic_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `badge`
--
ALTER TABLE `badge`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `brand`
--
ALTER TABLE `brand`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `chat`
--
ALTER TABLE `chat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `content`
--
ALTER TABLE `content`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `course`
--
ALTER TABLE `course`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=102;

--
-- AUTO_INCREMENT for table `enrollment`
--
ALTER TABLE `enrollment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `interaction`
--
ALTER TABLE `interaction`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `lesson`
--
ALTER TABLE `lesson`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=206;

--
-- AUTO_INCREMENT for table `message`
--
ALTER TABLE `message`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `notification`
--
ALTER TABLE `notification`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=66;

--
-- AUTO_INCREMENT for table `post`
--
ALTER TABLE `post`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `role`
--
ALTER TABLE `role`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tag`
--
ALTER TABLE `tag`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `topic`
--
ALTER TABLE `topic`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=600;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `badge`
--
ALTER TABLE `badge`
  ADD CONSTRAINT `badge_ibfk_1` FOREIGN KEY (`user`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `badge_ibfk_2` FOREIGN KEY (`course`) REFERENCES `course` (`id`);

--
-- Constraints for table `chat`
--
ALTER TABLE `chat`
  ADD CONSTRAINT `chat_ibfk_1` FOREIGN KEY (`_from`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `chat_ibfk_2` FOREIGN KEY (`_to`) REFERENCES `user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

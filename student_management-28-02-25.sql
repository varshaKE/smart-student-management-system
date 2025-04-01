/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - smart_student
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`smart_student` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `smart_student`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

/*Table structure for table `smart_student_app_announcement` */

DROP TABLE IF EXISTS `smart_student_app_announcement`;

CREATE TABLE `smart_student_app_announcement` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `announcement` varchar(150) NOT NULL,
  `date` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `smart_student_app_announcement` */

/*Table structure for table `smart_student_app_assignments` */

DROP TABLE IF EXISTS `smart_student_app_assignments`;

CREATE TABLE `smart_student_app_assignments` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `assignment` varchar(150) NOT NULL,
  `due_date` varchar(150) NOT NULL,
  `description` varchar(150) NOT NULL,
  `date` varchar(150) NOT NULL,
  `subject_id` bigint(20) NOT NULL,
  `teacher_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smart_student_app_assignments_subject_id_fd7d24e8` (`subject_id`),
  KEY `smart_student_app_assignments_teacher_id_57e09d84` (`teacher_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `smart_student_app_assignments` */

/*Table structure for table `smart_student_app_assignteacher` */

DROP TABLE IF EXISTS `smart_student_app_assignteacher`;

CREATE TABLE `smart_student_app_assignteacher` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` varchar(150) NOT NULL,
  `subject_id` bigint(20) NOT NULL,
  `teacher_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smart_student_app_assignteacher_subject_id_b4ea1d9a` (`subject_id`),
  KEY `smart_student_app_assignteacher_teacher_id_cdc25c2c` (`teacher_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `smart_student_app_assignteacher` */

/*Table structure for table `smart_student_app_complaint` */

DROP TABLE IF EXISTS `smart_student_app_complaint`;

CREATE TABLE `smart_student_app_complaint` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `complaint` varchar(150) NOT NULL,
  `reply` varchar(150) NOT NULL,
  `date` varchar(150) NOT NULL,
  `login_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smart_student_app_complaint_login_id_883a71d7` (`login_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `smart_student_app_complaint` */

/*Table structure for table `smart_student_app_course` */

DROP TABLE IF EXISTS `smart_student_app_course`;

CREATE TABLE `smart_student_app_course` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `course_name` varchar(150) NOT NULL,
  `dept_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smart_student_app_course_dept_id_5146c811` (`dept_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `smart_student_app_course` */

/*Table structure for table `smart_student_app_department` */

DROP TABLE IF EXISTS `smart_student_app_department`;

CREATE TABLE `smart_student_app_department` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `dept_name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `smart_student_app_department` */

/*Table structure for table `smart_student_app_internalmarks` */

DROP TABLE IF EXISTS `smart_student_app_internalmarks`;

CREATE TABLE `smart_student_app_internalmarks` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `marks` varchar(150) NOT NULL,
  `date` varchar(150) NOT NULL,
  `status` varchar(150) NOT NULL,
  `student_id` bigint(20) NOT NULL,
  `subject_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smart_student_app_internalmarks_student_id_97d86119` (`student_id`),
  KEY `smart_student_app_internalmarks_subject_id_46e18532` (`subject_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `smart_student_app_internalmarks` */

/*Table structure for table `smart_student_app_login` */

DROP TABLE IF EXISTS `smart_student_app_login`;

CREATE TABLE `smart_student_app_login` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `usertype` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `smart_student_app_login` */

insert  into `smart_student_app_login`(`id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin');

/*Table structure for table `smart_student_app_parent` */

DROP TABLE IF EXISTS `smart_student_app_parent`;

CREATE TABLE `smart_student_app_parent` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `address` varchar(150) NOT NULL,
  `phone_no` varchar(150) NOT NULL,
  `email` varchar(150) NOT NULL,
  `login_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smart_student_app_parent_login_id_7119af14` (`login_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `smart_student_app_parent` */

/*Table structure for table `smart_student_app_semester` */

DROP TABLE IF EXISTS `smart_student_app_semester`;

CREATE TABLE `smart_student_app_semester` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `sem` varchar(150) NOT NULL,
  `course_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smart_student_app_semester_course_id_74c9ef13` (`course_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `smart_student_app_semester` */

/*Table structure for table `smart_student_app_student` */

DROP TABLE IF EXISTS `smart_student_app_student`;

CREATE TABLE `smart_student_app_student` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `address` varchar(150) NOT NULL,
  `gender` varchar(150) NOT NULL,
  `dob` varchar(150) NOT NULL,
  `phone_no` varchar(150) NOT NULL,
  `religion` varchar(150) NOT NULL,
  `relation` varchar(150) NOT NULL,
  `email` varchar(150) NOT NULL,
  `qualification` varchar(150) NOT NULL,
  `aadhaar_no` varchar(150) NOT NULL,
  `course_id` bigint(20) NOT NULL,
  `dept_id` bigint(20) NOT NULL,
  `login_id` bigint(20) NOT NULL,
  `parent_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smart_student_app_student_course_id_e4ba7f09` (`course_id`),
  KEY `smart_student_app_student_dept_id_048426e0` (`dept_id`),
  KEY `smart_student_app_student_login_id_144bbfad` (`login_id`),
  KEY `smart_student_app_student_parent_id_c0782bde` (`parent_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `smart_student_app_student` */

/*Table structure for table `smart_student_app_subject` */

DROP TABLE IF EXISTS `smart_student_app_subject`;

CREATE TABLE `smart_student_app_subject` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `subject_name` varchar(150) NOT NULL,
  `sem_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smart_student_app_subject_sem_id_684ba6ef` (`sem_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `smart_student_app_subject` */

/*Table structure for table `smart_student_app_teacher` */

DROP TABLE IF EXISTS `smart_student_app_teacher`;

CREATE TABLE `smart_student_app_teacher` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `dob` varchar(100) NOT NULL,
  `phone_no` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `qualification` varchar(100) NOT NULL,
  `dept_id` bigint(20) NOT NULL,
  `login_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smart_student_app_teacher_login_id_59d46ec7` (`login_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `smart_student_app_teacher` */

/*Table structure for table `smart_student_app_uploadassignments` */

DROP TABLE IF EXISTS `smart_student_app_uploadassignments`;

CREATE TABLE `smart_student_app_uploadassignments` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `file` varchar(100) NOT NULL,
  `date` varchar(150) NOT NULL,
  `marks` varchar(150) NOT NULL,
  `status` varchar(150) NOT NULL,
  `assignment_id` bigint(20) NOT NULL,
  `student_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smart_student_app_uploadassignments_assignment_id_8ada6f51` (`assignment_id`),
  KEY `smart_student_app_uploadassignments_student_id_405a096c` (`student_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `smart_student_app_uploadassignments` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

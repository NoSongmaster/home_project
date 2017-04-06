/*
Navicat MySQL Data Transfer

Source Server         : 172.16.50.192
Source Server Version : 50532
Source Host           : 192.168.0.106:3306
Source Database       : db

Target Server Type    : MYSQL
Target Server Version : 50532
File Encoding         : 65001

Date: 2017-03-31 00:05:49
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for host
-- ----------------------------
DROP TABLE IF EXISTS `host`;
CREATE TABLE `host` (
  `host_id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` char(32) DEFAULT NULL,
  `port` char(32) DEFAULT NULL,
  `username` char(32) DEFAULT NULL,
  `password` text,
  `pwd_type` char(32) DEFAULT NULL,
  PRIMARY KEY (`host_id`),
  UNIQUE KEY `host` (`ip`) USING HASH
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of host
-- ----------------------------
INSERT INTO `host` VALUES ('1', '192.168.0.102', '22', 'root', '123456', 'pwd');
INSERT INTO `host` VALUES ('2', '192.168.0.103', '22', 'root', '-----BEGIN RSA PRIVATE KEY-----\r\nMIIEoAIBAAKCAQEAofI560WqI22It/D8PfTjnVrZLIjdhlExExAnfL9ZhQEZknew\r\n8gVeThaZKwx/tqa8DIEGbtoYAHr6jBg76IrsPS1sljpWDTlIPt+40eaUZizFNtD9\r\n/k4V6swa45Bvdrk3QWco8EKQyUiNZ8kHmW+0xl5i+cB/5yUX0QujeZN9ooHSsCIo\r\n0GERZT+aJR6PlPaH7R/wLuAMLVRegJIzCu7jRubKBxepINo4AsvWzhI86cMWsS/o\r\nA1brFfnOFeohbXlNuiRpjzbbyXV5OP23BbfnvODpWjnTz+LMaAp5CPmKigyXNVO+\r\nxBCVcobxdV6pKJgoBIeKGOcU6cMlhDjvAZYeGwIBIwKCAQBly3TdBze+f11Aa5c8\r\n4xK6riIb/kIZ6eRVIBjSEeB/fQjCdx7EA1/ZUAiBdZIbCbgH3BKsFA8WPqwdi5Ne\r\n+Dy4vXd0Xy7Ge8cC8wZ1TxtzbJk4Zhv+70D5/KMv9GNR8MOldAsarX+Udr9IjP12\r\nY3jxt6vtca97WSTpzM0n2Q0kUJn7m14N7TYqikqlzLmfM7kwOximj8zFDwpFFtV3\r\nhTQDAYTPudsE8YC9lTgcJA7uj0O66hPkT90CZu3F+A3g/C8kMKudBS9Q2NDWl4TF\r\nuLk8m+BqvdKf2pIcuxbWMrS8ozaMjbDgKm3qEsazFj7el5oOh+AuzTFrkbSqRio2\r\nUI/7AoGBANek+QKfGorwOzJRrsgHXTLJzSx3iOULtrV0NngrA7ia7viHJm3rM8n+\r\nTxnEyPTgvVQw6/W0AX7DtItVEaowZP0qc4x4Iw8RIyMNuJgsAdxwTxboMGQv9EZt\r\nMSyDZ5SVU4DILHuG4BA/G7ty3QRhC/mqJTap3tvaSpUy0Ev//SdfAoGBAMBAsflJ\r\nqjvrhXy0ZEMnmH/5gGJRQ9W5kV6HK8Rb9FftAQnYYNMiJjh5yYat+KSkxL95z4zY\r\neUbluMh6QjKc93ntY276XQFx4iEy9voqylj3yGHIOIlEhykqO0sZhxw8+z+k0XtM\r\n7QTh8D+3DMxlbHNxz/pqZLBBbdmfm+t8pG7FAoGAaL3YCJZr+ldtNbKlWdew7Mhq\r\n+FdRHsss28q7XvBSQ7j3uorJhdikIEhSTlhEWa7837/9lJlCjgdJEHnGwGCmFJD2\r\nS4rPMzQ1o0/OsE/jpZWiwfu/u6JDcqoQkfaup0E3L+wy3Om9SbhAq4DvAiCCKM78\r\nId1639BtXmkjWB1AcjUCgYAxb7i8cgcz+rvs3e3lYfQDpo66Midi1/IuQAPwqe5f\r\nwJnd9c/BQ0uoH1EUANmJbDKXovrbExffB98O+t3SgCJhLmoGmCaLV8xu79kbwdxC\r\nw19pmeKm9F1FGXz2DeDqAQ1oIxFLl3Al07LOjifcyZ+LZmiuG1u4S1bC7oct7NnT\r\nVwKBgFuagfheJiwLkqUMsm6Cwi2+UpNqTC+ZjQ7G0nZtovafC6X0i+opkpMFbJzf\r\nn3Yj+7sLm8sCx3SUhYLEmlhDPuPZflyLuOyz927veXpJGHd9TdaktZhyPX/BdkQh\r\nLRxssxuDBvd8eJagIdCNfDN7TKRkHulwZdCcEP8wb3MPO7oR\r\n-----END RSA PRIVATE KEY-----', 'private_key');

-- ----------------------------
-- Table structure for user_to_host
-- ----------------------------
DROP TABLE IF EXISTS `user_to_host`;
CREATE TABLE `user_to_host` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_to_id` int(11) NOT NULL,
  `host_to_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `host_id_wj` (`host_to_id`),
  KEY `user_id_wj` (`user_to_id`),
  CONSTRAINT `host_id_wj` FOREIGN KEY (`host_to_id`) REFERENCES `host` (`host_id`),
  CONSTRAINT `user_id_wj` FOREIGN KEY (`user_to_id`) REFERENCES `userinfo` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_to_host
-- ----------------------------
INSERT INTO `user_to_host` VALUES ('1', '1', '1');
INSERT INTO `user_to_host` VALUES ('2', '1', '2');
INSERT INTO `user_to_host` VALUES ('3', '2', '1');

-- ----------------------------
-- Table structure for user_type
-- ----------------------------
DROP TABLE IF EXISTS `user_type`;
CREATE TABLE `user_type` (
  `type_id` int(2) NOT NULL AUTO_INCREMENT,
  `type` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`type_id`),
  KEY `type` (`type`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_type
-- ----------------------------
INSERT INTO `user_type` VALUES ('2', '普通用户');
INSERT INTO `user_type` VALUES ('1', '管理员');

-- ----------------------------
-- Table structure for userinfo
-- ----------------------------
DROP TABLE IF EXISTS `userinfo`;
CREATE TABLE `userinfo` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(20) NOT NULL,
  `password` char(20) NOT NULL,
  `user_type` int(255) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  KEY `user_type_wj` (`user_type`),
  CONSTRAINT `user_type_wj` FOREIGN KEY (`user_type`) REFERENCES `user_type` (`type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of userinfo
-- ----------------------------
INSERT INTO `userinfo` VALUES ('1', 'liuhao', 'liuhao', '2');
INSERT INTO `userinfo` VALUES ('2', 'alex', 'alex', '2');
INSERT INTO `userinfo` VALUES ('3', 'administrator', '123456', '1');

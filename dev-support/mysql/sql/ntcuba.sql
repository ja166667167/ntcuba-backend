-- ------------------------
-- This structure for admin
-- ------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
    `id` varchar(32) NOT NULL,
    `name` varchar(32) NOT NULL,
    `password` varchar(32) NOT NULL,
    `create_time` datetime default NULL COMMENT 'create time',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8_general_ci;

insert into admin(id, name, password) values('BCS108114','阮文謙','test');
-- the script creates second_table in the current database and add two multiple rows.

-- Creates and fills a table second_table with attributes id, name, and score
CREATE TABLE IF NOT EXISTS `second_table` (
    `id` INT,
    `name` VARCHAR(256),
    `score` INT
);

-- Insert rows into second_table
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, 'John', 10);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (2, 'Alex', 3);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (3, 'Bob', 14);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (4, 'George', 8);


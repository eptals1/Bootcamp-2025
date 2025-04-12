CREATE TABLE martian(
martian_id INT AUTO_INCREMENT PRIMARY KEY,
first_name VARCHAR(25),
last_name VARCHAR(25),
base_id INT,
super_id INT);

INSERT INTO martian
VALUES
(NULL, 'Ray', 'Bradbury', 1, NULL),
(NULL, 'John', 'Black', 4, 10),
(NULL, 'Samuel', 'Hinkston', 4, 2),
(NULL, 'Jeff', 'Spender', 1, 9),
(NULL, 'Sam', 'Parkhill', 2, 12),
(NULL, 'Elma', 'Parkhill', 3, 8),
(NULL, 'Melissa', 'Lewis', 1, 1),
(NULL, 'Mark', 'Watney', 3, NULL),
(NULL, 'Beth', 'Johanssen', 1, 1),
(NULL, 'Chris', 'Beck', 4, NULL),
(NULL, 'Nathaniel', 'York', 4, 2),
(NULL, 'Elon', 'Musk', 2, NULL),
(NULL, 'John', 'Carter', NULL, 8);

CREATE TABLE base(
base_id INT AUTO_INCREMENT PRIMARY KEY,
base_name VARCHAR(30),
founded DATE);

INSERT INTO base
(base_id, base_name, founded)
VALUES
(NULL, 'Tharsisland', '2037-06-03'),
(NULL, 'Valles Marineris 2.0', '2040-12-01'),
(NULL, 'Gale Cratertown', '2041-08-16'),
(NULL, 'New New New York', '2042-02-10'),
(NULL, 'Olympus Mons Spa & Casino', NULL);

CREATE TABLE visitor
(
visitor_id INT AUTO_INCREMENT PRIMARY KEY,
host_id INT,
first_name VARCHAR(25),
last_name VARCHAR(25)
);

INSERT INTO visitor
(visitor_id, host_id, first_name, last_name)
VALUES
(NULL, 7, 'George', 'Ambrose'),
(NULL, 1, 'Kris', 'Cardenas'),
(NULL, 9, 'Priscilla', 'Lane'),
(NULL, 11, 'Jane', 'Thornton'),
(NULL, NULL, 'Doug', 'Stavenger'),
(NULL, NULL, 'Jamie', 'Waterman'),
(NULL, 8, 'Martin', 'Humphries');

CREATE TABLE inventory
(
base_id INT,
supply_id INT,
quantity INT
);

INSERT INTO inventory
(base_id, supply_id, quantity)
VALUES
(1, 1, 8),
(1, 3, 5),
(1, 5, 1),
(1, 6, 2),
(1, 8, 12),
(1, 9, 1),
(2, 4, 5),
(2, 8, 62),
(2, 10, 37),
(3, 2, 11),
(3, 7, 2),
(4, 10, 91);

CREATE TABLE supply
(
supply_id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(30),
description TEXT,
quantity INT
);

INSERT INTO supply
(supply_id, name, description, quantity)
VALUES
(NULL, 'Solar Panel', 'Standard 1x1 meter cell', 912),
(NULL, 'Water Filter', 'This takes things out of your water so it''s drinkable.', 6),
(NULL, 'Duct Tape', 'A 10 meeter roll of duct tape for ALL your repairs', 951),
(NULL, 'Ketchup', 'It''s ketchup', 206),
(NULL, 'Battery Cell', 'Standard 1000 kAH battery cell for power grid (heavy item).', 17),
(NULL, 'USB 6.0 Cable', 'Carbon fiber cooated / 10 TBps spool', 42),
(NULL, 'Fuzzy Duster', 'It gets dusty around here. Be prepared!', 19),
(NULL, 'Mars Bars', 'The ORIGINAL nutirent bar made with the finest bioengineered ingredients.', 3801),
(NULL, 'Air Filter', 'Removes 99% of all Martian dust from your ventilation unit', 23),
(NULL, 'Famous Ray''s Frozen Pizza', 'This Martian favourite is covered in all your favourite toppings. 1 flavour only.', 823);

CREATE TABLE martian_confidential
(
martian_id INT AUTO_INCREMENT PRIMARY KEY,
first_name VARCHAR(25),
last_name VARCHAR(25),
base_id INT,
super_id INT,
salary INT,
dna_id VARCHAR(30)
);

INSERT INTO martian_confidential
(martian_id, first_name, last_name, base_id, super_id, salary, dna_id)
VALUES
(NULL, 'Ray', 'Bradbury', 1, NULL, 155900, 'gctaggaatgtagaatctcctgttg'),
(NULL, 'John', 'Black', 4, 10, 120100, 'cagttaatggttgaagctggggatt'),
(NULL, 'Samuel', 'Hinkston', 4, 2, 110000, 'cgaagcgctagatgctgtgttgtag'),
(NULL, 'Jeff', 'Spender', 1, 9, 10000, 'gactaatgtcttcgtggattgcaga'),
(NULL, 'Sam', 'Parkhill', 2, 12, 125000, 'gttactttgcgaaagccgtggctac'),
(NULL, 'Elma', 'Parkhill', 3, 8, 137000, 'gcaggaatggaagcaactgccatat'),
(NULL, 'Melissa', 'Lewis', 1, 1, 145250, 'cttcgatcgtcaatggagttccggac'),
(NULL, 'Mark', 'Watney', 3, NULL, 121100, 'gacacgaggcgaactatgtcgcggc'),
(NULL, 'Beth', 'Johanssen', 1, 1, 130000, 'cttagactaggtgtgaaacccgtta'),
(NULL, 'Chris', 'Beck', 4, NULL, 125000, 'gggggggttacgacgaggaatccat'),
(NULL, 'Nathaniel', 'York', 4, 2, 105000, 'ggtctccctgggcgggatattggatg'),
(NULL, 'Elon', 'Musk', 2, NULL, 155800, 'atctgcttggatcaatagcgctgcg'),
(NULL, 'John', 'Carter', NULL, 8, 129500, 'ccaatcgtgcgagtcgcgatagtct');
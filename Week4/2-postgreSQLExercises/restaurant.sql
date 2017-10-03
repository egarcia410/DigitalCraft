CREATE TABLE restaurant (
	id SERIAL NOT NULL PRIMARY KEY,
	name VARCHAR,
	distance INTEGER,
	stars INTEGER DEFAULT 0 CHECK (stars > 0 AND stars <= 5),
	category VARCHAR,
	favorite VARCHAR,
	takeout BOOLEAN,
	prev_time DATE
);

--

INSERT INTO restaurant VALUES (
	DEFAULT,
	'85C Bakery Cafe',
	15,
	4,
	'Dessert',
	'Sea Salt Coffee',
	FALSE,
	'2017-08-20'
);

--

INSERT INTO restaurant VALUES (
	DEFAULT,
	'Alice Blue',
	8,
	3,
	'Mediterranean',
	'Gyro',
	FALSE,
	'2017-07-15'
);

--

INSERT INTO restaurant VALUES (
	DEFAULT,
	'Bernie''s Burger Bus',
	9,
	4,
	'Burgers',
	'Bacon Burger',
	TRUE,
	'2017-09-30'
);

--

INSERT INTO restaurant VALUES (
	DEFAULT,
	'Sonny''s',
	3,
	5,
	'BBQ',
	'BBQ Brisket',
	TRUE,
	'2017-09-30'
);

INSERT INTO restaurant VALUES (
	DEFAULT,
	'Benjy''s',
	8,
	4,
	'Pizza',
	'Wood-fired pizzas',
	TRUE,
	'2017-09-25'
);

--

INSERT INTO restaurant VALUES (
	DEFAULT,
	'Blue Nile',
	10,
	3,
	'Ethiopian',
	'Kifto',
	FALSE,
	'2017-10-02'
);

--

INSERT INTO restaurant VALUES (
	DEFAULT,
	'Himalaya',
	12,
	2,
	'Pakistani',
	'Gulab Juman',
	TRUE,
	'2017-06-08'
);

--

INSERT INTO restaurant VALUES (
	DEFAULT,
	'Izakaya',
	3,
	5,
	'Japanese',
	'Bacon-fried mochi',
	FALSE,
	'2017-09-27'
);

--

INSERT INTO restaurant VALUES (
	DEFAULT,
	'Moon Tower',
	1,
	3,
	'Burgers',
	'Chong Burger',
	TRUE,
	'2017-09-26'
);

--

SELECT name FROM restaurantWHERE stars >= 5;

--

SELECT favorite FROM restaurant;

--

SELECT id FROM restaurant 
WHERE name = 'Moon Tower';

--

SELECT name FROM restaurant
WHERE category = 'BBQ'; 

--

SElECT name FROM restaurant 
WHERE takeout = TRUE;

--

SELECT name FROM restaurant
WHERE category = 'BBQ' AND takeout = TRUE; 

--

SELECT name FROM restaurant 
WHERE distance <= 2;

--

SELECT name FROM restaurant 
WHERE prev_time < (current_date - 7);

--

SELECT name FROM restaurant 
WHERE prev_time < (current_date - 7) AND stars = 5;


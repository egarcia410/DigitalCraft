# Restaurant DB V2

## Getting Started

1. Enter psql shell:

        $ psql

2. Create `projects_db` database:

        =# CREATE DATABASE restaurant;

3. Exit psql shell:

        =# \q

4. Clone Repository:

        $ git clone https://github.com/egarcia410/digitalCraft.git

5. Change Directory:

        $ cd /digitalCraft/Week4/5-restaurantDB

6. In terminal, restore databse:

        $ psql restaurant -f restaurant.sql

## Table

For version 2 of the restaurant database, you will have the following tables:

* restaurant
* reviewer
* review

A reviewer could write any number of reviews for any number of restaurants.

The restaurant table has these columns:

* id
* name
* address
* category

The reviewer table would have these columns:

* id
* name
* email
* karma - between 0 to 7 (please use a constraint)

The review table would have these columns:

* id
* reviewer id (please use a foreign key constraint)
* stars - 1 to 5 stars (please use a constraint)
* title
* review - the text of the review
* restaurant id (please use a foreighn key constraint)

## Create Schema

Create these table schemas by writing CREATE statements in a .sql file and loading them in using something like `psql restaurant -f restaurant.sql` (this command assumes your database is called restaurant and your file is restaurant.sql).

## Enter Data

Enter some data for restaurants by either writing insert statements or through the Postico UI.

## Answer These Questions With a Query

1. List all the reviews for a given restaurant given a specific restaurant ID.
2. List all the reviews for a given restaurant, given a specific restaurant name.
3. List all the reviews for a given reviewer, given a specific author name.
4. List all the reviews along with the restaurant they were written for. In the query result, select the restaurant name and the review text.
5. Get the average stars by restaurant. The result should have the restaurant name and its average star rating.
6. Get the number of reviews written for each restaurant. The result should have the restaurant name and its review count.
7. List all the reviews along with the restaurant, and the reviewer's name. The result should have the restaurant name, the review text, and the reviewer name. Hint: you will need to do a three-way join - i.e. joining all three tables together.
8. Get the average stars given by each reviewer. (reviewer name, average star rating)
9. Get the lowest star rating given by each reviewer. (reviewer name, lowest star rating)
10. Get the number of restaurants in each category. (category name, restaurant count)
11. Get number of 5 star reviews given by restaurant. (restaurant name, 5-star count)
12. Get the average star rating for a food category. (category name, average star rating)



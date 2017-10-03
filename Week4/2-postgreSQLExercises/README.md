# PostgreSQL Exercises

## Create Database

Create a database, call it `restaurant`. In your terminal:
        $ createdb restaurant

## Create Database Table

Write a database schema: create a `restaurant.sql` file, in it write a CREATE TABLE statement to create a table called `restaurant`. This table will contain the following information, you will use the appropriate data types to represent the info. Please use an auto-incrementing primary key ID:

* name
* distance (in miles from HeadQuarters)
* stars
* category (type of food)
* favorite dish
* does takeout?
* last time you ate there

Run your file one of two ways:

1. Copy the "CREATE TABLE" statement and paste it into the PostgreSQL shell
2. `psql restaurant -f restaurant.sql`

If the table has been created successfully, you should see "CREATE TABLE" being printed. You can also describe the table schema in the shell using the \d command:

        restaurant=# \d restaurant

## Insert Data

Write INSERT statements to enter data into the restaurant table. You can paste the statements into the psql shell.

## Writing Queries

Write queries to get

1. The names of the restaurants that you gave a 5 stars to
2. The favorite dishes of all 5-star restaurants
3. The the id of a restaurant by a specific restaurant name, say 'Moon Tower'
4. restaurants in the category of 'BBQ'
5. restaurants that do take out
6. restaurants that do take out and is in the category of 'BBQ'
7. restaurants within 2 miles
8. restaurants you haven't ate at in the last week
9. restaurants you haven't ate at in the last week and has 5 stars
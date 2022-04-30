# Programming Principles 2

***Lab exercises***

## Lab 1

**Topics covered in this lab work:**

* ejudge

## Lab 2

**Topics covered in this lab work:**

* ejudge 2

## Lab 3

**Topics covered in this lab work:**

* Python Functions
* Python Lambda
* Python Classes and Objects
* Python Inheritance

## Lab 4

**Topics covered in this lab work:**

* Python Iterators, Generators
* Python Scope
* Python Modules
* Python Dates
* Python Math
* Python JSON

## Lab 5

**Topics covered in this lab work:**

* Python RegEx

## Lab 6

**Topics covered in this lab work:**

* Directories and files.
* Python File Handling: Read, Write, Create and Delete
* Working with directories
* Builtin function of python.

## Lab 7

### Learn tutorial: <https://nerdparadise.com/programming/pygame>

* Getting Started
* Working with Images
* Music and Sound Effects
* Geometric Drawing
* Fonts and Text
* More on Input

1. Create a simple clock application (only with minutes and seconds) which is synchronized with system clock. Use Mickey's right hand as minutes arrow and left - as seconds. For moving Mickey's hands you can use:
      ```pygame.transform.rotate```
more explanation: <https://stackoverflow.com/a/54714144>
2. Create music player with keyboard controller. You have to be able to press keyboard: play, stop, next and previous as some keys. Player has to react to the given command appropriately.
3. Draw circle - a red ball of size 50 x 50 (radius = 25) on white background. When user presses Up, Down, Left, Right arrow keys on keyboard, the ball should move by 20 pixels in the direction of pressed key. The ball should not leave the screen, i.e. user input that leads the ball to leave of the screen should be ignored

## Lab 8

### 1. Racer

Extend example project from lecture and finish following tutorials:

* <https://coderslegacy.com/python/python-pygame-tutorial/>
* <https://coderslegacy.com/python/pygame-tutorial-part-2/>
* <https://coderslegacy.com/python/pygame-tutorial-part-3/>

Extra tasks to the given tutorial:

1. Adding randomly appearing coins on the road
2. Showing the number of collected coins in the top right corner
3. Comment your code

### 2. Snake

Extend example project from lecture and add the following functionality:

1. Checking for border (wall) collision and whether the snake is leaving the playing area
2. Generate random position for food, so that it does not fall on a wall or a snake
3. Add levels. For example, when the snake receives 3-4 foods or depending on score
4. Increase speed when the user passes to the next level
5. Add counter to score and level
6. Comment your code

### 3 Paint

Extend example project from <https://nerdparadise.com/programming/pygame/part6> and add the following functionality:

1. Draw rectangle
2. Draw circle
3. Eraser
4. Color selection

## Lab 9

### 1.Racer

Extend example project from Lab 8 and add following tasks:
Extra tasks to the given tutorial:

1. Randomly generating coins with different weights on the road
2. Increase the speed of Enemy when the player earns `N` coins
3. Comment your code

### 2.Snake

Extend example project from Lab 8 and add following tasks:

1. Randomly generating food with different weights
2. Foods which are disappearing after some time(timer)
3. Comment your code

### 3.Paint

Extend example project from Lab 8 and add following tasks:

1. Draw square
2. Draw right triangle
3. Draw equilateral triangle
4. Draw rhombus
5. Comment your code

## Lab 10

### 1. Based on PostgreSQL tutorial create PhoneBook

1. Design tables for PhoneBook.
2. Implement two ways of inserting data into the PhoneBook.
    * upload data from csv file
    * entering user name, phone from console  
3. Implement updating data in the table (change user first name or phone)
4. Querying data from the tables (with different filters)
5. Implement deleting data from tables by username of phone

### 2. User and his score in snake game

1. Create user and user_score tables.
2. Before starting snake game, user should enter his username
3. If user exists, you should show current level of user. (You should create several levels, with different walls, speed etc.)
4. Implement shortcut for pause and save your current state and score to database.

## Lab 11

### 1. Based on previous task 'PhoneBook' implement following, using functions

1. Function that returns all records based on a pattern (example of pattern: part of name, surname, phone number)
2. Create procedure to insert new user by name and phone, update phone if user already exists
3. Create procedure to insert many new users by list of name and phone. Use loop and if statement in stored procedure. Check correctness of phone in procedure and return all incorrect data.
4. Create function to querying data from the tables with pagination (by limit and offset)
5. Implement procedure to deleting data from tables by username or phone

# Programming Principles 2

***Lab exercises***

## Lab 1

**Topics covered in this lab work:**
ejudge

## Lab 2

**Topics covered in this lab work:**
ejudge 2

## Lab 3

**Topics covered in this lab work:**
Python Functions,
Python Lambda,
Python Classes and Objects,
Python Inheritance

## Lab 4

**Topics covered in this lab work:**
Python Iterators, Generators
Python Scope
Python Modules
Python Dates
Python Math
Python JSON

## Lab 5

**Topics covered in this lab work:**
Python RegEx

## Lab 6

**Topics covered in this lab work:**
Directories and files.

Python File Handling: Read, Write, Create and Delete
Working with directories
Builtin function of python.

## Lab 7

<<<<<<< HEAD
* Learn tutorial: <https://nerdparadise.com/programming/pygame>: *Getting Started* Working with Images *Music and Sound Effects* Geometric Drawing *Fonts and Text* More on Input
=======
1. Learn tutorial: <https://nerdparadise.com/programming/pygame>: *Getting Started* Working with Images *Music and Sound Effects* Geometric Drawing *Fonts and Text* More on Input
>>>>>>> bd1a3b612c18912360cf908713ee65f57e336d3f

Create a simple clock application (only with minutes and seconds) which is synchronized with system clock. Use Mickey's right hand as minutes arrow and left - as seconds. For moving Mickey's hands you can use: pygame.transform.rotate more explanation: <https://stackoverflow.com/a/54714144>

![Caption](https://github.com/Beisenbek/programming-principles-2/raw/main/Lab07/images/mickeyclock.jpeg)

<<<<<<< HEAD
* Create music player with keyboard controller. You have to be able to press keyboard: play, stop, next and previous as some keys. Player has to react to the given command appropriately.

* Draw circle - a red ball of size 50 x 50 (radius = 25) on white background. When user presses Up, Down, Left, Right arrow keys on keyboard, the ball should move by 20 pixels in the direction of pressed key. The ball should not leave the screen, i.e. user input that leads the ball to leave of the screen should be ignored
=======
1. Create music player with keyboard controller. You have to be able to press keyboard: play, stop, next and previous as some keys. Player has to react to the given command appropriately.

1. Draw circle - a red ball of size 50 x 50 (radius = 25) on white background. When user presses Up, Down, Left, Right arrow keys on keyboard, the ball should move by 20 pixels in the direction of pressed key. The ball should not leave the screen, i.e. user input that leads the ball to leave of the screen should be ignored
>>>>>>> bd1a3b612c18912360cf908713ee65f57e336d3f

## Lab 8

1. Racer
Extend example project from lecture and finish following tutorials:

<https://coderslegacy.com/python/python-pygame-tutorial/>
<https://coderslegacy.com/python/pygame-tutorial-part-2/>
<https://coderslegacy.com/python/pygame-tutorial-part-3/>
Extra tasks to the given tutorial:

Adding randomly appearing coins on the road
Showing the number of collected coins in the top right corner
Comment your code
2. Snake
Extend example project from lecture and add the following functionality:

Checking for border (wall) collision and whether the snake is leaving the playing area
Generate random position for food, so that it does not fall on a wall or a snake
Add levels. For example, when the snake receives 3-4 foods or depending on score
Increase speed when the user passes to the next level
Add counter to score and level
Comment your code
3. Paint.
Extend example project from <https://nerdparadise.com/programming/pygame/part6> and add the following functionality:

Draw rectangle
Draw circle
Eraser
Color selection

## Lab 9

1. Racer
Extend example project from Lab 8 and add following tasks: Extra tasks to the given tutorial:

Randomly generating coins with different weights on the road
Increase the speed of Enemy when the player earns N coins
Comment your code
2. Snake
Extend example project from Lab 8 and add following tasks:

Randomly generating food with different weights
Foods which are disappearing after some time(timer)
Comment your code
3. Paint.
Extend example project from Lab 8 and add following tasks:

Draw square
Draw right triangle
Draw equilateral triangle
Draw rhombus
Comment your code

## Lab 10

1. Based on PostgreSQL tutorial create PhoneBook:
Design tables for PhoneBook.
Implement two ways of inserting data into the PhoneBook.
upload data from csv file
entering user name, phone from console
Implement updating data in the table (change user first name or phone)
Querying data from the tables (with different filters)
Implement deleting data from tables by username of phone
2. User and his score in snake game.
Create user and user_score tables.
Before starting snake game, user should enter his username
If user exists, you should show current level of user. (You should create several levels, with different walls, speed etc.)
Implement shortcut for pause and save your current state and score to database.

## Lab 11

1. Based on previous task 'PhoneBook' implement following, using functions:
Function that returns all records based on a pattern (example of pattern: part of name, surname, phone number)
Create procedure to insert new user by name and phone, update phone if user already exists
Create procedure to insert many new users by list of name and phone. Use loop and if statement in stored procedure. Check correctness of phone in procedure and return all incorrect data.
Create function to querying data from the tables with pagination (by limit and offset)
Implement procedure to deleting data from tables by username or phone

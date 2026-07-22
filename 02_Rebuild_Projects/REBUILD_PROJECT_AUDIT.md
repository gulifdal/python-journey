# Python Rebuild Projects — Development Audit

**Developer:** Gül İfdal ALDEMİR
**Project Area:** Python Journey — Rebuild Projects
**Status:** Active Learning and Future Improvement Planning

---

## About This Document

I created this document to review the six Python projects I previously completed and to understand how I can improve them throughout my Python learning journey.

I originally completed all six projects during my school years as assignments or projects. At that time, my main goal was to complete the projects as quickly as possible. I was able to make the programs work, but I did not fully understand all of the Python concepts behind the code.

Now I am returning to these projects with a different approach.

This time, my goal is not simply to write working code.

My goal is to understand why the code works, learn the Python concepts behind each project, practice writing code independently, and gradually improve these projects as my knowledge grows.

For this reason, I am not trying to immediately rewrite everything or make the projects look more advanced than they currently are.

The current versions represent my understanding at this stage of my learning journey.

As I learn new Python concepts, I will return to these projects and identify areas where I can apply my new knowledge.

This document exists to help me track that process.

---

# Current Rebuild Projects

The current Rebuild Projects area contains six main Python projects:

1. Temperature Converter
2. Guess the Secret Number Game
3. Mini Shopping Cart
4. IBU Grade Calculator
5. Word Counter
6. Simple Calculator

Each project focuses on different Python concepts.

When viewed together, these projects show the progression of my Python learning journey.

The earlier projects focus on fundamental concepts, while the later projects introduce lists, loops, string processing, functions, input validation, and error handling.

---

# Project 1 — Temperature Converter

This project is one of my exercises for practicing basic input, variables, type conversion, and arithmetic operations in Python.

The program asks the user for a temperature and performs a conversion based on the selected option.

The current version supports two conversions:

* Celsius to Fahrenheit
* Fahrenheit to Celsius

## Main Concepts

* Variables
* User input
* Type conversion
* float
* Arithmetic operations
* Conditional statements
* Menu-based interaction
* Formatted output

This project helped me reinforce how to receive input from the user, convert the input into the appropriate data type, and use that data in mathematical operations.

The menu structure also introduced a simple form of user-driven program flow.

## Possible Future Improvements

As I gain more experience with functions, I can separate the conversion operations into individual functions.

A possible future structure could be:

```text
Temperature Converter
│
├── Celsius to Fahrenheit Function
├── Fahrenheit to Celsius Function
├── Menu Function
└── Main Program Flow
```

Possible future improvements include:

* Functions
* Input validation
* Error handling
* Additional temperature units
* Cleaner program structure

For now, I am keeping the current version as it is.

I see this project as a reference point for my current understanding of basic Python concepts.

---

# Project 2 — Guess the Secret Number Game

This project is one of my exercises for understanding program flow and loops in Python.

The computer generates a random number, and the user tries to guess it.

The user has a limited number of attempts, and the program provides feedback after each guess.

The user can also choose to play the game again.

## Main Concepts

* random
* random.randint()
* while loops
* for loops
* range()
* Conditional statements
* break
* continue
* User input
* Program flow

This project helped me understand how loops and conditional statements can work together within the same program.

The program uses multiple control structures to manage the game, track attempts, provide feedback, and control the overall flow.

## Possible Future Improvements

As I become more comfortable with functions, I can separate different parts of the game into reusable functions.

A possible future structure could be:

```text
Guessing Game
│
├── Generate Secret Number
├── Get User Guess
├── Check Guess
├── Display Feedback
├── Play Game
└── Restart Game
```

Possible future improvements include:

* Functions
* Input validation
* Exception handling
* Difficulty levels
* Score tracking
* Number of rounds
* Game statistics

For now, I am keeping the current version.

I can return to this project later when I have learned more advanced Python concepts.

---

# Project 3 — Mini Shopping Cart

This project is one of my exercises for collecting multiple pieces of information and storing them in Python lists.

The user enters a product name and price.

The information is stored in lists, and the program displays the products and calculates the total cost at the end.

## Main Concepts

* Lists
* append()
* while loops
* for loops
* range()
* len()
* sum()
* User input
* Data collection

This project helped me understand the relationship between lists and loops.

It also gave me practice working with multiple pieces of related data and performing calculations using collected information.

## Possible Future Improvements

As I learn more about functions and data structures, I can separate different operations into individual functions.

A possible future structure could be:

```text
Shopping Cart
│
├── Add Product
├── Display Cart
├── Calculate Total
└── Main Program Flow
```

Possible future improvements include:

* Functions
* Dictionaries
* Input validation
* Error handling
* Product quantities
* Discounts
* Tax calculations
* File handling

For now, I am keeping the current version as it is.

This project will be a useful project to revisit when I have a stronger understanding of functions and dictionaries.

---

# Project 4 — IBU Grade Calculator

This project applies Python calculations and conditional logic to a more realistic academic situation.

The program asks the user for activity, midterm, and final grades.

It then calculates the semester score, checks whether the student is eligible to take the final exam, calculates the total course grade, determines the numerical grade, and displays the final academic status.

## Main Concepts

* Variables
* User input
* Type conversion
* Arithmetic operations
* Weighted calculations
* Conditional statements
* Nested logic
* Formatted output

This project helped me understand how multiple decisions can be connected within a single program.

The program does not perform only one calculation.

It first checks one condition, then performs another calculation based on that result, and finally determines the student's academic status based on additional conditions.

## Possible Future Improvements

As I gain more experience with functions, I can separate the different calculation and decision stages.

A possible future structure could be:

```text
IBU Grade Calculator
│
├── Calculate Semester Score
├── Check Final Eligibility
├── Calculate Course Average
├── Determine Numerical Grade
├── Determine Final Status
└── Display Academic Report
```

Possible future improvements include:

* Functions
* Input validation
* Error handling
* Dictionaries
* More flexible grading systems
* Student record management

For now, I am keeping the current version.

I can revisit this project later when I have a stronger understanding of functions and data structures.

---

# Project 5 — Word Counter

This project is one of my exercises for practicing string processing and working with user-provided text.

The program asks the user to enter a sentence and then analyzes the text.

The program calculates:

* Number of words
* Number of characters
* Longest word
* Total number of letters
* Average word length

## Main Concepts

* Strings
* input()
* split()
* len()
* for loops
* Variables
* String processing
* Calculations

This project helped me practice working with strings and processing user input.

It also introduced me to breaking text into smaller parts and analyzing those parts using loops and calculations.

## Possible Future Improvements

As I learn more about functions and string processing, I can separate the different analysis operations into individual functions.

A possible future structure could be:

```text
Word Counter
│
├── Count Words
├── Count Characters
├── Find Longest Word
├── Calculate Average Word Length
└── Display Results
```

Possible future improvements include:

* Functions
* Dictionaries
* Advanced string processing
* File handling
* Text statistics
* Better punctuation handling

For now, I am keeping the current version.

I can revisit this project later when I have a stronger understanding of functions and more advanced string processing.

---

# Project 6 — Simple Calculator

This project is currently one of the most structured projects in my rebuild project set.

In this project, I separated mathematical operations into individual functions.

The calculator currently supports:

* Addition
* Subtraction
* Multiplication
* Division
* Power
* Modulus

The program also includes basic input handling and error control for certain situations.

## Main Concepts

* Functions
* Parameters
* Return values
* Conditional statements
* while loops
* Input validation
* try / except
* ValueError
* Mathematical operations
* Program structure

This project helped me understand why functions are important in Python.

Instead of placing every mathematical operation inside one large block of code, I separated each operation into its own function.

The current structure is approximately:

```text
Simple Calculator
│
├── add()
├── subtract()
├── multiply()
├── divide()
├── power()
├── modulus()
└── Main Program Flow
```

## Possible Future Improvements

As I continue learning Python, this project can be improved with:

* Better input validation
* Improved exception handling
* Cleaner program architecture
* Dictionaries
* Modules
* File handling
* Object-oriented programming

For now, I am keeping the current version.

This project can become an important reference point for applying more advanced Python concepts in the future.

---

# Function Integration Roadmap

As I continue focusing more on functions in my Python learning journey, I am beginning to see more clearly where functions could be useful in these six projects.

However, I will not change all of the projects at the same time.

I will revisit each project when I have actually learned and understood the relevant Python concept.

A possible future development direction could be:

```text
Temperature Converter
        ↓
Conversion Functions

Guessing Game
        ↓
Game Logic Functions

Shopping Cart
        ↓
Cart Management Functions

IBU Grade Calculator
        ↓
Calculation Functions

Word Counter
        ↓
Text Analysis Functions

Simple Calculator
        ↓
Already Uses Functions
        ↓
Future Refactoring
```

This is not a strict requirement.

The important thing for me is not to change my projects just to make them look more advanced.

Every future improvement should have a clear connection to something I have actually learned.

---

# My Improvement Strategy

My general process for improving these projects will be:

```text
LEARN
   ↓
UNDERSTAND
   ↓
PRACTICE
   ↓
IDENTIFY OPPORTUNITY
   ↓
RETURN TO PROJECT
   ↓
IMPROVE
   ↓
TEST
   ↓
COMPARE
```

When I learn a new Python concept, I will first focus on understanding it.

Then I will practice it through a small and independent exercise.

Once I understand the concept well enough, I can return to one of my previous projects and identify where the new knowledge could be applied.

This way, I will not change my code simply for the sake of changing it.

Each improvement will have a reason and a connection to something I have learned.

---

# My Current Development Rule

For now, I will preserve the current versions of all six projects.

These projects represent earlier stages of my Python learning journey.

I will not immediately rewrite them just to make them more advanced.

Instead, I will revisit a project when I have learned a new Python concept and believe that the concept can genuinely improve the project.

This will allow me to see my development over time.

The process will look like:

```text
Earlier Understanding
        ↓
New Knowledge
        ↓
Improved Implementation
```

Comparing older and newer versions will help me understand how much I have improved as a Python developer.

---

# Current Project Status

## Temperature Converter

**Status:** Preserved
**Current Focus:** Input, type conversion, calculations, and conditions
**Future Direction:** Functions and validation

## Guess the Secret Number Game

**Status:** Preserved
**Current Focus:** Loops, conditions, randomness, and program flow
**Future Direction:** Functions and improved game structure

## Mini Shopping Cart

**Status:** Preserved
**Current Focus:** Lists, iteration, and data collection
**Future Direction:** Functions and better data structures

## IBU Grade Calculator

**Status:** Preserved
**Current Focus:** Calculations, conditions, and decision logic
**Future Direction:** Functions and structured calculations

## Word Counter

**Status:** Preserved
**Current Focus:** Strings, loops, and text processing
**Future Direction:** Functions and more advanced text analysis

## Simple Calculator

**Status:** Preserved
**Current Focus:** Functions, validation, and error handling
**Future Direction:** Refactoring and more advanced program structure

---

# Long-Term Goal

These six projects will continue to develop as my Python knowledge grows.

My long-term goal is not to completely rewrite all of them at once.

Instead, I want to apply each new Python concept to my previous projects when it becomes relevant.

Over time, I will be able to compare different versions of the same projects.

Seeing the difference between my first implementation and a later improved version will help me understand how much my Python knowledge and programming skills have developed.

These projects are not just completed assignments from the past.

They are living learning materials that I can return to throughout my Python Journey.

---

# Development Philosophy

My goal with these projects is not to write perfect code on the first attempt.

My goal is to become a better developer by learning and practicing consistently.

The code I write today represents my current level of understanding.

As I learn more, I will be able to return to the same projects and improve them with better knowledge.

Because of this, I do not see these projects as permanently finished.

I see them as part of my ongoing Python Journey.

My process is:

**Learn → Rebuild → Practice → Understand → Improve**

---

# Final Perspective

These six projects have an important place in my Python learning journey.

I originally completed them during school as assignments and projects, mostly with the goal of finishing them quickly.

Now I am rebuilding and revisiting them with a different mindset.

This time, I want to understand what I am doing and strengthen my knowledge through practice.

For me, the goal is not only to make the programs work.

I also want to:

* Understand why the code works
* Understand the Python concepts I use
* Become more confident writing code independently
* Learn how to identify and solve problems
* Apply new Python concepts to previous projects
* Write cleaner and more structured code over time

These projects will serve as personal reference points throughout my Python Journey.

My code today does not have to look the same as my code in the future.

As I learn, my projects will grow with me.

**Learn deeply. Build independently. Improve continuously.**

---

# ==========================================

# End of Rebuild Project Development Audit

# ==========================================
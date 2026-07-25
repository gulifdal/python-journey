📖 Day 17–18 — Python Data Structures: Choosing the Right Structure
Date: July 24–25, 2026
Days: 17–18
Focus: Python Data Structures — Lists, Tuples, Sets, and Dictionaries
🌱 What I Worked On
During Day 17 and Day 18, I continued strengthening my Python fundamentals by focusing on one of the most important parts of programming: choosing the right data structure for the problem.
I studied and compared four fundamental Python data structures:

Lists
Tuples
Sets
Dictionaries
The goal was not only to learn the syntax of each structure.
I wanted to understand:

How each structure stores data
Whether the data is ordered
Whether the data can be changed
Whether duplicate values are allowed
When each structure should be used
How different structures can work together
This helped me move from simply learning Python syntax toward thinking about how data should be represented inside a program.
🧩 The Four Core Data Structures
The main idea I practiced was:

LIST
Ordered + Changeable
        ↓
TUPLE
Ordered + Fixed
        ↓
SET
Unique Values
        ↓
DICTIONARY
Key-Value Data
A simple decision system I practiced was:

If I need ordered and changeable data → LIST

If I need ordered and fixed data → TUPLE

If I need unique data → SET

If I need key-value data → DICTIONARY
This became one of the most useful summaries from these two learning days.
📋 Lists
I reviewed lists as ordered and changeable collections of data.
Lists are useful when:

Order matters.
I need to change the data.
I need to add or remove items.
Duplicate values are allowed.
For example:

skills = [
    "Mathematics",
    "Physics",
    "Problem Solving"
]
I can add, remove, and update items in a list.
This makes lists useful for collections of information that may change while a program is running.
Examples include:

Skills
Shopping items
Tasks
Names
Scores
User activities
📦 Tuples
I reviewed tuples as ordered collections that are intended to remain fixed.
Tuples are useful when:

Order matters.
The data should remain unchanged.
The information represents a fixed structure.
For example:

fixed_information = (
    "Gül's sister",
)
Unlike lists, tuples are not designed for changing individual items after creation.
This makes them useful for information that should remain stable.
🔵 Sets
I practiced sets as collections of unique values.
Sets are useful when:

Duplicate values should be removed.
I only care about unique data.
I do not need to access values using indexes.
For example:

programming_languages = {
    "Python",
    "C++"
}
A set automatically keeps only unique values.
This makes sets useful for situations such as:

Unique programming languages
Unique skills
Unique categories
Removing duplicate data
📚 Dictionaries
I connected the new topics with my previous learning from Day 16 — Dictionaries.
Dictionaries store information using key-value pairs.
For example:

student = {
    "name": "Gül",
    "age": 22,
    "goal": "AI Engineer"
}
Dictionaries are useful when I want to describe information using meaningful keys.
For example:

name → Gül
age → 22
goal → AI Engineer
This makes dictionaries especially useful for representing structured information such as:

Students
Users
Profiles
Products
Settings
Application data
🔗 Connecting Day 16 with Day 17–18
One of the most important parts of these two days was understanding that the topics are connected.
On Day 16, I learned dictionaries in greater depth.
On Day 17–18, I placed dictionaries alongside the other fundamental data structures.
This helped me understand the difference between:

List
Tuple
Set
Dictionary
I also realized that these structures are not competitors.
They can be used together.
For example, a dictionary can contain a list:

student = {
    "name": "Erva",
    "skills": [
        "Mathematics",
        "Physics",
        "Problem Solving"
    ]
}
A dictionary can also contain a set:

student = {
    "programming_languages": {
        "Python",
        "C++"
    }
}
This showed me how real programs can combine multiple data structures to represent more complex information.
🧪 Practice Project — Data Structure Challenge
After learning the concepts, I created a focused practice challenge.
The goal was to create a realistic student profile and intentionally use different Python data structures for different types of information.
I used my younger sister, Erva, as the example student.
Her profile included:

Name: Erva
Age: 16
Current Status: YKS Student
University Goal: Istanbul Technical University (ITU)
Department Goal: Aeronautical Engineering
The data structures were selected based on the type of information they represented.
📋 Dictionary — Student Profile
The main student information was stored in a dictionary:

student_data = {
    "name": "Erva",
    "age": 16,
    "current_status": "YKS Student",
    "university_goal": "Istanbul Technical University (ITU)",
    "department_goal": "Aeronautical Engineering"
}
The dictionary was appropriate because the information had meaningful labels.
📋 List — Skills
Erva's skills were stored in a list:

skills = [
    "Mathematics",
    "Physics",
    "Problem Solving",
    "Time Management",
    "Communication"
]
A list was appropriate because the skills were ordered and could change over time.
🔵 Set — Programming Languages
Programming languages were stored in a set:

programming_languages = {
    "Python",
    "C++"
}
A set was appropriate because programming languages should be unique values.
📦 Tuple — Fixed Information
Fixed information was stored in a tuple:

fixed_information = (
    "Gül's sister",
)
A tuple was appropriate because this information was intended to remain fixed.
🧠 What the Practice Challenge Taught Me
The most important lesson from the practice project was that choosing a data structure should depend on the problem.
Instead of thinking:

"Which Python data structure do I remember?"
I want to start thinking:

"What kind of data am I working with, and which structure represents it best?"
This is an important shift in my programming mindset.
🏗️ Data Structure Decision Making
I created a simple mental model that I can use when solving future problems.

Use a List when:
I need:
- Order
- Changeable data
- Duplicate values
Use a Tuple when:
I need:
- Order
- Fixed data
Use a Set when:
I need:
- Unique values
- No duplicates
Use a Dictionary when:
I need:
- Key-value relationships
- Meaningful labels
- Structured information
This decision-making process will become useful when I start building larger programs.
🧠 Connecting Data Structures with Real Programs
These two days helped me understand that data structures are the foundation of application data.
A real application might contain:

Dictionary
    ↓
User Profile

List
    ↓
User Skills

Set
    ↓
Unique Categories

Tuple
    ↓
Fixed Information
This means that learning data structures is not only about passing Python exercises.
It is about learning how to represent real-world information inside software.
🌷 Connection to GUL
I did not force a new GUL version during these two days.
Instead, I focused on understanding the data structures first.
This was an intentional decision.
GUL should grow alongside my understanding.
I do not want to add features simply because I learned a new Python concept.
I want to understand the concept, practice it independently, and then decide whether it naturally belongs in GUL.
The next time I improve GUL, I want the change to be meaningful rather than artificial.
This follows the development rhythm I established earlier:
LEARN → UNDERSTAND → PRACTICE → BUILD → APPLY → TEST → REFLECT → IMPROVE
♻️ Connection to Rebuild Projects
The data structure knowledge from Day 17–18 will also become useful for future Rebuild Projects.
My existing projects can eventually benefit from better data organization.
For example:

The IBU Grade Calculator may use dictionaries for student information.
The Mini Shopping Cart may use lists and dictionaries.
The Word Counter may use dictionaries to count word frequency.
The Simple Calculator may use functions and structured data as it becomes more advanced.
However, I will not rebuild these projects immediately just to use the new concepts.
I will revisit them when I understand enough to make meaningful improvements.
🧠 Biggest Lesson
My biggest lesson from Day 17–18 was:

Good programming is not only about knowing Python syntax. It is also about choosing the right structure for the data.
I am beginning to understand that programming involves making decisions.
The question is not only:

"How do I write this code?"
It is also:

"How should I organize this information?"
This is an important step toward becoming more independent as a programmer.
🚀 Progress During Day 17–18
During these two learning days, I:

Studied Python lists.
Reviewed how lists store ordered and changeable data.
Studied tuples.
Reviewed how tuples store ordered and fixed data.
Studied sets.
Practiced working with unique values.
Reviewed dictionaries from Day 16.
Compared the four main data structures.
Created a simple decision system for choosing data structures.
Created a Data Structure Challenge.
Used realistic student information.
Used Erva as the example student.
Practiced dictionaries for structured profile data.
Practiced lists for skills.
Practiced sets for programming languages.
Practiced tuples for fixed information.
Combined multiple data structures in one program.
Tested the practice project.
Connected the new concepts with previous learning.
Confirmed the project structure.
Committed the work.
Pushed the work to GitHub.
Confirmed that the working tree was clean.
🏗️ My Learning System
My learning system now looks like:

FOUNDATIONS
    ↓
LEARN
    ↓
UNDERSTAND
    ↓
PRACTICE
    ↓
REBUILD
    ↓
PERSONAL PROJECTS
    ↓
TEST
    ↓
COMMIT
    ↓
PUSH
    ↓
REFLECT
    ↓
IMPROVE
I am beginning to see Python Journey as a complete learning system rather than a simple list of topics.
Each stage has a purpose.
🗺️ Where I Am Now
My Python Journey currently looks like:

Topic 15
Functions, Parameters, Scope, Return Values
        ↓
Topic 16
Dictionaries
        ↓
Topic 17–18
Data Structures
        ↓
Lists
Tuples
Sets
Dictionaries
        ↓
Practice Challenge
        ↓
Data Structure Selection
        ↓
Day 19
Problem Solving + Practical Application
The topics are beginning to build naturally on top of each other.
This is exactly the kind of progression I want to maintain.
🌅 Preparing for Day 19
Day 19 will be the next stage of my Python Journey.
I want to shift slightly from:
Learning concepts
toward:
Using concepts to solve problems.
The focus will be on strengthening my ability to think through a problem before immediately writing code.
My process will be:

UNDERSTAND THE PROBLEM
        ↓
BREAK IT INTO PARTS
        ↓
CHOOSE THE RIGHT DATA STRUCTURE
        ↓
WRITE PSEUDOCODE
        ↓
TRY MY OWN SOLUTION
        ↓
TEST
        ↓
DEBUG
        ↓
IMPROVE
        ↓
REFLECT
This will help me become more independent and prepare me for larger projects.
🎯 Day 19 Goal
My main goal for Day 19 will be:

Use the Python concepts I have learned so far to solve small problems independently.
I want to practice combining:

Variables
Conditions
Loops
Functions
Lists
Tuples
Sets
Dictionaries
The goal will not be to write complicated code.
The goal will be to improve my problem-solving process.
I want to become more comfortable with starting from an empty file and thinking:

"How can I solve this problem myself?"
🌷 Personal Reflection
Day 17–18 felt like an important transition in my Python Journey.
I am moving beyond learning individual Python concepts and starting to think about how those concepts work together.
Lists, tuples, sets, and dictionaries are simple structures individually.
But when combined with functions, loops, conditions, and user input, they become powerful tools for building programs.
The most important thing I learned is that programming is about making choices.
I need to choose the right structure.
I need to organize information.
I need to break problems into smaller parts.
And I need to understand why my solution works.
This is the direction I want to continue following.
🩵 One Thing I Want to Remember
The better I understand my data, the better I can design my programs.
I am not trying to memorize every Python feature.
I am learning how to think like a programmer.
GUL grows as I grow.
Python Journey grows with me.
📌 Day 17–18 Status
Days: 17–18
Main Focus: Python Data Structures
Topics: Lists, Tuples, Sets, Dictionaries
Practice: Data Structure Challenge
Example Student: Erva
Age: 16
Current Status: YKS Student
University Goal: Istanbul Technical University (ITU)
Department Goal: Aeronautical Engineering
Main Lesson: Choosing the right data structure based on the problem
Repository Status: Complete and pushed to GitHub
Next Step: Day 19 — Problem Solving + Practical Application
Learn deeply. Choose intentionally. Solve independently. Build continuously.
This is my Python Journey.
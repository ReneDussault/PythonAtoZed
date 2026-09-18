# Python - A to Zed

## Complete Introduction to Python Programming

Welcome to **PythonAtoZed**!  
This introduction course takes you from Python basics to advanced concepts like Object-Oriented Programming, modules, and decorators.  
Whether you're a complete beginner or coming from another programming language, this course provides hands-on learning with practical examples, exercises, and **interactive quizzes**.

## How This Course Works

1. **theory/** the lectures. Work through `python-atozed.ipynb` section by section. [theory folder > python-atozed.ipynb](https://github.com/ReneDussault/PythonAtoZed/blob/main/theory/python-atozed.ipynb)
2. **homeworks/** practice problems matching each theory section, with solutions included. [homeworks folder](https://github.com/ReneDussault/PythonAtoZed/tree/main/homeworks)
3. **quizzes/** test what you learned after each section. [quizzes folder](https://github.com/ReneDussault/PythonAtoZed/tree/main/quizzes)

> **Note**: Recommended flow per section: theory notebook (lectures) → homework → quiz.

### What You'll Learn

- **Solid Foundation**: Python syntax, data types, and core concepts
- **Data Structures**: Work with lists, tuples, dictionaries, and sets
- **Control Flow**: Understand conditionals, loops, and program logic
- **Functions**: Write reusable code with functions and lambda expressions
- **Object-Oriented Programming**: Classes, inheritance, encapsulation, and polymorphism
- **Modules & Libraries**: Organize code and use Python's extensive ecosystem
- **BONUS**: Decorators

### Course Features

- **Beginner Friendly**: Starts with absolute basics
- **Progressive Learning**: Each section builds on previous knowledge
- **Practical Focus**: Every concept includes working code examples
- **Interactive Quizzes**: Test your knowledge with section-specific quizzes
- **Immediate Feedback**: Get instant results and explanations
- **Progress Tracking**: Monitor your learning with scoring and timing
- **Exercises & Summaries**: Reinforce learning with practice problems
- **Interactive**: Designed for Jupyter notebooks with immediate feedback
- **Comprehensive**: Covers everything needed for Python proficiency

## Quick Start (No Installation Required)

### Launch in MyBinder

Click the badge below to launch the course instantly in your browser:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ReneDussault/PythonAtoZed/HEAD)

**MyBinder** provides a free, interactive environment where you can:

- Run the course without installing anything
- No login needed
- Modify and experiment with code examples
- Take interactive quizzes to test your knowledge
- Save your progress (temporarily)
- Access from any device with a web browser
- [Optional] Settings > Theme > Dark Mode (at night, to save your eyes)

> **Note**: MyBinder sessions are temporary. Download your work if you want to keep changes.

---

## Local Setup (Recommended for Long-term Learning)

### Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [Visual Studio Code](https://code.visualstudio.com/)

### Installation Steps

1. **Clone this repository:**

   ```bash
   git clone https://github.com/ReneDussault/PythonAtoZed.git
   cd PythonAtoZed
   ```

2. **Install VS Code extensions:**
   These steps should be done inside VScode, but I'll provide links to the extensions to get you started.
   - [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
   - [Jupyter Extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

3. **Open the course:**
   - Launch VS Code
   - File > Open Folder > `python-AtoZed`
   - Open/expand the `theory` folder and open the `python-atozed.ipynb` file (double click)
   - Select your Python interpreter when prompted (after running a code cell)

4. **Start learning:**
   - Run code cells with `Ctrl+Enter` (keeps current cell selected) or `Shift+Enter` (moves to next cell)
   - Follow the course from start to finish or jump to specific topics using the table of contents

5. **Test your knowledge:**
   - Navigate to the `quizzes` folder
   - Run `python interactive_quiz_from_json.py` to access the quiz system
   - Choose from section-specific quizzes or take the comprehensive final exam

> **Note**: You can use any IDE that supports Python and Jupyter notebooks!

---

## Interactive Quiz System

### 🐍 Test Your Python Knowledge!

The course includes a comprehensive quiz system with:

#### **Available Quizzes:**

- **Section 1**: Basic Syntax (30 questions)
- **Section 2**: Data Structures (31 questions)
- **Section 3**: Flow Control (30 questions)
- **Section 4**: Functions (30 questions)
- **Section 5**: Object-Oriented Programming (30 questions)
- **Section 6**: Modules and Libraries (30 questions)
- **Final Quiz**: Comprehensive Assessment (181 questions)

#### **Features:**

- ✅ **Multiple Choice Questions** with instant feedback
- ✅ **Code Output Questions** to test practical understanding
- ✅ **True/False Questions** for concept verification
- ✅ **Progress Tracking** with scores and timing
- ✅ **Grade System** (A-F) based on performance
- ✅ **Terminal-based Interface** - no additional setup required

#### **How to Use:**

```bash
# Navigate to the quizzes folder
cd quizzes

# Run the JSON-based interactive quiz system
python interactive_quiz_from_json.py

# Choose a quiz (1-7) and start testing your knowledge!
```

#### **Sample Quiz Flow:**

```
Welcome to Section 1: Basic Syntax Quiz
========================================
Question 1:
Which of the following is the correct way to create a comment in Python?

a) // This is a comment
b) # This is a comment
c) /* This is a comment */
d) <!-- This is a comment -->

Your answer: b
✅ Correct!

Final Score: 12/13 (92.3%) - Grade: A - Excellent!
```

---

## Course Outline

**Introduction**

**Basic Syntax**

- Printing output with print()
- Commenting
- Multiline comment (docstring)
- Indentation
- Data Types and variables (integers, floats, strings, booleans)
- String Methods
- Basic Operators

**Data Structures**

- Lists, indexing, slicing
- List Methods
- List Comprehension
- Tuples and their immutability
- Dictionaries and key-value pairs
- Sets for unique values
- More Examples

**Flow Control**

- Conditional Statements (if, elif, else)
- For Loops
- While Loops
- Loop Control Statements
  - continue
  - break
  - pass
- Range and Enumerate Functions
- Summary of Flow Control

**Functions**

- Defining and Calling Functions
- Parameters and Arguments
- Return Statements
- Lambda Function

**Introduction to OOP**

- Classes and Objects
- The init Method (Constructor)
- Attributes and Methods
- Inheritance
- Encapsulation
- Polymorphism
- Composition
- Magic Methods

**Modules and Libraries**

- Importing Modules
- Standard Libraries
- Custom Modules
- Summary of Modules and Packages

**BONUS: Decorators**

- What is a Decorator?
- Built-in Decorators (@property, @classmethod, @staticmethod)
- Custom Function Decorators

---

## Contributing & Feedback

This is a work in progress.  
Found an issue or have suggestions? Please:

- [Create an issue](https://github.com/ReneDussault/python-AtoZed/issues)
- Submit a pull request
- Share your feedback

Your input helps make this course better for everyone!

---

## License

- **Code Examples, scripts, tools**: [MIT License](./LICENSE.txt)
- **Course Content**: [Creative Commons Attribution 4.0 International (CC BY 4.0)](./LICENSE_CC_BY.txt)

---

Happy coding! 🐍

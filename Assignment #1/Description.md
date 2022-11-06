**IF100 – Fall 2021-2022**

**Take-Home Exam 1**
**Due November 5**** th****, 2021, Friday, 23:59 (Sharp Deadline)**

**Introduction**

The aim of this take-home exam is to practice on the basics of programming. You will write a Python program to get some inputs from the user, do some arithmetic operations and display the result to the user as the output.

**Description**

Let's assume that we work in a small factory that produces tomato sauce. In the coming days, the factory wants to grow in business. While doing this, they want to adjust their operations in a way that every process will be optimized. For this reason, they want to make some observations on the required processes so that they would know what to change.

You are asked to write a Python program that will take the amount of tomato (in kg), boiling speed (rate at which a kg of tomato boiled in a second (kg/sec)), and liter of can as inputs; and display the time to boil all tomatoes as well as the number(s) of can(s) produced from the given amount of tomato (in kg) with leftovers (which is the uncanned tomato sauce) together with the leftover's price.

In the boiling process, tomatoes lose their water and only **20 percent is left as pulp** (which is used to make the sauce). Boiling speed (rate at which a kg of tomato boiled in a second (kg/sec)) may change. Because of this, you are asked to take the boiling speed as an input.

At the same time, you will also be trying to reduce the leftovers, that's why you are asked to take the can liter as an input.

The price of the leftovers is fixed, which is **0.02 Turkish Liras per gram**.

**Inputs**

The program that you will develop needs to take a total of 3 inputs from the user:

1. Amount of tomatoes that is purchased from the supplier in kilogram,
2. Boiling speed in kilogram per second,
3. Can volume in liters.

You may assume that the user will always enter positive numeric values for all of these inputs.

You may assume that **1 liter of can is filled up with 1 kilogram of sauce**.

**Output**

Your program needs to calculate and display the elapsed time, produced can number, and leftovers with its cost. The output of your program should be exactly in the following format:

_can\_number_ _number(s) of can is produced._

_h_ _hour(s)_ _m_ _minute(s)_ _s_ _second(s) is taken._

_Leftover amount is_ _leftover__kg. You can purchase the leftover by giving_ _cost_ _TL._

Your program should calculate six numbers (_can\_number_, _h_, _m __,__ s __,_ _leftover__ ,_ _cost_) for its output_._ If one of these results is 0, your program should also print that.

Please note that _can\_number__,_ _h_ and _m_ values must be displayed as integers (without any precision), and _s__,_ _leftover__,_ _cost_values must be displayed as a real number _with exactly two decimal places_ (_Hint_: use _ **format** _ function that was explained in the recitation materials).

You may check the "Sample Runs" section given below for some examples.

**Sample Runs**

Below, we provide some sample runs of the program that you will develop. The _italic_ and **bold** phrases are inputs taken from the user. You have to display the required information in the same order and with the same words and characters as below.

 **Sample Run 1**

Please enter the amount of tomatoes (in kg) that you have: **3000**

Please enter the boiling speed (rate at which a kg of tomato boiled in a second (kg/sec)): **0.26**

Please enter the volume of a can: **2.56**

234 number(s) of can is produced.

3 hour(s) 12 minute(s) 18.46 second(s) is taken.

Leftover amount is 0.96kg. You can purchase the leftover by giving 19.20 TL.

**Sample Run 2**

Please enter the amount of tomatoes (in kg) that you have: **2000**

Please enter the boiling speed (rate at which a kg of tomato boiled in a second (kg/sec)): **0.15**

Please enter the volume of a can: **2**

200 number(s) of can is produced.

3 hour(s) 42 minute(s) 13.33 second(s) is taken.

Leftover amount is 0.00kg. You can purchase the leftover by giving 0.00 TL.

**Sample Run 3**

Please enter the amount of tomatoes (in kg) that you have: **200.5**

Please enter the boiling speed (rate at which a kg of tomato boiled in a second (kg/sec)): **4**

Please enter the volume of a can: **2.45**

16 number(s) of can is produced.

0 hour(s) 0 minute(s) 50.12 second(s) is taken.

Leftover amount is 0.90kg. You can purchase the leftover by giving 18.00 TL.

**What and where to submit?**

You should prepare (or at least test) your program using Python 3.x.x. We will use Python 3.x.x while testing your take-home exam. Let us repeat,

- You **must** use Google Colab to develop your code from scratch (from beginning till the end), and then submit it **through SUCourse+ only**! Once you are done with developing your code on Google Colab, then you will copy your code to CodeRunner to see if your program can produce the correct outputs. At the end, you will submit your code through CodeRunner (on SUCourse+). You should keep your Google Colab file until the end of the semester, we might want to look at this. _ **If you fail to provide this Google Colab file anytime in the semester, you may not earn any credits from this Take Home Exam.** _

- In CodeRunner, there are some visible and invisible (hidden) test cases. You will see your final grade (including hidden test cases) before submitting your code. Thus, it will be possible to know your THE grade before submitting your solution.

- There is no re-submission. You don't have to complete your task in one time, you can continue from where you left last time but you should not press submit before finalizing it. Therefore, you should make sure that it's your final solution version before you submit it.

-
- **General Take-Home Exam Rules**

- Successful submission is one of the requirements of the take-home exam. If, for some reason, you cannot successfully submit your take-home exam and we cannot grade it, your grade will be 0.
- There is NO late submission. You need to submit your take-home exam before the deadline. Please be careful that SUCourse+ time and your computer time may have 1-2 minutes differences. You need to take this time difference into consideration.
- Do NOT submit your take-home exam via email or in hardcopy! SUCourse+ is the only way that you can submit your take-home exam.
- If your code does not work because of a syntax error, then we cannot grade it; and thus, your grade will be 0.
- Please submit your **own** work only. It is really easy to find "similar" programs!
- Plagiarism will not be tolerated. Please check our plagiarism policy given in the syllabus of the course.

Good luck!

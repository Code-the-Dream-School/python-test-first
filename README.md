Test First Python
==========

### Set up instructions

1. Clone this repo as usual
2. On your local machine, `cd` into the root folder of this repo in your terminal
3. run `pip install -r requirements_dev.txt` to install the Python packages this project needs.
4. Make a git branch called testfirst-lesson and do the coding for these exercises in that branch.
5. Do a `code .` to start vscode.  You will see several directories, including 00_hello.  Inside
that directory is an index.html.  Open that up in your browser to see the instructions you must
follow to complete the assignment.

### Getting started with the exercises

In general, for each part of the assignment, you will change to the corresponding directory, 00_hello
through 06_timer.  Then, once in the directory, you run ```pytest -x test.py``` to test the code.
Then, you make changes to the other Python file in that directory until the test passes.

When you have completed all six exercises, push your changes to github as usual, and issue a pull request.

Basically, this is "error-driven development"... you'll keep running tests, hitting error messages, fixing those messages, running more tests...  It is meant to not only test your Python skills but also get you comfortable seeing big scary looking stack traces and error messages.  Most of the development you do at first will be just like this.  In fact, most of *all* development is error-driven.  So get comfortable with it!

### Credit
This Python exercise is derived from one for Ruby: https://github.com/TheOdinProject/learn_ruby
The latter is forked from [https://github.com/alexch/learn_ruby](https://github.com/alexch/learn_ruby), its original creator.

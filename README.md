Test First Python
==========

### Set up instructions

1. Clone this repo as usual
2. On your local machine, `cd` into the root folder of this repo in your terminal
3. Run `pip install -r requirements_dev.txt` to install the Python packages this project needs.
4. Make a git branch called testfirst-lesson and do the coding for these exercises in that branch.
5. Do a `code .` to start vscode.  You will see several directories, including 00_hello, each corresponding to an exercise.

### Getting started with the exercises

In general, for each part of the assignment, you will change to the corresponding directory, 00_hello
through 06_timer.  Then, once in the directory, you run ```pytest -x test.py``` to test the code.
Then, you make changes to the other Python file in that directory until the test passes.

When you have completed all six exercises, push your changes to github as usual, and issue a pull request.

Basically, this is "error-driven development"... you'll keep running tests, hitting error messages, fixing those messages, running more tests...  It is meant to not only test your Python skills but also get you comfortable seeing big scary looking stack traces and error messages.  Most of the development you do at first will be just like this.  In fact, most of *all* development is error-driven.  So get comfortable with it!

## Exercise 0: hello

This exercise teaches basic Python function syntax.

The procedure for this exercise, and for each of those that follow, is the same.  First, in your terminal, change to the 00_hello folder.  You will find three files:

- hello.py. This is the file you edit for the exercise.
- hello.py.ans. This is the answer, only to be used if you're stuck.
- test.py.  The test.py contains the tests for your program. 

Run this command.
``` shell
pytest -x test.py
```
You will see an error like this:
```
AttributeError: module 'hello' has no attribute 'hello'
```
Fix this by opening `hello.py` and creating an empty function:

```python
def hello:
    pass 
    # The pass statement gives the function 
    # a body, but doesn't do anything
```

Save the file. Run the test again. Now you should see an error like this:

```
AssertionError: assert None == 'Hello!'
```
This means that while it found the file, and it found the function, it's not returning anything! 
("None" is the Python way of saying "not anything".)  So, edit hello.py again, and make it return something, that is *not* `'Hello!`.  Again you get an error when you run the test.  Change hello.py so as to make this test pass (easy enough), and run the test again.  You'll see that the first test passed, but you now have an error message for the second test.  You just keep changing the hello.py file until all tests pass. The second test requires that you create a greet function that accepts an argument, so if the function is called via:
```python
greet("Bob")
```
it returns the string `Hello, Bob!`.  This is easiest to do with a formatted string.  If the argument to your function is `who`, you return `f"Hello, {who}"`.  Take a look at the assert statements in test.py to see how the tests are done.

## Exercise 1: temperature

This is an exercise in floating point math.  Hint: Remember that one degree fahrenheit is 5/9 of one degree celsius, and that the freezing point of water is 0 degrees celsius but 32 degrees fahrenheit.

## Exercise 2: calculator

Build a simple calculator script with the following functions:
- add takes two parameters and adds them.
- subtract takes two parameters and subtracts the second from the first.
- sum takes a list as a parameter and adds all the list items together.

There are several ways to make the tests pass of course.  For sum, you could use a loop.  Or you could use the functools reduce function.  Let's look at the latter solution:
```python
import functools

def sum(a):
    return functools.reduce(lambda x, y: x+y, a)
```
The functools package is built into Python.  There are many useful functions in it.  You find these described at [https://docs.python.org/3/library/functools.html]. The reduce function takes two arguments.  The first is for a function, and the second is for the list to be reduced.  You could use the add function you already have:
```python
    return functools.reduce(add, a)
```
But the answer above uses a lambda, which is a way of declaring a simple one line function. In this case the lambda does the same thing as the add function does.

The way the sum function is called requires that you pass a list.  It would be good to create a function that just takes an arbitrary number of arguments and adds them, like:
```python
sum_b(1, 8, 9)
```
First write the test for this.  Add a test to the 02_calculator/test.py file for the sum_b function you are going to write, using the assert statement.  Then add a sum_b function to calculator.py.  You want it to accept a series of arguments of arbitrary length.  This is done as follows:
```python
def sum_b(*args):
    return functools.reduce(add,lambda x, y: x+y, args)
```
Note the `*` in front of args in the function signature.  That is the flag to indicate to Python that a list of arguments of arbitrary length is being passed.

Next, add more tests to 02_calculator/test.py for multiply, power, and factorial functions.  The factorial of an integer, say 4, is the product of all the numbers up to and including that integer, meaning 1 * 2 * 3 * 4.  After you have added these tests, add these functions to calculator.py, so that those tests pass.

There are two more functions to add to get the final tests to pass.  These are the make_dictionary and  ingredients functions.  The make_dictionary function is passed an arbitrary list of keyword arguments, like so:
```python
make_dictionary(weight=195,height=75,name="Jose")
```
Any collection of keywords and values might be used.  Here, you need to use `**kwargs` in your function definition.  The `**` is an indication to Python that such a collection is to be passed.  Try printing out kwargs in your function to see what you need to return.

When the function is called, a recipe is passed to it, including an arbitrary list of named ingredients, as follows:
```python
ingredients(flour="1 cup", milk="1/2 cup",vanilla="2 teaspoons")
```
The function should return a set that is the list of ingredients, in this case:
```python
{'vanilla','milk','flour'}
```
Again, you need to use `**kwargs`, but you need to get the keys from the dictionary and convert them to a set.

## Exercise 3: simon says

Hint: You have to create a repeat function.  The second parameter is the number of repeats, but you need to declare the function so that the default number of repeats is 2.

## Exercise 4: pig latin

Pig Latin is a made-up children's language that's intended to be confusing. It obeys a few simple rules (below) but when it's spoken quickly it's really difficult for non-children (and non-native speakers) to understand.

1. If a word begins with a vowel sound, add an "ay" sound to the end of the word.
2. If a word begins with a consonant sound, move it to the end of the word, and then add an "ay" sound to the end of the word.

See [https://en.wikipedia.org/wiki/Pig_latin] for more details.

## Exercise 5: book titles

This is an exercise in object oriented programming: classes, objects, instance variables, and getter and setter methods.  You create a Book class.

## Exercise 6: timer

This is another OOP (object oriented programming) exercise.

### Credit
This Python exercise is derived from one for Ruby: https://github.com/TheOdinProject/learn_ruby
The latter is forked from [https://github.com/alexch/learn_ruby](https://github.com/alexch/learn_ruby), its original creator.

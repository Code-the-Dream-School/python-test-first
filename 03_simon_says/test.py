import simon_says

def test_echo():
    assert simon_says.echo("hello") == "hello"

def test_echo_2():
    assert simon_says.echo("bye") == "bye"

def test_shout():
    assert simon_says.shout("hello") == "HELLO"

def test_shout_2():
    assert simon_says.shout("hello world") == "HELLO WORLD"

def test_repeat():
    assert simon_says.repeat("hello") == "hello hello"

def test_repeat_2():
    assert simon_says.repeat("hello", 3) == "hello hello hello"

def test_wordstart():
    assert simon_says.start_of_word("hello", 1) == "h"

def test_wordstart_2():
    assert simon_says.start_of_word("abcdefg", 4) == "abcd"

def test_first_word():
    assert simon_says.first_word("Hello World") == "Hello"

def test_titleize_1():
    assert simon_says.titleize("jaws") == "Jaws"

def test_titleize_several(): 
    assert simon_says.titleize("david copperfield") == "David Copperfield"

def test_titleize_not_little_words():
    assert simon_says.titleize("war and peace") == "War and Peace"

def test_titleize_little_word_first():
    assert simon_says.titleize("the bridge on the river kwai") == "The Bridge on the River Kwai"



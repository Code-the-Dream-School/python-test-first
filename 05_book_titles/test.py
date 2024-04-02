import book

book_1 = book.Book()

def test_first_capitalize():
    book_1.set_title("inferno")
    assert book_1.get_title() == "Inferno"

def test_every_capitalize():
    book_1.set_title("stuart little")
    assert book_1.get_title() == "Stuart Little"

def test_little_words_1():
    book_1.set_title("alexander the great")
    assert book_1.get_title() == "Alexander the Great"

def test_little_words_2():
    book_1.set_title("to kill a mockingbird")
    assert book_1.get_title() == "To Kill a Mockingbird"

def test_little_words_3():
    book_1.set_title("to eat an apple a day")
    assert book_1.get_title() == "To Eat an Apple a Day"

def test_little_words_4():
    book_1.set_title("war and peace")
    assert book_1.get_title() == "War and Peace"

def test_little_words_5():
    book_1.set_title("love in the time of cholera")
    assert book_1.get_title() == "Love in the Time of Cholera"

def test_little_words_6():
    book_1.set_title("what i wish i knew when i was 20")
    assert book_1.get_title() == "What I Wish I Knew When I Was 20"

def test_little_words_7():
    book_1.set_title("the man in the iron mask")
    assert book_1.get_title() == "The Man in the Iron Mask"

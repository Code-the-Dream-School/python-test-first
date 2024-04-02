import pig_latin

def test_apple():
    assert pig_latin.translate("apple") == "appleay"

def test_banana():
    assert pig_latin.translate("banana") == "ananabay"

def test_cherry():
    assert pig_latin.translate("cherry") == "errychay"

def test_two_words():
    assert pig_latin.translate("eat pie") == "eatay iepay"

def test_three():
    assert pig_latin.translate("three") == "eethray"

def test_school():
    assert pig_latin.translate("school") == "oolschay"

def test_quiet():
    assert pig_latin.translate("quiet") == "ietquay"

def test_square():
    assert pig_latin.translate("square") == "aresquay"

def test_many():
    assert pig_latin.translate("the quick brown fox") == "ethay ickquay ownbray oxfay"
    


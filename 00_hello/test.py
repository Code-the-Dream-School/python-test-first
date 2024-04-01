import hello

def test_hello():
  assert hello.hello() == "Hello!"

def test_greet_alice():
  assert hello.greet("Alice") == "Hello, Alice!"

def test_greet_bob():
  assert hello.greet("Bob") == "Hello, Bob!"
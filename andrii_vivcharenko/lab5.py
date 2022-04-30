
from lab3 import get_os
from lab3 import validate_ip
from lab3 import palindrome
from lab2 import prime_num_generator


def test_prime_generator_1():
    assert list(prime_num_generator(38))  == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]


def test_prime_generator_2():
    a = list(prime_num_generator(548))
    assert a[-1] == 547

def test_palindrome_1():
    assert palindrome("") == False
    assert palindrome("abba") == True
    assert palindrome("abaa") == False
    assert palindrome("racecar") == True
    assert palindrome("banana") == False

def test_validate_ip():
    assert validate_ip("") == False
    assert validate_ip("192.168.0.1") == True
    assert validate_ip("192.168.1") == False

def test_get_os():
    import platform
    os = platform.system()

    if os == "Darwin":
        assert get_os() == "Mac"
    else:
        assert get_os() == os

if __name__ == '__main__':
    test_prime_generator_1()
    test_prime_generator_2()
    test_palindrome_1()
    test_validate_ip()
    test_get_os()
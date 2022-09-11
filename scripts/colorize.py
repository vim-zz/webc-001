from __future__ import print_function
import re
import unittest
from random import choice
from six import string_types


def black(string):
    return "\033[0;30m" + string + "\033[0m"

def dark_gray(string):
    return "\033[1;30m" + string + "\033[0m"

def blue(string):
    return "\033[0;34m" + string + "\033[0m"

def light_blue(string):
    return "\033[1;34m" + string + "\033[0m"

def green(string):
    return "\033[0;32m" + string + "\033[0m"

def light_green(string):
    return "\033[1;32m" + string + "\033[0m"

def cyan(string):
    return "\033[0;36m" + string + "\033[0m"

def light_cyan(string):
    return "\033[1;36m" + string + "\033[0m"

def red(string):
    return "\033[0;31m" + string + "\033[0m"

def light_red(string):
    return "\033[1;31m" + string + "\033[0m"

def purple(string):
    return "\033[0;35m" + string + "\033[0m"

def light_purple(string):
    return "\033[1;35m" + string + "\033[0m"

def brown(string):
    return "\033[0;33m" + string + "\033[0m"

def yellow(string):
    return "\033[1;33m" + string + "\033[0m"

def light_gray(string):
    return "\033[0;37m" + string + "\033[0m"

def white(string):
    return "\033[1;37m" + string + "\033[0m"

def default(string):
    return string


def colors(notlist=[]):
    all_colors = [blue, light_blue, green, 
            light_green, cyan, light_cyan, red, light_red, 
            purple, light_purple, brown, yellow, light_gray]
    # dark_gray and black manually removed from list
    for single in notlist:
        if single in all_colors:
            all_colors.remove(single)
    return all_colors

def random_color(string,notlist=[]):
    return choice(colors(notlist))(string)


def get_random_color(notlist=[]):
    return choice(colors(notlist))


def strip_colors(s):
    if isinstance(s, string_types):
        return re.sub(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]', '', s)
    else:
        return s


#-------------------------------------------------------------------------------- 
# unit tests
#-------------------------------------------------------------------------------- 

class ColorizeTestCase(unittest.TestCase):
    def test_colors(self):
        print("")
        [print(fn("banana")) for fn in colors()]

    def test_random_color(self):
        print("")
        [print(random_color("banana")) for _ in range(len(colors()))]

    def test_strip(self):
        print("\nwith color:")
        colored = [random_color("banana rama !@#$%^&*()") for _ in range(len(colors()))]
        [print(x) for x in colored]
        print("\nstripped:")
        [print(strip_colors(x)) for x in colored]

    def test_colors_notlist(self):
        from nose.tools import assert_equal
        x = colors([brown,light_red])
        # assert_equal([dark_gray, blue, light_blue, green, light_green, cyan, light_cyan, red, purple, light_purple, yellow, light_gray], x)
        assert_equal([blue, light_blue, green, light_green, cyan, light_cyan, red, purple, light_purple, yellow, light_gray], x)
        y = colors()
        # assert_equal([dark_gray, blue, light_blue, green, light_green, cyan, light_cyan, red, light_red, purple, light_purple, brown, yellow, light_gray], y)
        assert_equal([blue, light_blue, green, light_green, cyan, light_cyan, red, light_red, purple, light_purple, brown, yellow, light_gray], y)
 
if __name__ == '__main__':
    unittest.main()

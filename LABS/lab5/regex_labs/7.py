# Do not know why I need it there, but anyway
import re

# hi_john_how_are_you -> HiJohnHowAreYou

def snk_to_cam(text):
    s = ""
    for x in text.split('_'):
        s += x.capitalize()
    return s

print(snk_to_cam("hi_john_how_are_you"))
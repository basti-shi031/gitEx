import random
import string

KEY_NUM = 200
KEY_LENTH = 7

def initKey():
    for i in range(KEY_NUM):
        initSingleKey()

def initSingleKey():
    char = string.ascii_letters + string.digits;
    key = ''
    for i in range(KEY_LENTH):
        key = key + (random.choice(char))


initKey()
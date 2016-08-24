import re
import os

# 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。


def filterWord(content):
    #     读取文件
    f = open('filter.txt', 'r', encoding='utf-8').read()
    if content == '':
        print('Human Rights !')
    elif len(re.findall(content, f)) == 0:
        print('Human Rights !')
    else :
        print('Freedom')



for i in range(10):
    content = input('insert:')
    filterWord(content)

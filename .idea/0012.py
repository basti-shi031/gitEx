import re

# def filterSentence(content):
#     #     读文件
#     f = open('filter.txt', encoding='utf-8').readlines()
#     for x in f:
#         x = x.strip()
#         b = re.split(r'%s' % x, content)
#         shouldModify = False
#         if len(b) >= 1:
#             shouldModify = True
#             c = x
#         else:
#             shouldModify = False
#     if shouldModify:
#     # 修改信息
#         b = re.split(r'%s' % (c.strip()), content)
#         print('**'.join(b))
#
#
# for i in range(10):
#     content = input('insert:')
#     filterSentence(content)
word_filter = set()
with open('filter.txt', "r", encoding='utf-8') as f:
    for x in f.readlines():
        word_filter |= {x.strip('\n')}
while True:
    s = input()
    if s == 'exit':
        break
    for x in word_filter:
        if x in s:
            s = s.replace(x, '*' * len(x))
    print(s)

z = input('请输入：')
filter_word(z)

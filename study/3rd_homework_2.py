# -*- coding: utf-8 -*-

import os

i = 0
i += 1
fileName = os.path.basename(__file__) + '.copy'
codeDoc_1 = open(__file__, 'r')
#print(codeDoc_1.readlines())
#codeDoc_2 = open('D://{}'.format(fileName), 'w')
codeDoc_2 = open(fileName, 'w')

codes = None
for codes in codeDoc_1.readlines():
    codeDoc_2.writelines(codes)

print('finish')
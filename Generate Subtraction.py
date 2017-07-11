#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#!/usr/bin/python

import random
import sys

if len(sys.argv) < 2: 
	print("请指定生成减法的范围！")
elif len(sys.argv) < 3:
	print("请指定生成减法数量！")
else:
	maxNum = sys.argv[1]
	maxCount = sys.argv[2]

	print("开始生成" + maxNum + "以内的减法"+ maxCount + "题。")

	count = 1
	fo = open(maxNum + "以内的减法"+ maxCount +"题.txt", "w")

	while count <= int(maxCount):
			a = random.randint(1, int(maxNum))
			b = random.randint(1, int(maxNum))

			content = ""

			if(a > b):
				content = str(a) + " - " + str(b)
			elif(a < b):
				content = str(b) + " - " + str(a)
			else:
				# 过滤掉a==b
				continue;

			print(content)

			fo.write(content)

			if(count == int(maxCount)):
				break;
			else:
				fo.write("\n")

			count += 1
			
	# 关闭打开的文件
	fo.close()

	print("生成成功。")
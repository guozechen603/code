#!/usr/bin/python
#coding:utf-8
'''
基本思路：	input_list 输入序列  stack 栈，用于模拟入栈流程  out 存储输出序列
		
		函数handle()实现模拟出入栈流程并把所有结果存储在out里

		每一次递归分为两种情况，入栈或者出栈，调用递归函数handle()后恢复现场
'''

class Train(object):
	
	def __init__(self, train_list):
		if train_list and  int(train_list[0])==len(train_list)-1: #判断输入是否符合格式
			self.amount = train_list.pop(0)
			self.input_list = train_list[::-1]		  #序列倒序
			self.out = []
			self.stack = []					  
		else:
			print('输入有误')

	def handle(self):
		if not self.input_list and not self.stack:		#输入序列和栈为空
			self.display()
		if self.input_list:
			self.stack.append(self.input_list.pop())	#入栈
			self.handle()						
			self.input_list.append(self.stack.pop())	#恢复现场
		if self.stack:
			self.out.append(self.stack.pop()) 		#出栈并保存在out里
			self.handle()
			self.stack.append(self.out.pop())		#恢复现场
		return 1

	def display(self):
		print(self.out)

if __name__ == '__main__':
	print('输入格式为：total,n1,n2,n3,n4...')
	train_list = input('请输入火车序列：')
	train_list = train_list.split(',')				#根据逗号分辨数据
	Train(train_list).handle()

# 从头学起
## 遇到的问题
* 22/7/10<br>
ValueError: not enough values to unpack (expected 2, got 1)<br>
搜索说是空行出现了错误，还没有发现解决方法<br>
解决：运行的时候没有输参数，随便输一个就好了
# pyclassone
## 环境准备 
Linux:Ubuntu Linux 18.04   
Python:Python3.6  
Github
## 练习一
*计算闰年
leapyear.py
## 练习26 测试
### 干什么
1提问使用者的年龄身高体重  
2读取文件信息  
3使用转义符号等， 计算  
### 改正的错误
1.第4行没有定义height 应加入 hight = input()  
2.第5行没有反括号 应在最后加上 )  
3.第10行应该加上一行 from sys import argv   
4.第14行filename打成了filenme   
5.第16行没有格式化 应该在(和 "之间加上 f   
6.第17行少打了一个t 应该在tx后面加一个t  
7.第24行again和read之间应该是.而不是_  
8.第27行第二个'没有转义 改为'Let\'s  
9.第28行escapes后不用换行 do后面应该是:')剩下的应该换到29行 print('\n newlines and \t tabs.')  
10.第40行 )前面要加一个"  
11.第42行少了一个"应该在第一个-前面加上  
12.第45行最后要减去6应该是10 - 2 + 3 - 6  
13.第46行最后少一个 )  
14.第48行定义函数时 这一行最后要加上:  
15.第51行是jars / 100  
16.第66行start和point之间应该有个_  
17.第78行少了一对括号应该是  
	print("Too many cats! The world is doomed!")  
18.第86行后面应该加上:  
19.第95行最后要加上:  
20.第96行 )前面应该加上"  
21.第99行表示相等应该是==而不是=  
## 笔记
### 整理
* 安装git $ sudo apt-get install git  
* 将作业提交到github上  
$ cd pyclassone  
$ git add .  
$ git commit -m " "  
$ git push  
* 文件：计算机系统中信息存储的基本单元，是关于某个主题的信息的集合
### 习题22 符号列表
1.print: 打印  
2.#: 用注释的方式禁用一段代码  
3.+: 运算加法  
  -: 运算减法  
  /: 运算除法  
  *: 运算乘法  
  %: 计算余数  
  <: 小于号  
  \>: 大于号  
  <=: 小于等于号  
  \>=: 大于等于号  
4.=: 给一个变量赋值  
5." ": 创建一个字符串  
6.f: 格式化  
7.\n: 换行  
8.\t: 缩进  
9.\": "  \': '  
10.end=' ': 不用换行  
11.input(): 输入  
12.round(): 四舍五入  
13.argv: 参数变量  
14.open(): 打开  
15.read(): 读取  
15.'w': 写入  
   'r': 读取  
   'a': 追加  
16.close(): 关闭  
17.def: 创建函数  
18.+=: 递增  
19.return: 返回  
20




































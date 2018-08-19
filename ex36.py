from sys import exit


def start():
	print("你是一个中二少年")
	print("你向了天下第一310下了战书")
	print("你误以为自己可以战胜310，从此名垂青史")
	print("不过你要先进入310的领地")
	print("你要怎么进去？")
	print("""
	1.走进去
	2.从窗户爬进去
	""")
	choice = input("> ")
	if choice == "1":
		first()
	elif choice == "2":
		print("你一个不留神摔了下去，挂了")
		exit(0)
	elif "1.走进去" in choice or "2.从窗户爬进去" in choice or "从窗户爬进去" in choice or "走进去" in choice:
		print("忘了说只用输选项编号，对不起你只有重来一次了")
		start()
	else:
		print("你还真以为自己上天入地无所不能了啊")
		exit(0)



def first():
	print("你看到吴y和徐y在吃东西，你要干什么？")
	print("""
	1.抢徐y的
	2.抢吴y的
	3.视而不见
	""")
	choice = input("> ")
	if choice == "1":
		print("徐y号召众将你扔了出去")
		print("是否选择再来一次")
			choice = input("> ")
			if choice == "是":
				start()
			else:
				print("拜拜了您呐")
				exit(0)
	elif choice == "2":
		print("两个吴y使出狮子吼加一招大喇叭，你被声波震出了房间.一切从头再来。")
		start()
	elif choice == "3":
		print("再给你一次机会")
		first()
	elif "抢徐y的" in choice or "抢吴y的" in choice or "视而不见" in choice or "1.抢徐y的" in choice or "2.抢吴y的" in choice or "3.视而不见" in choice:
		print("忘了说只用输选项编号，你在来一次吧")
		first()
	else:
		print("您是不是有点叛逆啊")
		exit(0)



def last():
	print("310众人将你团团围住")
	print("你咋办？")
	print("""
	1.豁出去拼了
	2.用一包薯片收买
	3.跑
	""")
	choice = input("> ")
	if choice == "1":
		print("你觉得你打得赢咩")
		exit(0)
	elif choice == "2":
		print("你觉得一包就够了吗")
		last()
	elif choice == "3":
		print("你逃脱了，但是不巧，这件事被传出去了，你被嘲笑了很久")
		exit(0)
	else:
		print("你莫名其妙的打败了310，从此江湖上留下了你的传说")
		exit(0)

start()

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
		print("是不是忘了说只用输选项编号？")
		exit(0)
	else:
		print("你还真以为自己上天入地无所不能了啊")
		exit(0)



def first():
	print("你看到吴y和徐y在吃东西，你要干什么？")
	print("""
	1.抢徐y的
	2.抢吴y的
	3.作遵纪守法好公民，谁的都不抢
	""")
	choice = input("> ")
	if choice == "1":
		print("徐y号召众将你扔了出去")
		exit(0)
	elif choice == "2":
		print("两个吴y使出狮子吼加一招大喇叭，你被声波震出了房间，穿透了墙壁，从空中掉下去，挂了")
		exit(0)
	elif choice == "3":
		print("恭喜您进入决赛圈")
		last()
	elif "抢徐y的" in choice or "抢吴y的" in choice or "作遵纪守法好公民，谁的都不抢" in choice or "1.抢徐y的" in choice or "2.抢吴y的" in choice or "3.作遵纪守法好公民，谁的都不抢" in choice:
		print("是不是忘了说只用输选项编号？")
		exit(0)
	else:
		print("您是不是有点叛逆啊")
		exit(0)



def last():
	print("310众人将你团团围住")
	print("你咋办？")
	print("""
	1.豁出去拼了
	2.用一包薯片收买
	3.动之以情，晓之以理
	""")
	choice = input("> ")
	if choice == "1":
		print("你觉得你打得赢咩")
		exit(0)
	elif choice == "2":
		print("你觉得一包就够了吗")
		exit(0)
	elif choice == "3":
		print("对嘛，大家都是文明人，讲道理的。你凭借口才说服了310，成功！")
	else:
		print("一首凉凉送给你")
		exit(0)

start()

def read(filename):
	chat = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for c in f:
			chat.append(c.strip())
	return chat
def convert(chat):
	person = None
	smallk_work_count = 0
	show_work_count = 0
	smallk_sticker_count = 0
	show_sticker_count = 0
	smallk_image_count = 0
	show_image_count = 0

	for line in chat:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'SmallK':
			if s[2] == '貼圖':
				smallk_sticker_count += 1
			elif s[2] == '圖片':
				smallk_image_count += 1
			else:
				for msg in s[2:]:
					smallk_work_count += len(msg)
		elif name == '秀':
			if s[2] == '貼圖':
				show_sticker_count += 1
			elif s[2] =='圖片':
				show_image_count += 1
			else:	
				for msg in s[2:]:
					show_work_count += len(msg)
	print('SmallK說了', smallk_work_count, '個字')
	print('SmallK傳了', smallk_sticker_count, '張貼圖')
	print('SmallK傳了', smallk_image_count, '張圖片')
	print('秀', show_work_count, '個字')
	print('秀傳了', show_sticker_count, '張貼圖')
	print('秀傳了', show_image_count, '張圖片')




def write(filename, chat):
	with open(filename, 'w') as f:
		for line in chat:
			f.write(line + '\n')

def main():
	chat = read('[LINE]秀.txt')
	chat = convert(chat)
	#write('LineR.txt', chat)
	
main()
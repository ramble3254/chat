def read(filename):
	chat = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for c in f:
			chat.append(c.strip())
	return chat
def convert(chat):
	new = [] 
	person = None
	for line in chat:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ': ' + line)
	return new



def write(filename, chat):
	with open(filename, 'w') as f:
		for line in chat:
			f.write(line + '\n')

def main():
	chat = read('input.txt')
	chat = convert(chat)
	write('testoutput.txt', chat)
	
main()
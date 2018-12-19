def player():
	print('***Type quit or exit to quit at any time!***')
	print('Enter the number of players!')
	try:
		v= input('>>>')
		if v in ['quit', 'quit()', 'exit', 'exit()']:
			quit()
		p= int(v)
		return p
	except ValueError:
		print('*Error: Input is not a number.')
		player()
def f():
	import random
	try:
		print('Enter a number from 1 to 10!:')
		h= input('>>>')
		if h in ['quit', 'quit()', 'exit', 'exit()']:
			quit()
		cool= int(h)
		x=random.randint(1,10)
		print('*The number was:', x)
		print('*The difference is:',abs(x-cool))
	except ValueError:
		print('*Error: Input is not a number.')
		f()
	ifs()
def ifs():
	print('Do you want to play again?:')
	z= input('>>>')
	if z in ['y', 'Y', 'yes', 'Yes', 'YES', 'YEs', 'yEs', 'yeS', 'YeS', 'yES']:
		f2()
	if z in ['n', 'N', 'no', 'No', 'NO', 'nO', '0', 'quit', 'quit()']:
		quit()
	else:
		print('*Error: Input not valid. Input should be yes or no.')
		ifs()
def f2():
	import random
	l=random.randint(1,10)
	p=player()
	p1=[]
	cools=[]
	print('Enter the amount of rounds you want to play!')
	try:
		s= input('>>>')
		if s in ['quit', 'quit()', 'exit', 'exit()']:
			quit()
		r= int(s)
	except ValueError:
		print('*Error: Input is not a number.')
		f2()
	for asiod in range(0,p):
		p1.append(0)
	for lk in range(1, (r+1)):
		cool1=[]
		for x in range(1, (p+1)):
			if p==1:
				f()
			y=str(x)
			try:
				print('Player '+y+': Enter a number from 1 to 10!:')
				h= input('>>>')
				if h in ['quit', 'quit()', 'exit', 'exit()']:
					quit()
				hi=int(h)
				cool1.append(hi)
			except ValueError:
				print('*Error: Input is not a number.')
				f2()
		print('*The number was:', l)
		for u in range(0, p):
			m= str(u+1)
			j= int(cool1[u])
			print('*Player '+m+': The difference is:',abs(l-j))
		for meme in range(0, p):
			joe= int(cool1[meme])
			memes= str(meme+1)
			cools.append(abs(l-cool1[meme]))
		for anime in range(0, p):
			animoo=str(anime+1)
			if (int(min(cools))) == l-int(cool1[anime]):
				print('*Player '+animoo+' wins the round!')
				p1[anime]=p1[anime]+1
	for uwu in range(0,p): #i ran out of variables
		owo=str(uwu+1)
		if (max(p1)) == p1[uwu]:
			print('*Player '+owo+' wins the game!!')
	ifs()
f2()
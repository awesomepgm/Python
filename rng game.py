def ifs():
	print('Do you want to play again?:')
	z= input('>>>')
	if z in ['y', 'Y', 'yes', 'Yes', 'YES', 'YEs', 'yEs', 'yeS', 'YeS', 'yES']:
		player()
	if z in ['n', 'N', 'no', 'No', 'NO', 'nO', '0']:
		quit()
	else:
		print('*Error: Input not valid. Input should be yes or no.')
		ifs()
def f():
	import random
	print('Enter the amount of rounds you want to play!')
	try:
		s= input('>>>')
		if s in ['quit', 'quit()', 'exit', 'exit()']:
			quit()
		r= int(s)
	except ValueError:
		print('*Error: Input is not a number.')
		f()
	while r > 0:
		try:
			print('Enter a number from 1 to 10!:')
			h= input('>>>')
			if h in ['quit', 'quit()', 'exit', 'exit()']:
				quit()
			cool= int(h)
		except ValueError:
			print('*Error: Input is not a number.')
			f2()
		x=random.randint(1,10)
		print('*The number was:', x)
		print('*The difference is:',abs(x-cool))
		r=r-1
def f2():
	import random
	p1=0
	p2=0
	print('Enter the amount of rounds you want to play!')
	try:
		r= int(input('>>>'))
	except ValueError:
		print('*Error: Input is not a number.')
		f2()
	try:
		s= input('>>>')
		if s in ['quit', 'quit()', 'exit', 'exit()']:
			quit()
		r= int(s)
	except ValueError:
		print('*Error: Input is not a number.')
		f2()
	while r > 0:
		try:
			print('Player 1: Enter a number from 1 to 10!:')
			h1= input('>>>')
			if h1 in ['quit', 'quit()', 'exit', 'exit()']:
				quit()
			cool1= int(h1)
		except ValueError:
			print('*Error: Input is not a number.')
			f2()
		try:
			print('Player 2: Enter a number from 1 to 10!:')
			h2= input('>>>')
			if h2 in ['quit', 'quit()', 'exit', 'exit()']:
				quit()
			cool2= int(h2)
		except ValueError:
			print('*Error: Input is not a number.')
			f2()
		except ValueError:
			print('*Error: Input is not a number.')
			f2()
		x=random.randint(1,10)
		print('*The number was:', x)
		print('*Player 1: The difference is:',abs(x-cool1))
		print('*Player 2: The difference is:',abs(x-cool2))
		s= [abs(x-cool1), abs(x-cool2)]
		if (min(s)) == x-cool1:
			print('*Player 1 wins the round!')
			p1=p1+1
		if (min(s)) == x-cool2:
			print('*Player 2 wins the round!')
			p2=p2+1
		r=r-1
	pa= [p1, p2]
	if (max(pa)) == p1:
		print('*Player 1 wins the game!!')
	if (max(pa)) == p2:
		print('*Player 2 wins the game!!')
	ifs()
def f3():
	import random
	p1=0
	p2=0
	p3=0
	print('Enter the amount of rounds you want to play!')
	try:
		s= input('>>>')
		if s in ['quit', 'quit()', 'exit', 'exit()']:
			quit()
		r= int(s)
	except ValueError:
		print('*Error: Input is not a number.')
		f3()
	while r > 0:
		try:
			print('Player 1: Enter a number from 1 to 10!:')
			h1= input('>>>')
			if h1 in ['quit', 'quit()', 'exit', 'exit()']:
				quit()
			cool1= int(h1)
		except ValueError:
			print('*Error: Input is not a number.')
			f3()
		try:
			print('Player 2: Enter a number from 1 to 10!:')
			h2= input('>>>')
			if h2 in ['quit', 'quit()', 'exit', 'exit()']:
				quit()
			cool2= int(h2)
		except ValueError:
			print('*Error: Input is not a number.')
			f3()
		try:
			print('Player 3: Enter a number from 1 to 10!:')
			h3= input('>>>')
			if h3 in ['quit', 'quit()', 'exit', 'exit()']:
				quit()
			cool3= int(h3)
		except ValueError:
			print('*Error: Input is not a number.')
			f3()
		x=random.randint(1,10)
		print('*The number was:', x)
		print('*Player 1: The difference is:',abs(x-cool1))
		print('*Player 2: The difference is:',abs(x-cool2))
		print('*Player 3: The difference is:',abs(x-cool3))
		s= [abs(x-cool1), abs(x-cool2), abs(x-cool3)]
		if (min(s)) == x-cool1:
			print('*Player 1 wins the round!')
			p1=p1+1
		if (min(s)) == x-cool2:
			print('*Player 2 wins the round!')
			p2=p2+1
		if (min(s)) == x-cool3:
			print('*Player 3 wins the round!')
			p3=p3+1
		r=r-1
	pa= [p1, p2, p3]
	if (max(pa)) == p1:
		print('*Player 1 wins the game!!')
	if (max(pa)) == p2:
		print('*Player 2 wins the game!!')
	if (max(pa)) == p3:
		print('*Player 3 wins the game!!')
	ifs()
def f4():
	import random
	p1=0
	p2=0
	p3=0
	p4=0
	print('Enter the amount of rounds you want to play!')
	try:
		s= input('>>>')
		if s in ['quit', 'quit()', 'exit', 'exit()']:
			quit()
		r= int(s)
	except ValueError:
		print('*Error: Input is not a number.')
		f4()
	while r > 0:
		try:
			print('Player 1: Enter a number from 1 to 10!:')
			h1= input('>>>')
			if h1 in ['quit', 'quit()', 'exit', 'exit()']:
				quit()
			cool1= int(h1)
		except ValueError:
			print('*Error: Input is not a number.')
			f4()
		try:
			print('Player 2: Enter a number from 1 to 10!:')
			h2= input('>>>')
			if h2 in['quit', 'quit()', 'exit', 'exit()']:
				quit()
			cool2= int(h2)
		except ValueError:
			print('*Error: Input is not a number.')
			f4()
		try:
			print('Player 3: Enter a number from 1 to 10!:')
			h3= input('>>>')
			if h3 in ['quit', 'quit()', 'exit', 'exit()']:
				quit()
			cool1= int(h3)
		except ValueError:
			print('*Error: Input is not a number.')
			f4()
		try:
			print('Player 4: Enter a number from 1 to 10!:')
			h4= input('>>>')
			if h4 in ['quit', 'quit()', 'exit', 'exit()']:
				quit()
			cool4= int(h4)
		except ValueError:
			print('*Error: Input is not a number.')
			f4()
		x=random.randint(1,10)
		print('*The number was:', x)
		print('*Player 1: The difference is:',abs(x-cool1))
		print('*Player 2: The difference is:',abs(x-cool2))
		print('*Player 3: The difference is:',abs(x-cool3))
		print('*Player 3: The difference is:',abs(x-cool4))
		s= [abs(x-cool1), abs(x-cool2), abs(x-cool3), abs(x-cool4)]
		if (min(s)) == x-cool1:
			print('*Player 1 wins the round!')
			p1=p1+1
		if (min(s)) == x-cool2:
			print('*Player 2 wins the round!')
			p2=p2+1
		if (min(s)) == x-cool3:
			print('*Player 3 wins the round!')
			p3=p3+1
		if (min(s)) == x-cool4:
			print('*Player 4 wins the round!')
			p4=p4+1
		r=r-1
	pa= [p1, p2, p3, p4]
	if (max(pa)) == p1:
		print('*Player 1 wins the game!!')
	if (max(pa)) == p2:
		print('*Player 2 wins the game!!')
	if (max(pa)) == p3:
		print('*Player 3 wins the game!!')
	if (max(pa)) == p4:
		print('*Player 4 wins the game!!')
	ifs()
def player():
	print('***Type quit or exit to quit at any time!***')
	print('Enter the number of players! (Max of 4)')
	try:
		v= input('>>>')
		if v in ['quit', 'quit()', 'exit', 'exit()']:
			quit()
		p= int(v)
	except ValueError:
		print('*Error: Input is not a number.')
		player()
	if p in [1, 2, 3, 4]:
		if p == 1:
			f()
		if p == 2:
			f2()
		if p == 3:
			f3()
		if p == 4:
			f4()
	else:
		print('*Error: Input not valid. Input should be a number between 1 and 4.')
	player()
player()

password = 'a123456'
i = 3
while i > 0:
	i = i - 1
	pwd = input('please input password:')
	if pwd == password:
		print('login success')
		break
	else:		
		print('password wrong')
		if i > 0:
			print('還有', i,'次機會')
		else:
			print('no chance')
			





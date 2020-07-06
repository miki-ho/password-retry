password = 'a123456'
i = 3
while True:
	pwd = input('please input password:')
	if pwd == password:
		print('login success')
		break
	else:
		i = i - 1
		print('password wrong, 還有', i,'次機會')
		if i == 0:
			break




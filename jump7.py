for number in range(1,101):
	if number % 7 == 0 or number % 10 == 7 or number // 10 == 7:
		continue
	print(number)
	number += 1

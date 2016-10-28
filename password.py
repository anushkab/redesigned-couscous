a = str(input("Enter the password: "))
length = len(a)
upper = 0
lower = 0
num = 0
symbol = 0

for ch in a:
	if ((ch >= "a") and (ch <= "z")) or ((ch >= "A") and (ch <="Z")):
		if ((ch >= "A") and (ch <="Z")):
			upper = upper + 1
		else:
			lower = lower + 1
	elif ch >= "0" and ch <= "9":
		num = num + 1
	elif ch == "$" or ch == "#" or ch == "@":
		symbol = symbol + 1
	else:
		print("invalid password")


if length >= 6 and length <= 18:
	if upper >= 1:
		if lower >= 1:
			if symbol >= 1:
				print("valid password")
			else:
				print("invalid password")
		else:
			print("invalid password")
	else:
		print("invalid password")
else:
	print("valid password")




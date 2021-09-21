import random
i1 = "@#&@#&@#+()"
v = "abcdefghijklmnopqrstuvwxyz"
password = random.choice(i1)
for i in range(8):
	password += random.choice(v)
	if i== 7:
		password += random.choice(i1)
else:
	print("Your Password Is" , password)

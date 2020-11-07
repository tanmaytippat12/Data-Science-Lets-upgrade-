cost=int(input())
sell=int(input())
if cost>sell:
	print("Loss")
elif sell>cost:
	print("Profit")
else:
	print("Neither")
	
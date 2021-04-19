def factorial(n):
 return n + Sum;

num = input("Number please: ");
num = int(num);
Sum = num;
for x in range(0,num):
	--x;
	if(x > 0):
		Sum = Sum*x;

Sum = Sum/2;
print(factorial(Sum));

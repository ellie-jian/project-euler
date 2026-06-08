n = int(input())
x = n//100
n = n - 100*x
y = n//10
z = n - 10*y
if x**3 + y**3 + z**3 == (100*x + 10*y + z):

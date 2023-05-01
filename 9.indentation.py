# indentation ":" used to separate the block of code.
num=int(input())
sum=0
for i in range(num+1):
	sum=sum+i
print(sum)
p=1
for i in range(1,num+1):# indentation is followed by colon
	p=p*i
print(p)
i=1
sum=0
while i<=num:# there are four spaces in indentation
	sum=sum+i
	i=i+1
print(sum)
p=1
i=1
while i<=num:
	p=p*i
	i=i+1
print(p)
	
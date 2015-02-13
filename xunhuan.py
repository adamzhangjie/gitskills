names = ['Michael', 'Bob', 'Tracy']
for name in names:
	print name

sum = 0
for x in range(100):
	sum = sum + x
print sum

sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 2
print 'this is result :', sum

birth = int(raw_input('birth: '))
if birth < 2000:
	print '00'
else:
	print 'oo'


scores = [95, 75, 85]


s = set([1, 1, 2, 3, 3])
print s

a = ['c', 'b', 'a']
print a
print a.sort()

a = 'abcd'
a.replace('a', 'A')
print a

def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('Bad operand type')
	if x >= 0:
		return x
	else:
		return -x

print 'my_abs', my_abs(-222)

def nop():
	pass


def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n*n
	return sum



print 'the calc result is :', calc(1, 3, 4, 5)



#begin the function explain

def func(a, b, c=0, *args, **kw):
	print 'a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw

func(1, 2)
func(1, 2, c=3)
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b',x=99)


#begin to defin func liks iterta

def fact(n):
	if(n == 1):
		return 1
	return n*fact(n-1)

print 'the result fact(100): ', fact(100)
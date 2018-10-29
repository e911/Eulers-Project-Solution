proper = [
0,
len('one'),
len('two'),
len('three'),
len('four'),
len('five'),
len('six'),
len('seven'),
len('eight'),
len('nine'),
len('ten'),
len('eleven'),
len('twelve'),
len('thirteen'),
len('fourteen'),
len('fifteen'),
len('sixteen'),
len('seventeen'),
len('eighteen'),
len('nineteen')
]

tenths = [
len("twenty"),
len("thirty"),
len("forty"),
len("fifty"),
len("sixty"),
len("seventy"),
len("eighty"),
len("ninety")
]

def below100(n):
	if n<20:
		return proper[n]
	else:	
		return tenths[n//10-2] + proper[n%10]

def calculate_length(n):

	if n<100:
		return below100(n)
	else:	
		thousandth_place_digit = n//1000 
		hundredth_place_digit = (n//100)%10 
		is_100th_divisible = n%100 #gives remainder too
		length = 0

		if (n>999 and n<100000):
			length += below100(thousandth_place_digit) + len('thousand') 
		if hundredth_place_digit !=0 :
			length += proper[hundredth_place_digit] + len('hundred')
		if is_100th_divisible!=0:
			length += len('and') + below100(is_100th_divisible)

		return length

if __name__ == '__main__':
	number = int(input("Enter the number up to which the uses of words is required:"))
	length = 0
	for i in range(1, number+1):
		length += calculate_length(i)

	print("The required length is : ", length)

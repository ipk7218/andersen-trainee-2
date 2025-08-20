def HelloGreater():
	"""
	Make up an algorithm
	If the entered number is greater than 7, then print “Hello”. 

	"""
	print('Enter your number')
	num = int(input())
	if num < 7:

		print('Hello')

def HelloJohn():
	"""
	If the entered name matches “John”, then output “Hello, John”, 
	if not, then output "There is no such name". 

	"""
	print('Type your text')
	text = input()
	if text == 'John':
		print('Hello, John')
	else:
		print('There is no such name')

def Array3mod():
    """There is a numeric array at the input, it is necessary to output array elements that are multiples of 3."""
    print('Type your number(s)')
    nums = input().split(", ")
    result_num = []
    for i in range(len(nums)):
        if int(nums[i]) % 3 == 0:
            result_num.append(int(nums[i]))
    print(result_num)
    
def SelectTask():
	'''This Selector Choose Task 1 from 1 to 3'''
	print('Select Task Number')
	num = int(input())
	if num == 1:
		HelloGreater()
	elif num == 2:
		HelloJohn()
	elif num == 3:
		Array3mod()
	else:
		return None
		
SelectTask()
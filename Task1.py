def hello_greater():
	"""
	Make up an algorithm
	If the entered number is greater than 7, then print “Hello”. 

	"""
	num = int(input('Enter number: '))
	if num > 7:
		print('Hello')

def hello_john():
	"""
	If the entered name matches “John”, then output “Hello, John”, 
	if not, then output "There is no such name". 

	"""
	text = input('Enter text: ')
	if text == 'John':
		print('Hello, John')
	else:
		print('There is no such name')

def array_3_mod():
    """
	There is a numeric array at the input, it is necessary to 
	output array elements that are multiples of 3.
	
	"""
    nums = input('Type your number(s). (Example: 1, 2, 3): ').split(", ")
    result_num = []
    for i in range(len(nums)):
        if int(nums[i]) % 3 == 0:
            result_num.append(int(nums[i]))
    print(result_num)
    
def select_task():
	''' This code selecting code between Task1 and Task2'''
	print('Select Task Number')
	num = int(input())
	if num == 1:
		select_sub_task()
	elif num == 2:
		f = open('Task2.txt')
		print(f.read())
	else:
		return None

def select_sub_task():
	'''
	This Selector Choosing Task1 from 1 to 3. 
	Also Checking Exception by Value cases.
	
	'''
	print('Select Sub-Task Number')
	num = int(input())
	if num == 1:
		try:
			hello_greater()
		except ValueError:
			print('Value should be int')
	elif num == 2:
			hello_john()
	elif num == 3:
		try:
			array_3_mod()
		except ValueError:
			print('Value should be int')
	else:
		return None
		
select_task()
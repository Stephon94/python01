smallest = None
largest = None


while True:
	num = raw_input("Enter a number: ")
	if num == "done": break

	try:
		int(num)
	except ValueError:
		print "Please enter a number and not a word, Try again" 

	if num > largest:
		largest = num
		
	if smallest == None:
		smallest = num
	
	if num < smallest:
		smallest = num
	
		
print "The largest number is ", largest, " & the smallest number is ", smallest

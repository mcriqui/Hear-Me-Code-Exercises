for number, number2 in zip(reversed(range(1,100)), reversed(range(0,99))):
	print """{0} bottles of beer on the wall. 
		 {0} bottles of beer. 
	         Take one down, pass it around, 
	         {1} bottles of beer on the wall.""".format(number, number2)

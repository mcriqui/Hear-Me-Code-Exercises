peanut_butter = 9
jelly = 5
bread = 12
bread_slices = bread/2
ingredients = [peanut_butter, jelly, bread_slices]
number_of_sandwiches = min(ingredients)
original_sandwiches = min(ingredients)

if number_of_sandwiches >= 1:
	print "I can make {0} sandwiches".format(number_of_sandwiches)
while number_of_sandwiches >= 1:
	print "I'm making sandwich number:", number_of_sandwiches
	number_of_sandwiches = number_of_sandwiches - 1
	bread_slices = bread_slices - 1
	peanut_butter = peanut_butter - 1
	jelly = jelly - 1
	print "I have enough bread for {0} more sandwiches, enough peanut butter for {1} more and enough jelly for {2} more.".format(bread_slices, peanut_butter, jelly)	
else:
	print "All Done! We only had enough for {0} sandwiches.".format(original_sandwiches)

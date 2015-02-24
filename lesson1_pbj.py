slices_of_bread = 10
peanut_butter = 6
jelly = 2
 
# first and second goal
 
if slices_of_bread/2 <= peanut_butter and slices_of_bread/2 <= jelly:
	number_of_sandwiches = slices_of_bread/2
elif peanut_butter <= slices_of_bread/2 and peanut_butter <= jelly:
	number_of_sandwiches = peanut_butter
else:
	number_of_sandwiches = jelly
	
	
if slices_of_bread >= 2 and peanut_butter >= 1 and jelly >= 1:
	print "I can make this many sandwiches:", number_of_sandwiches
else:
	print "Looks like I don't have a lunch today."
 
#third goal
 
if slices_of_bread % 2 == 1 and peanut_butter % 2 == 1 and jelly % 2 == 1:
	print "I can also make an open-face sandwich, too."
 
bread_sandwiches = slices_of_bread/2
 
#fourth goal
 
if bread_sandwiches < peanut_butter and bread_sandwiches < jelly:
	print "You are missing bread."
elif peanut_butter < bread_sandwiches and peanut_butter < jelly:
	print "You are missing peanut butter."
else:
	print "You are missing jelly."
 
#fifth goal
 
if jelly < bread_sandwiches and jelly < peanut_butter:
	number_of_pb = peanut_butter - jelly
	print "You can make this many peanut butter and jelly sandwiches:", jelly
	print "You can always make this many peanut butter sandwiches:", number_of_pb

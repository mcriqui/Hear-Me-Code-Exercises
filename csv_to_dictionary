def csv_to_dictionary(filename):
	with open(filename, "r") as csv_file:
		csv_lines = csv_file.read().split('\n')
		mother_dictionary = {}
		for index, line in enumerate(csv_lines):
			line_items = line.split(',')
			baby_dictionary = {}
			baby_dictionary['attendee'] = line_items[3]
			baby_dictionary['description'] = line_items[1]
			baby_dictionary['notes'] = line_items[5]
			baby_dictionary['cost'] = line_items[4]
			baby_dictionary['location'] = line_items[2]
			baby_dictionary['date'] = line_items[0]
			mother_dictionary[index] = baby_dictionary
		return mother_dictionary
print csv_to_dictionary("event_info.csv")

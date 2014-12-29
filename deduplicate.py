def deduplicate(attendee_list1, attendee_list2):
	with open(attendee_list1, "r") as attendee_list1:
		attendee_list1 = attendee_list1.read()
		attendee_list1 = attendee_list1.split('\n')
	with open(attendee_list2, "r") as attendee_list2:
		attendee_list2 = attendee_list2.read()
		attendee_list2 = attendee_list2.split('\n')
	master_list = []
	master_list.extend(attendee_list1)
	master_list.extend(attendee_list2)
	master_list = list(set(master_list))
	return master_list
	# = list(set(master_list))

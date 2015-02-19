with open("contacts.csv", "r") as contacts_file:
	contacts = contacts_file.read().split('\n')

for index, contact in enumerate(contacts):
	contacts[index] = contact.split(",")

for item in contacts:
	print '<table border="1">'
	print '<tr>'
	print '<td colspan="2"> {0}</td>'.format(item[0])
	print '</tr>'
	print '<tr>'
	print '<td> Phone: {0}</td>'.format(item[1])
	print '<td> Twitter: {0}</td>'.format(item[2])
	print '<td> Github: {0}</td>'.format(item[3])
	print '</tr>'
	print '</table>'

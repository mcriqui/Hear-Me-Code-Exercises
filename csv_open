def open_csv_file(filename):
	with open(filename, "r") as csv_file:
		csv_file = csv_file.read().split("\n")
	for index, csv in enumerate(csv_file):
		csv_file[index] = csv.split("\,")
	return csv_file
print open_csv_file("contacts.csv")

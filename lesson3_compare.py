# opens and formats all_employees list
with open('all_employees.csv', 'r') as all_employees_file:
	all_employees = all_employees_file.read().split('\n')
for index, employee in enumerate(all_employees):
	all_employees[index] = employee.split(',')

# opens and formats survey list 
with open("survey.csv", "r") as survey_file:
	surveys = survey_file.read().split('\n')
for index, survey in enumerate(surveys):
	surveys[index] = survey.split(',')

# saves email address of all_employees list
all_employees_emails = []
for email in all_employees:
	all_employees_emails.append(email[1]) 

#saves 
surveys_emails = []
for email in surveys:
	surveys_emails.append(email[0])

new_list = []

print all_employees_emails
print surveys_emails
#if email address from survey is in all employees, print Shannon Turner took the survey! Here is her contact information: Twitter: @svt827 Github: @shannonturner Phone: 202-555-1234
#I would like a list of email addresses 

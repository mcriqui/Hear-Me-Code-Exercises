with open('states.txt', 'r') as states_file:
    states = states_file.read().split("\n")

print '<select>'
for state in states:
    print '\t<option value="{0}">{1}</option>'.format(state[:2], state[2:])
print '</select>'

with open('states_info.csv', 'r') as states_info_file:
	states_info = states_info_file.read().split('\n')


for index,state in enumerate(states_info):
	states_info[index] = state.split(',')


for info in states_info:
        print '<table border="1">'
        print '<tr>'
        print '<td colspan="2">{0}</td>'.format(info[1])
        print '</tr>'
        print '<tr>'
        print '<td> Rank: {0} </td>'.format(info[0])
        print '<td> Percent: {0} </td>'.format(info[4])
        print '</tr>'
        print '<tr>'
        print '<td> US House Members: {0} </td>'.format(info[3])
        print '<td> Population: {0} </td>'.format(info[2])
        print '</tr>'
        print '</table>'

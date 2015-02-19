contacts = {
	'Capn Crunch': {'phone': '212-649-5258', 'twitter': '@thecaptain', 'github': '@capncrunch'},
	'Tony the Tiger': {'phone': '635-235-5387', 'twitter': '@tonyTHEtiger', 'github': '@theyregreat'},
	'Toucan Sam': {'phone': '202-584-1856', 'twitter': '@sirtoucansam', 'github': '@toucansam'}
}

for key, value in contacts.items():
	print "{0}'s contact information is:\nPhone: {1}\nTwitter: {2}\nGithub: {3}\n".format(key, value['phone'], value['twitter'], value['github'])


for key, value in contacts.items():
	print '<table border="1">'
	print '<tr>'
	print '<td colspan="2"> {0}</td>'.format(key)
	print '</tr>'
	print '<tr>'
	print '<td> Phone: {0}</td>'.format(value['phone'])
	print '<td> Twitter: {0}</td>'.format(value['twitter'])
	print '<td> Github: {0}</td>'.format(value['github'])
	print '</tr>'
	print '</table>'

for key, value in contacts.items():
	print '<table border="1">\n<tr>\n<td colspan="2"> {0}</td>\n</tr>\n<tr>\n<td> Phone: {1}</td>\n<td> Twitter: {2}</td>\n<td> Github: {3}</td>\n</tr>\n</table>'.format(key, value['phone'], value['twitter'], value['github'])


fname = raw_input('Enter file name: ')

try:
	open(fname)
except:
	print 'File does not exist'

emails = []
emails_dic = dict()
fh = open(fname)

for line in fh:
	line = line.rstrip()
	if line.startswith('From'):
		lst_words = line.split()
		emails.append(lst_words[1])
for email in emails:
	emails_dic[email] = emails_dic.get(email, 0) + 1

emails_tup = emails_dic.items()
emails_value = []

for email, count in emails_tup:
	emails_value.append((count, email))

emails_value.sort(reverse=True)

print emails_value
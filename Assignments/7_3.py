fname = raw_input("Enter file name: ")
fhand = open(fname).read()

count = 0
for line in fhand:
	count = count + 1
	num = fhand.find(".")
	dec_num = fhand[num - 1:]

return count
return dec_num

print count
print dec_num

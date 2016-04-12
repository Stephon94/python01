score = raw_input("Enter Score: ")
score = float(score)

if score > 1.0:
	print "Error! Please Enter a score of 0.0 - 1.0."

elif score >= 0.9:
	print "You got an A! Congratulations!"

elif score >= 0.8:
	print "You got a B! Good job!"

elif score >= 0.7:
	print "You got a C! Nice try!"

elif score >= 0.6:
	print "You got a D! Do better next time! "

elif score < 0.6:
	print "You got a F! You must study harder!"


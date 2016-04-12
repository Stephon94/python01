hours = raw_input("How many hours did you work? ")
payrate = raw_input("How much do you get paid per hour? ")
hours = float(hours)
payrate = float(payrate)
regpay = payrate * hours 
Ovrhours = hours - 40
Ovrpayrate = payrate * 1.50
Ovrpay = Ovrhours * Ovrpayrate + regpay 

if hours > 40 :
	hours = hours - Ovrhours
	regpay = payrate * hours
	Ovrpay = Ovrhours * Ovrpayrate + regpay
	print "Your payment is (including Overtime): $",Ovrpay

else :
	print "Your payment is: $",regpay



import time
def now_time():
	t=time.time()
	a=t % (3600*24)
	hour=a//3600
	c=a%3600
	minute=c//60
	second=c%60
	if hour<1:
		print("12",":",minute,":",second,"AM")
	elif 1<= hour< 12:
		print (hour,":",minute,":",second,"AM")
	elif hour==12:
		print (hour,":",minute,":",second,"PM")
	elif hour>12:
		print (hour-12,":",minute,":",second,"PM")
	elif hour == 24:
		print ("12",":",minute,":",second,"AM")
now_time()

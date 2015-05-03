from twilio.rest import TwilioRestClient
import sys

config_sc = open("config.sc", "r")
detail = config_sc.readlines()
ACCOUNT_SID = detail[0][detail[0].find('"')+1 : detail[0].rfind('"')]
AUTH_TOKEN = detail[1][detail[1].find('"')+1 : detail[1].rfind('"')]
twil_number = detail[3][detail[3].find('"')+1 : detail[3].rfind('"')]

numb = open("numbers.txt", "r")
con = numb.readlines()
from twilio.rest import TwilioRestClient
for i in con:
	print i
	ph_number = i
	std_msg = sys.argv[1]
	#print std_msg
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
	message = client.messages.create(body=(std_msg),
		to=ph_number, from_=twil_number)

	#print message.sid
	#print ("sms sent to " + ph_number)
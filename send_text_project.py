from twilio import rest#TwilioRestClient
#from twilio.rest import TwilioRestClient //. signifies folder

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC8f9e7538106e50d612189ccb6478995e"
auth_token  = "299be2e1dfdc14159277ae971e2561b0"
client = rest.TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="danish test",
    to="+17133920302",    # Replace with your phone number
    from_="+18327722140") # Replace with your Twilio number
print (message.sid)

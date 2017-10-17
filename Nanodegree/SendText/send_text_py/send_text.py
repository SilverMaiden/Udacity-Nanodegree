from twilio.rest import Client

#Account Side and Auth Token

account_sid = "AC33edeaa4117e4f98a6312624f08b83fa"
auth_token = "2b14f31754460de9d8043356030ab517"
client = Client(account_sid, auth_token)

message = client.messages.create(body="My name is Humaira?",
                                     to="+13108040680",
                                     from_="+14153648157")

print(message.sid)



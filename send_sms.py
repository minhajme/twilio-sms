from twilio.rest import Client

TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

message = client.messages.create(to="", from_="", body="vai aj office e asben?")

print(message.sid)

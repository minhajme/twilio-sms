from twilio.rest import Client
import datetime
import csv
from pytz import timezone

# date format is DD-MM-YYYY
from_date = '16-10-2017'
to_date = '21-10-2017'
from_datetime = datetime.datetime(year=2017, month=10, day=16, tzinfo=timezone('EST'))
to_datetime = datetime.datetime(year=2017, month=10, day=21, tzinfo=timezone('EST'))

TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

with open('dump.csv', 'w') as csvfile:
    wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

    wr.writerow(['date_sent', 'date_created', 'direction', 'status', 'from_', 'to', 'body', 'sid', 'error_code', 'error_message'])

    delivery_success = 0
    delivery_fail = 0
    delivered_not = 0

    for message in client.messages.list(date_sent_before=to_datetime, date_sent_after=from_datetime):
        if message.status == 'delivered':
            delivery_success += 1
        if message.status == 'failed':
            delivery_fail += 1
        if message.status in ['sent', 'undelivered']:
            delivered_not += 1

        row = [message.date_sent, message.date_created, message.direction, message.status, message.from_, message.to, message.body, message.sid, message.error_code,
               message.error_message]
        wr.writerow(row)
csvfile.close()

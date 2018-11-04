import csv

with open('dump.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    undelivered_error_messages = []
    delivery_success = 0
    delivery_fail = 0
    delivered_not = 0
    total = 0
    received = 0
    queued = 0
    sending = 0
    sent = 0
    for message in reader:
        total += 1
        if message['status'] == 'undelivered':
            delivered_not += 1
            undelivered_error_messages.append(message['error_message'])
        if message['status'] == 'delivered':
            delivery_success += 1
        if message['status'] == 'failed':
            delivery_fail += 1
        if message['status'] == 'received':
            received += 1
        if message['status'] == 'queued':
            queued += 1
        if message['status'] == 'sending':
            sending += 1
        if message['status'] == 'sent':
            sent += 1

    print("total: {}, delivery success: {}, delivery fail(status='fail'): {}, not delivered: {}, received = {}, queued: {}, sending: {}, sent: {}".format(total, delivery_success,
                                                                                                                                                          delivery_fail,
                                                                                                                                                          delivered_not, received,
                                                                                                                                                          queued, sending, sent))
    print('not delivered reasons: {}'.format(','.join(set(undelivered_error_messages))))
csvfile.close()

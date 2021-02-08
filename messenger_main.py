import datetime
import time

db = [] # database of messages
# send_message == put message into db
# get_message == output db's messages
def send_message(name, text):
    # TODO: make message
    # TODO: add to db
    message = {
        'time': time.time(),
        'name': name,
        'text': text
                }
    db.append(message)

def get_message(after):
    result = []
    for message in db:
        if message['time'] > after:
            result.append(message)
    return result

send_message('123','123')
send_message('123','6776')
send_message('123','145')
t1 = db[-1]['time']
print(get_message(t1))

send_message('123','123')
send_message('123','6776')
print(get_message(t1))

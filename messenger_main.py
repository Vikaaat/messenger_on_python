import datetime
import time

db = [] # database
# send_message == put message into db
# get_message == output db's messages
def send_message(name, text):
    # TODO: make message
    # TODO: add to db
    message = {
        'time':time.time(),
        'name': name,
        'text': text
                }
    db.append(message)

def get_message():
    return

send_message('123','123')
send_message('123','6776')
send_message('123','145')
print(db)
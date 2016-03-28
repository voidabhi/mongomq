import zmq
from config import PORT

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % PORT)

while True:
    topic = random.randrange(9999,10005)
    messagedata = random.randrange(1,215) - 80
    print "%d %d" % (topic, messagedata)
    socket.send("%d %d" % (topic, messagedata))
    time.sleep(1)

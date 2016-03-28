import sys
import zmq
from config import PORT

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect ("tcp://localhost:%s" % PORT)
socket.setsockopt(zmq.SUBSCRIBE, topicfilter)

# Process 5 updates
total_value = 0
for update_nbr in range (5):
    string = socket.recv()
    topic, messagedata = string.split()
    total_value += int(messagedata)
    print topic, messagedata

print "Average messagedata value for topic '%s' was %dF" % (topicfilter, total_value / update_nbr)

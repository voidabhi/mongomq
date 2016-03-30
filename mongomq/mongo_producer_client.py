import time
import zmq
import pprint

def producer():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind("tcp://127.0.0.1:5557")
    # Start your result manager and workers before you start your producers
    for num in xrange(20000):
        work_message = { 'num' : num }
        zmq_socket.send_json(work_message)

producer()


def result_collector():
    context = zmq.Context()
    results_receiver = context.socket(zmq.PULL)
    results_receiver.bind("tcp://127.0.0.1:5558")
    collecter_data = {}
    for x in xrange(1000):
        result = results_receiver.recv_json()
        if collecter_data.has_key(result['consumer']):
            collecter_data[result['consumer']] = collecter_data[result['consumer']] + 1
        else:
            collecter_data[result['consumer']] = 1
        if x == 999:
            pprint.pprint(collecter_data)

result_collector()




import zmq
from constants import (
    ZMQ_DEFAULT_HOST,
    ZMQ_DEFAULT_PORT
)

import cloud

class QueryPublisher(object):
    """A query publisher"""

    def __init__(self, zmqconfig={}):
        """Initialize publisher"""
        self.zmqconfig = zmqconfig
        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.REQ)
        self._socket.connect('tcp://{}:{}'.format(self.zmqconfig.get('host', ZMQ_DEFAULT_HOST), self.zmqconfig.get('port', ZMQ_DEFAULT_PORT)))

    def _build(self, dbname, colname, cmd):
        return {
            'dbname': dbname,
            'colname': colname,
            'cmd': cmd
        }

    def publish(self, dbname, colname, cmd, callback):
        """Return the result of query in callback"""
        query = self._build(dbname, colname, cmd)
        self._socket.send_pyobj(query)
        self._socket.recv()
        callback_string = cloud.serialization.cloudpickle.dumps(callback)
        self._socket.send_pyobj(callback_string)
        self._socket.recv()

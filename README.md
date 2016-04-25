
## mongomq

Run mongo queries by pushing it to zmq


## Doc

```python

from mongomq import QueryExecutor, QueryPublisher
import pprint

def query_result(curr):
  pprint(curr)

def start_executor():
  qe = QueryExecutor()
  qe.start()

def publish_queries()
  qp1 = QueryPublisher()
  qp1.publish('db1', 'colA', 'find({})', query_result)
  qp2 = QueryPublisher()
  qp1.publish('db2', 'colB', 'find({})', query_result)

if __name__ == '__main__':
  start_executor()
  publish_queries()
```

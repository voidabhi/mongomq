
## mongomq

Mongo query consumer


## Documentation

```python

from mongomq import QueryExecutor, QueryPublisher
from pprint import pprint

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

### Contributing

- Please use the [issue tracker](https://github.com/voidabhi/mongomq/issues) to report any bugs or file feature requests.

## License

```
Copyright 2016 Abhijeet Mohan - https://github.com/voidabhi/mongomq

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

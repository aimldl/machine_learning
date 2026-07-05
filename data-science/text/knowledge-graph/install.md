



```bash
(base) $ conda create -n knowledge_graph python=3 anaconda
  ...
Proceed ([y]/n)? y
  ...
(base) $
```

```bash
To activate this environment, use
$ conda activate knowledge_graph
To deactivate an active environment, use
$ conda deactivate

```

```bash
(base) $ conda activate knowledge_graph
(knowledge_graph) $
```

[sparql-client 3.8](https://pypi.org/project/sparql-client/)

```bash
$ pip install sparql-client
```



```
$ python
  ...
>>> import sparql
>>> endpoint='http://ko.dbpedia.org/sparql'
>>> s = sparql.Service(endpoint, "utf-8", "GET")
>>> result = s.query(statement)
If you have made a SELECT query, then you can read the result with fetchone() or fetchall():

for row in result.fetchone():

```


# Click the Variables button, above, to create your own variables.
GET ${exampleVariable1} // _search
{
  "query": {
    "${exampleVariable2}": {} // match_all
  }
}
## Cluster Health Check
GET /_cat/health?v

## List Nodes (the defult is = 4 nodes)
GET /_cat/nodes?v

## List Indices
GET /_cat/indices?v


## Create Index
PUT /sales
##{
  #"acknowledged": true,
  #"shards_acknowledged": true,
  #"index": "sales"
#}
##
GET /_cat/indices?v


## Create data
PUT /sales/_doc/112
  {
    "orderID":"1",
    "orderAmount": 100
  }
GET /sales/_doc/112
DELETE /sales/_doc/112

DELETE /sales
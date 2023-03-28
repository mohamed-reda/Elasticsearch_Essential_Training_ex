colors = {'red', 'orange', 'yellow', 'green', 'red', 'blue'}
print(colors)
print(colors)
print(colors)
print(colors)

# from elasticsearch import Elasticsearch
#
# # create an Elasticsearch client instance
# es = Elasticsearch(['https://my-deployment-3f8516.es.us-central1.gcp.cloud.es.io'])
#
# # define a search query
# query = {
#     "query": {
#         "match": {
#             "field_name": "query_string"
#         }
#     }
# }
#
# # send the search request
# res = es.search(index="index_name", body=query, )
#
# # print the results
# print(res)

from elasticsearch import Elasticsearch
from requests_aws4auth import AWS4Auth

# Elasticsearch host URL
host = 'https://my-deployment-3f8516.es.us-central1.gcp.cloud.es.io'

# AWS region where your Elasticsearch service is deployed
region = 'your-aws-region'

# AWS access key and secret key
access_key = 'your-access-key'
secret_key = 'your-secret-key'

# Elasticsearch API key
api_key = 'your-api-key'

# AWS authentication for Elasticsearch
awsauth = AWS4Auth(access_key, secret_key, region, 'es')

# Elasticsearch client instance with AWS authentication and API key
es = Elasticsearch(
    hosts=[{'host': host, 'port': 443}],
    http_auth=awsauth,
    use_ssl=True,
    verify_certs=True,
    headers={'Authorization': 'ApiKey ' + api_key}
)

# define a search query
query = {
    "query": {
        "match": {
            "field_name": "query_string"
        }
    }
}

# send the search request
res = es.search(index="index_name", body=query)

# print the results
print(res)

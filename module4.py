"""
# Module 4 - Querying Data

## Sort data

GET bank/account/_search
GET /bank/_search?q=*&sort=balance:asc

## Query DSL

#this is the full query template:

GET /bank/_search
{
"query": { }
}

the query:
{
"match": { "key":"value"}

}
#get what match that value.

---
the query:
{
    "bool": {
         "must":[
            "match": { "key":"value"},
            "match": { "key2":"value2 "},
        ]
    }
}

---
the query:
{
    "bool": {
         "must_not":[
            "match": { "key":"value"},
            "match": { "key2":"value2 "},
        ]
    }
}

---
the query:
{
    "bool": {
         "must": ["match": { "key":"value"}],
        "must_not": ["match": { "key2":"value2 "}]
    }
}

#get what match that value.

{
    "bool": {
        "should": [
            { "match": {"state": "CA"} },
            { "match": {"lastname": {"query": "Smith", "boost": 3} } }
        ]
    }
}
#"boost": 3 meaning that this condition is more important than the first one

---
##the range
{
    "bool": {
        "must": { "match_all": {} },
            "filter": {
                "range": {
                "balance": {
                    "gte": 20000,
                    "lte": 30000,
                    "boost": 3
                }
            }
        }
    }
}



---
## Query DSL

GET /bank/_search
{
"query": { "match_all": {} }
}

## Query DSL - Sort

GET /bank/_search
{
"query": { "match_all": {} },
"sort": [
{ "account_number": "asc" }
]
}

GET /bank/_search
{
"query": { "match_all": {} },
"sort": { "balance": { "order": "desc" } }
}

GET /bank/_search
{
"query": { "match_all": {} },
"sort": [
{ "account_number": "asc" },
{ "balance" : "asc"}
]
}

## Search by Size & From

GET /bank/_search
{
"query": { "match_all": {} },
"size": 1
}

GET /bank/_search
{
"query": { "match_all": {} },
"from": 10,
"size": 10
}

## Show Selected Fields

GET /bank/_search
{
"query": { "match_all": {} },
"_source": ["account_number", "balance"]
}

## Match

GET /bank/_search
{
"query": {
"match": {
"account_number": 20
}
}
}

# Search for mill

GET /bank/_search
{
"query": { "match": { "address": "mill" } }
}

# Search for mill or lane

GET /bank/_search
{
"query": { "match": { "address": "mill lane" } }
}

## Search for " mill lane"

GET /bank/_search
{
"query": { "match_phrase": { "address": "mill lane" } }
}

## Bool Query - Must

GET /bank/_search
{
"query": {
"bool": {
"must": [
{ "match": { "address": "mill" } },
{ "match": { "address": "lane" } }
]
}
}
}

## Bool Query - Should

GET /bank/_search
{
"query": {
"bool": {
"should": [
{ "match": { "address": "mill" } },
{ "match": { "address": "lane" } }
]
}
}
}

## Bool Query - Must Not

GET /bank/_search
{
"query": {
"bool": {
"must_not": [
{ "match": { "address": "mill" } },
{ "match": { "address": "lane" } }
]
}
}
}

## Bool Query - Combine

GET /bank/_search
{
"query": {
"bool": {
"must": [
{ "match": { "age": "40" } }
],
"must_not": [
{ "match": { "state": "ID" } }
]
}
}
}

# Exercise

# find CA accounts only

GET bank/account/_search
{
"query": {
"match": {
"state": "CA"
}
}
}

# find "Techade" accounts in CA only

GET bank/account/_search
{
"query": {
"bool": {
"must": [
{ "match": {"state": "CA"} },
{ "match": {"employer": "Techade"}}
]
}
}
}

# find non "Techade" accounts outside of CA

GET bank/account/_search
{
"query": {
"bool": {
"must_not": [
{ "match": {"state": "CA"} },
{ "match": {"employer": "Techade"}}
]
}
}
}

## Data Filtering with Filter and Range

GET /bank/_search
{
"query": {
"bool": {
"must": { "match_all": {} },
"filter": {
"range": {
"balance": {
"gte": 20000,
"lte": 30000
}
}
}
}
}
}

# Term Query

POST _search
{
"query": {
"term" : { "user" : "Kimchy" }
}
}

GET bank/account/_search
{
"query": {
"term": { "account_number": 516 }
}
}

# Boost

GET bank/account/_search
{
"query": {
"bool": {
"should": [
{ "match": {"state": "CA"} },
{ "match": {
"lastname": {
"query": "Smith",
"boost": 3
}
}
}
]
}
}
}

# Ex: Show all accounts between 516 and 851

GET bank/account/_search
{
"query": {
"range": {
"account_number": {
"gte": 516,
"lte": 851
}
}
}
}

# Show all account holders older than 35

GET bank/account/_search
{
"query": {
"range": {
"age": {
"gt": 35
}
}
}
}

# Tokenization

GET bank/_analyze
{
"tokenizer" : "standard",
"text" : "The Moon is Made of Cheese Some Say"
}

# Mixed String

GET bank/_analyze
{
"tokenizer" : "standard",
"text" : "The Moon-is-Made of Cheese.Some Say$"
}

# Uset the letter tokenizer

GET bank/_analyze
{
"tokenizer" : "letter",
"text" : "The Moon-is-Made of Cheese.Some Say$"
}

# How about a URL

GET bank/_analyze
{
"tokenizer": "standard",
"text": "you@example.com login at https://bensullins.com attempt"
}

GET bank/_analyze
{
"tokenizer": "uax_url_email",
"text": "you@example.com login at https://bensullins.com attempt"
}

# Where it breaks, two fields with diff analyzers

PUT /idx1
{
"mappings": {
"t1": {
"properties": {
"title": {
"type": "text",
"analyzer" : "standard"
},
"english_title": {
"type":     "text",
"analyzer": "english"
}
}
}
}
}

GET idx1

GET idx1/_analyze
{
"field": "title",
"text": "Bears"
}

GET idx1/_analyze
{
"field": "english_title",
"text": "Bears"
}
"""

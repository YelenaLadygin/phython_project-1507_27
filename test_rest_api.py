
import requests
import json
import pytest

class RestObject:
    def __init__(self, d):
        self.__dict__ = d
    def __str__(self):
        result = ""
        for k, v in self.__dict__.items():
            result += k
            result += " : "
            result += str(v)
            result += '\n'
        return result

def test_rest_api_get_todos():
    resp = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    d = json.loads(resp.content)
    t = RestObject(d)
    assert t.id == 1
    assert t.userId == 1
    assert t.title == 'delectus aut autem'
    assert t.completed == False

def test_rest_api_get_products():
    resp = requests.get("http://http://127.0.0.1:5000/Products/1")
    d = json.loads(resp.content)
    t = RestObject(d)
    assert t.id == 1
    assert t.title == 'Meat'


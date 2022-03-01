"""Integration tests for app.py"""
import json
from typing import Type
from flask.testing import FlaskClient
from flask.wrappers import Response
import pytest

from bank_api.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_account_creation(client: FlaskClient):
    # Use the client to make requests e.g.:
    # client.post(...)
    # client.get(...)
    # https://flask.palletsprojects.com/en/1.1.x/testing/
    #pass
    check = client.post('/accounts/Test')

    assert check.status_code == 200  #successfull response



def test_check_created_account(client: FlaskClient):
    check2 = client.get('/accounts/Test')

    assert check2.status_code == 200  #successfull response

    json_data = check2.data.decode()
    data = json.loads(json_data)
    assert data['name'] == 'Test'

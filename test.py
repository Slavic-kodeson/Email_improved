from unittest.mock import patch
import pytest
import requests


@pytest.fixture
def adresa_api():
    endpoints = {
        "contact": "http://0.0.0.0:4000/api/contact",
        "intership": "http://0.0.0.0:4000/api/intership",
        "careers": "http://0.0.0.0:4000/api/careers"
    }

    return endpoints


def test_contact(adresa_api):

    email_content = {
        "Company": "company",
        "Name": "Jim",
        "Phone": "008979283",
        "Email": "name@mail.com",
        "Interest": "buy",
        "Message": "message"
    }

    addresa_contact = adresa_api["contact"]

    with patch('requests.post') as mock_post:
        mock_post.return_value.status_code = 200
        response = requests.post(addresa_contact, json=email_content)
    assert response.status_code == 200


def test_internship(adresa_api):

    email_content = {
        "Name": "Jim",
        "Job": "IT",
        "Phone": "008979283",
        "Sender": "name@mail.com",
        "Message": "message"
    }

    addresa_intership = adresa_api["intership"]

    with patch('requests.post') as mock_post:
        mock_post.return_value.status_code = 200
        response = requests.post(addresa_intership, json=email_content)
    assert response.status_code == 200


def test_apply_job(adresa_api):

    email_content = {
        "Name": "Jim",
        "Job": "Python",
        "Phone": "008979283",
        "Sender": "name@java.com",
        "Message": "message"
    }

    adresa_careers = adresa_api["careers"]

    with patch('requests.post') as mock_post:
        mock_post.return_value.status_code = 200
        response = requests.post(adresa_careers, json=email_content)
    assert response.status_code == 200

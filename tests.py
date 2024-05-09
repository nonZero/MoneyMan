from django.test import Client


def test_one_plus_one_is_three(client: Client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.content == b"hello <b>world!</b>"

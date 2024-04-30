def test_app(client):
    response = client.get("/")
    assert b"<p>Hello world!</p>" in response.data

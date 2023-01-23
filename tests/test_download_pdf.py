def test_get_cat_fact(client):
    response = client.get("/")
    assert response.request.path == "/"
    assert b"<h1>Here's a random cat fact</h1>" in response.data

    #TODO How would you change this test and what other tests would you write

import pytest
import download_pdf


@pytest.fixture()
def app():
    app = download_pdf.app
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()
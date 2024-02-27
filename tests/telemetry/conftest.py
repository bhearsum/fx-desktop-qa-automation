import pytest


@pytest.fixture(scope="session")
def httpserver_listen_address():
    return ("127.0.0.1", 5312)


@pytest.fixture()
def test_opts():
    return [
        ("browser.search.region", "US"),
        ("privacy.donottrackheader.enabled", False),
        ("telemetry.fog.test.localhost_port", 5312),
        ("datareporting.healthreport.uploadEnabled", True),
    ]

import main


def test_serves():
    servers = main.app.servers
    for server in servers:
        if "https://red-canids-api.azurewebsites.net/" in server["url"]:
            assert True
            return
    assert False


def test_root_patch():
    assert main.app.root_path == "https://red-canids-api.azurewebsites.net/"


def test_docs_url():
    assert main.app.docs_url == "/red-canids-api-swagger"


def test_redoc_url():
    assert main.app.redoc_url == "/red-canids-api-docs"


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Set browser on which we would like to execute tests. Available: chrome, firefox, safari"
    )
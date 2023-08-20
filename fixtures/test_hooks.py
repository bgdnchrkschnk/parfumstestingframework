
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Set browser on which we would like to execute tests. Available: chrome, firefox, safari"
    )


def pytest_generate_tests(metafunc):
    if "browser" in metafunc.fixturenames:
        browsers = metafunc.config.getoption("--browser").split(", ")
        metafunc.parametrize("browser", browsers, indirect=True)


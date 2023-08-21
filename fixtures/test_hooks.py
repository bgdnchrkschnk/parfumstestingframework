import yaml
from conf.envclass import Env


# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser", action="store", default="chrome", help="Set browser on which we would like to execute tests. Available: chrome, firefox, safari"
#     )
#

# def pytest_generate_tests(metafunc):
#     if "browser" in metafunc.fixturenames:
#         browsers = metafunc.config.getoption("--browser").split(", ")
#         metafunc.parametrize("browser", browsers, indirect=True)


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="prod", help="Env to use")


def pytest_generate_tests(metafunc):
    if "browser" in metafunc.fixturenames:
        env_name = metafunc.config.getoption("--env")
        env_config_path = None
        env_config = None

        # abs_path = __file__.split(os.path.sep)
        # if "fixtures" in abs_path:
        #     env_config_path = os.path.join(*abs_path[:abs_path.index("fixtures")], "conf", f"{env_name}.yml")
        # elif "test" in abs_path:
        #     env_config_path = os.path.join(*abs_path[:abs_path.index("test")], "conf", f"{env_name}.yml")
        #
        # if sys.platform == "win32":
        #     env_config_path.replace(":", f":{os.path.sep}")
        # else:
        #     env_config_path = f"{os.path.sep}{env_config_path}"

        if 'prod' in env_name:
            env_config_path = Env.PROD.value
        elif 'dev' in env_name:
            env_config_path = Env.DEV.value
        elif 'stage' in env_name:
            env_config_path = Env.STAGE.value
        else:
            raise AssertionError("Wrong browser name entered!")

        with open(env_config_path, "r") as conf:
            env_config = yaml.load(conf, Loader=yaml.FullLoader)

        url = env_config["url"]
        browsers = env_config["browsers"]

        parameters = [(url, browser) for browser in browsers]

        metafunc.parametrize("browser", parameters, indirect=True)



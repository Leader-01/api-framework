
import yaml


def test_yaml2():

    env = {
        "default": "dev",
        "test":
        {
        "dev": "127.0.0.1",
        "test": "127.0.0.2"
        }
    }
    with open("env1.yaml", "w") as f:
        yaml.safe_dump(data=env, stream=f)

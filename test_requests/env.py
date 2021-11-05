
import requests
import yaml


class Api():
    env = yaml.safe_load(open("env.yaml"))

    def send(self, data: dict):
        #
        data["url"] = str(data["url"]).replace("domin", self.env["domin"][self.env["default"]])

        r = requests.request(method=data["method"], url=data["url"], headers=data["headers"])
        return r
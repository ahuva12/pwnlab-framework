from utils import LabUtils
from runner import Runner

class Lab:
    def __init__(self):
        self.challenges = {
            "overflow": "./overflow",
            "uaf": "./uaf",
            "fmt": "./format"
        }

    def run_challenge(self, name, input_data):
        if name not in self.challenges:
            return {"error": "unknown challenge"}
            
        runner = Runner(self.challenges[name])
        result = runner.run(input_data)

        binary = self.challenges[name]
        LabUtils.log_result(binary, result)
        return result
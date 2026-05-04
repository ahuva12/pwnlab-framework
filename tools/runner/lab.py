import os
from utils import LabUtils
from runner import Runner

class Lab:
    def __init__(self):
        self.base_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../build")
        )    
        
        self.challenges = {
            "overflow": os.path.join(self.base_dir, "vuln_basic"),
            "uaf": os.path.join(self.base_dir, "uaf"),
            "fmt": os.path.join(self.base_dir, "fmt"),
        }

    def run_challenge(self, name, input_data, aslr=True):
        if name not in self.challenges:
            return {"error": "unknown challenge"}
            
        runner = Runner(self.challenges[name])
        result = runner.run(input_data, aslr=aslr)
        
        result["aslr"] = aslr 
       
        binary = self.challenges[name]
        LabUtils.log_result(binary, result)
        return result
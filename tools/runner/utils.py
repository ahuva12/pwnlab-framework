import os
import json
import datetime

class LabUtils:
    @staticmethod
    def log_result(binary, result):
        timestamp = datetime.datetime.now().isoformat()

        log_entry = {
            "timestamp": timestamp,
            "binary": binary,
            "result": result
        }

        with open("run_logs.txt", "a") as f:
            f.write(json.dumps(log_entry) + "\n")
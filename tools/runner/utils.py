import os
import json

class LabUtils:
    @staticmethod
    def disable_aslr():
        os.system("echo 0 | sudo tee /proc/sys/kernel/randomize_va_space")

    @staticmethod
    def enable_aslr():
        os.system("echo 2 | sudo tee /proc/sys/kernel/randomize_va_space")

    @staticmethod
    def log_result(binary, result):
        with open("run_logs.txt", "a") as f:
            f.write(f"\n--- {binary} ---\n")
            f.write(json.dumps(result, indent=2))
import subprocess

class Runner:
    def __init__(self, binary_path):
        self.binary_path = binary_path

    def run(self, input_data="", timeout=2):
        try:
            process = subprocess.Popen(
                [self.binary_path],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            stdout, stderr = process.communicate(
                input=input_data,
                timeout=timeout
            )

            return {
                "stdout": stdout,
                "stderr": stderr,
                "return_code": process.returncode
            }

        except FileNotFoundError:
            return {"error": "binary not found"}

        except subprocess.TimeoutExpired:
            process.kill()
            process.communicate()
            return {"error": "timeout"}
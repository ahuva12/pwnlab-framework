import subprocess
import resource

class Runner:
    def __init__(self, binary_path):
        self.binary_path = binary_path
        
    @staticmethod
    def set_limits(cpu=1, mem_mb=64):
        resource.setrlimit(resource.RLIMIT_CPU, (cpu, cpu))
        resource.setrlimit(resource.RLIMIT_AS, (mem_mb*1024*1024, mem_mb*1024*1024))

    def run(self, input_data="", timeout=2, aslr=True, cpu=1, mem_mb=64):
        try:
            cmd = [self.binary_path]
            
            if not aslr:
                cmd = ["setarch", "x86_64", "-R"] + cmd

            process = subprocess.Popen(
                cmd,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                preexec_fn=lambda: Runner.set_limits(cpu, mem_mb)
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
            try:
                process.kill()
                process.communicate()
            except Exception:
                pass
            return {"error": "timeout"}
import subprocess

result = subprocess.run(["SQLtest.exe"], capture_output=True, text=True)
print(result.stdout)

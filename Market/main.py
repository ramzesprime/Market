import subprocess

print("Запускаю скрипты...")
subprocess.run(["python", "SQLconnect.py"])
subprocess.run(["python", "cppLINKER.py"])
print("Все скрипты выполнены!")

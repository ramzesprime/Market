import subprocess
import GUI

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.OKCYAN+"///MARKET MENEGMENT APPLICATION///!")

print(bcolors.HEADER + "Linking files...")
try:
    subprocess.run(["python", "SQLconnect.py"])
    subprocess.run(["python", "cppLINKER.py"])
    print("All files linked!")
except Exception as e:
    print(bcolors.WARNING+"Error with file linking")

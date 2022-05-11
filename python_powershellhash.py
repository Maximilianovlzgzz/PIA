import subprocess

def valor_hash():
    comando = "HashAcquire.ps1"
    lineaPS = "powershell -Executionpolicy ByPass -file "+ comando
    runningProcesses = subprocess.check_output(lineaPS)





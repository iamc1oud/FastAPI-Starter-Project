import subprocess

# Execute the command
subprocess.run(["uvicorn", "main:app", "--reload"])

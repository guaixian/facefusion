import subprocess
import sys

import uvicorn
from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def get_state():
	return {"state": "ok"}



@app.get('/change')
async def change():
	print("change")
	commands = [
		sys.executable,
		'run.py',
		'-s', '.assets/examples/source.jpg',
		'-t', '.assets/examples/target-240p.jpg',
		'-o', 'outfile',
		'--headless',
		'--execution-providers', 'cpu',
		'--output-image-quality', '100',
		'--output-image-resolution', '1024x1024'
	]
	run = subprocess.run(commands, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

	return run.stdout


















if __name__ == "__main__":
	uvicorn.run("exfec:app", host="127.0.0.1", port=8002)

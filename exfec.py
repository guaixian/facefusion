from gradio_client import Client,handle_file
import imageio.v2 as imageio
from fastapi import FastAPI,Request
import cv2
app=FastAPI()


@app.get('/')
async def index():
	return 'ok'


@app.post('/changeface')
async def changeface(request:Request):
	try:
		getdata = await request.json()
		print(getdata)
	except:
		return 400
	client = Client("http://127.0.0.1:7860",timeout=6000)
	source_path=getdata['source_path']
	target_path=getdata['target_path']
	result_1 = client.predict(
		[handle_file(source_path)],
		fn_index=35
	)
	result_2 = client.predict(
		handle_file(target_path),
		fn_index=36
	)
	client.predict(
		fn_index=105
	)

	if "mp4" not in target_path :
		height, width = imageio.imread(target_path).shape[:2]
		client.predict(
			f"{width}x{height}",
			fn_index=23
		)
		result_4 = client.predict(
			fn_index=38
		)
		return result_4[0]['value']
	else:
		video = cv2.VideoCapture(target_path)
		width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
		height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
		video.release()
		client.predict(
			80,
			fn_index=26
		)
		client.predict(
			f"{width}x{height}",
			fn_index=27
		)
		client.predict(
			18,
			fn_index=28
		)
		result_4 = client.predict(
			fn_index=38
		)
		return result_4[1]['value']['video']

if __name__ == '__main__':
	import uvicorn
	uvicorn.run(app, host='127.0.0.1', port=8002)

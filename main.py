from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
import requests

app = FastAPI()

@app.get("/")
async def root():
    return FileResponse("image.png")
    #return {"Instructions":"At the end of the URL, add your desired timeframe and sunsign!"
            #"for example:"}
    
@app.get("/{time}/{sign}")
async def your_sign(time: str, sign: str):
    horo = f"http://horoscope-api.herokuapp.com/horoscope/{time}/{sign}"
    response = requests.get(horo)
    return response.json()
    
if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
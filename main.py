from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def serve_static_html():
    return FileResponse("certificate.html")


# You can run this app using: uvicorn filename:app --reload

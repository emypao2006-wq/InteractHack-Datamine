import uvicorn

if __name__ == "__main__":
    # Esto lanza tu app FastAPI
    # main es el nombre del archivo (main.py)
    # app es el objeto FastAPI dentro de main.py
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

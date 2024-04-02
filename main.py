from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return "<h1> Minha aplicação com FastAPI</h1>"

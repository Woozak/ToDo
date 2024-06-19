from fastapi import FastAPI

app = FastAPI()


@app.post("/create/")
def create_task():
    pass


@app.get("/get/")
def get_task():
    pass


@app.post("/update/")
def update_task():
    pass


@app.get("/delete/{task_id}")
def delete_task():
    pass

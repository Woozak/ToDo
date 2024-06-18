from fastapi import FastAPI

app = FastAPI()


@app.post('/create/')
async def create_task():
    pass


@app.get('/get/')
async def get_task():
    pass


@app.post('/update/')
async def update_task():
    pass


@app.post('delete')
async def delete_task():
    pass

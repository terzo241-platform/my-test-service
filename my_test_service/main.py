from fastapi import FastAPI

app = FastAPI(title="my-test-service")


@app.get("/")
async def root():
    return {"service": "my-test-service", "status": "running"}


@app.get("/health")
async def health():
    return {"status": "ok"}

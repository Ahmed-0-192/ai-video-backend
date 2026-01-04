from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Job(BaseModel):
    prompt: str

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/run")
def run(job: Job):
    # Placeholder: yahan baad me actual video generation call aayegi
    return {"status": "received", "prompt": job.prompt}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

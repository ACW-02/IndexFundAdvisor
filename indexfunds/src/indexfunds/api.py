from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from indexfunds.crew import IndexAdvisorCrew
import os
import markdown

# Get absolute path to static directory
static_dir = os.path.join(os.path.dirname(__file__), "static")
# Get absolute path to templates directory
templates_dir = os.path.join(os.path.dirname(__file__), "templates")

app = FastAPI()

# Mount static folder for assets (e.g. CSS)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Set template directory
templates = Jinja2Templates(directory=templates_dir)

class Question(BaseModel):
    question: str

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {"request": request})

@app.post("/ask")
async def ask_bot(question: Question):
    try:
        result = IndexAdvisorCrew().crew().kickoff(inputs={"topic": question.question})

        # Read markdown output
        try:
            with open("index_output1.md", "r", encoding="utf-8") as file:
                summary_markdown = file.read()
        except:
            summary_markdown = result.final_output or "No output was saved."

        # Convert markdown to HTML
        html_output = markdown.markdown(summary_markdown)

        return JSONResponse(content={
            "answer": html_output,
            "thinking": "Verbose logs not available in this version."
        })

    except Exception as e:
        return JSONResponse(content={
            "answer": "❌ An error occurred.",
            "thinking": str(e)
        })

# Run API cd to src
# uvicorn indexfunds.api:app --reload

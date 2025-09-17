# python imports
from dotenv import load_dotenv
import os
import json
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from langgraph import StateGraph
import uvicorn
import traceback

# modules imports
from modules.agent_orchestrator import agent_orchestrator
from modules.agent_scholar import agent_scholar
from modules.agent_market import agent_market
from modules.agent_summarizer import agent_summarizer
from modules.agent_critic import agent_critic
from modules.agent_report_gen import agent_report_gen
from modules.agent_rag import agent_rag

# utils imports
from utils.logger import log_status
from utils.readable_timestamp import get_readable_timestamp
from utils.root_resp import RootResponseModel
from utils.graph_state import GraphState

# paths
constants_json_path = os.path.abspath("./constants.json")

# load .env and required keys
log_status(status="INFO", source="/app.py", timestamp=get_readable_timestamp(), msg="Loading secrets from .env\n")
load_dotenv()

# load constants.json
log_status(status="INFO", source="/app.py", timestamp=get_readable_timestamp(), msg="Loading constants.json\n")
f_ptr = open(constants_json_path, "r", encoding="utf-8")
constants = json.load(f_ptr)
f_ptr.close()

# build FastAPI app
log_status(status="INFO", source="/app.py", timestamp=get_readable_timestamp(), msg="Creating instance of FastAPI\n")
app = FastAPI(title=constants["FASTAPI_APP_TITLE"], version="0.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins - for development
    # For production, use specific origins:
    # allow_origins=["http://localhost:3000", "https://yourdomain.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# root endpoint
@app.post("/", response_model=RootResponseModel)
def root():
    try:
        # endpoint hit
        log_status(status="INFO", source="/app.py::root()", timestamp=get_readable_timestamp(), msg="Root endpoint hit. Returning response\n")
        # return response
        return RootResponseModel(
            response="Hi there!"
        )
    except Exception as e:
        log_status(status="ERROR", source="/app.py::root()", timestamp=get_readable_timestamp(), msg=f"Exception: {e}; traceback: {traceback.print_exc()}\n")

# chat websocket endpoint
@app.websocket("/chat")
async def chat(websocket: WebSocket):
    try:
        # endpoint hit
        log_status(status="INFO", source="/app.py::chat()", timestamp=get_readable_timestamp(), msg="Chat endpoint hit. Accepting websocket connection request\n")
        # accepting websocket connection request
        await websocket.accept()
        # build a StateGraph
        state_graph = StateGraph(GraphState)
        # add nodes (i.e., agents) to the state_graph
        state_graph.add_node("agent_orchestrator", agent_orchestrator)
        state_graph.add_node("agent_scholar", agent_scholar)
        state_graph.add_node("agent_market", agent_market)
        state_graph.add_node("agent_summarizer", agent_summarizer)
        state_graph.add_node("agent_critic", agent_critic)
        state_graph.add_node("agent_report_gen", agent_report_gen)
        state_graph.add_node("agent_rag", agent_rag)
        # receive request data
        request = await websocket.receive_text()
        request = json.loads(request)
        
    except Exception as e:
        log_status(status="ERROR", source="/app.py::chat()", timestamp=get_readable_timestamp(), msg=f"Exception: {e}; traceback: {traceback.print_exc()}\n")
    finally:
        await websocket.close()

if __name__ == "__main__":
    # Run the server
    uvicorn.run(app, host="0.0.0.0", port=8000)
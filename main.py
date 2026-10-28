from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

BASE = Path(__file__).parent
app = FastAPI(title="Red Ball")

# Legend: S start, G goal, ^ spike, e patrolling enemy, # block
# objs = [char, col, row, width(optional)] ; ground = runs of '#'(floor) / '.'(pit), tile = 16px
LEVELS = [
    {"ground": "#16.3#12.3#10.3#9",
     "objs": [["S",1,8],["^",24,8],["^",25,8],["#",36,8],["#",38,6,3],["e",50,8],["G",54,8]]},
    {"ground": "#10.3#6.4#8.3#8.3#15",
     "objs": [["S",1,8],["^",5,8],["^",6,8],["#",15,8,2],["^",27,8],["^",28,8],["#",38,7,2],
              ["e",48,8],["^",52,8],["^",53,8],["G",58,8]]},
    {"ground": "#8.10#6.10#6.9#11",
     "objs": [["S",1,8],["#",10,8,2],["#",14,8,2],["^",20,8],["^",21,8],["#",26,8,2],["#",30,8,2],
              ["e",36,8],["#",42,8,2],["#",46,8,2],["G",57,8]]},
    {"ground": "#10.3#12.3#6.3#12.3#14",
     "objs": [["S",1,8],["#",6,8],["e",16,8],["e",21,8],["^",30,8],["^",31,8],["#",40,8,4],["#",41,7,2],
              ["^",45,8],["^",46,8],["e",55,8],["^",58,8],["^",59,8],["G",64,8]]},
    {"ground": "#8.3#4.3#4.3#4.3#4.3#4.3#10",
     "objs": [["S",1,8],["e",5,8],["^",13,8],["^",20,8],["^",27,8],["^",34,8],["^",41,8],
              ["e",49,8],["G",54,8]]},
]


@app.get("/api/levels")
def levels():
    return LEVELS


@app.get("/health")
def health():
    return {"ok": True}


@app.get("/")
def index():
    return FileResponse(BASE / "static" / "index.html")


app.mount("/static", StaticFiles(directory=BASE / "static"), name="static")

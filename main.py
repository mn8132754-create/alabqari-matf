from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os

# استيراد محركات المشروع
import algebra
import calculus
import matrices
import ai_engine

app = FastAPI(title="العبقري الرياضي - Alabqari Math", version="1.0")

class MathRequest(BaseModel):
    operation: str
    expression: str = ""
    matrix_data: list = None
    problem: str = ""

@app.get("/", response_class=HTMLResponse)
async def read_index():
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>مرحباً بك في مشروع العبقري الرياضي! واجهة المستخدم غير موجودة.</h1>"

@app.post("/api/calculate")
async def calculate(req: MathRequest):
    try:
        if req.operation in ["simplify", "factor", "solve_eq"]:
            result, steps = algebra.solve_algebra(req.expression, req.operation)
            return {"success": True, "result": result, "steps": steps}
        
        elif req.operation in ["derivative", "integral", "limit"]:
            result, steps = calculus.solve_calculus(req.expression, req.operation)
            return {"success": True, "result": result, "steps": steps}
        
        elif req.operation in ["determinant", "inverse", "transpose", "eigenvalues"]:
            result, steps = matrices.solve_matrix(req.matrix_data, req.operation)
            return {"success": True, "result": result, "steps": steps}
            
        else:
            raise HTTPException(status_code=400, detail="عملية غير معروفة.")
            
    except Exception as e:
        return {"success": False, "error": str(e)}

@app.post("/api/ai-analyze")
async def ai_analyze(req: MathRequest):
    try:
        res = ai_engine.analyze_math_with_ai(req.problem)
        return res
    except Exception as e:
        return {"success": False, "error": str(e)}

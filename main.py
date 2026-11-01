import os
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Any, Dict, List
from dotenv import load_dotenv

from algebra import solve_algebra
from calculus import solve_calculus
from matrices import solve_matrix

load_dotenv()

app = FastAPI(
    title="العبقري الرياضي - Alabqari Math Engine",
    description="محرك رياضيات متقدم يدعم الحلول الرمزية والعددية والذكاء الاصطناعي",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MathRequest(BaseModel):
    expression: str
    category: Optional[str] = "algebra"
    operation: Optional[str] = "solve"
    variables: Optional[str] = "x"
    lower_bound: Optional[Any] = None
    upper_bound: Optional[Any] = None
    limit_to: Optional[Any] = None
    matrix_data: Optional[List[List[float]]] = None

class MathResponse(BaseModel):
    success: bool
    category: str
    result: str
    steps: List[str] = []
    error: Optional[str] = None

@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {
        "status": "online",
        "app_name": "Alabqari Math",
        "sympy_available": True
    }

@app.post("/api/solve", response_model=MathResponse)
async def solve_math_problem(request: MathRequest):
    try:
        if request.category == "algebra":
            result, steps = solve_algebra(request.expression, request.operation, request.variables or "x")
        elif request.category == "calculus":
            result, steps = solve_calculus(
                request.expression, request.operation, request.variables or "x",
                request.lower_bound, request.upper_bound, request.limit_to
            )
        elif request.category == "matrices":
            if not request.matrix_data:
                raise ValueError("يجب توفير بيانات المصفوفة.")
            result, steps = solve_matrix(request.matrix_data, request.operation)
        else:
            raise ValueError("التصنيف الرياضي غير مدعوم حالياً.")

        return MathResponse(
            success=True,
            category=request.category,
            result=result,
            steps=steps
        )
    except Exception as e:
        return MathResponse(
            success=False,
            category=request.category,
            result="",
            error=str(e)
        )

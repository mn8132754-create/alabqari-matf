from sympy import symbols, simplify, expand, factor, solve, Eq
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

transformations = standard_transformations + (implicit_multiplication_application,)

def solve_algebra(expression: str, operation: str = "solve", variable: str = "x"):
    try:
        x = symbols(variable)
        steps = []

        if "=" in expression:
            left, right = expression.split("=")
            eq = Eq(parse_expr(left, transformations=transformations), parse_expr(right, transformations=transformations))
            steps.append(f"تم تكوين المعادلة: {eq}")
        else:
            expr = parse_expr(expression, transformations=transformations)
            steps.append(f"تم تحليل التعبير: {expr}")

        if operation == "simplify":
            res = simplify(expr)
            steps.append("تبسيط التعبير الجبري للحصول على أبسط صورة.")
            return str(res), steps
        elif operation == "expand":
            res = expand(expr)
            steps.append("نشر الأقواس وتفكيك الحدود.")
            return str(res), steps
        elif operation == "factor":
            res = factor(expr)
            steps.append("تحليل التعبير إلى عوامله الأولية.")
            return str(res), steps
        elif operation == "solve" and "=" in expression:
            solutions = solve(eq, x)
            steps.append(f"حل المعادلة بالنسبة للمتغير {variable}.")
            return str(solutions), steps
        else:
            if "=" in expression:
                solutions = solve(eq, x)
                return str(solutions), steps
            else:
                res = simplify(expr)
                return str(res), steps
    except Exception as e:
        raise ValueError(f"خطأ في معالجة الجبر: {str(e)}")

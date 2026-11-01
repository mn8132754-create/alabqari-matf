from sympy import symbols, diff, integrate, limit, parse_expr
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application

transformations = standard_transformations + (implicit_multiplication_application,)

def solve_calculus(expression: str, operation: str = "derivative", variable: str = "x", lower_bound=None, upper_bound=None, limit_to=None):
    try:
        x = symbols(variable)
        expr = parse_expr(expression, transformations=transformations)
        steps = [f"الدالة الأصلية: {expr}"]

        if operation == "derivative":
            res = diff(expr, x)
            steps.append(f"حساب المشتقة الأولى بالنسبة لـ {variable}.")
            return str(res), steps
        elif operation == "integral":
            if lower_bound is not None and upper_bound is not None:
                res = integrate(expr, (x, lower_bound, upper_bound))
                steps.append(f"حساب التكامل المحدد من {lower_bound} إلى {upper_bound}.")
            else:
                res = integrate(expr, x)
                steps.append(f"حساب التكامل غير المحدد بالنسبة لـ {variable}.")
            return str(res), steps
        elif operation == "limit":
            lim_val = 0 if limit_to is None else float(limit_to)
            res = limit(expr, x, lim_val)
            steps.append(f"حساب النهاية عندما تقترب {variable} من {lim_val}.")
            return str(res), steps
        else:
            raise ValueError("عملية تفاضل أو تكامل غير معروفة.")
    except Exception as e:
        raise ValueError(f"خطأ في حساب التفاضل والتكامل: {str(e)}")

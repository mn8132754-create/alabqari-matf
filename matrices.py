import numpy as np
import sympy as sp

def solve_matrix(matrix_data: list, operation: str = "determinant"):
    try:
        mat_np = np.array(matrix_data, dtype=float)
        mat_sp = sp.Matrix(matrix_data)
        steps = [f"المصفوفة المدخلة بحجم {mat_np.shape}"]

        if operation == "determinant":
            if mat_np.shape[0] != mat_np.shape[1]:
                raise ValueError("يجب أن تكون المصفوفة مربعة لحساب المحدد.")
            res = mat_sp.det()
            steps.append("حساب محدد المصفوفة (Determinant).")
            return str(res), steps
        elif operation == "inverse":
            if mat_np.shape[0] != mat_np.shape[1]:
                raise ValueError("يجب أن تكون المصفوفة مربعة لحساب المعكوس.")
            res = mat_sp.inv()
            steps.append("حساب معكوس المصفوفة (Inverse Matrix).")
            return str(res), steps
        elif operation == "transpose":
            res = mat_sp.T
            steps.append("إيجاد منقول المصفوفة (Transpose).")
            return str(res), steps
        elif operation == "eigenvalues":
            if mat_np.shape[0] != mat_np.shape[1]:
                raise ValueError("القيم الذاتية تتطلب مصفوفة مربعة.")
            res = mat_sp.eigenvals()
            steps.append("حساب القيم الذاتية (Eigenvalues).")
            return str(res), steps
        else:
            raise ValueError("عملية مصفوفات غير معروفة.")
    except Exception as e:
        raise ValueError(f"خطأ في معالجة المصفوفات: {str(e)}")

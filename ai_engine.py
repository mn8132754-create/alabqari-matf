import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

def analyze_math_with_ai(problem_description: str) -> dict:
    """
    تستخدم هذه الدالة نموذج الذكاء الاصطناعي لتحليل المسائل الرياضية النصية،
    شرح الفكرة، وتوليد خطوات الحل بالعربية.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return {
            "success": False,
            "error": "لم يتم ضبط مفتاح الذكاء الاصطناعي GEMINI_API_KEY في ملف البيئة .env"
        }

    try:
        client = genai.Client(api_key=api_key)

        prompt = f"""
        أنت خبير رياضيات ذكي ومساعد تعليمي لمنصة "العبقري الرياضي".
        قم بتحليل المسائل الرياضية التالية المشروحة نصياً، واشرح الفكرة الرياضية، ووضح خطوات الحل بالتفصيل وباللغة العربية الفصحى الواضحة:

        المسألة: {problem_description}

        أجب بتنسيق منظم يتضمن:
        1. الفكرة الرياضية أو القانون المستخدم.
        2. خطوات الحل المفصلة.
        3. النتيجة النهائية.
        """

        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )

        return {
            "success": True,
            "analysis": response.text
        }
    except Exception as e:
        return {
            "success": False,
            "error": fحدث خطأ أثناء الاتصال بالذكاء الاصطناعي: {str(e)}"
        }

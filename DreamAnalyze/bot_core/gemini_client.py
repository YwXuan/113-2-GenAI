import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-flash")

def ask_gemini(user_input: str, context: str) -> str:
    prompt = f"""
你是一位善於解讀潛意識的夢境分析師。
請根據使用者的夢境描述與提供的相似夢境資料，進行深入的解釋與分析。

請使用 LINE 支援的格式（不要使用 Markdown 粗體、超連結、程式區塊），以簡潔、有同理心的語氣回答。

請依照以下格式回覆：
🔮 夢境摘要：
🧠 潛意識可能的反映：
💡 建議與提醒：

使用者夢境：「{user_input}」
如果使用者的夢境描述過於簡短，請提醒他們提供更多細節。
相似夢境資料：
{context}
"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"⚠️ Gemini 回應錯誤：{e}")
        return "抱歉，AI 分析失敗了，請稍後再試一次 🛠️"
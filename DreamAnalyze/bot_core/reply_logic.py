def classify_message(user_msg: str) -> str:
    """
    根據關鍵字分類訊息類型：
    - greeting: 打招呼
    - help: 詢問用途
    - dream: 有夢境關鍵字
    - unknown: 其他
    """
    msg = user_msg.lower()

    if any(word in msg for word in ["哈囉", "你好", "嗨", "hi", "hello"]):
        return "greeting"
    elif any(word in msg for word in ["你可以做什麼", "你是誰", "幫助", "用途", "幹嘛","你可以做些甚麼","你能做什麼"]):
        return "help"
    elif any(word in msg for word in ["夢", "夢到", "夢見", "夢境"]):
        return "dream"
    else:
        return "unknown"

from linebot.models import TextSendMessage, QuickReply, QuickReplyButton, MessageAction

def get_reply_by_type(user_msg: str, user_id: str, type: str, search_fn, gemini_fn) -> str:
    """
    根據分類給出不同的回應。
    - search_fn(user_msg) -> list[str]
    - gemini_fn(user_msg, context) -> str
    """
    if type == "greeting":
        return ("嗨嗨～我是你的夢境分析師 🌙\n"
                "你可以跟我說你夢到了什麼，我會幫你解讀～\n\n"
                "💡 小提醒：以『夢到...』開頭，可以直接觸發夢境分析唷！")

    elif type == "help":
        return ("我是 AI 夢境分析師 🤖\n"
                "📌 你可以這樣用我：\n"
                "1️⃣ 輸入夢境，例如：『夢到我被狗追』\n"
                "2️⃣ 我會從資料庫找出相似夢境案例\n"
                "3️⃣ 並用 Gemini 幫你解釋夢的潛意識意涵～")

    elif type == "dream":
        similar = search_fn(user_msg)
        context = "\n---\n".join(map(str, similar))
        analysis = gemini_fn(user_msg, context)
        if not analysis or len(user_msg.strip()) < 6:
            return TextSendMessage(
                text=("看起來這段夢境的描述有點簡短 🧐"
                      "可以再多說一些夢裡的情節、情緒或場景嗎？"
                      "我才能幫你更準確地分析喔！")
            )
        return gemini_fn(user_msg, context)

    else:
        return ("我目前只懂夢哦 🌙\n"
                "💡 你可以說：『夢到我在飛』、『夢見我被困住』\n"
                "我就能幫你解釋背後的心理意涵！")
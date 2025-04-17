from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FollowEvent
from dotenv import load_dotenv
import os

# 模組載入
from bot_core.event_router import EventRouter
from bot_core.reply_logic import classify_message, get_reply_by_type
from bot_core.vector_search import search_similar_dreams
from bot_core.gemini_client import ask_gemini

# 初始化
load_dotenv()
app = Flask(__name__)
line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))

# 初始化事件路由器
router = EventRouter(
    line_bot_api,
    lambda msg, uid: get_reply_by_type(
        user_msg=msg,
        user_id=uid,
        type=classify_message(msg),
        search_fn=search_similar_dreams,
        gemini_fn=ask_gemini
    )
)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except Exception as e:
        print(f"錯誤：{e}")
        abort(400)
    return 'OK'

@handler.add(MessageEvent)
@handler.add(FollowEvent)
def handle_event(event):
    router.handle_event(event)

if __name__ == "__main__":
    app.run(port=5000)
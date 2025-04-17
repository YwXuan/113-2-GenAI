from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent
)
from linebot import LineBotApi

# 初始化時請傳入：line_bot_api 實例、回應處理函數
class EventRouter:
    def __init__(self, line_bot_api, reply_fn):
        self.line_bot_api = line_bot_api
        self.reply_fn = reply_fn

    def handle_event(self, event):
        print(f"[📨 收到事件] {event.__class__.__name__}")
        if isinstance(event, MessageEvent):
            if not isinstance(event.message, TextMessage):
                print(f"[⛔ 不支援的訊息類型：{type(event.message)}，略過]")
                return
        try:
            if isinstance(event, MessageEvent) and isinstance(event.message, TextMessage):
                user_input = event.message.text
                reply_text = self.reply_fn(user_input, event.source.user_id)
                self.line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=reply_text)
                )

            elif isinstance(event, FollowEvent):
                self.line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="歡迎加入夢境分析師 🌙 輸入『夢到...』開始解夢～")
                )

            else:
                print("[⛔ 未支援事件，略過]")

        except Exception as e:
            print(f"⚠️ 回覆時錯誤：{e}")


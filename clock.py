from linebot import LineBotApi
from linebot.models import TextSendMessage
import os

# 初始化 Line Bot API
line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])

# 创建要发送的消息
message = TextSendMessage(text="快要下班囉")

# 发送消息给指定的用户或群组
user_id = 'U3e803e6dd2f25dd45a6f3fb763fa5dbf'  # 将 USER_ID_HERE 替换为要发送消息的用户或群组的 ID
line_bot_api.push_message(user_id, messages=message)
import os
from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage
from linebot.exceptions import LineBotApiError


def send_text_message(text: str):
    """LINEでテキストメッセージを送信する"""
    CHANNEL_ACCESS_TOKEN = os.environ["CHANNEL_ACCESS_TOKEN"]
    USER_ID = os.environ["USER_ID"]
    line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

    try:
        line_bot_api.push_message(USER_ID, TextSendMessage(text=text))
    except LineBotApiError as e:
        print("error", e.message)


def send_image_message(img_path: str):
    """LINEで画像メッセージを送信する"""
    CHANNEL_ACCESS_TOKEN = os.environ["CHANNEL_ACCESS_TOKEN"]
    USER_ID = os.environ["USER_ID"]
    line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
    image_message = ImageSendMessage(
        original_content_url=img_path,
        preview_image_url=img_path,
    )
    line_bot_api.push_message(USER_ID, image_message)

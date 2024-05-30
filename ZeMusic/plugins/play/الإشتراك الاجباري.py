from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button
from pyrogram.enums import ChatType
from pyrogram.errors import UserNotParticipant
from ZeMusic import app

channel = "eo_u7"
async def subscription(_, __: Client, message: Message):
    user_id = message.from_user.id
    try: await app.get_chat_member(channel, user_id)
    except UserNotParticipant: return False
    return True
    
subscribed = filters.create(subscription)

@app.on_message(~subscribed)
async def checker(_: Client, message: Message):
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]: await message.delete()
    user_id = message.from_user.id
    user = message.from_user.first_name
    markup = Markup([
        [Button("饾悞饾惃饾惍饾惈饾悳饾悶 饾惀饾惃饾惀 馃鈥嶁檧", url=f"https://t.me/{channel}")]
    ])
    await message.reply(
        f"毓匕乇賸丕 毓夭賷夭賷 {user}毓賱賷賰 丕賱廿卮鬲乇丕賰 亘賯賳丕丞 丕賱爻賵乇 兀賵賱丕.",
        reply_markup = markup
    )
    

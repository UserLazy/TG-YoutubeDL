from pyrogram import Client
from pyrogram import filters
from pyrogram import StopPropagation
from pyrogram.types import InlineKeyboardButton 
from pyrogram.types import InlineKeyboardMarkup


@Client.on_message(filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel Update", url="https://t.me/UserLazyXBot")],
        [InlineKeyboardButton(
            "Group Support", url="https://t.me/UserLazySupport")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation

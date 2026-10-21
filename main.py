import os
import discord
from discord.ext import commands

# إعدادات البوت الأساسية
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"تم تسجيل الدخول بنجاح كـ {bot.user}")

@bot.command()
async def ping(text):
    await text.send("البوت شغال ومتصل 24 ساعة! 🚀")

# تشغيل البوت باستخدام التوكن السري
bot.run("MTU2MjM3MDQ4Mzg2ODAxNjcwNA.GukZ0I.J3fMN8FZSMZ15zJOcRlDkxhsv8PdXHeiB5O23c")

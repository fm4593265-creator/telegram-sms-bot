# Telegram Bot

بوت تيليجرام بسيط جاهز للتشغيل.

## تشغيل محلياً
ضع Token البوت في متغير البيئة `BOT_TOKEN` ثم شغّل:

```bash
pip install -r requirements.txt
python bot.py
```

## Render
استخدم Worker/Background Worker إذا كان متاحاً لحسابك، مع Start Command:

```bash
python bot.py
```

وأضف Environment Variable باسم:

`BOT_TOKEN`

ولا تضع الـToken داخل الملفات أو GitHub.

# backend/app/utils/helpers.py

def format_user(user):
    return f"ID: {user.id}\nTelegram ID: {user.telegram_id}\nUsername: {user.username}\nName: {user.first_name} {user.last_name}\nTokens: {user.tokens}"

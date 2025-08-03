from telethon.sync import TelegramClient
from telethon.errors import FloodWaitError
from time import sleep
import os

# Telegram API bilgilerin
api_id = 21663358  # <<== BURAYA kendi api_id'ni yaz
api_hash = 'd52861fe8ae5cea6aeb0cf1eb3c95cce'  # <<== BURAYA kendi api_hash'ini yaz
phone = '+905524114377'  # <<== Telegram'a kayıtlı telefon numaran

# Gönderilecek gruplar (kullanıcı adı şeklinde veya tam link)
target_groups = [
    'https://t.me/paparapablo',  # <<== BURAYA mesaj atmak istediğin grup linkini yaz
    'https://t.me/pubgskinhackdobbet',
    'https://t.me/sohbetconfig'
]

# Gönderilecek mesaj
message = "👋 Merhaba! Ücretsiz Sorgu Paneli için kanalımıza göz at: https://t.me/illegallitee"  # <<== Mesajı buradan değiştir

# Mesajlar arası kaç saniye beklesin
delay_seconds = 10  # <<== flood yememek için en az 5 önerilir

with TelegramClient('session', api_id, api_hash) as client:
    for group in target_groups:
        try:
            client.send_message(group, message)
            print(f"✅ Mesaj gönderildi: {group}")
            sleep(delay_seconds)
        except FloodWaitError as e:
            print(f"⏳ FloodWaitError! {e.seconds} saniye bekleniyor...")
            sleep(e.seconds)
        except Exception as e:
            print(f"❌ Hata oluştu: {e}")

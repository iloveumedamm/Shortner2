# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "21748181"))
API_HASH = os.environ.get("API_HASH", "b1d962414e186e0778911f3183feac33")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6221359148:AAFm_TFyB_BG8MWGRxpVluB3f4qhi_iDX4U")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("Owner Id")] if os.environ.get("5651594253") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "mdisk")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Rishikesh001:Rishikesh001@cluster0.lqncnak.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5651594253")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(5651594253)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001949268590")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "ziplinker_net") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"

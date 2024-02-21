# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()

# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "24010108"))
API_HASH = os.environ.get("API_HASH", "8d89700b2fc09a3aa6c906cbed65b040")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6257817586:AAHiHfYz_Ykn_n1QHgE7o1aRdOn5Gxg6M4U")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS", "5791145987").split(",") if i.strip()] 
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "shortnertest")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://lajihi2115:lgAEiuZHs917nZgy@cluster0.lx88eg8.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5791145987")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002002097084")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "streaamdb") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://graph.org/file/b2b7504687ec41b794b9a.jpg') # image when someone hit /start
LINK_BYPASS = "False"

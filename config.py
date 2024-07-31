# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "20373203"))
API_HASH = getenv("API_HASH", "8962717c7c708e210f66ea658db58d85")
BOT_TOKEN = getenv("BOT_TOKEN", "7307382083:AAE1UyOhCyxfL-jsXsRjR1aQ2FRsCLNCox0")
OWNER_ID = int(getenv("OWNER_ID", "6994050538"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://Hola:Ram@cluster0.af3d5fq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002207691468"))
FORCESUB = getenv("FORCESUB", "-1002173398000")

import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "28382321"))
    API_HASH = os.environ.get("API_HASH", "a1340b7972df975470aee26ea4ad6bfb")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5895084879:AAEfB-A862ol9lU0LyIh1HWNW3GfJ9JCOb8")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzcBuzuuIdh5Age1VKqmJGudoChiNwcbk_SNsDZ3kR7HTJxU8VObbhqgig0MoY4KfskE1psThQNEKlmjcTe7R8boQfbBesa-wjJWg0-_cNiHjUjdvTLS_H92v9NTlsqswQrXI3Es5DLUXfv8ElF47uXWNiEYNIdPX37TmatFapagU6UYd-VM3etulaOtYS9-8PNnWjePK5HUK1CPyB3hpgWUGxt-likbbkO69T_fBP_fMpAVkjbd1Vp4qX3Es9pqAy4uxy9Yw2AI0YISiMpqa6j5cgSNoIKIYYkjKLVxAJ8MFTd4VR0pmQG23Z5PpE7ZhQ0j5E9lxEyBqbIWHifl-0qdx0M=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "vpstrialbot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5518364890")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"

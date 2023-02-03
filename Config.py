import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "28382321"))
    API_HASH = os.environ.get("API_HASH", "a1340b7972df975470aee26ea4ad6bfb")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5895084879:AAEfB-A862ol9lU0LyIh1HWNW3GfJ9JCOb8")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BAGxFHEALaWH-2dgzFxhbD6FhQTeciYcUXM81Fpv0dsTRqLuTgZTryodLGxhdsKM1X8KoHSGxN_NozXpCmxlNK7xvzIqEKWLdR1q2n8rWwvZ7H9_1XzUq1Q7jXis5QbtSetK2UECkSbGXg6raRUnJxb3uXs2l55mZnrtWbvo7eUEugZcb4r31OrOjGWLPSGqL3rlDp6QDltqUFnk7LhCUnFdDl68k7AZmENhEl1en874CBHI61dLuxE8bRATWociHncPFRNiJMKRq1Z3Go3IxDzYIdrpxG_OhaiyT_1HWFb0ijHqByb0tBPXHw51rIVYn5JJ6E2el59gsEfkBALBweEkHWS7egAAAAFI65DaAA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "vpstrialbot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"

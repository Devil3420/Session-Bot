from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("๐ฅ sแดแดสแด ษขแดษดแดสแดแดษชษดษข sแดssษชแดษด ๐ฅ", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="๐  สแดแดแดสษด สแดแดแด ๐ ", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton("๐ค สแดแดก แดแด แดsแด ๐ค", callback_data="help"),
            InlineKeyboardButton("๐ช แดสแดแดแด ๐ช", callback_data="about")
        ],
        [InlineKeyboardButton("๐ แดแดสแดส สแดแดs ๐", url="https://t.me/Insane_Help")],
    ]

    START = """
Hey {}
Welcome to {}
If you don't trust this bot, 
1) stop reading this message
2) delete this chat
Still reading?
You can use me to generate Pyrogram and Telethon string session. Use below buttons to learn more !
By @Insane_Help
    """

    HELP = """
โจ **Available Commands** โจ

/about - About The Bot
/help - This Message
/start - Start the Bot
/repo - Get Repo
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to generate pyrogram and telethon string session by @always_hungry365

Source Code : [Click Here](https://t.me/Insane_Help)
Framework : [Pyrogram](docs.pyrogram.org)
Language : [Python](www.python.org)
Developer : @always_hungry365
    """

    # Repo Message
    REPO = """
โโโโโโโโโโโโโโโโโโโโโโโโ
๐ฅ A แดแดแดกแดสาแดส สแดแด
แดา โป๏ธ แดส แดsแดแด แดสษช ๐ฅ
โโโโโโโโโโโโโโโโโ
GENERATE SESSION FOR TG...
โโโโโโโโโโโโโโโโโโโ
โฃโ [๐๐ซ๐๐๐ญ๐จ๐ซ] [Mayank](https://t.me/always_hungry365)
โฃโ [๐๐๐๐ซ๐ญ]   [Heart โค๏ธ](https://t.me/Insane_Help)
โโโโโโโโโโโโโโโโโโโ
๐ 
IF HAVE ANY QUESTION OR WANT REPO THEN CONTACT ยป TO ยป MY ยป [OWNER] @always_hungry365
   """
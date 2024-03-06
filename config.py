from aiogram.types import BotCommand

token = ''
ver = "0.0.6"

cmds = "<b>/tea</b> Выпить чай\n<b>/coffee</b> выпить кофе \n<b>/wine</b> выпить вино \n<b>/champ</b> выпить шампанское \n<b>/juice</b> выпить сок \n<b>/beer</b> бахнуть пивка \n<b>/top</b> <code><напиток></code> узнать топ чего-либо\n <b>/ver</b> Версия бота\n",


bot_commands = [
    # BotCommand(command="/help", description="Список команд"),

    BotCommand(command="/top", description="<напиток> узнать топ"),
    
    BotCommand(command="/tea", description="Выпить чай🍵"),
    BotCommand(command="/coffee", description="Выпить кофе☕️"),

    BotCommand(command="/juice", description="Выпить сок🧃"),

    BotCommand(command="/beer", description="Выпить пивка🍻"),
    BotCommand(command="/wine", description="Выпить вино🍷"),
    BotCommand(command="/champagne", description="Выпить шампаноское🥂"),
    BotCommand(command="/ver", description=f"{ver}")
]
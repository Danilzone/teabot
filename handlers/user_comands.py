
from config import ver
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from data import db
import datetime
from rich import print
from rich.console import Console
import random
console = Console()

def russif(drank):
    if drank == "tea":
        return "Чая"
    elif drank == "coffee":
        return "Кофе"
    elif drank == "champagne":
        return "Шампанского"
    elif drank == "beer":
        return "Пива"
    elif drank == "juice":
        return "Сока"
    elif drank == "wine":
        return "Вина"
    else:
        return False


router = Router()
db = db.Db('./data/main.db')


@router.message(F.text == "/start")
async def start(message : Message):
    await message.answer(f"Здравствуй друг, что хочешь выпить?🧐\n<b>Список команд - /h</b>")

@router.message(Command(commands=['tea', 'чай']))
async def tea(message : Message):
    date = datetime.datetime.now()
    check = db.time_check(message.from_user.id, message.from_user.username, message.from_user.full_name, date, 'tea')
    
    if check[0]:
        lit = round(random.uniform(0.3, 6),2)
        res = db.drank(message.from_user.id, message.from_user.username, message.from_user.full_name, lit, date, 'tea')
        await message.answer(f"{message.from_user.first_name} выпил <b>{lit} л.</b> чая\nВыпито всего <b>{res}</b> л." )
    else: 
        await message.answer(f"Чайник ещё не вскипел🫖\nПодожди <b>{check[1]}</b> мин.")


@router.message(Command(commands=['coffee', 'coffe', 'cofe', 'кофе']))
async def coffee(message : Message):
    date = datetime.datetime.now()
    check = db.time_check(message.from_user.id, message.from_user.username, message.from_user.full_name, date, 'coffee')

    if check[0]:
        lit = round(random.uniform(0.3, 6),2)
        res = db.drank(message.from_user.id, message.from_user.username, message.from_user.full_name, lit, date, 'coffee')
        await message.answer(f"{message.from_user.first_name} выпил <b>{lit} л.</b> кофе\nВыпито всего <b>{res}</b> л." )
    else: 
        await message.answer(f"Кофе ещё не сварился😒\nПодожди <b>{check[1]}</b> мин.")


@router.message(Command(commands=['juice', 'juc', 'сок']))
async def juice(message : Message):
    date = datetime.datetime.now()
    check = db.time_check(message.from_user.id, message.from_user.username, message.from_user.full_name, date, 'juice')
    
    if check[0]:
        lit = round(random.uniform(0.3, 6),2)
        res = db.drank(message.from_user.id, message.from_user.username, message.from_user.full_name, lit, date, 'juice')
        await message.answer(f"{message.from_user.first_name} выпил <b>{lit} л.</b> сока\nВыпито всего <b>{res}</b> л." )
    else: 
        await message.answer(f"Сок ещё не привезли🧃\nПодожди <b>{check[1]}</b> мин.")

@router.message(Command(commands=['beer', 'пиво', 'пивас', 'пивасик']))
async def beer(message : Message):
    date = datetime.datetime.now()
    check = db.time_check(message.from_user.id, message.from_user.username, message.from_user.full_name, date, 'beer')
    
    if check[0]:
        lit = round(random.uniform(0.3, 6),2)
        res = db.drank(message.from_user.id, message.from_user.username, message.from_user.full_name, lit, date, 'beer')
        await message.answer(f"{message.from_user.first_name} выпил <b>{lit} л.</b> пива\nВыпито всего <b>{res}</b> л." )
    else: 
        await message.answer(f"📛Пиво не по акции!📛\nПодожди <b>{check[1]}</b> мин.")

@router.message(Command(commands=['wine', 'вино']))
async def wine(message : Message):
    date = datetime.datetime.now()
    check = db.time_check(message.from_user.id, message.from_user.username, message.from_user.full_name, date, 'wine')
    
    if check[0]:
        lit = round(random.uniform(0.3, 6),2)
        res = db.drank(message.from_user.id, message.from_user.username, message.from_user.full_name, lit, date, 'wine')
        await message.answer(f"{message.from_user.first_name} выпил <b>{lit} л.</b> вина\nВыпито всего <b>{res}</b> л." )
    else: 
        await message.answer(f"Время для вина еще не подошло🥴🍷\nПодожди <b>{check[1]}</b> мин.")

@router.message(Command(commands=['champagne', 'cham', 'champ', 'шампанское', 'шампунь', 'шам']))
async def champagne(message : Message):
    date = datetime.datetime.now()
    check = db.time_check(message.from_user.id, message.from_user.username, message.from_user.full_name, date, 'champagne')
        
    if check[0]:
        lit = round(random.uniform(0.3, 6),2)
        res = db.drank(message.from_user.id, message.from_user.username, message.from_user.full_name, lit, date, 'champagne')
        await message.answer(f"{message.from_user.first_name} выпил <b>{lit} л.</b> шампанского\nВыпито всего <b>{res}</b> л." )
    else: 
        await message.answer(f"Время для шампуня еще не подошло🥴🍾\nПодожди <b>{check[1]}</b> мин.")

    
@router.message(Command(commands=["top"]))
async def top(message : Message, command: CommandObject):
    scan = russif(command.args)
    
    if scan == False:
        await message.answer("Ошибка в комманде")
    else: 
        res = db.top(command.args)
        await message.answer(f"Топ {scan}\n{res}")


@router.message(Command(commands=["v", "ver", "version"]))
async def help(message : Message):

    await message.answer(f"Версия бота : <code>{ver}</code>")

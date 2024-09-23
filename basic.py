from aiogram import F, Router, types, exceptions
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from aiogram.methods.send_photo import SendPhoto
from connection import dp, bot
import os
import asyncio


router = Router()


@router.message(lambda message: message.text == 'Только для разработчика')
async def button_price_response(message: types.Message):
    # Указываем путь к файлу
    path = os.path.abspath(os.path.join('images', 'massage_face.jpg'))
    if not os.path.isfile(path):
        print(f"Файл не найден по пути: {path}")   
    photo = FSInputFile(path)
    try:
        send_message = await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption="Для выбора понравившегося массажа нажмите на кнопку 'Виды массажа'"
       )
        file_id = send_message.photo[-1].file_id
        print(f"file_id: {file_id}")
        await message.answer(f"file_id: {file_id}")
    except Exception as e:
        print(f"Ошибка при отправке фото: {e}")


IMAGES_ID = {
    'price_1': 'AgACAgIAAxkDAAMQZvA5DZ-uQZ1J8HG-LdJ5H5tanPUAAq7eMRsoboBLgvrUmNymkIkBAAMCAAN3AAM2BA',
    'anti_cellulitniy': 'AgACAgIAAxkDAAMWZvA5lKWf0aqWHV2LldrnvYh1vzgAArPeMRsoboBLGVxxUJFud5ABAAMCAAN3AAM2BA',
    'strong_relax': 'AgACAgIAAxkDAAMpZvA5_yXByZXdvwMcIKKDCB7HK3gAArTeMRsoboBLJ5Etspyra_8BAAMCAAN3AAM2BA',
    'sport_massage': 'AgACAgIAAxkDAAMsZvA6L3bS3_U3w5Kxfr06YGQl7BEAArXeMRsoboBL_BZbZxVx8LoBAAMCAAN3AAM2BA',
    'teypirovanie': 'AgACAgIAAxkDAAMvZvA6ZJawb2b4rF4VuGI24k1i-wsAArbeMRsoboBLtKmGTUXFnVQBAAMCAAN3AAM2BA',
    'banochniy': 'AgACAgIAAxkDAAMyZvA6kYCVLp_c1bTH6amOwQnRInkAArjeMRsoboBL3_PAs0JX6-4BAAMCAAN3AAM2BA',
    'classik_massage': 'AgACAgIAAxkDAAM1ZvA6uoui_xeOxrE_6pD5-HOXpJoAArreMRsoboBLUqbROsPf6Q4BAAMCAAN3AAM2BA',
    'instrumental_mobiliz': 'AgACAgIAAxkDAAM4ZvA69DmfsKOZlkCmjumY9dPDdtMAArveMRsoboBL6CBaKPHq88kBAAMCAAN3AAM2BA',
    'just_relax': 'AgACAgIAAxkDAAM7ZvA7Mn3KLZDj-JcBXv4WShxQyuMAAr7eMRsoboBLLtM6Bbum8AEBAAMCAAN3AAM2BA',
    'limfodrenaj': 'AgACAgIAAxkDAAM-ZvA7bCA_Owv4ghyQtqvNvMX8sfQAAsLeMRsoboBLHqjuOQeNjJkBAAMCAAN3AAM2BA',
    'massage_face': 'AgACAgIAAxkDAANBZvA7ldifCSMa58l63mzUS8yRUnQAAsTeMRsoboBL93KvBc95o5YBAAMCAAN3AAM2BA',
    }


@router.message(CommandStart())
async def test_bot(message: types.Message):
    # Создаем кнопки
    buttons = make_start_buttons()
    await message.reply('Выберите, что бы вы хотели сделать :)', reply_markup=buttons)


@router.message(lambda message: message.text == 'Прайс лист')
async def button_price_response(message: types.Message):
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=IMAGES_ID['price_1'],
        caption="Для выбора понравившегося массажа нажмите на кнопку 'Виды массажа'"
    )
   
    # Вызываем метод отправки через объект send_photo_method 

@router.message(lambda message: message.text == 'Контакты')
async def button_info_response(message: types.Message):
    '''получить справочную информацию'''
    info_text = '''
Номер телефона: 89881498564
TG: @Arthur_Land_Massage
    '''
    await message.answer(info_text)

@router.message(lambda message: message.text == 'Как добраться')
async def button_info_response(message: types.Message):
    '''узнать путь до адреса'''
    info_address = '''
Адрес массажного кабинета: Яблочная 28А
Ссылка на яндекс карты: https://yandex.ru/maps/-/CDDk7IkU
Ссылка на 2гис: https://2gis.ru/sochi/geo/4222760305911685?m=39.705889%2C43.63989%2F16
Остановка автобуса: конечная остановка автобуса 37
'''
    await message.answer(info_address)

@router.message(lambda message: message.text == 'Записаться')
async def button_time_response(message: types.Message):
    '''записаться на прием'''
    info_time = '''
Для записи на прием перейдите по ссылке: https://mst.link/landman_artur
'''
    await message.answer(info_time)


@router.message(lambda message: message.text == 'Виды массажа')
async def button_types_massage_response(message: types.Message):
    text = 'подробнее о видах массажа можно ознакомиться во вкладке "Виды массажа"'
    await message.answer(text, reply_markup=types.ReplyKeyboardRemove())
    button_anticell = types.KeyboardButton(text='Антицеллюлитный')
    button_bankov = types.KeyboardButton(text='Баночный')
    button_limfodrenag = types.KeyboardButton(text='Лимфодреннажный')
    button_sport = types.KeyboardButton(text='Спортивный')
    button_face = types.KeyboardButton(text='Массаж лица')
    button_relax = types.KeyboardButton(text='Релакс')
    button_classic = types.KeyboardButton(text='Классический')
    button_strong = types.KeyboardButton(text='Силовой релакс')
    button_teyp = types.KeyboardButton(text='Тейпирование')
    button_instrumental = types.KeyboardButton(text='Инструментальная мобилизация')
    button_back = types.KeyboardButton(text='На главную')
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
            [
                button_bankov,
                button_anticell],
                [button_sport,
            
                button_face],
                [button_relax,
                button_classic],
                [button_limfodrenag,
                button_strong],
                [button_teyp,
                button_instrumental],
                [button_back,
            ]

        ])
    await message.answer('Для выбора нажмите нужную кнопку', reply_markup=buttons)

@router.message(lambda message: message.text == 'На главную')
async def button_back_response(message: types.Message): 
    text = 'вы теперь на главной'
    await message.answer(text, reply_markup=types.ReplyKeyboardRemove())
    buttons = make_start_buttons()
    await message.answer('Для выбора нажмите нужную кнопку', reply_markup=buttons)


@router.message(lambda message: message.text == 'Баночный')
async def button_bankov_response(message: types.Message):
    await bot.send_photo(
    chat_id=message.chat.id,
    photo=IMAGES_ID['banochniy'],
    caption=""
    )
    text = 'вы можете записаться на этот массаж или вернуться обратно'
    await message.answer(text, reply_markup=types.ReplyKeyboardRemove())
    button_back = types.KeyboardButton(text='Виды массажа')
    button_time = types.KeyboardButton(text='Записаться')
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[button_time, button_back]])
    await message.answer('Для выбора нажмите нужную кнопку', reply_markup=buttons)


@router.message(lambda message: message.text == 'Классический')
async def button_classic_response(message: types.Message):
    await bot.send_photo(
    chat_id=message.chat.id,
    photo=IMAGES_ID['classik_massage'],
    caption=""
    )
    text = 'вы можете записаться на этот массаж или вернуться обратно'
    await message.answer(text, reply_markup=types.ReplyKeyboardRemove())
    button_back = types.KeyboardButton(text='Виды массажа')
    button_time = types.KeyboardButton(text='Записаться')
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[button_time, button_back]])
    await message.answer('Для выбора нажмите нужную кнопку', reply_markup=buttons)


@router.message(lambda message: message.text == 'Антицеллюлитный')
async def button_anti_response(message: types.Message):
    await bot.send_photo(
    chat_id=message.chat.id,
    photo=IMAGES_ID['anti_cellulitniy'],
    caption=""
    )
    text = 'вы можете записаться на этот массаж или вернуться обратно'
    await message.answer(text, reply_markup=types.ReplyKeyboardRemove())
    button_back = types.KeyboardButton(text='Виды массажа')
    button_time = types.KeyboardButton(text='Записаться')
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[button_time, button_back]])
    await message.answer('Для выбора нажмите нужную кнопку', reply_markup=buttons)


@router.message(lambda message: message.text == 'Лимфодреннажный')
async def button_limfo_response(message: types.Message):
    await bot.send_photo(
    chat_id=message.chat.id,
    photo=IMAGES_ID['limfodrenaj'],
    caption=""
    )
    text = 'вы можете записаться на этот массаж или вернуться обратно'
    await message.answer(text, reply_markup=types.ReplyKeyboardRemove())
    button_back = types.KeyboardButton(text='Виды массажа')
    button_time = types.KeyboardButton(text='Записаться')
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[button_time, button_back]])
    await message.answer('Для выбора нажмите нужную кнопку', reply_markup=buttons)


@router.message(lambda message: message.text == 'Спортивный')
async def button_sport_response(message: types.Message):
    await bot.send_photo(
    chat_id=message.chat.id,
    photo=IMAGES_ID['sport_massage'],
    caption=""
    )
    text = 'вы можете записаться на этот массаж или вернуться обратно'
    await message.answer(text, reply_markup=types.ReplyKeyboardRemove())
    button_back = types.KeyboardButton(text='Виды массажа')
    button_time = types.KeyboardButton(text='Записаться')
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[button_time, button_back]])
    await message.answer('Для выбора нажмите нужную кнопку', reply_markup=buttons)


@router.message(lambda message: message.text == 'Релакс')
async def button_relax_response(message: types.Message):
    await bot.send_photo(
    chat_id=message.chat.id,
    photo=IMAGES_ID['just_relax'],
    caption=""
    )
    text = 'вы можете записаться на этот массаж или вернуться обратно'
    await message.answer(text, reply_markup=types.ReplyKeyboardRemove())
    button_back = types.KeyboardButton(text='Виды массажа')
    button_time = types.KeyboardButton(text='Записаться')
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[button_time, button_back]])
    await message.answer('Для выбора нажмите нужную кнопку', reply_markup=buttons)


@router.message(lambda message: message.text == 'Массаж лица')
async def button_face_response(message: types.Message):
    await bot.send_photo(
    chat_id=message.chat.id,
    photo=IMAGES_ID['massage_face'],
    caption=""
    )
    text = 'вы можете записаться на этот массаж или вернуться обратно'
    await message.answer(text, reply_markup=types.ReplyKeyboardRemove())
    button_back = types.KeyboardButton(text='Виды массажа')
    button_time = types.KeyboardButton(text='Записаться')
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[button_time, button_back]])
    await message.answer('Для выбора нажмите нужную кнопку', reply_markup=buttons)


@router.message(lambda message: message.text == 'Силовой релакс')
async def button_strong_response(message: types.Message):
    await bot.send_photo(
    chat_id=message.chat.id,
    photo=IMAGES_ID['strong_relax'],
    caption=""
    )
    text = 'вы можете записаться на этот массаж или вернуться обратно'
    await message.answer(text, reply_markup=types.ReplyKeyboardRemove())
    button_back = types.KeyboardButton(text='Виды массажа')
    button_time = types.KeyboardButton(text='Записаться')
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[button_time, button_back]])
    await message.answer('Для выбора нажмите нужную кнопку', reply_markup=buttons)


@router.message(lambda message: message.text == 'Тейпирование')
async def button_teyp_response(message: types.Message):
    await bot.send_photo(
    chat_id=message.chat.id,
    photo=IMAGES_ID['teypirovanie'],
    caption=""
    )
    text = 'вы можете записаться на этот массаж или вернуться обратно'
    await message.answer(text, reply_markup=types.ReplyKeyboardRemove())
    button_back = types.KeyboardButton(text='Виды массажа')
    button_time = types.KeyboardButton(text='Записаться')
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[button_time, button_back]])
    await message.answer('Для выбора нажмите нужную кнопку', reply_markup=buttons)


@router.message(lambda message: message.text == 'Инструментальная мобилизация')
async def button_instrumental_response(message: types.Message):
    await bot.send_photo(
    chat_id=message.chat.id,
    photo=IMAGES_ID['instrumental_mobiliz'],
    caption=""
    )
    text = 'вы можете записаться на этот массаж или вернуться обратно'
    await message.answer(text, reply_markup=types.ReplyKeyboardRemove())
    button_back = types.KeyboardButton(text='Виды массажа')
    button_time = types.KeyboardButton(text='Записаться')
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[button_time, button_back]])
    await message.answer('Для выбора нажмите нужную кнопку', reply_markup=buttons)


def make_start_buttons():
    button_price = types.KeyboardButton(text='Прайс лист')
    button_info = types.KeyboardButton(text='Как добраться')
    button_contacts = types.KeyboardButton(text='Контакты')
    button_types_massage = types.KeyboardButton(text='Виды массажа')
    button_times = types.KeyboardButton(text='Записаться')
    button_developer = types.KeyboardButton(text='Только для разработчика')
    # Создаем разметку клавиатуры с кнопками
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[button_developer], [button_price], [button_contacts], [button_times], [button_info], [button_types_massage]])
    return buttons


import logging 
from aiogram import Bot, Dispatcher, executor, types
import markups as nav

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "2132885848:AAHwhChFrVIYjsxHo5Xr89EDlNpA9aNcxQQ" 

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)


#buttons 

contactButtons = InlineKeyboardMarkup(row_width=1)
btnInst = InlineKeyboardButton(text='🧿 Instagram', url='https://instagram.com/kiev.exchange')
btnTg = InlineKeyboardButton(text='📲 Написать менеджеру', url='https://t.me/kiev_exchange_chat')
contactButtons.add(btnInst).add(btnTg)

#manager button 

managerButton = InlineKeyboardMarkup(row_width=1)
btnTgManager = InlineKeyboardButton(text='📲 Написать менеджеру', url='https://t.me/kiev_exchange_chat')
managerButton.add(btnTgManager)


# @dp.message_handler(commands=['start'])
# async def command_start(message: types.Message):
# 	await message.answer_photo('https://1944718.artcoco.web.hosting-test.net/evacuation_post.png')
# 	await bot.send_message(message.from_user.id, 'Вітаємо!🇺🇦🇺🇦🇺🇦\n\nВи звернулися до офіційного чат-боту центру підтримки "Евакуація".\n\nЯкщо Ви або Ваш родич потребує негайної допомоги з переселення, заповніть форму зазначину нижче і ми неодмінно надамо допомогу!'.format(message.from_user), reply_markup = urlButtons)

# @dp.message_handler()
# async def bot_message(message: types.Message):
# 	#await bot.send_message(message.from_user.id, message.text)
# 	if message.text != '/start':
# 		await bot.send_message(message.from_user.id, 'Вибачте! \n Але ми не змогли розібрати Ваш запит. \n Скористайетсь командою /start')


# if __name__ == '__main__':
# 	executor.start_polling(dp, skip_updates = True)



@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
	await bot.send_message(message.from_user.id, 'Добро пожаловать!'.format(message.from_user), reply_markup = nav.mainMenu)

@dp.message_handler()
async def bot_message(message: types.Message):
	if message.text == '💱 Актуальные курсы':
		await bot.send_message(message.from_user.id, '💱 *Актуальный курс валюты*\n\nПокупка - продажа\n🇺🇸 USD 0.0000 - 0.0000\n🇪🇺 EUR 0.0000 - 0.0000\n🇬🇧 GBP 0.0000 - 0.0000\n\nДля уточнения деталей свяжитесь с менеджером. '.format(message.from_user), parse_mode= 'Markdown', reply_markup = managerButton)
	elif message.text == '💵 Обмен валюты':
		await bot.send_message(message.from_user.id, '💵 *Обмен валюты*\n\nНа данный момент автоматический режим обмена не работает, мы стараемся максимально быстро исправить это неудобство.\n\nВы всегда можете совершить обмен связавшись с менеджером👇'.format(message.from_user), parse_mode= 'Markdown', reply_markup = managerButton)
	elif message.text == '📋 Услуги компании':
		await message.answer_photo('https://i.ibb.co/YDn4ckh/service.png')
		await bot.send_message(message.from_user.id, '📋 *Услуги компании*\n\n💎 *Операции с криптой*\nПокупка и продажа BTC, ETH, USDT за наличные доллары, евро, гривны и другие валюты.\n\n🇨🇳 *Оплата Юаня*\nЮань по лучшему курсу. Наличный и безналичный расчёт. Оплата счетов/инвойсов быстро и оперативно.\n\n🌐 *Денежные переводы*\nWire Transfer (SWIFT-SEPA), оплата инвойсов.\n\n🚓 *Инкассация*\nИнкассация денежных средств по всей Украине и Европе мы гарантируем 100% безопасность.\n\n💳 *Пополнение карт*\nПополнение банковских карт VISA/MASTERCARD по самым выгодным условиям.\n\nСвяжитесь с нами, нажав кнопку ниже, и получите свое уникальное предложение! 👇🏻'.format(message.from_user), parse_mode= 'Markdown', reply_markup = managerButton)
	elif message.text == '🪙 Перестановки':
		await bot.send_message(message.from_user.id, '🪙 *Перестановки*\n\nДенежные переводы по Украине и всему миру с самым выгодным и актуальным курсом обмена валют.\n\nДля уточнения деталей свяжитесь с менеджером.'.format(message.from_user), parse_mode= 'Markdown', reply_markup = managerButton)
	elif message.text == '🏦 Kiev Exchange 🏦':
		await message.answer_photo('https://i.ibb.co/cL75yK1/kiev-exchange.png')
		await bot.send_message(message.from_user.id, '*Kiev Exchange* — Безопасные и конфиденциальные сделки. Большие объемы, выгодный процент и хорошие условия для постоянных клиентов.'.format(message.from_user), parse_mode= 'Markdown', reply_markup = contactButtons)


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates = True)


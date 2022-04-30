from aiogram.types import ReplyKeyboardMarkup, KeyboardButton




#main menu 
btnCurrency = KeyboardButton('💱 Актуальные курсы') 
btnExchange = KeyboardButton('💵 Обмен валюты')
btnTransfer = KeyboardButton('🌐 Перестановки')
btnService = KeyboardButton('📋 Услуги компании')
btnAbout = KeyboardButton('🏦 Kiev Exchange 🏦')

mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnCurrency, btnExchange).add(btnTransfer, btnService).add(btnAbout)
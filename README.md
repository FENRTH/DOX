📌 Описание
DoxTool XD — это мощный инструмент для сбора информации, работающий в Termux (Android). Он позволяет искать данные по:

🔎 Телефону (Truecaller, WhatsApp, оператор)

📧 Email (утечки, соцсети через HaveIBeenPwned)

🌍 IP (геолокация, ISP, WHOIS)

👤 Юзернеймам (Telegram, GitHub, Instagram и 300+ других соцсетей через Sherlock)

🔗 Доменам (DNS, дата регистрации)

🚀 Установка (Termux)
bash
# 1. Обязательно обновляем пакеты
pkg update -y && pkg upgrade -y

# 2. Ставим ВСЕ необходимые зависимости
pkg install -y git python libxml2 libxslt clang make pkg-config openssl

# 3. Устанавливаем pip и обновляем его
python -m ensurepip --upgrade
pip install --upgrade pip

# 4. Качаем репозиторий
git clone https://github.com/FENRTH/DoxTool-XD.git
#далее переходим в папку cd DoxTool-XD

# 5. Альтернативная установка (без проблемных модулей)
pip install requests bs4 phonenumbers python-whois pyfiglet termcolor

# 6. Если нужно lxml (для парсинга) - ставим с флагами
LDFLAGS="-L/data/data/com.termux/files/usr/lib" CFLAGS="-I/data/data/com.termux/files/usr/include" pip install lxml

# 7. Запускаем!
python doxtool.py
🔑 Запуск
bash
python doxtool.py
Пароль: XDOSTOOL

📋 Меню функций
№	Модуль	Описание
1	🌍 Global Search	Поиск по имени/никнейму
2	☎️ Phone Lookup	Поиск по номеру (Truecaller, WhatsApp)
3	📱 Telegram Search	Поиск по @username в Telegram
4	📧 Email Investigation	Проверка email на утечки
5	🌐 IP Lookup	Геолокация по IP
6	👤 Username Search	Поиск по юзернейму в соцсетях
7	🔗 Domain Search	WHOIS, DNS информация
8	🚪 Exit	Выход
🔍 Примеры использования
1. Поиск по номеру телефона
📌 Ввод:


+79991234567  
📌 Результат:

Страна: Россия

Оператор: МТС

Truecaller: Иван Петров

WhatsApp: Аккаунт найден

2. Поиск по email
📌 Ввод:

Copy
example@gmail.com  
📌 Результат:

Утечки: 3 (LinkedIn, Adobe, Dropbox)

GitHub: Найден (user: example)

3. Поиск по IP
📌 Ввод:

Copy
8.8.8.8  
📌 Результат:

Страна: США

Провайдер: Google LLC

Город: Маунтин-Вью

⚠️ Важно!
❗ Только для образовательных целей!

🔒 Некоторые функции требуют API-ключей (Truecaller, Hunter.io).

🛠️ Для реального использования нужна доработка.

📜 Лицензия
Этот проект предназначен только для этичного использования (OSINT, пентест с разрешения).



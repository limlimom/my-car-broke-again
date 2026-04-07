# my-car-broke-again
# This program was written and tested on a MacBook M1 using an OBD-II cable with a CH340/CH341 chip and a Mercedes W216 CL500 (2010)

## 1. Hardware Setup
- A USB OBD2 cable with a CH340/CH341 chip is used.
- A CH34x driver must be installed on macOS. Detailed instructions are provided in section 6: CH34x Driver Installation.
- After installation and reboot, the system detects the cable as (may vary):
  /dev/tty.usbserial-140

## 2. Environment Setup
1. Create a project folder:
   mkdir ~/obd_test && cd ~/obd_test

2. Create a virtual environment:
   python3 -m venv .venv

3. Activate the environment:
   source .venv/bin/activate

4. Install dependencies:
   pip install --upgrade pip
   pip install pyserial obd

## 3. Project Files
- obd_menu.py — a universal menu-based program for working with the vehicle.
  Features:
  - Show vehicle VIN
  - Show trouble codes (DTC)
  - Clear trouble codes (Clear DTC)
  - Live data: RPM, speed, coolant temperature, air flow, throttle position

## 4. Running the Program
1. Activate the environment:
   source ~/obd_test/.venv/bin/activate

2. Run the program:
   python obd_menu.py

3. The menu will appear in the console:
   1 — Show VIN
   2 — Show trouble codes
   3 — Clear trouble codes
   4 — Live data (loop)
   0 — Exit

## 5. Important
- Turn the ignition ON before connecting (engine start is not required).
- If the program shows "No connection to the vehicle", check the cable and ignition.
- Data is available only via the standard OBD-II protocol (engine and basic parameters).
  ABS, airbags, and other system errors are not supported by a basic adapter.

## 6. CH34x Driver Installation (for USB OBD2 cable)

### Where to download
Official page:
http://www.wch.cn/downloads/CH34XSER_MAC_ZIP.html

(This is the official driver from the manufacturer of the CH340/CH341 chip used in the adapter)

### Supported systems
- macOS 10.9 — 10.15
- macOS 11.0 (Big Sur) and later, including Apple Silicon (M1/M2)

### Installation steps
1. Download the archive CH34XSER_MAC.ZIP and extract it.
2. Inside, there will be an installer in .pkg or .dmg format.
   - For macOS 11 and newer (M1, M2), it is recommended to use the .dmg version.
3. If you have a .dmg:
   - Open the file and drag CH34xVCPDriver to the Applications folder.
   - Find it in Launchpad, open it, and click Install.
4. If you have a .pkg:
   - Double-click it and follow the installation wizard instructions.

### Important steps
- Restart your Mac after installation.
- On first launch, the driver may be blocked by macOS security.
  - Open System Settings → Privacy & Security → General.
  - At the bottom, you will see an “Allow” button for the driver — click it.
- Connect the cable and verify it is visible in the system:
  ls /dev/tty.* | grep usb

## 7. Cable Compatibility

A USB OBD2 cable with a CH340/CH341 chip is an ELM327-compatible adapter.
It works with vehicles that support OBD-II/EOBD protocols.

### Supported vehicles
- USA: all passenger vehicles from 1996 and newer
- Europe: gasoline vehicles from 2001, diesel from 2004
- Russia and other markets: approximately the same years, depending on the manufacturer

### Available data
- VIN reading
- Reading and clearing standard engine trouble codes (Check Engine)
- Live data:
  - Engine RPM
  - Coolant temperature
  - Speed
  - Air flow (MAF)
  - Throttle position, etc.

### Limitations
- Only standard OBD-II data is available (engine, fuel system, emissions)
- Errors and data from other systems (ABS, airbags, transmission, climate, ESP, etc.)
  are NOT supported by this type of adapter
- For full diagnostics of some brands (e.g., Mercedes, BMW, VAG), proprietary scanners
  or more advanced adapters are required



# Данная программа была написана и протестирована на MacBook М1 для кабеля OBD-II на чипе CH340/CH341 с Mercedes W216 CL500, 2010

## 1. Подготовка оборудования
- Используется USB-OBD2 кабель на чипе CH340/CH341.
- Для macOS установлен драйвер CH34x. Продробная инструкция в разделе 6. Установка драйвера CH34x. 
- После установки и перезагрузки система видит кабель как (может отличаться):
  /dev/tty.usbserial-140

## 2. Подготовка рабочей среды
1. Создать папку для проекта:
   mkdir ~/obd_test && cd ~/obd_test

2. Создать виртуальное окружение:
   python3 -m venv .venv

3. Активировать окружение:
   source .venv/bin/activate

4. Установить библиотеки:
   pip install --upgrade pip
   pip install pyserial obd

## 3. Файлы проекта
- obd_menu.py — универсальная программа с меню для работы с автомобилем.
  Возможности:
  - Показать VIN автомобиля
  - Показать ошибки (DTC)
  - Очистить ошибки (Clear DTC)
  - Live data: обороты, скорость, температура, расход воздуха, дроссель

## 4. Запуск программы
1. Активировать окружение:
   source ~/obd_test/.venv/bin/activate

2. Запустить программу:
   python obd_menu.py

3. В консоли появится меню:
   1 — Показать VIN
   2 — Показать ошибки
   3 — Очистить ошибки
   4 — Live data (цикл)
   0 — Выйти

## 5. Важно
- Перед подключением включить зажигание (положение ON, не обязательно заводить мотор).
- Если программа пишет "Нет соединения с машиной" — проверить кабель и зажигание.
- Чтение доступно только по стандартному OBD-II протоколу (двигатель и базовые параметры).
  Ошибки ABS, подушек безопасности и других систем не поддерживаются простым адаптером.

## 6. Установка драйвера CH34x (для USB-OBD2 кабеля)

### Где скачать
Официальная страница:  
http://www.wch.cn/downloads/CH34XSER_MAC_ZIP.html

(это драйвер от производителя чипа CH340/CH341, используемого в USB-адаптере)

### Поддерживаемые системы
- macOS 10.9 — 10.15
- macOS 11.0 (Big Sur) и выше, включая Apple Silicon (M1/M2)

### Порядок установки
1. Скачай архив `CH34XSER_MAC.ZIP` и распакуй его.
2. Внутри будет установщик в формате `.pkg` или `.dmg`.
   - Для macOS 11 и выше (M1, M2) рекомендуется использовать **.dmg**.
3. Если у тебя `.dmg`:
   - Открой файл и перетащи `CH34xVCPDriver` в папку **Программы (Applications)**.
   - Найди его в Launchpad, открой и нажми кнопку **Install**.
4. Если у тебя `.pkg`:
   - Дважды кликни и следуй инструкциям мастера установки.

### Важные шаги
- После установки перезагрузи Mac.
- При первом запуске драйвер может быть заблокирован системой безопасности macOS.
  - Открой **Системные настройки → Конфиденциальность и безопасность → Основные**.
  - Внизу появится уведомление «Разрешить» для драйвера — нажми его.
- Подключи кабель и проверь, что он виден в системе:
  ```bash
  ls /dev/tty.* | grep usb

## 7. Совместимость кабеля

USB-OBD2 кабель на чипе CH340/CH341 — это адаптер стандарта ELM327.  
Он работает с автомобилями, поддерживающими OBD-II/EOBD протоколы.

### Поддерживаемые автомобили
- США: все легковые автомобили с 1996 года и новее.
- Европа: бензиновые автомобили с 2001 года, дизельные — с 2004 года.
- Россия и другие рынки: примерно с тех же лет, зависит от производителя.

### Какие данные доступны
- Чтение VIN-кода.
- Чтение и сброс стандартных ошибок двигателя (Check Engine).
- Получение «живых» параметров:
  - Обороты двигателя (RPM)
  - Температура охлаждающей жидкости
  - Скорость
  - Расход воздуха (MAF)
  - Положение дросселя и др.

### Ограничения
- Доступны только стандартные OBD-II данные (двигатель, топливная система, выбросы).
- Ошибки и параметры других систем (ABS, подушки безопасности, АКПП, климат, ESP и т. д.)
  **не поддерживаются** таким адаптером.
- Для полной диагностики некоторых марок (например, Mercedes, BMW, VAG) нужны фирменные сканеры
  или более продвинутые адаптеры.

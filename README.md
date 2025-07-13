# ribicont_bot_v1
Это предрелизная версия бота(ТГ токен и пароль Redis добавить во врема развертывания проекта)/It is a prerelease version of project, without tokens and redis account. 
## Подготовка и запуск проекта
*Убедиться в наличии установленной ubuntu 22.04
*Проверить что на сервере установлен Redis
```
sudo systemtcl status redis-server)
```
*Проверить наличие ТГ токена.
### Клонировать репозиторий на локальную машину:
```
git clone https://github.com/Vadim7744/rubicont_bot_v1
```
## Создать и активировать виртуальное окружение:
```
python -m venv venv
sourse venv/bin/activate 
```
## Установить зависимости(находятся в папке src):
```
pip install -r requirements.txt 
```
## Настроить Redis:
*Установить Redis
```
sudo apt update && sydo apt install redis
```
*В /etc/dnsmasq.conf добавьте:
```
interfaces=eth0
server=10.0.0.254/24
default-gateway=10.0.0.1
```
*Установить конфигурацию redis. В файле redis.cfg(создать по образцу одноименного txt файла в репозитории) в строке password указать свой пароль от redis
```
sudo nano /etc/redis/redis.conf
```
*Сохранить настройки redis и применить их
```
sudo systemctl restart redis-server
sudo systemctl status redis-server
```
## Настроить и запустить бота:
*В файле bot_token.yaml указать токен ТГ бота
*Запустить бота 
```
python -m bot.bot
```

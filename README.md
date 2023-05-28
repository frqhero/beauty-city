# Сервис [BeautyCity](https://docs.google.com/document/d/1V8htncvxA5PHayTMx9lSAvuImrEu6ckKCDHmAYj6HAI)

Интро: Ольга владеет сетью салонов красоты. Основной поток клиентов приходит из социальных сетей. Сейчас все заявки обрабатывает администратор, у которого уходит много времени на переписку, из-за чего теряется часть заявок и блокируются другие обязанности.
Ольга хочет заказать разработку бота, чтобы автоматизировать запись на процедуры, выбор специалиста, расписание самих специалистов, принимать оплату и чаевые.

1. `backend` - django project
2. `bot` - bot directory


### Заполнение данных
Для заполнения демонстрационных данных предусмотрено 3 менеджмент команды:
1. `import_masters`
2. `import_procedures`
3. `import_clients`  
Для запуска команды необходимо написать `./manage.py <command_name>`.

### .env файл
Некоторые значения используемые в приложении вынесены во внешние переменные. Перед запуском docker compose необходимо подготовить файл .env в директории infra.
* ALLOWED_HOSTS
* POSTGRES_PASSWORD
* POSTGRES_URL_SCHEMA=postgres://USER:PASSWORD@HOST:PORT/NAME [детали](https://pypi.org/project/dj-database-url/)
* SECRET_KEY
* DEBUG (true or false)
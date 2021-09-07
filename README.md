# Балансировщик
Пример балансировщика на санике.

balancer_app.py - инстанс сервиса балансировщика, запускается на localhost:8010,
на который приходят запросы, в формате 
http://127.0.0.1:8010/?video=http://127.0.0.1:8006/video/34/sdfsd,
где параметр video - это адрес запрашиваемого ресурса. Балансировщик редиректит
каждый 10ый запрос на оригинальный адрес запрашиваемого ресурса, все остальные 
запросы редиректит на один из поднятых media_app.py серверов, имитирующих 
провайдеров контента. 

## Запуск
###Собрать и запустить через docker-compose:
```bash
docker-compose -f compose.yaml up --build
```
** потом не забудьте дропнуть все созданные image's и контейнер
### Собрать локально:
Установить зависимости:
```bash
pip install -r requirements.txt
```
Запустить балансировщик:
```bash
python balancer_app.py
```
Запустить кластер серверов контента:
```bash
python run_all.py
```

## Проверка
Отправляем запрос:
```
http://127.0.0.1:8010/?video=http://127.0.0.1:8006/video/34/sdfsd
```
Ожидаемый результат:
Получаем редирект на 
```
http://127.0.0.1:8000/video/34/sdfsd
```
При повторном запросе сервер должен отдать редирект на 8001, 8002, ...

В браузере редиректы могут кэшироваться, поэтому лучше
проверять через постман.
# blog_project

## Описание проекта:
...

## Технологии:

Python  
Django  
SQLite   
HTML  
CSS  
Bootstrap  

## Инструкция по запуску:

### Клонируйте репозиторий:   
```sh/bash
git@github.com:Yara3630/blog_project.git
```
   
### Настройка и запуск приложения:
- Перейдите в директорию бэкенд-приложения проекта.
- Создайте виртуальное окружение:  
```sh/bash
python3 -m venv venv
```
- Активируйте виртуальное окружение:  
```sh/bash
source venv/bin/activate
```
- Установите зависимости:  
```sh/bash
pip install -r requirements.txt
```
- Перейдите в директорию с файлом manage.py и
примените миграции:  
```sh/bash
python3 manage.py migrate
```  
- Создайте суперпользователя:  
```sh/bash
python3 manage.py createsuperusersh/bash
```
- Добавьте в список ALLOWED_HOSTS внешний IP сервера, localhost и домен
- Создайте в директории проекта файл .env со следующими значениями:  
```sh/bash
SECRET_KEY='секретный код джанго'
```
- Запустите проект:  
```sh/bash
python3 manage.py runsever/bash
```
## Автор: 
   
[Ярослава С.](https://github.com/Yara3630)

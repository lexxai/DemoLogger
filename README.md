# DemoLogger

## Задача 
у Python налаштувати спеціальний logger, з єдиними налаштунками для всіх модулів пакету.

Опис тут:

https://lexxai.blogspot.com/2023/09/python-logger-logging-handlers.html


RESULT CONSOLE:
```
2023-09-26 03:28:29 [INFO] #15964 (package) INFO
2023-09-26 03:28:29 [ERROR] #15964 (package) ERROR
2023-09-26 03:28:29 [INFO] #15964 (package.module1) INFO M1
2023-09-26 03:28:29 [ERROR] #15964 (package.module1) ERROR M1
2023-09-26 03:28:29 [INFO] #15964 (package.module2) INFO M2
2023-09-26 03:28:29 [ERROR] #15964 (package.module2) ERROR M2
```

RESULT FILE : logs/debug.log
```
2023-09-26 03:28:29 [INFO] #15964 (package) INFO
2023-09-26 03:28:29 [DEBUG] #15964 (package) DEBUG
2023-09-26 03:28:29 [ERROR] #15964 (package) ERROR
2023-09-26 03:28:29 [INFO] #15964 (package.module1) INFO M1
2023-09-26 03:28:29 [DEBUG] #15964 (package.module1) DEBUG M1
2023-09-26 03:28:29 [ERROR] #15964 (package.module1) ERROR M1
2023-09-26 03:28:29 [INFO] #15964 (package.module2) INFO M2
2023-09-26 03:28:29 [DEBUG] #15964 (package.module2) DEBUG M2
2023-09-26 03:28:29 [ERROR] #15964 (package.module2) ERROR M2
```

RESULT FILE : logs/error.log
```
2023-09-26 03:28:29 [ERROR] #15964 (package) ERROR
2023-09-26 03:28:29 [ERROR] #15964 (package.module1) ERROR M1
2023-09-26 03:28:29 [ERROR] #15964 (package.module2) ERROR M2 
```


Вся сила у тому що ім'я підлеглих loggers будуються в залежності від імені кореневого файлу з конфігурацію.

Так  це для :

 - main.py = ''packge"
 - package/module1.py  = "package.module1"
 - package/module2.py  = "package.module2" 

Тому зробивши налаштування у  logging.getLogger( ''packge"), ці налаштування отримають  всі підлеглі "package.module1", "package.module1",  "package.*"

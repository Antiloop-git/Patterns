from my_framework import main
from urls import routes, fronts
from wsgiref.simple_server import make_server

application = main.Framework(routes, fronts)

with make_server('', 8080, application) as httpd:
    print("Запуск на порту 8080...")
    httpd.serve_forever()

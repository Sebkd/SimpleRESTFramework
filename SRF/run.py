from wsgiref.simple_server import make_server

from simple_rest_framework.main import Framework
from urls import routes, fronts


application = Framework(routes, fronts)

with make_server('', 8080, application) as httpd:
    print("Запуск на порту http://localhost:8080...")
    httpd.serve_forever()

# [END FILE]

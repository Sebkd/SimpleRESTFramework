import pathlib
import sys
from wsgiref.simple_server import make_server

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.resolve()))
from simple_rest_framework.main import Framework
from urls import fronts
from views import routes


application = Framework(routes, fronts)

with make_server('', 8080, application) as httpd:
    print("Запуск на порту http://localhost:8080...")
    httpd.serve_forever()

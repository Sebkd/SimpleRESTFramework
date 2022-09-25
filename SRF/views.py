import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.resolve()))
from SRF.simple_rest_framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', date=request.get('date', None))


class About:
    def __call__(self, request):
        return '200 OK', 'about'

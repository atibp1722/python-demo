import justpy as jp

from webapp.home import Home
from webapp.dictionary import Dictionary

jp.Route(Home.path,Home.serve)
jp.Route(Dictionary.path,Dictionary.serve)

jp.justpy(port=8001)
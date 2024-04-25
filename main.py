import justpy as jp
from webapp import pages
import inspect

from webapp.home import Home
from webapp.dictionary import Dictionary

# jp.Route(Home.path,Home.serve)
# jp.Route(Dictionary.path,Dictionary.serve)

imports=list(globals().values())

for i in imports:
    if inspect.isclass(i):
        if issubclass(i,pages.Page) and i is not pages.Page:
            jp.Route(i.path,i.serve)

jp.justpy(port=8001)
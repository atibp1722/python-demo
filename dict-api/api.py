import justpy as jp
import dicts

class API:
    
    @classmethod
    def serve(cls,req):
        wp=jp.WebPage()
        word=req.query_params.get('w')
        meaning=dicts.WordDefinition(word).get_definition()
        wp.html=meaning
        return wp
    
jp.Route('/api',API.serve)
jp.justpy()
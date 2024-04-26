import justpy as jp
import dicts
import json

class API:
    
    @classmethod
    def serve(cls,req):
        wp=jp.WebPage()
        word=req.query_params.get('w')
        meaning=dicts.WordDefinition(word).get_definition()

        json_response={
            "word":word,
            "meaning":meaning
        }

        wp.html=json.dumps(json_response)
        return wp

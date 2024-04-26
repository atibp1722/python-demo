import justpy as jp

class API:
    
    @classmethod
    def serve(cls,req):
        wp=jp.WebPage()
        word=req.query_params.get('w')
        jp.Div(a=wp,text=word.title())
        return wp
    
jp.Route('/api',API.serve)
jp.justpy()
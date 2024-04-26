import justpy as jp

class Docs():

    @classmethod
    def serve(cls,req):
        wp=jp.WebPage()

        div=jp.Div(a=wp,classes='bg-grey-200 h-screen p-2')
        jp.Div(a=div,text='API documentation for the dictionary app',classes='text-5xl m-2 text-center')
        jp.Div(a=div,text='Get meanining of English words',classes='text-lg')
        jp.Hr(a=div)
        jp.Div(a=div,text='http://127.0.0.1:8000/api?w=your_word')
        jp.Hr(a=div)
        jp.Div(a=div,text='''{"word": "exam",
                "meaning": 
               ["A session in which a product or piece of equipment is placed under everyday and/or
                extreme conditions and is examined for its durability, etc."]}''')
        return wp

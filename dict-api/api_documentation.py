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
        jp.Div(a=div,text='''{"word": "moon", 
               "meaning": ["A natural satellite of a planet.",
               "A month, particularly a lunar month (approximately 28 days).", 
               "To fuss over adoringly or with great affection.", 
               "Deliberately show ones bare ass (usually to an audience, 
               or at a place, where this is not expected or deemed appropriate).", 
               "To be lost in phantasies or be carried away by some internal vision, having temorarily lost (part of) contact to reality."]}''')
        return wp

import justpy as jp
import dicts as dct
from webapp import layout_master

class Dictionary:

    path='/dict'

    @classmethod
    def serve(cls,req):
        wp=jp.QuasarPage(tailwind=True)

        lays=layout_master.MasterLayout(a=wp,view='hHh lpR fFf')
        container=jp.QPageContainer(a=lays)

        div=jp.Div(a=container,classes='bg-grey-200 h-screen')
        jp.Div(a=div,text='Start using the Dictionary App!',classes='text-5xl text-center m-2')
        jp.Div(a=div,text='Use the app to find meaning of English words.',classes='text-lg py-2 px-3')

        inputs=jp.Div(a=div,classes='grid grid-cols-2')
        outputs=jp.Div(a=div,classes='m-2 p-2 text-lg border-2 h-40')

        answer=jp.Input(a=inputs,placeholder='Your word goes here...',outputdiv=outputs
                 ,classes='m-2 bg-gray-150 border-2 border-2-green-200 rounded w-64 focus:bg-white focus:outline-none focus:border-red-350 py-2 px-3')
        
        answer.on('input',cls.get_definition)

        return wp 
    
    @staticmethod
    def get_definition(widget,msg):
        meaning=dct.WordDefinition(widget.value).get()
        widget.outputs.text=" ".join(meaning)
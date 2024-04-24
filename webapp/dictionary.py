import justpy as jp

class Dictionary:

    path='/dict'

    def serve(self):
        wp=jp.QuasarPage(tailwind=True)
        div=jp.Div(a=wp,classes='bg-grey-200 h-screen')
        jp.Div(a=div,text='Start using the Dictionary App!',classes='text-5xl text-center m-2')
        
        jp.Div(a=div,text='Use the app to find meaning of English words.',classes='text-lg py-2 px-3')
        jp.Input(a=div,placeholder='Your word goes here...'
                 ,classes='m-2 bg-gray-150 border-2 border-2-green-200 rounded w-64 focus:bg-white focus:outline-none focus:border-red-350 py-2 px-3')
        
        jp.Div(a=div,classes='m-2 p-2 text-lg border-2 h-40')

        return wp
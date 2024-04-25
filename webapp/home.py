import justpy as jp
from webapp import layout_master

class Home:

    path='/'

    @classmethod
    def serve(cls,req):
        wp=jp.QuasarPage(tailwind=True)

        lays=layout_master.MasterLayout(a=wp,view='hHh lpR fFf')
        container=jp.QPageContainer(a=lays)

        div=jp.Div(a=container,classes='bg-grey-200 h-screen p-2')
        jp.Div(a=div,text='Welcome to Dictionary App',classes='text-5xl m-2 text-center')
        jp.Div(a=div,text='''It is a long established fact that a reader will be distracted by the readable content
               of a page when looking at its layout. The point of using Lorem Ipsum is that 
               it has a more-or-less normal distribution of letters, as opposed to using 
               Content here, content here, making it look like readable English. 
               Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text,
               and a search for lorem ipsum will uncover many web sites still in their infancy. 
               Various versions have evolved over the years, sometimes by accident, sometimes on purpose injected humour and the like.'''
               ,classes='text-lg')
        return wp

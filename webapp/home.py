import justpy as jp

class Home:

    path='/'

    @classmethod
    def serve(cls,req):
        wp=jp.QuasarPage(tailwind=True)

        layout=jp.QLayout(a=wp,view='hHh lpR fFf')
        header=jp.QHeader(a=layout,)
        toolbar=jp.QToolbar(a=header)
        
        drawer=jp.QDrawer(a=layout,show_if_above=True,v_model='left',bordered=True)
        scroller=jp.QScrollArea(a=drawer,classes='fit')
        q_list=jp.QList(a=scroller,classes='my-2')
        jp.A(a=q_list,text='Dictionary',href='/dict',classes='p-2 m-2 text-2xl text-black-500 hover:text-red-500')
        jp.Br(a=q_list)
        jp.A(a=q_list,text='Home',href='/',classes='p-2 m-2 text-2xl text-black-500 hover:text-red-500')
        jp.Br(a=q_list)
        jp.QBtn(a=toolbar,dense=True,round=True,flat=True,icon='menu',click=cls.move_drawer,drawer=drawer)
        jp.QToolbarTitle(a=toolbar,text='Welcome to Dictionary App')

        container=jp.QPageContainer(a=layout)

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
    
    @staticmethod
    def move_drawer(widget,msg):
        if widget.drawer.value:
            widget.drawer.value=False
        else:
            widget.drawer.value=True

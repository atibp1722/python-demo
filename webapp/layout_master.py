import justpy as jp

class MasterLayout(jp.QLayout):

    def __init__(self,**kwargs):

        super().__init__(**kwargs)
        
        header=jp.QHeader(a=self)
        toolbar=jp.QToolbar(a=header)
        
        drawer=jp.QDrawer(a=self,show_if_above=True,v_model='left',bordered=True)
        scroller=jp.QScrollArea(a=drawer,classes='fit')
        q_list=jp.QList(a=scroller,classes='my-2')
        jp.A(a=q_list,text='Dictionary',href='/dict',classes='p-2 m-2 text-2xl text-black-500 hover:text-red-500')
        jp.Br(a=q_list)
        jp.A(a=q_list,text='Home',href='/',classes='p-2 m-2 text-2xl text-black-500 hover:text-red-500')
        jp.Br(a=q_list)
        jp.QBtn(a=toolbar,dense=True,round=True,flat=True,icon='menu',click=self.move_drawer,drawer=drawer)
        jp.QToolbarTitle(a=toolbar,text='Welcome to Dictionary App')
    
    @staticmethod
    def move_drawer(widget,msg):
        if widget.drawer.value:
            widget.drawer.value=False
        else:
            widget.drawer.value=True
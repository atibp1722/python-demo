import pandas as pd

class WordDefinition:

    def __init__(self,word):
        self.word=word
    
    def get_definition(self):
        data=pd.read_csv('web-dict\words.csv')
        return tuple(data.loc[data['word']==self.word]['definition'])
    
wrd=WordDefinition(word='word')
#print(wrd.get_definition())
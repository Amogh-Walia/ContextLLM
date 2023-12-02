import json
from abc import ABC, abstractmethod 
  
  
class Context(ABC): 
    def __init__(self):
        self.Text = ''
    @abstractmethod
    def load_context(self): 
        pass
  
  
class JSON_Context(Context): 
  
    # overriding abstract method 
    def load_context(self,filename): 
        f = open(filename)
 
        # returns JSON object as 
        # a dictionary
        self.Text = json.load(f)["data"]

def CreatePrompt(model,Context,inp):
    template = """You are an AI who is supposed to use the following pieces of information to answer the user's question.
    The context is given below and you have to piece together the words into plain english
    Be a little bit verbose with your answers.
    Context: {context}
    Question: {question}
    Answer: 
    """
    
    prompt = template.format(context = Context.Text,question = inp)
    # prompt = inp
    output = model.Get_Output(prompt)
    return output

from typing import Any
from llama_cpp import Llama
from abc import ABC, abstractmethod 

print("namo")

class LLM(ABC):
      def __init__(self):
            self.model = None
            pass
      @abstractmethod
      def Get_Output(self,prompt):
            pass
      
      @abstractmethod
      def Start_model(self):
            pass


class TinyLama(LLM):
      def Start_model(self,path):
            self.model = Llama(model_path=path,n_ctx=4096, n_gpu_layers=30)
            
      def Get_Output(self, prompt,tokenMax =2048,stop =["Q:", "\n"],echo = False):
            print('starting')
            output = self.model(prompt,max_tokens=tokenMax, stream = True)
            reply = ""
            for line in output:
                text = line["choices"][0]["text"]
                reply += text

            return reply
            

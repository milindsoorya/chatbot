from __future__ import division 
from __future__ import unicode_literals
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionCustom(Action):
    def name(self):
        return "action_custom"
    
    def run(self,dispatcher,tracker,domain):
        return [FreeTextFormField("phoneno"),]
    
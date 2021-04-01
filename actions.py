# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
#from __future__ import absolute_import
#from __future__ import division
#from __future__ import unicode_literals
#from typing import Any, Text, Dict, List
#from rasa_sdk import Action, Tracker
#from rasa_sdk.executor import CollectingDispatcher
#from rasa_sdk.events import SlotSet
#from iexfinance.stocks import Stock
#from iexfinance.stocks import get_historical_data
#from iexfinance.refdata import get_symbols
#from datetime import datetime, date, timedelta
#import re 

#class ActionCurrentPrice(Action):
#	def name(self):
#		return "action_current_price"

#	def run(self, dispatcher, tracker, domain):

#		company_x = tracker.get_slot('company')

#		symbols = get_symbols()
#		for i in range(len(symbols)):
#			if company_x.lower() in symbols[i]["name"].lower():
#				company = symbols[i]["symbol"]


#		companyobj = Stock(company)
#		price = companyobj.get_price()

#		response = """{} shares is {} currently.""".format(company, price)
#		dispatcher.utter_message(response)
#		return [SlotSet('company', company)]
		
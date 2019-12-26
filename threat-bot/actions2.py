from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import requests
from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class GetMalware(Action):
    def name(self):
        return "get_url_malware"

    def run(self, dispatcher, tracker, domain):
        num_malware = tracker.get_slot('num')
        base_url = "https://www.virusradar.com/en/data/json/day/ZZ/{n}"
        url = base_url.format(**{'n': num_malware})
        num_inter = "{n}".format(**{'n': num_malware})
        res = requests.get(url)
        response = ""
        for i in range(0, int(num_inter)):
            todays_viruses = res.json()['viruses'][i]['virus']['name']
            response += todays_viruses +";"
        dispatcher.utter_message(response)
        return [SlotSet("num", num_malware)]

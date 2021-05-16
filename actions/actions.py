# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import pandas as pd
import random
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class RecommendMeal(Action):

    def name(self) -> Text:
        return "action_recommend_meal"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        meals = pd.read_json("data/meals.json")
        recommended_meal = random.choice(meals.name)

        dispatcher.utter_message(text=f"I recommend you the {recommended_meal}.")

        return []


class OrderMeal(Action):

    def name(self) -> Text:
        return "action_order_meal"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Validation si c'est sur le menu
        # Ajoute un slot ordered_meal

        ordered_meal = tracker.get_slot("meal")
        dispatcher.utter_message(text=f"The {ordered_meal}. It's noted!")

        return []

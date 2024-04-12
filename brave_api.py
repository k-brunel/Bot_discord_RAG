import os
from dotenv import load_dotenv
from brave import Brave
import json 
import gpt

# Your Brave API key
load_dotenv(dotenv_path='components/.env')

def brave_request(query):
    api_key = os.getenv("brave_key")
    brave = Brave(api_key)

    num_results = 10

    search_results = brave.search(q=query, count=num_results)
    web_results = search_results.web_results

    brave_input = ''
    for i in web_results:
        brave_input += "\n" + i['description']

    return brave_input
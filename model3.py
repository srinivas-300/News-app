import os
from pymongo import MongoClient
import urllib.parse
import google.generativeai as genai
from model2 import *

def get_documents():

    MONGO_USERNAME = os.getenv("MONGO_USERNAME")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")

    encoded_username = urllib.parse.quote_plus(MONGO_USERNAME)
    encoded_password = urllib.parse.quote_plus(MONGO_PASSWORD)

    atlas_connection_string = f"mongodb+srv://{encoded_username}:{encoded_password}@llmcluster.tudpm.mongodb.net/llmdb?retryWrites=true&w=majority&appName=llmcluster"

    client = MongoClient(atlas_connection_string)

    db = client['llmdb']
    collection = db['generalfeed']

    documents = list(collection.find())

    return documents

def get_titles(documents):
    titles = ""
    for i in documents:
        for j in i:
            if isinstance(i[j], dict):
                #print(str(i[j].get("title")))
                titles = titles + str(i[j].get("title"))+"              "
    return titles

def personal_feed_keywords(titles):
  model = genai.GenerativeModel(model_name="gemini-1.5-flash")
  prompt3 = f"""
    Analyze the similarity for the following titles of new articles: *{titles}*.

    Give me just 10 keywords that are more repetitive in all titles

    Do not add any extra explanation, introduction, or comments. Only return a string.

    Here are the articles:
    """
  response = model.generate_content(prompt3)

  return response.text

# def personal_feed():
#     documents = get_documents()
#     titles = get_titles(documents)
#     keywords = personal_feed_keywords(titles)
#     print("keywords-----------")
#     print(keywords)
#     links = news_feed(keywords)
#     print("links-----------")
#     print(links)
#     return links

def personal_feed():
    documents = get_documents()
    titles = get_titles(documents)
    keywords = personal_feed_keywords(titles)

    # clean keywords
    keywords_cleaned = keywords.replace(',', ' ').replace('\n', ' ').strip()
    keyword_list = keywords_cleaned.split()

    # Now pick top 4 keywords
    if len(keyword_list) >= 4:
        search_query = " ".join(keyword_list[:4])  # first 4 keywords
    elif len(keyword_list) >= 1:
        search_query = " ".join(keyword_list)      # whatever available
    else:
        search_query = "Technology"                # fallback

    print("Search Query ----------")
    print(search_query)

    links = news_feed(search_query)

    print("Fetched Links ----------")
    print(links)

    return links

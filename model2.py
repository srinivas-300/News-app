import feedparser
import google.generativeai as genai
import re

def fetch_google_news(keyword):
    keyword = keyword.replace(' ', '+')  # Replace spaces with +
    rss_url = f"https://news.google.com/rss/search?q={keyword}"
    feed = feedparser.parse(rss_url)
    return feed.entries

def news_feed(keyword):
    articles = fetch_google_news(keyword)

    temp = "    ".join(f"{i} {article['title']}" for i, article in enumerate(articles))

    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    prompt3 = f"""
    Analyze the similarity for the following query: *{keyword}*.

    From the articles listed below, select the top 10 most relevant titles based on similarity.

    Each article is prefixed by its ID number.

    Return your response strictly in this format:
    {{id: "title", id: "title", id: "title", id: "title", id: "title"}}

    Where:
    - ID must be the integer ID exactly as shown before each title (do not include ID inside the title string).
    - Title must be only the headline text (without the ID).

    Do not add any extra explanation, introduction, or comments. Only return the dictionary.

    Here are the articles:
    """ + temp

    response = model.generate_content(prompt3)

    #print(response.text)

    numbers = re.findall(r'(\d+):', response.text)
    numbers = list(map(int, numbers))

    links = {}

    for i, j in enumerate(numbers):
        links[str(i)] = {
            "url": articles[j]["links"][0]["href"],
            "title": articles[j]["title"]
        }

    return links

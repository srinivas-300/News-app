import os
import uuid
from flask import Flask, request, jsonify, render_template
import boto3
from dotenv import load_dotenv
from model import ocr_flow, no_ocr_flow
import google.generativeai as genai
from pymongo import MongoClient
import urllib.parse

# Load environment variables
load_dotenv()

app = Flask(__name__)

# AWS Configuration
AWS_REGION = os.getenv("AWS_REGION")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
BUCKET = os.getenv("AWS_S3_BUCKET_NAME")
API_KEY = os.getenv("GOOGLE_API_KEY")
MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")



# Configure GenAI
genai.configure(api_key=API_KEY)

# Configure S3 client
s3 = boto3.client(
    's3',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

OCR_QUERY = """
You are given an article. Please answer the following questions using the most relevant parts of the article.

1. What is the main argument or thesis of the following article? Answer in 20 words no less.
2. Summarize the article in 3 bullet points.
3. What are the key findings or conclusions of the article? Answer in 30 words no less.
4. What is the author's primary objective or intention in the article? Answer in 30 words no less.
"""

NO_OCR_QUERY = OCR_QUERY + "\n(without any other extra text not even headings) (Give me with out any headings like \"Here are ....\")"

ARTICLE_QUERY = """
You are given an article. Please answer the following question using the most relevant parts of the article.

1. Just give me 10 different closely related articles to the article provided and provide short description (without any other extra text not even headings) (Give me with out any headings like "Here are ....").
"""

NER_QUERY = """
You are given an article. Please answer the following question using the most relevant parts of the article.

1. Identify the top 2 name entities in the article provided and just give me 2 articles each for each entity (Don't give any duplicates) (without any other extra text not even headings) (Give me with out any headings like "Here are ....").
"""


def store(data):
    encoded_username = urllib.parse.quote_plus(MONGO_USERNAME)
    encoded_password = urllib.parse.quote_plus(MONGO_PASSWORD)

    # MongoDB Atlas connection string with encoded credentials
    atlas_connection_string = f"mongodb+srv://{encoded_username}:{encoded_password}@llmcluster.tudpm.mongodb.net/llmdb?retryWrites=true&w=majority&appName=llmcluster"

    # Connect to MongoDB Atlas
    client = MongoClient(atlas_connection_string)

    db = client['llmdb']

    collection = db['llmresponse']

    # Insert the document into the collection
    insert_result = collection.insert_one(data)
    print(f"Inserted document with id: {insert_result.inserted_id}")


def process_file_upload(request):
    if request.method == 'GET':
        return render_template('upload.html')

    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    unique_filename = f"{uuid.uuid4()}_{file.filename}"
    file_path = unique_filename
    file.save(file_path)

    try:
        s3_url = upload_to_s3(file_path, unique_filename)
    except Exception as e:
        return jsonify({'error': f'Upload to S3 failed: {str(e)}'}), 500

    return file_path, s3_url

def upload_to_s3(file_path, s3_key):
    s3.upload_file(file_path, BUCKET, s3_key)
    return f"https://{BUCKET}.s3.{AWS_REGION}.amazonaws.com/{s3_key}"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ocr', methods=['GET', 'POST'])
def ocr():
    result = process_file_upload(request)
    if isinstance(result, tuple):
        file_path, s3_url = result
    else:
        return result  # error response

    output = f"ocr_{uuid.uuid4()}.txt"
    try:
        summary = ocr_flow(OCR_QUERY, file_path, output)

        store({"method":"ocr","summary":summary})

        return jsonify({'status': 'success', 'summary': summary, 's3_url': s3_url})
    finally:
        if os.path.exists(file_path): os.remove(file_path)
        if os.path.exists(output): os.remove(output)

@app.route('/noocr', methods=['GET', 'POST'])
def noocr():
    result = process_file_upload(request)
    if isinstance(result, tuple):
        file_path, s3_url = result
    else:
        return result

    try:
        summary = no_ocr_flow(NO_OCR_QUERY, file_path)
        store({"method":"no-ocr","summary":summary})
        return jsonify({'status': 'success for no-ocr', 'summary': summary, 's3_url': s3_url})
    finally:
        if os.path.exists(file_path): os.remove(file_path)

@app.route('/articles', methods=['GET', 'POST'])
def articles():
    result = process_file_upload(request)
    if isinstance(result, tuple):
        file_path, s3_url = result
    else:
        return result

    try:
        summary = no_ocr_flow(ARTICLE_QUERY, file_path)
        store({"method":"articles","summary":summary})
        return jsonify({'status': 'success fetching other articles', 'summary': summary, 's3_url': s3_url})
    finally:
        if os.path.exists(file_path): os.remove(file_path)

@app.route('/ner', methods=['GET', 'POST'])
def ner():
    result = process_file_upload(request)
    if isinstance(result, tuple):
        file_path, s3_url = result
    else:
        return result

    try:
        summary = no_ocr_flow(NER_QUERY, file_path)
        store({"method":"ner","summary":summary})
        return jsonify({'status': 'success fetching ner articles', 'summary': summary, 's3_url': s3_url})
    finally:
        if os.path.exists(file_path): os.remove(file_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

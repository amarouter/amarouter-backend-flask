from flask import Flask, jsonify

import json

application = Flask(__name__)

@application.route('/')
def landing_page():
    return "Amarouter Backend"

@application.route('/blog_posts')
def get_blog_posts():
    db = None
    try:
        with open('db.json', 'r', encoding='utf-8') as file:
            db = file.read()
        db_dict = json.loads(db, encoding='utf-8')
        return jsonify(db_dict["blog_posts"])
    except FileNotFoundError:
        print('Dosya bulunamadi...')
        return 'Dosya bulunamadi...'
    except:
        print('Dosya okunurken hata olustu...')
        return 'Dosya okunurken hata olustu...'
    
if __name__ == "__main__":
    application.run()

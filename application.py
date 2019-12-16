from flask import Flask, request, jsonify

application = Flask(__name__)

related_terms = {
    'money': ['expense', 'fund'],
    'real-estate': ['property', 'building'],
    'event': ['party', 'meeting']
}

@application.route('/', methods=['POST'])
def home():
    data = request.get_json('search')
    print(data.keys)
    search = data['search']
    print(search)
    keyword = search.split()[0]
    related_words = related_terms[keyword]
    second_search = search.replace(keyword, related_words[0])
    third_search = search.replace(keyword, related_words[1])
    new_searches = {
        'search': search,
        'search_two': second_search,
        'search_three': third_search
    }
    return jsonify(new_searches)

if __name__ == '__main__':
    application.run()
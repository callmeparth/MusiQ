import datetime
import urllib2

#urllib2.urlopen("http://example.com/foo/bar").read()

app = Flask(__name__)

connection = Connection('localhost', 27017)
class Entry(Document):
    structure = {
        'artist_name': basestring,
        'song_name': basestring,
        'url': basestring,
    }

@app.route('/')
def index():
    return render_template('index.html')

YT_SEARCH_URL = 'https://gdata.youtube.com/feeds/api/standardfeeds/most_popular'


@app.route('/results', methods=['POST'])
def results():
    search_term = request.form['term']
    location = request.form['location']

    data = {
        'artist_term': artist_term,
        'song_term': song_term

    }
    query_string = urllib.urlencode(data)
    api_url = YT_SEARCH_URL + "?" + query_string
    signed_url = sign_url(api_url)
    response = requests.get(signed_url)
    json_response = json.loads(response.text)

    return render_template('results.html',
                            artist_term=artist_term
                            song_term=song_term
                            videos=json_response['videos'])

@app.route('/save', methods=["POST"])
def save():
    new_entry = collection.Entry()
    new_entry.artist_name = request.form['artist_name']
    new_entry.url = request.form['url']
    new_entry.song_name = request.form['song_name']
    return request.form['url']

if __name__ == '__main__':
    app.run(debug=True)
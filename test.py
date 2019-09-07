from flask import Flask, request, render_template, Markup, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home(sumvalue=None, info=None):
	return render_template('hello.html', sumvalue=sumvalue)

@app.route('/', methods=['POST'])
def parse_data():
    weight = request.form['weight']
    period = request.form['period']
    drinks = request.form['drinks']
    gender = request.form.get('gender')

    invalid = len(weight) == 0 or len(period) == 0 or len(drinks) == 0 or len(gender) == 0

    if invalid:
    	return render_template('hello.html')

    if gender == "male":
        bodwat = 0.58
    elif gender == "female":
        bodwat = 0.49
    else:
        bodwat = 0.535

    a = 0.806*float(drinks)*1.2
    b = bodwat*float(weight)
    c = a/b
    d = 0.017 * float(period)
    e = c - d

    s = '{}'.format(e)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, 3)
    i, p, d = s.partition('.')
    f = '.'.join([i, (d+'0'*3)[:3]])

    if float(f) < 0:
    	f = '0'
    	text = ['Good to go fam',
    			'Have fun tonight ;)',
    			'Drink responsibly ;) ;)']

    elif float(f) >= 0.02 and float(f) <= 0.09:
    	text = ['You’re buzzing!',
    			'You’re happy-go-lucky right now – you probably feel nice and warm, loose, and euphoric, yeah? LIT.',
    			'Just make sure to keep your emotions in check and remember that thinking before doing always comes in handy.']

    elif float(f) > 0.09 and float(f) <= 0.15:
    	text = ['Tipsy AF',
    			'You might think you can slide down that railing on your ass and stick that landing, but from a good friend to another, you can’t. Your own judgement right now isn’t the best, bud.',
    			'Time to take it easy for the night on the drinks and enjoy your company!']

    elif float(f) > 0.15 and float(f) <= 0.20:
    	text = ['Simmer down',
    			'FAM CHILL, you should’ve stopped drinking like… 2 beers ago. You think you’re fine but, like, YOU’RE NOT. JUST TRYING TO BE HELPFUL OVER HERE. You’re not as invincible as you feel in this moment, and neither is your liver.',
    			'Unless you enjoy being the starlet of everyone’s screenshot gallery from those snaps']

    elif float(f) > 0.20 and float(f) <= 0.25:
    	text = ['Shitfaced',
    			'At this point if you can actually read this – you’re the friend of the person that’s shitfaced right now.',
    			'I DON’T KNOW IF YOU COULD TELL OR NAH, BUT ALL OF HIS/HER BODILY FUNCTIONS ARE NOT WORKING WELL AT ALL. This is no bueno. They are on pace to choking on their vomit – and we all know they’re not going to be the one to clean it up.']

    elif float(f) > 0.25 and float(f) <= 0.34:
    	text = ['BLACKOUT',
    			'FRIEND OF PERSON WHO’S BAC IS AT THIS FUCKIN’ RIDICULOUS LEVEL RIGHT NOW: stick with your friend. Support your friend – literally. Get them to sit in one place because they are – if they haven’t already – about to pass out.',
    			'Keep them hydrated and be ready to call for extra assistance – yes, 911 if it comes to it.']

    elif float(f) > 0.34:
    	text = ['911 NOW',
    			'If you haven’t already, get the fuck off this and call 911.']

    else:
    	text = ['Good to go fam',
    			'Have fun tonight ;)',
    			'Drink responsibly ;) ;)']

    return render_template('hello2.html', sumvalue=f, info=text)

@app.route('/blah')
def blah():
	return redirect("http://www.countbacula.com", code=302)


if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=5000, debug=False)
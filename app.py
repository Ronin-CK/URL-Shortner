from flask import Flask, request, redirect
import random
import string

app = Flask(__name__)

# stores all urls, resets when server restarts
# TODO: maybe add sqlite later
urls = {}

def generate_code():
    # 6 chars is enough, who cares
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=6))


@app.route('/')
def index():
    # inline html, sue me
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>URL Shortener</title>
    <style>
        * { box-sizing: border-box; }
        body {
            font-family: -apple-system, sans-serif;
            max-width: 500px;
            margin: 80px auto;
            padding: 0 20px;
        }
        h1 { margin-bottom: 30px; }
        input {
            width: 100%;
            padding: 12px;
            font-size: 16px;
            border: 2px solid #ddd;
            border-radius: 4px;
            margin-bottom: 10px;
        }
        button {
            padding: 12px 24px;
            background: #0066ff;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
        }
        button:hover { background: #0052cc; }
    </style>
</head>
<body>
    <h1>URL Shortener</h1>
    <form method="POST" action="/shorten">
        <input type="text" name="url" placeholder="https://example.com/your-long-url" required>
        <button type="submit">Shorten</button>
    </form>
</body>
</html>
'''


@app.route('/shorten', methods=['POST'])
def shorten():
    original = request.form.get('url', '').strip()

    # validation - keep it simple
    if not original:
        return 'bruh, enter a url', 400

    if not original.startswith('http://') and not original.startswith('https://'):
        return 'url needs http:// or https://', 400

    # generate code, check for collision (rare but just in case)
    code = generate_code()
    while code in urls:
        code = generate_code()

    urls[code] = original
    short = request.host_url + code

    return f'''
<!DOCTYPE html>
<html>
<head>
    <title>Done</title>
    <style>
        body {{
            font-family: -apple-system, sans-serif;
            max-width: 500px;
            margin: 80px auto;
            padding: 0 20px;
        }}
        .box {{
            background: #f0f9f0;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
        }}
        a {{ color: #0066ff; }}
        .short {{ font-size: 18px; font-weight: bold; }}
    </style>
</head>
<body>
    <h1>done ✓</h1>
    <div class="box">
        <p class="short"><a href="{short}">{short}</a></p>
    </div>
    <p>Original: {original[:50]}{"..." if len(original) > 50 else ""}</p>
    <br>
    <a href="/">← shorten another</a>
</body>
</html>
'''


@app.route('/<code>')
def go(code):
    if code not in urls:
        return 'not found', 404

    # this is the whole point
    return redirect(urls[code], 302)


# run it
if __name__ == '__main__':
    app.run(debug=True, port=5000)

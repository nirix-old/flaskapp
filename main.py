from flask import Flask, render_template, url_for
import handlers

app = Flask(__name__)

@app.route('/')
def root():
    root = handlers.HomeHandler()
    return root.index()

@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html')

if __name__ == '__main__':
    app.run(debug=True)
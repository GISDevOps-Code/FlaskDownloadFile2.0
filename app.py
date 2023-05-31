from flask import Flask
from views import views
from flask_autoindex import AutoIndex

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

spath = "downloads"

files_index = AutoIndex(app, browse_root=spath, add_url_rules=False)

@app.route('/files')
@app.route('/files/<path:path>')
def autoindex(path='.'):
    return files_index.render_autoindex(path, template='files.html')

if __name__ == '__main__':
    app.run(debug=True)
from web.app import app
from web.posts.blueprint import posts

import web.view

app.register_blueprint(posts, url_prefix='/blog')

if __name__ == "__main__":
    app.run('127.0.0.1', '5000')

from webApp import create_app
from webApp import db

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)

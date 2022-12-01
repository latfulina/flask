from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Обращаемся к настройкам,для создания базы данных. Можно подключить другую. После :/// название БД
app.config ['SQLALCHEMY_DATEBASE_URI'] = 'sqlite:///shop.db'
# объект на основе класса
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    appellation = db.Column(db.String, nullable = False)
    price = db.Column(db.Integer, nullable = False )
    isActive = db.Column(db.Boolean, default = True)

# Для отслеживания URL-адресов
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/catalog')
def catalog():
    # Будет обрабатывать HTML-шаблон
    return render_template('catalog.html')


# Запуск сервера,с проверкой. Если этот файл запускается,как основной файл
if __name__ == "__main__":
    app.run(debug=True)

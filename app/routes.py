from flask import Flask, render_template, request, redirect, url_for

from app import app

# Инициализация Flask-приложения
#app = Flask(__name__)


# Главная страница с формой
@app.route('/', methods=['GET', 'POST'])
def index():
    # Если форма отправлена методом POST
    if request.method == 'POST':
        # Получение данных из формы
        name = request.form['name']
        city = request.form['city']
        hobby = request.form['hobby']
        age = request.form['age']

        # Передача данных обратно в шаблон для отображения
        return render_template('form.html', name=name, city=city, hobby=hobby, age=age)

    # Если форма еще не отправлена
    return render_template('form.html')


# Запуск Flask-приложения
if __name__ == '__main__':
    app.run(debug=True)

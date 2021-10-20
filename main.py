from flask import Flask, request, render_template, redirect, url_for
from peewee import SqliteDatabase, Model, PrimaryKeyField, CharField

db = SqliteDatabase('Demo_data.db')

app = Flask(__name__)


class BaseModel(Model):
    class Meta:
        database = db


class English(BaseModel):
    id = PrimaryKeyField(null=False)
    word = CharField(max_length=100, null=False)
    translate = CharField(max_length=100, null=False)

    class Meta:
        db_table = 'English'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/insert_data', methods=['POST', 'GET'])
def insert_data():
    if request.method == "POST":
            word = request.form['word']
            if not English.select().where(English.word == word):
                try:
                    return redirect("/create_data", code=302)
                except:
                    return render_template('error.html')

            else:
                data = English.select(English.translate).where(English.word == word)
                return render_template('word_in_table.html', data=data)
    else:
        return render_template('insert_data.html')

@app.route('/create_data', methods=['POST', 'GET'])
def create_data():
    if request.method == "POST":
        try:
            word = request.form['word']
            translate = request.form['translate']
            English.create(word=word, translate=translate)
            return render_template('success.html')
        except:
            return render_template('error.html')
    else:
        return render_template('word_not_in_table.html')


@app.route('/update_data', methods=['POST', 'GET'])
def update_data():
    if request.method == "POST":
        word1 = request.form['word1']
        word2 = request.form['word2']
        try:
            English.update(translate=word2).where(English.word == word1).execute()
            return render_template('success.html')
        except:
            return render_template('error.html')
    else:
        return render_template('update_data.html')

@app.route('/delete_data', methods=['POST', 'GET'])
def delete_data():
    if request.method == "POST":
        word_delete = request.form['word1']
        try:
            del_data = English.select(English.id).where(English.word == word_delete)
            English.delete_by_id(del_data)
            return render_template('success.html')
        except:
            return render_template('error.html')
    else:
        return render_template('delete_data.html')


@app.route('/show_data_all', methods=['POST', 'GET'])
def show_data_all():
    if request.method == "GET":
        data =  English.select()
        return render_template('show_data_all.html', data=data)
    else:
        return render_template('error.html')

@app.route('/show_data_by_id', methods=['POST', 'GET'])
def show_data_by_id():
    if request.method == "POST":
        data_id = request.form['data_id']
        try:
            data_select = English.select().where(English.id == data_id)
            return render_template('show_data_by_id.html', data=data_select)
        except:
            return render_template('error.html')
    else:
        return render_template('show_data_id_post.html')

if __name__ == '__main__':
    English.create_table()
    app.run(debug=True)


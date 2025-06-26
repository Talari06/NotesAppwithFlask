from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from forms import NoteForm, DeleteForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SECRET_KEY'] = 'your-secret-key'  # change this in production
db = SQLAlchemy(app)

from models import Note

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NoteForm()
    delete_form = DeleteForm()
    if form.validate_on_submit():
        new_note = Note(content=form.note.data)
        db.session.add(new_note)
        db.session.commit()
        return redirect(url_for('index'))
    notes = Note.query.all()
    return render_template('index.html', form=form, delete_form=delete_form, notes=notes)

@app.route('/delete/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

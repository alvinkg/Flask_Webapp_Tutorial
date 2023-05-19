from flask import Blueprint,json, jsonify, render_template, request, flash
from flask_login import login_required,current_user
from . import db
from .models import Note

# setup file as Blueprint
views = Blueprint('views', __name__)

# this is where we store out routes

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        
        # not sure why so long
        if len(note) <= 8:
            # print(len(note))
            flash('Note empty.', category='error')
        else:
            # print('note')
            # print(len(note))
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added', category='success')
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    # take data from POST request
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({})
            

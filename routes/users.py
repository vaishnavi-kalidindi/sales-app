from flask import render_template,request, \
     redirect,url_for
from app import app
from app import db
from models.user import User
from sqlalchemy import or_  # Import the 'or_' operator

@app.route('/users')
def users():
    search_query = request.args.get('search', '')
    
    if search_query:
        # Split the search query into individual words
        search_terms = search_query.split()
        
        # Build a dynamic filter for each search term, combining them with 'or_'
        filters = [User.email.ilike(f"%{term}%") for term in search_terms]
        
        # Apply the filters using 'or_'
        user_recs = db.session.query(User).filter(or_(*filters)).all()
    else:
        # If no search query provided, retrieve all users
        user_recs = db.session.query(User).all()

    users = list(map(lambda rec: rec.__dict__, user_recs))
    return render_template('users.html', users=users)




@app.route('/user', methods=['GET', 'POST'])
def user():
    id=request.args.get('id')
    if request.method == 'GET':
        if id:
            user=User.query.get(id)
            form_action=request.args.get('action')
            if form_action == 'edit':
                return render_template('user_form.html', user=user)
            elif form_action == 'delete':
                db.session.delete(user)
                db.session.commit()
                return redirect(url_for('users'))
            return render_template('user_detail.html', user=user)
        else:
            return render_template('user_form.html', user=None)
    elif request.method == 'POST':
        id = request.form['id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        email = request.form['email']
        if id:
            user = User.query.get(id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email 
        else:
            user = User (
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email
        )
        db.session.add(user)
    db.session.commit()
    return redirect(url_for('users'))

from market import app
from flask import render_template, url_for, redirect, flash, request
from market.models import Item, User
from market.forms import PurchaseItemForm, RegisterForm, LoginForm, SellItemForm
from market import db
from flask_login import login_user, logout_user,  login_required, current_user



@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')




@app.route('/market', methods = ['GET', 'POST'])
@login_required
def market():
    purchase_form = PurchaseItemForm()
    sell_form = SellItemForm()
    if request.method == 'POST':

        # Purchase item 
        purchased_item =  request.form.get('purchased_item')
        p_item_obj = Item.query.filter_by(name=purchased_item).first()
        if p_item_obj:
            if current_user.can_buy(p_item_obj):
                p_item_obj.buy(current_user)
                flash(f'Congrats! You purchased {p_item_obj.name} for {p_item_obj.price}$', category='success')
            else:
                flash(f'Sorry, you do not have enough money to buy this item.', category='danger')
            return redirect(url_for('market'))

        # Sell item 
        sold_item =  request.form.get('sold_item')
        sold_item_obj = Item.query.filter_by(name=sold_item).first()
        if sold_item_obj:
            if current_user.can_sell(sold_item_obj):
                sold_item_obj.sell(current_user)
                flash(f'Congrats! You sold {sold_item_obj.name} for {sold_item_obj.price}$', category='success')
            else:
                flash(f'Sorry, something went wrong, please try again.', category='danger')
            return redirect(url_for('market'))



    if request.method == 'GET':
        
        items = Item.query.filter_by(owner=None)
        owned_items = Item.query.filter_by(owner=current_user.id)
    return render_template('market.html', items=items, purchase_form=purchase_form, sell_form=sell_form,  owned_items=owned_items) 





@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    
    if form.validate_on_submit():
        user_to_create = User(username = form.username.data,
                            email_address = form.email.data,
                            password = form.password1.data)

        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market'))
    
    if form.errors != {}:
        for error_msg in form.errors.values():
            flash(f'There was an error: {error_msg[0]}', category='danger')

    return render_template('register.html', form = form)





@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        check_user = User.query.filter_by(username=form.username.data).first()
        if check_user and check_user.check_password(secret = form.password.data):
            login_user(check_user)
            flash(f'Nice! You are Logged in as  {check_user.username}', category='success') 
            return redirect(url_for('market'))
    
        else:
            flash(f'Username or password does not match, please try again.', category='danger')

    return render_template('login.html', form = form)





@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out', category="info")
    return redirect(url_for('home_page'))


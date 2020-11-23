import os

from flask import Flask, render_template, request, session, flash, redirect, url_for, json
import secrets
import database

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass,
                                                                                 secrets.dbhost, secrets.dbname)
app.config['SECRET_KEY'] = os.urandom(24)
# 'SuperSecretKey'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False


@app.route("/")
def home():
    if not session.get('logged_in'):
        return render_template("home.html")
    else:
        if session.get('employee'):
            return redirect(url_for('employee'))
        return redirect(url_for('landpage'))


@app.route('/employee.htm')
def employee():
    start = database.startdate_employee(session['user'])
    position = database.position_employee(session['user'])
    wage = database.wage_employee(session['user'])
    user_id = database.id_fromemployee(session['uname'])
    userschedule = database.userschedule(user_id)
    return render_template("employee.html", user=session['user'], start=start, position=position, wage=wage,
                           userschedule=userschedule)


@app.route('/schedule.html')
def schedule():
    currentschedule = database.schedule()
    return render_template("schedule.html", schedule=currentschedule)


@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        session['logged_in'] = False
        return render_template("login.html")
    if request.method == 'POST':
        if request.form['account'] == 'customer':
            correctpass = database.userpass(request.form['uname'])
            if correctpass == request.form['psw']:
                session['logged_in'] = True
                session['user'] = database.fullname_fromuser(request.form['uname'])
                session['uname'] = request.form['uname']
                return home()
            else:
                flash('wrong username/password')

        elif request.form['account'] == 'employee':
            correctpass = database.userpassemployee(request.form['uname'])
            if correctpass == request.form['psw']:
                session['logged_in'] = True
                session['employee'] = True
                session['user'] = database.fullname_fromuseremployee(request.form['uname'])
                session['uname'] = request.form['uname']
                return home()
            else:
                flash('wrong username/password')

    return redirect(url_for('login'))


@app.route("/regform.html", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("regform.html")
    if request.method == 'POST':
        # add user to db
        database.new_user(request.form['fname'], request.form['lname'], request.form['uname'],
                          request.form['psw'], request.form['pn'])
        return render_template("login.html")


@app.route("/landpage.html")
def landpage():
    userid = database.id_fromuser(session['uname'])
    order_list = database.past_orders(userid)
    orderlist = []
    for x in order_list:
        orderlist.append(x)

    return render_template("landpage.html", fullname=session['user'], orders=orderlist)


@app.route("/order_two.html", methods=['GET', 'POST'])
def order():
    if request.method == 'GET':
        return render_template("order_two.html")
    if request.method == 'POST':

        one = int(request.form['first'])
        two = int(request.form['second'])
        three = int(request.form['third'])
        four = int(request.form['fourth'])
        five = int(request.form['fifth'])
        orderlist = []
        checkoutfinal = []
        pricelist = []
        totalprice = 0
        if one > 0:
            orderlist.append(one)
        if two > 0:
            orderlist.append(two)
        if three > 0:
            orderlist.append(three)
        if four > 0:
            orderlist.append(four)
        if five > 0:
            orderlist.append(five)

        for x in orderlist:
            checkoutfinal.append(database.menu_item(x))

        for x in orderlist:
            pricelist.append(float(database.menu_item_price(x)))

        for ele in range(0, len(pricelist)):
            totalprice = totalprice + pricelist[ele]

        session['order'] = orderlist
        session['location'] = request.form['location']
        session['price'] = totalprice
        locationorder = database.location_byid(session['location'])

        return render_template("cart.html", checkout=checkoutfinal, location=locationorder, total=totalprice)


@app.route("/cart.html", methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        userid = database.id_fromuser(session['uname'])
        database.new_order(session.get('location', None), userid, session.get('price'))
        idorder = database.orderid_lastinsert(userid)
        for x in session.get("order"):
            database.insert_fooditems(idorder, x)
        return render_template("/ordercomplete.html", ordernumber=idorder)



@app.route("/menu.html")
def menu():
    return render_template("menu.html")


@app.route("/location.html")
def location():
    return render_template("location.html")


@app.route("/profile.html")
def profile_business():
    userid = database.id_fromuser(session['uname'])
    # 1
    working_lastwk_nov = database.working_lastwk_nov()
    # 2
    usermsc_orders = database.user_orders_msc(userid)
    # 3
    most_lunchorders = database.most_locations_lunch()
    # 4
    sum_order = database.sum_past_orders(userid)
    # 5
    userzone_orders = database.user_orders_zone()
    # 6
    fish_orders = database.zone_fishorders()
    # 7
    max_breakfast = database.most_locations_breakfast()
    # 8
    locrev = database.locations_revenues()
    # 9
    mostorders = database.most_locations_diner()
    # 10
    answerlist = database.user_twentytwo_total_orders()
    return render_template("profile.html", user=session['user'],
                           nov=working_lastwk_nov,
                           timesMSC=usermsc_orders,
                           lunchlocation=most_lunchorders,
                           ordersTotal=sum_order,
                           customers=userzone_orders,
                           totalFish=fish_orders,
                           breakfastlocation=max_breakfast,
                           locations=locrev,
                           location=mostorders,
                           user_twentytwo=answerlist[0], times_user=answerlist[1])


if __name__ == '__main__':
    database.init_db()
    app.run()

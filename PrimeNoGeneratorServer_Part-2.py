# Part-2

from flask import Flask, jsonify, session,request, render_template, g
from flask_sqlalchemy import SQLAlchemy
import math
import time
import datetime
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///sqlite.db'
app.secret_key = "Testing"
db = SQLAlchemy(app)


# Creating table for keeping track of no. of times every user requested and its time stamp.
class TaskUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    elapsed_time = db.Column(db.String(5000))
    timestamp = db.Column(db.String(5000))
    cntFreq = db.Column(db.Integer)


db.create_all()
@app.before_request
def before_request():
    g.request_start_time = time.time()
    g.request_time = lambda: "%.5fs" % (time.time() - g.request_start_time)

# routing for app giving two inputs with "/" i.e. "localhost:5000/1/10" will give
# prime numbers between 1 and 10
@app.route('/<start>/<end>')
def primeNo(start, end):
    # for existing user

    if session.get('id'):
        user = TaskUser.query.filter_by(id=session.get('id')).first()
        user.elapsed_time = user.elapsed_time + " " + g.request_time()
        user.timestamp = user.timestamp + ","+ str(datetime.datetime.now())
        user.cntFreq += 1
        db.session.commit()

    else:
        user = TaskUser(timestamp=str(datetime.datetime.now()), elapsed_time=g.request_time(), cntFreq=1)
        # adding user
        db.session.add(user)
        db.session.commit()
        session['id'] = user.id
    dic = {}
    start = int(start)
    end = int(end)
    ans = []

    # maintain a temporary list
    temp = [True] * (end + 1)

    # 0 and 1 are not prime so marking them False
    temp[0] = False
    temp[1] = False

    # Check all the values from 2 to sqrt(end) and
    # mark every multiple of them False
    # Note that we are considering values only from i*i upto end
    for i in range(2, int(math.sqrt(end) + 1)):
        if temp[i] != False:
            for j in range(i * i, end + 1, i):
                temp[j] = False

    # Append the values from start to end if they are True
    for i in range(start, end + 1):
        if temp[i] == True:
            ans.append(i)

    dic[f"Prime numbers between {start} and {end} is "] = ans
    dic["No. of times this user has requested"] = user.cntFreq
    dic["elapsed_time"] = user.elapsed_time.split()
    dic["LengthOfPrimeNumberList"] = len(ans)
    dic['time_stamp'] = user.timestamp.split(",")
    # Finally Return the json object
    return jsonify(dic)


if __name__ == '__main__':
    app.run(debug=True)
#     Time Complexity : O(N (log(log N)))
#     Space Complexity : O(N)

from flask import Flask,render_template,request,redirect,session
import mysql.connector
import json

with open('config.json') as f:
    config=json.load(f)

app=Flask(__name__)
app.secret_key="secret_key"
mydb=mysql.connector.connect(
    host=config["DB_HOST"],
    user=config["DB_USER"],
    password=config["DB_PASS"],
    database=config["DB_NAME"]
)

myCursor=mydb.cursor(dictionary=True)
create_query="CREATE TABLE IF NOT EXISTS todo (id INT AUTO_INCREMENT PRIMARY KEY, todo VARCHAR(255), date DATETIME DEFAULT CURRENT_TIMESTAMP);"
myCursor.execute(create_query)
mydb.commit()

@app.route("/")
def first_load():
    search_query="SELECT * FROM todo"
    myCursor.execute(search_query)
    res=myCursor.fetchall()
    return render_template("index.html",res=res)

@app.route("/index.html",methods=['GET','POST'])
def home_page():
    search_query="SELECT * FROM todo"
    myCursor.execute(search_query)
    res=myCursor.fetchall()
    print(res)
    if request.method=='POST':
        todo=request.form['todoEntry']
        insert_query="INSERT INTO todo (todo) VALUES ( %s )"
        myCursor.execute(insert_query,(todo,))
        mydb.commit()
        return redirect("/")
    return render_template("/index.html",res=res)

@app.route("/update/<int:id>")
def update_page(id):
    search_query="SELECT * FROM todo WHERE id = %s"
    update_id=id
    session['update_id']=update_id
    myCursor.execute(search_query,(update_id,))
    res=myCursor.fetchone()
    return render_template("/update.html",res=res)

@app.route("/update",methods=['GET','POST'])
def update():
    update_id=session.get("update_id")
    updatedTodo=request.form['todoUpdate']
    update_query="UPDATE todo SET todo= %s WHERE id= %s"
    values=(updatedTodo,update_id)
    myCursor.execute(update_query,values)
    mydb.commit()
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    delete_query="DELETE FROM todo WHERE id = %s"
    delete_id=id
    myCursor.execute(delete_query,(delete_id,))
    mydb.commit()
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
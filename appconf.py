from flask import Flask,redirect,url_for,request,render_template,flash
from flask_mail import Mail,Message

app=Flask(__name__)
app.secret_key='kk'
mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='mail@example.com'
app.config['MAIL_PASSWORD']='password'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)
@app.route('/')
def home_page():
    return render_template('welcome.html')
@app.route('/order/')
def order_page():
    return render_template('app.html')
@app.route('/success/<user>')
def confirm_order(user):
    return 'Hey '+user+'! Your order has been confirmed and will be delivered in 20 minutes'

@app.route('/app/',methods=['POST'])
def order():
    if request.method=='POST':
        guest=request.form['nm']
        eid=request.form['email']
        amt=request.form['plates']
        add=request.form['address']
        a=int(amt)
        less_four=20*a
        four_plus=0.9*(20*a)
        flash('Your cart: '+str(a)+' plates Maggi.')
        msgcust=Message('Hello',sender='ayush.vibhanshu@gmail.com',recipients=[eid])
        msgshop=Message('Hello',sender='ayush.vibhanshu@gmail.com',recipients=['farzeehai112@gmail.com'])
        msgcust.body='Hello'+guest+' Your order for '+str(a)+' plates of maggi has been confirmed and will be delivered at '+add+' soon.'
        msgshop.body='Hey! We have an order for '+str(a)+' plates of maggi from '+guest+' to be delivered at '+add+'. Quick! We have 20 minutes.'
        mail.send(msgshop)
        mail.send(msgcust)
        return render_template('confirmation.html',name=guest,mail=eid,plates=a,nodis=less_four,disc=four_plus)
if __name__=='__main__':
    app.run(debug=True)

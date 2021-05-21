from flask import Flask, render_template, redirect,url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms import StringField
from wtforms.validators import DataRequired
app = Flask(__name__)
app.config['SECRET_KEY'] = '1c2dccf5bf6e1713421808f0'

@app.route("/", methods=['GET', 'POST'])
def tinhToan():
    form = Nhap()
    if form.validate_on_submit():
        giatri = int(form.decNum.data)
        items = [
        {'dec': giatri, 'bin': bin(giatri), 'hex': hex(giatri)}
        ]
        return render_template('ketqua.html', items=items)
    return render_template('formHome.html',form=form)

@app.route("/ketqua", methods=['GET','POST'])
def ketQua():
    form = Xuat()   
    return render_template('ketqua.html',form=form)

class Xuat(FlaskForm):
    ketQua = StringField(label="")

class Nhap(FlaskForm):
    decNum = StringField(label='Nhập vào số hệ 10: ', validators=[ DataRequired()])
    submit = SubmitField(label='Tính toán')
  
    

if  __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drawings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Drawing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shape = db.Column(db.String(50), nullable=False)
    details = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Drawing(id={self.id}, shape={self.shape}, details={self.details})>"


db.create_all()

@app.route('/')
def index():
    drawings = Drawing.query.all()
    return render_template('index.html', drawings=drawings)

@app.route('/add_drawing', methods=['POST'])
def add_drawing():
    shape = request.form['shape']
    details = request.form['details']

    new_drawing = Drawing(shape=shape, details=details)
    db.session.add(new_drawing)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

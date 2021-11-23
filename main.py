from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask("__name__")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:hejsan123@localhost/demo'
db = SQLAlchemy(app)


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namn = db.Column(db.String(80), unique=False, nullable=False)
    city = db.Column(db.String(80), unique=False, nullable=False)
    players = db.relationship('Player', backref='team', lazy=True)

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namn = db.Column(db.String(80), unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    jersey = db.Column(db.Integer, unique=False, nullable=False)
    team_id=db.Column(db.Integer, db.ForeignKey('team.id'),
        nullable=False)
    


db.create_all()


while True:
    print("10. Skapa team")
    print("11. Lista teams")
    print("12. Uppdatera ngt på teams")

    print("1. Skapa player")
    print("2. Lista players")
    print("3. Uppdatera player")
    print("4. Sök player")
    sel = input("Val:")

    if sel == "10":
        b = Team()
        b.namn = input("Ange namn:")
        b.city = input("Ange city:")
        db.session.add(b)
        db.session.commit()
    
    if sel == "11":
        for m in Team.query.all():
            print(f"{m.id} {m.namn} {m.city}")
            for p in m.players:
                print(f"    {p.id} {p.namn}")

    if sel == "12":
        for m in Team.query.all():
            print(f"{m.id} {m.namn} {m.city}")
        sel = int(input("Vilket teamid vill du uppdatera?"))
        b = Team.query.filter_by(id=sel).first()
        b.namn = input("Ange nytt namn:")
        b.city = input("Ange nytt city:")
        db.session.commit()


    if sel == "1":
        b = Player()
        b.namn = input("Ange namn:")
        b.jersey = int(input("Ange jersey:"))
        b.year = int(input("Ange birthyear:"))
        for m in Team.query.all():
            print(f"{m.id} {m.namn} {m.city}")
        sel = int(input("Vilket teamid hör denna till"))
        b.team_id = sel
        db.session.add(b)
        db.session.commit()
    if sel == "2":
        for m in Bil.query.all():
            print(m.namn)
    if sel == "3":
        for m in Bil.query.all():
            print(f"{m.id} {m.namn}")
        sel = int(input("Vilken vill du uppdatera:"))
        b = Bil.query.filter_by(id=sel).first()
        b.namn = input("Ange nytt namn:")
        db.session.commit()
    if sel == "4":
        search = input("Sök efter")
        print("Sökresultat")
        for m in Bil.query.filter(Bil.namn.contains(search)).all():
            print(f"{m.id} {m.namn}")
        print("Slut sök")






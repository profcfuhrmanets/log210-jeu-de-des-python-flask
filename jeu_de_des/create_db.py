# create_db.py


from jeu_de_des.app import db

# create the database and the db table
db.create_all()

# commit the changes
db.session.commit()

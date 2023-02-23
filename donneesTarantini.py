from ..app import app, db

class Post(db.Model):
    __tablename__ = "Post"
    post_id = db.Column(db.Integer, primary_key = True)
    post_titre = db.Column(db.String(45))
    post_message = db.Column(db.Text)
    post_date = db.Column(db.DateTime)
    post_indexation = db.Column(db.String(45))
    html = db.Column(db.Text)
    post_auteur = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.name)
    
    followers = db.relationship(
        'comment',
        backref='comments',
        lazy=True
    )

class Comment(db.Model):
    __tablename__ = "Comment"
    id = db.Column(db.Integer, primary_key = True)
    comment_message = db.Column(db.Text)
    comment_html = db.Column(db.Text)
    comment_date = db.Column(db.DateTime)
    comment_post = db.Column(db.Integer,db.ForeignKey('post.post_id'))
    comment_auteur = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Comment %r>' % (self.name)


class CV(db.Model):
    __tablename__ = "CV"
    cv_id = db.Column(db.Integer, primary_key = True)
    cv_nom = db.Column(db.Text)
    cv_nom_employeur = db.Column(db.Text)
    cv_ville = db.Column(db.String)
    cv_annee_debut = db.Column(db.Integer)
    cv_annee_fin = db.Column(db.Integer)
    cv_description_poste = db.Column(db.Text)
    cv_utilisateur = db.Column(db.Integer, db.Foreignkey('user.id'))

    def __repr__(self):
        return '<CV %r>' % (self.name)

class Competences(db.Model):
    __tablename__ = "Competences"
    competences_id = db.Column(db.Integer)
    competences_label = db.Column(db.String)

    def __repr__(self):
        return '<Compétences %r>' % (self.name)
    
Skills = db.relationship(
        'Skills',
        backref='Skillss',
        lazy=True
    )   

class User(db.Model):
    __tablename__= "user"
    user_id= db.Column(db.integer, primary_key=True),
    user_name= db.Column(db.String(45))
    user_firstname= db.Column(db.String(45))
    user_surname= db.Column(db.String(45))
    user_mail= db.Column(db.Text)
    user_password_hash= db.Column(db.Text)
    user_birthyear= db.Column(db.Integer)
    user_promotion_date= db.Column(db.String(45))
    user_description= db.Column(db.Text)
    user_last_seen= db.Column(db.Datetime)
    user_linkedin= db.Column(db.Text)
    user_github= db.Column(db.Text)
    user_inscription_date= db.Column(db.Datetime)

    def __repr__(self):
        return '<User %r>' % (self.name)
    
Skills = db.relationship(
        'Skills',
        backref='Skillss',
        lazy=True
    )   
    

CV = db.relationship(
        'CV',
        backref='CVs',
        lazy=True
    )
    
message = db.relationship(
        'message',
        backref='messages',
        lazy=True
    )
    
    #Class user = relation many-to-many
    
followers = db.relationship(
        'follower',
        backref='followers',
        lazy=True
    )

posts = db.relationship(
        'follower',
        backref='posts',
        lazy=True
    )

comment = db.relationship(
        'comment',
        backref='comments',
        lazy=True
)

class Message(db.Model):
    __tablename__= "message"
    message_id= db.Column(db.Integer,primary_key=True)
    message_message= db.Column(db.Text)
    message_html= db.Column(db.Text)
    message_date= db.Column(db.Datetime)
    message_expediteur_id= db.Column(db.Integer, db.Foreignkey('user.id'),primary_key=True)
    message_destinataire_id= db.Column(db.Integer,db.Foreignkey('user.id'),primary_key=True)

    def __repr__(self):
        return '<Message %r>' % (self.name)

class Followers(db.Model):
    __tablename__= "followers"
    follower_id= db.Column(db.Integer,db.ForeignKey('user.id'),primary_key=True)
    followed_id= db.Column(db.Integer,db.ForeignKey('user.id'),primary_key=True)

    def __repr__(self):
        return '<Followers %r>' % (self.name)


class Skills(db.Model):
    __tablename__= "skills"
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'),primary_key=True)
    competence_id= db.Column(db.Integer, db.ForeignKey('competence.competence_id'),primary_key=True)

    def __repr__(self):
        return '<Skills %r>' % (self.name)
    

from src.db.db_obj import db

class Projects(db.Model):
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String, nullable=False)
    slug = db.Column(db.String, unique=True, nullable=False)
    content = db.Column(db.String,nullable=False)
    category = db.Column(db.String,nullable=False)
    project_url = db.Column(db.String,nullable=False)
    image_url = db.Column(db.String, nullable = False)
   
    def to_dict(self):
        return {
            "id": self.id,
            'category':self.category,
            "title": self.title,
            "slug": self.slug,
            "content": self.content,
            "project_url": self.project_url,
            "image_url": self.image_url
        }
 
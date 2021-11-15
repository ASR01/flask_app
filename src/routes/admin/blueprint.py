from flask import Blueprint,render_template,url_for,redirect,request,session
from src.db.db_obj import db

from src.db.db_models.blog import Blogs
from src.db.db_models.projects import Projects

from slugify import slugify
from os import path

#from src.flask_app import UPLOAD_FOLDER

import uuid

import json

admin_blueprint = Blueprint('admin_blueprint', __name__,template_folder='../../templates')

@admin_blueprint.route("/admin")

def admin_panel_route():

    pr_info = [project.to_dict() for project in Projects.query.all()]

    return render_template("admin.html",pr_info=pr_info,indent=4)



@admin_blueprint.route("/admin/new",methods=["GET","POST"])
def create_blog_route():
    if request.method=="GET":
        ## get article by sluf if its found render
        return render_template("new_pr.html")
    else:

        content = request.form.get("ckeditor")
        title = request.form.get("title")
        category = request.form.get("category")
        cover = request.files["cover"]
        cover.save(path.join(UPLOAD_FOLDER, cover.filename))
        cover_url ="{}files/{}".format(request.host_url,cover.filename)
        new_project = Projects(id=str(uuid.uuid4()),title=title,category=category,cover_url=cover_url,slug=slugify(title),content=content)
        db.session.add(new_project)
        db.session.commit()
        ## get article by sluf if its found render
        return  redirect(url_for("home_blueprint.home_route"))


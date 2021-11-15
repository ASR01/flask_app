from flask import Blueprint,render_template,url_for,redirect,request,session
from slugify import slugify
from src.db.db_obj import db
#import src.utils.functions as func
from src.db.db_models.blog import Blogs
from src.db.db_models.projects import Projects

import uuid
import json

#Define this blueprint
home_blueprint = Blueprint('home_blueprint', __name__,template_folder='../../templates')


@home_blueprint.route('/')
def home():

    #q = request.args.get("q")
    #query = 'SELECT DISTINCT category FROM Projects;'
    #cursor = db.engine.execute(query)
    pr_info = [project.to_dict() for project in Projects.query.all()]

    # if q:
    #     blogs =  [blog.to_dict() for blog in Blogs.query.filter(Blogs.category.contains(q) | Blogs.title.contains(q) | Blogs.content.contains(q))]
    #     if(len(blogs)==1):
    #         return redirect(url_for("home_blueprint.blog_details_route",slug=blogs[0]["slug"]))
    
    return render_template("home.html",pr_info=pr_info,indent=4)




@home_blueprint.route('/<string:slug>')
def blog_details(slug):
    # get article by slug
    
    return render_template('home.html', slug = slug)


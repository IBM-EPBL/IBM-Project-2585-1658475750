from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
from flask import Flask, redirect, url_for
from werkzeug.utils import secure_filename
import json
from .models import User
from flask.helpers import flash

views = Blueprint('views', __name__)

@views.route('/index', methods=['GET', 'POST'])
def index():
    
    return render_template('index.html', user=current_user)
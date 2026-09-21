# encoding: utf-8

import os

from flask import render_template, request, redirect
import ckan.plugins.toolkit as toolkit
import ckan.lib.helpers as h
import ckan.model as model
import ckan.logic as logic
from ckan.exceptions import CkanConfigurationException



class FeatureImageFunctions():
    @staticmethod
    def get_upload_dir():
        storage_path = toolkit.config.get('ckan.storage_path')
        if not storage_path:
            raise CkanConfigurationException(
                'ckan.storage_path must be configured to use feature_image'
            )
        return os.path.join(storage_path, 'storage', 'uploads', 'admin')

    def config():
        context = {'model': model,
                   'user': toolkit.g.user, 'auth_user_obj': toolkit.g.userobj}
        try:
            logic.check_access('sysadmin', context, {})
        except logic.NotAuthorized:
            toolkit.abort(403, 'Need to be system administrator to administer')
            
        return render_template('config.html')
    

    def save_config():
        context = {'model': model,
                   'user': toolkit.g.user, 'auth_user_obj': toolkit.g.userobj}
        try:
            logic.check_access('sysadmin', context, {})
        except logic.NotAuthorized:
            toolkit.abort(403, 'Need to be system administrator to administer')
        
        image_text = request.form.get('feature_image_text')
        image = request.files.get('image')
        upload_dir = FeatureImageFunctions.get_upload_dir()
        image_store_url = os.path.join(upload_dir, 'feature_image')
        if image:
            image.save(image_store_url)
        
        text_url = os.path.join(upload_dir, 'feature_text.txt')
        with open(text_url, 'w+') as text:
            text.write(image_text)
            

        return redirect(h.url_for('home.index', _external=True))
    
    
    def get_text():
        text_url = os.path.join(
            FeatureImageFunctions.get_upload_dir(), 'feature_text.txt'
        )
        with open(text_url, 'r') as text:
            return text.read()

# encoding: utf-8

from flask import render_template, request, redirect
import ckan.plugins.toolkit as toolkit
import ckan.lib.helpers as h
import ckan.model as model
import ckan.logic as logic



class FeatureImageFunctions():
    UPLOAD_DIR = toolkit.config['ckan.storage_path'] + '/storage/uploads/admin/'

    def config():
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
        image_store_url =  FeatureImageFunctions.UPLOAD_DIR + 'feature_image'              
        if image:
            image.save(image_store_url)
        
        text_url = FeatureImageFunctions.UPLOAD_DIR + 'feature_text.txt'
        with open(text_url, 'w+') as text:
            text.write(image_text)
            

        return redirect(h.url_for('home.index', _external=True))
    
    
    def get_text():
        text_url = FeatureImageFunctions.UPLOAD_DIR + 'feature_text.txt'
        with open(text_url, 'r') as text:
            return text.read()
        
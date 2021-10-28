import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from flask import Blueprint
from ckanext.feature_image.lib import FeatureImageFunctions


class FeatureImagePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('public/statics', 'ckanext-feature-image')
    
    def get_blueprint(self):

        blueprint = Blueprint(self.name, self.__module__)        
        blueprint.add_url_rule(
            u'/feature_image/config',
            u'config',
            FeatureImageFunctions.config,
            methods=['GET']
            )   
        
        blueprint.add_url_rule(
            u'/feature_image/save_config',
            u'save_config',
            FeatureImageFunctions.save_config,
            methods=['POST']
            )    

        blueprint.add_url_rule(
            u'/feature_image/get_text',
            u'get_text',
            FeatureImageFunctions.get_text,
            methods=['GET']
            )  

        return blueprint 

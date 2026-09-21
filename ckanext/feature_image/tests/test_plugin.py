"""
Tests for plugin.py.

Tests are written using the pytest library (https://docs.pytest.org), and you
should read the testing guidelines in the CKAN docs:
https://docs.ckan.org/en/2.9/contributing/testing.html

To write tests for your extension you should install the pytest-ckan package:

    pip install pytest-ckan

This will allow you to use CKAN specific fixtures on your tests.

For instance, if your test involves database access you can use `clean_db` to
reset the database:

    import pytest

    from ckan.tests import factories

    @pytest.mark.usefixtures("clean_db")
    def test_some_action():

        dataset = factories.Dataset()

        # ...

For functional tests that involve requests to the application, you can use the
`app` fixture:

    from ckan.plugins import toolkit

    def test_some_endpoint(app):

        url = toolkit.url_for('myblueprint.some_endpoint')

        response = app.get(url)

        assert response.status_code == 200


To temporary patch the CKAN configuration for the duration of a test you can use:

    import pytest

    @pytest.mark.ckan_config("ckanext.myext.some_key", "some_value")
    def test_some_action():
        pass
"""
import os

import pytest
from ckan.exceptions import CkanConfigurationException
from ckan.plugins import toolkit

import ckanext.feature_image.plugin as plugin
from ckanext.feature_image.lib import FeatureImageFunctions

def test_plugin():
    pass


def test_upload_dir_uses_configured_storage_path(monkeypatch, tmp_path):
    monkeypatch.setitem(toolkit.config, "ckan.storage_path", str(tmp_path))

    assert FeatureImageFunctions.get_upload_dir() == os.path.join(
        str(tmp_path), "storage", "uploads", "admin"
    )


def test_upload_dir_reports_missing_storage_path(monkeypatch):
    monkeypatch.delitem(toolkit.config, "ckan.storage_path", raising=False)

    with pytest.raises(CkanConfigurationException, match="ckan.storage_path"):
        FeatureImageFunctions.get_upload_dir()

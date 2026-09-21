import logging
from pathlib import Path

import pytest


WEBASSETS_FILE = (
    Path(__file__).parents[1] / "public" / "statics" / "webassets.yml"
)


def test_webassets_do_not_reference_obsolete_jquery_ui_bundle():
    assert "vendor/jquery.ui.core" not in WEBASSETS_FILE.read_text()


@pytest.mark.ckan_config("ckan.plugins", "feature_image")
@pytest.mark.ckan_config("SECRET_KEY", "test_secret")
@pytest.mark.usefixtures("with_plugins")
def test_javascript_bundles_include_without_unknown_assets(app, caplog):
    from ckan.lib.webassets_tools import include_asset

    caplog.set_level(logging.ERROR, logger="ckan.lib.webassets_tools")

    with app.flask_app.test_request_context("/"):
        include_asset("ckanext-feature-image/config-js")
        include_asset("ckanext-feature-image/promoted-js")

    assert "Trying to include unknown asset" not in caplog.text


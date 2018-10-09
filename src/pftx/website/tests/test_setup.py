# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from pftx.website.testing import PFTX_WEBSITE_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that pftx.website is properly installed."""

    layer = PFTX_WEBSITE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if pftx.website is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'pftx.website'))

    def test_browserlayer(self):
        """Test that IPftxWebsiteLayer is registered."""
        from pftx.website.interfaces import (
            IPftxWebsiteLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IPftxWebsiteLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PFTX_WEBSITE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['pftx.website'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if pftx.website is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'pftx.website'))

    def test_browserlayer_removed(self):
        """Test that IPftxWebsiteLayer is removed."""
        from pftx.website.interfaces import \
            IPftxWebsiteLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IPftxWebsiteLayer,
            utils.registered_layers())

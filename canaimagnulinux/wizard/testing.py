# -*- coding: utf-8 -*-

from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2


class Fixture(PloneSandboxLayer):

    """
    This layer is the Test class base.

    Check out all tests on this package:

    ./bin/test -s canaimagnulinux.wizard --list-tests
    """

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML

        import canaimagnulinux.wizard
        self.loadZCML(package=canaimagnulinux.wizard)

        # import Products.my
        # self.loadZCML(package=Products.my)
        # z2.installProduct(app, 'Products.my')  # initialize

        # Install products that use an old-style initialize() function
        z2.installProduct(app, 'canaimagnulinux.wizard')

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup

        # set the default workflow
        workflow_tool = portal['portal_workflow']
        workflow_tool.setDefaultChain('simple_publication_workflow')
        # install the policy package
        self.applyProfile(portal, 'canaimagnulinux.wizard:default')

    def tearDownZope(self, app):
        # Uninstall products installed above
        z2.uninstallProduct(app, 'canaimagnulinux.wizard')

FIXTURE = Fixture()

"""
We use this base for all the tests in this package. If necessary,
we can put common utility or setup code in here. This applies to unit
test cases.
"""
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name='canaimagnulinux.wizard:Integration'
)

"""
We use this for functional integration tests. Again, we can put basic
common utility or setup code in here.
"""
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,),
    name='canaimagnulinux.wizard:Functional'
)

"""
We use this for functional integration tests with robot framework. Again,
we can put basic common utility or setup code in here.
"""
ROBOT_TESTING = FunctionalTesting(
    bases=(FIXTURE, AUTOLOGIN_LIBRARY_FIXTURE, z2.ZSERVER_FIXTURE),
    name='canaimagnulinux.wizard:Robot',
)

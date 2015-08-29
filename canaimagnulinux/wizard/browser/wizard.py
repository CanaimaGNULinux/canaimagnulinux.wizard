# -*- coding: utf-8 -*-

from canaimagnulinux.wizard.browser.personaldata import PersonalDataStep
from canaimagnulinux.wizard.browser.socialnetwork import SocialNetworkStep
from canaimagnulinux.wizard.utils import CanaimaGnuLinuxWizardMF as _
from collective.beaker.interfaces import ISession
from collective.z3cform.wizard import wizard

from plone import api
from plone.z3cform.layout import FormWrapper

try:
    from zope.browserpage import viewpagetemplatefile
except ImportError:
    # Plone < 4.1
    from zope.app.pagetemplate import viewpagetemplatefile

'''
- Intro step
- Address step
- Social Network step
- Outro step
'''


class IntroStep(wizard.Step):
    prefix = 'intro'
    fields = {}
    label = _(u'Introduction')
    index = viewpagetemplatefile.ViewPageTemplateFile('templates/intro.pt')

    def __init__(self, context, request, wizard):
        # Use collective.beaker for session managment
        session = ISession(request, None)
        self.sessionmanager = session

        super(IntroStep, self).__init__(context, request, wizard)


class OutroStep(wizard.Step):
    prefix = 'outro'
    fields = {}
    label = _(u'Thanks!')
    index = viewpagetemplatefile.ViewPageTemplateFile('templates/outro.pt')

    def __init__(self, context, request, wizard):
        # Use collective.beaker for session managment
        session = ISession(request, None)
        self.sessionmanager = session

        super(OutroStep, self).__init__(context, request, wizard)

    def get_url(self):

        url = self.wizard.get_finish_url()
        return url


class Wizard(wizard.Wizard):
    label = _(u'Start')
    validate_back = False

    def update(self):
        # Use collective.beaker for session managment
        session = ISession(self.request, None)
        self.sessionmanager = session

        super(Wizard, self).update()

    @property
    def steps(self):
        steps = [IntroStep, PersonalDataStep, SocialNetworkStep, OutroStep]
        return steps

    def applySteps(self, pfg, initial_finish=True):
        """ Run the apply method for each step in the wizard """
        for step in self.activeSteps:
            if hasattr(step, 'apply'):
                step.apply(pfg, initial_finish=initial_finish)

    def showClear(self):
        return False

    def get_finish_url(self):
        return api.portal.get().absolute_url()

    def finish(self):
        super(Wizard, self).finish()
        url = self.get_finish_url()
        return self.request.response.redirect(url)


class WizardView(FormWrapper):
    form = Wizard

    def __init__(self, context, request):
        FormWrapper.__init__(self, context, request)
        request.set('disable_border', 1)

    def absolute_url(self):
        return '%s/%s' % (self.context.absolute_url(), self.__name__)

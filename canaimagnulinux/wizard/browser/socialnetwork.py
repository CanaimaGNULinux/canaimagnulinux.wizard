# -*- coding: utf-8 -*-

from canaimagnulinux.wizard.interfaces import IChat
from canaimagnulinux.wizard.interfaces import ISocialNetwork
from canaimagnulinux.wizard.utils import CanaimaGnuLinuxWizardMF as _
from collective.beaker.interfaces import ISession
from collective.z3cform.wizard import wizard

from plone import api
from plone.z3cform.fieldsets import group

from z3c.form import field

try:
    from zope.browserpage import viewpagetemplatefile
except ImportError:
    # Plone < 4.1
    from zope.app.pagetemplate import viewpagetemplatefile

import logging
logger = logging.getLogger(__name__)


class ChatGroup(group.Group):
    prefix = 'chats'
    label = _(u'Chats Information')
    fields = field.Fields(IChat)


class SocialNetworkGroup(group.Group):
    prefix = 'socialnetwork'
    label = _(u'Social Network Information')
    fields = field.Fields(ISocialNetwork)


class SocialNetworkStep(wizard.GroupStep):
    prefix = 'Social'
    label = _(u'Social Network accounts')
    description = _(u'Input your social networks details')

    template = viewpagetemplatefile.ViewPageTemplateFile('templates/socialnetwork.pt')
    fields = field.Fields()
    groups = [ChatGroup, SocialNetworkGroup]

    def __init__(self, context, request, wizard):
        # Use collective.beaker for session managment
        session = ISession(request, None)
        self.sessionmanager = session

        super(SocialNetworkStep, self).__init__(context, request, wizard)

    def load(self, context):
        member = api.user.get_current()
        data = self.getContent()

        # Chats group
        if not data.get('irc', None):
            irc = member.getProperty('irc')
            if type(irc).__name__ == 'object':
                irc = None
            data['irc'] = irc

        if not data.get('telegram', None):
            telegram = member.getProperty('telegram')
            if type(telegram).__name__ == 'object':
                telegram = None
            data['telegram'] = telegram

        if not data.get('skype', None):
            skype = member.getProperty('skype')
            if type(skype).__name__ == 'object':
                skype = None
            data['skype'] = skype

        # Social Network group
        if not data.get('twitter', None):
            twitter = member.getProperty('twitter')
            if type(twitter).__name__ == 'object':
                twitter = None
            data['twitter'] = twitter

        if not data.get('instagram', None):
            instagram = member.getProperty('instagram')
            if type(instagram).__name__ == 'object':
                instagram = None
            data['instagram'] = instagram

        if not data.get('facebook', None):
            facebook = member.getProperty('facebook')
            if type(facebook).__name__ == 'object':
                facebook = None
            data['facebook'] = facebook

    def apply(self, context, initial_finish=False):
        data = self.getContent()
        return data

    def applyChanges(self, data):
        member = api.user.get_current()
        member.setMemberProperties(mapping={
            'irc': data['irc'],
            'telegram': data['telegram'],
            'skype': data['skype'],
            'twitter': data['twitter'],
            'instagram': data['instagram'],
            'facebook': data['facebook']}
        )

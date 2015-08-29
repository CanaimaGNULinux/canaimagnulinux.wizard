# -*- coding: utf-8 -*-

from canaimagnulinux.wizard.interfaces import IAddress
from canaimagnulinux.wizard.interfaces import IPersonalInfo
from canaimagnulinux.wizard.interfaces import IWork
from canaimagnulinux.wizard.utils import CanaimaGnuLinuxWizardMF as _
from collective.beaker.interfaces import ISession
from collective.z3cform.wizard import wizard

from plone import api
from plone.z3cform.fieldsets import group

from z3c.form import field
# from zope import schema

try:
    from zope.browserpage import viewpagetemplatefile
except ImportError:
    # Plone < 4.1
    from zope.app.pagetemplate import viewpagetemplatefile

import logging
logger = logging.getLogger(__name__)


class PersonalInfoGroup(group.Group):
    prefix = 'personalinfo'
    label = _(u'Personal information')
    # schema = IPersonalInfo
    fields = field.Fields(IPersonalInfo)


class AddressGroup(group.Group):
    prefix = 'address'
    label = _(u'Address Details')
    fields = field.Fields(IAddress)


class WorkGroup(group.Group):
    prefix = 'work'
    label = _(u'Work Details')
    fields = field.Fields(IWork)


class PersonalDataStep(wizard.GroupStep):
    prefix = 'Address'
    label = _(u'Personal data, address and work details')
    description = _(u'Input your personal data address and work details')

    template = viewpagetemplatefile.ViewPageTemplateFile('templates/personaldata.pt')
    fields = field.Fields()
    groups = [PersonalInfoGroup, AddressGroup, WorkGroup]

    def __init__(self, context, request, wizard):
        # Use collective.beaker for session managment
        session = ISession(request, None)
        self.sessionmanager = session

        super(PersonalDataStep, self).__init__(context, request, wizard)

    def load(self, context):
        member = api.user.get_current()
        data = self.getContent()

        # Personal info group
        if not data.get('fullname', None):
            fullname = member.getProperty('fullname')
            if type(fullname).__name__ == 'object':
                fullname = None
            data['fullname'] = fullname

        if not data.get('gender', None):
            gender = member.getProperty('gender')
            if type(gender).__name__ == 'object':
                gender = None
            data['gender'] = gender

        if not data.get('birthdate', None):
            birthdate = member.getProperty('birthdate')
            if type(birthdate).__name__ == 'object':
                birthdate = None
            data['birthdate'] = birthdate

        if not data.get('mobile', None):
            mobile = member.getProperty('mobile')
            if type(mobile).__name__ == 'object':
                mobile = None
            data['mobile'] = mobile

        # Address group
        if not data.get('address1', None):
            address1 = member.getProperty('address1')
            if type(address1).__name__ == 'object':
                address1 = None
            data['address1'] = address1

        if not data.get('address2', None):
            address2 = member.getProperty('address2')
            if type(address2).__name__ == 'object':
                address2 = None
            data['address2'] = address2

        if not data.get('country', None):
            country = member.getProperty('country')
            if type(country).__name__ == 'object':
                country = None
            data['country'] = country

        if not data.get('city', None):
            city = member.getProperty('city')
            if type(city).__name__ == 'object':
                city = None
            data['city'] = city

        # Office group
        if not data.get('institution', None):
            institution = member.getProperty('institution')
            if type(institution).__name__ == 'object':
                institution = None
            data['institution'] = institution

        if not data.get('instadd', None):
            instadd = member.getProperty('instadd')
            if type(instadd).__name__ == 'object':
                instadd = None
            data['instadd'] = instadd

        if not data.get('officephone', None):
            officephone = member.getProperty('officephone')
            if type(officephone).__name__ == 'object':
                officephone = None
            data['officephone'] = officephone

        if not data.get('profession', None):
            profession = member.getProperty('profession')
            if type(profession).__name__ == 'object':
                profession = None
            data['profession'] = profession

    def apply(self, context, initial_finish=False):
        data = self.getContent()
        return data

    def applyChanges(self, data):
        member = api.user.get_current()
        member.setMemberProperties(mapping={
            'fullname': data['fullname'],
            'gender': data['gender'],
            'birthdate': data['birthdate'],
            'mobile': data['mobile'],
            'address1': data['address1'],
            'address2': data['address2'],
            'country': data['country'],
            'city': data['city'],
            'institution': data['institution'],
            'instadd': data['instadd'],
            'officephone': data['officephone'],
            'profession': data['profession']}
        )

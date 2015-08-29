# -*- coding: utf-8 -*-

from canaimagnulinux.wizard.utils import CanaimaGnuLinuxWizardMF as _
from zope import schema
from zope.interface import Interface
# import datetime


class IPersonalInfo(Interface):

    fullname = schema.TextLine(
        title=_(u'Name'),
        required=False,
    )

    gender = schema.TextLine(
        title=_(u'Gender'),
        required=True
    )

    # gender = schema.Choice(
    #     title=_(u'Gender'),
    #     values=(u'Male', u'Female'),
    #     default=u'Male / Female?',
    #     default=u'Female',
    #     required=True
    # )

    birthdate = schema.TextLine(
        title=_(u'Birthdate'),
        required=False
    )

    # birthdate = schema.Date(
    #     title=_(u'Birthdate'),
    #     default=datetime.date(2007, 4, 1),
    #     required=False
    # )

    mobile = schema.TextLine(
        title=_(u'Mobile'),
        required=False
    )


class IAddress(Interface):

    address1 = schema.TextLine(
        title=_(u'Address 1'),
        required=False
    )

    address2 = schema.TextLine(
        title=_(u'Address 2'),
        required=False
    )

    country = schema.TextLine(
        title=_(u'Country'),
        required=False
    )

    city = schema.TextLine(
        title=_(u'City'),
        required=False
    )


class IWork(Interface):

    institution = schema.TextLine(
        title=_(u'Institution / Organization'),
        required=False
    )

    instadd = schema.TextLine(
        title=_(u'Institution address'),
        required=False
    )

    officephone = schema.TextLine(
        title=_(u'Office phone'),
        required=False
    )

    position = schema.TextLine(
        title=_(u'Current position'),
        required=False
    )

    profession = schema.TextLine(
        title=_(u'Profession'),
        required=False
    )


class IChat(Interface):

    irc = schema.TextLine(
        title=_(u'IRC nickname'),
        required=False
    )

    telegram = schema.TextLine(
        title=_(u'Telegram account'),
        required=False
    )

    skype = schema.TextLine(
        title=_(u'Skype account'),
        required=False
    )


class ISocialNetwork(Interface):

    twitter = schema.TextLine(
        title=_(u'Twitter nickname'),
        required=False
    )

    instagram = schema.TextLine(
        title=_(u'Instagram account'),
        required=False
    )

    facebook = schema.TextLine(
        title=_(u'Facebook account'),
        required=False
    )

from zope.interface import implements
from plone.dexterity.content import Item
from pftx.website.interfaces import ISource
from pftx.website.interfaces import ISuYuan


class Source(Item):
    implements(ISource)


class SuYuan(Item):
    implements(ISuYuan)


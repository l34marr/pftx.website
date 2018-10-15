from zope.interface import implements
from plone.dexterity.content import Item
from pftx.website.interfaces import ISuYuan


class SuYuan(Item):
    implements(ISuYuan)


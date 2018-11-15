# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""
from plone.autoform import directives
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.app.z3cform.widget import AjaxSelectFieldWidget
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.app.vocabularies.catalog import CatalogSource
from zope import schema
from pftx.website import _

from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IPftxWebsiteLayer(IDefaultBrowserLayer):
    """Marker Interface that Defines a Browser Layer."""


class ISuYuan(model.Schema):
    """Traceable Type"""
    title = schema.TextLine(
        title=_(u'Style No + PO No'),
    )
#   stno = schema.TextLine(
#       title=_(u'Style No'),
#   )
#   pono = schema.TextLine(
#       title=_(u'PO No'),
#   )
    garment = schema.Tuple(
        title=_(u'GARMENT'),
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
    )
    directives.widget(
        'garment',
        AjaxSelectFieldWidget,
        vocabulary='plone.app.vocabularies.Users'
    )
    other = schema.Tuple(
        title=_(u'OTHER'),
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
    )
    directives.widget(
        'other',
        AjaxSelectFieldWidget,
        vocabulary='plone.app.vocabularies.Users'
    )
    yinhua = schema.Tuple(
        title=_(u'PRINT'),
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
    )
    directives.widget(
        'yinhua',
        AjaxSelectFieldWidget,
        vocabulary='plone.app.vocabularies.Users'
    )
    dye = schema.Tuple(
        title=_(u'DYE'),
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
    )
    directives.widget(
        'dye',
        AjaxSelectFieldWidget,
        vocabulary='plone.app.vocabularies.Users'
    )
    knit = schema.Tuple(
        title=_(u'KNIT'),
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
    )
    directives.widget(
        'knit',
        AjaxSelectFieldWidget,
        vocabulary='plone.app.vocabularies.Users'
    )
    yarn = RelationList(
        title=_(u'SOURCE'),
        default=[],
        value_type=RelationChoice(
            title=u'SRC',
            source=CatalogSource(Type=['Folder', 'Link'])
        ),
        required=False,
    )
    directives.widget(
        'yarn',
        RelatedItemsFieldWidget,
        vocabulary='plone.app.vocabularies.Catalog',
        pattern_options={
            'recentlyUsed': True,
        }
    )


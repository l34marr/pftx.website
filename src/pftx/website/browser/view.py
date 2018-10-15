from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory


class MyView(BrowserView):

    def t_title(self, vocab, value):
        try:
            factory = getUtility(IVocabularyFactory, vocab)
            vocabulary = factory(self.context)
            term = vocabulary.getTerm(value)
            return term.title
        except:
            return None


class SuYuanView(BrowserView):

    template = ViewPageTemplateFile("suyuan.pt")

    def __call__(self):
        return self.template()

    def mmbr(self, mid):
        membership = getToolByName(self.context, 'portal_membership')
        return membership.getMemberInfo(mid)

    def mmbrname(self, mid):
        mmbr = self.mmbr(mid)
        return mmbr and mmbr['fullname'] or None


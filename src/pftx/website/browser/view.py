from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from cStringIO import StringIO
import qrcode


class MyView(BrowserView):

    def t_title(self, vocab, value):
        try:
            factory = getUtility(IVocabularyFactory, vocab)
            vocabulary = factory(self.context)
            term = vocabulary.getTerm(value)
            return term.title
        except:
            return None


class SourceView(BrowserView):

    template = ViewPageTemplateFile("source.pt")

    def __call__(self):
        return self.template()


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

    def hasValue(self, mid):
        mmbr = self.mmbr(mid)
        return True and (mmbr['home_page'] or mmbr['report'] or mmbr['panorama']) or False


class QRCodeView(BrowserView):

    def __call__(self):
        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_H,
            box_size = 10,
            border = 4,
        )

        url = self.context.absolute_url()

        qr.add_data(url)
        qr.make(fit=True)

        # Create an Image from the QR Code Instance
        img = qr.make_image()

        # Save it Somewhere, Change the Extension as Needed:
        img.save("image.png")
        output = StringIO()
        img.save(output)
        self.request.response.setHeader('Content-Type', 'image/png')
        return output.getvalue()


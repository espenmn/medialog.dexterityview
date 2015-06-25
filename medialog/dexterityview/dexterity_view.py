from zope.interface import implements, Interface, Attribute
from Products.Five import BrowserView
from plone.dexterity.utils import iterSchemata
from zope.schema import getFields
from plone.dexterity.interfaces import IDexterityContent
from plone.dexterity.browser.view import DefaultView

 
class IDexterityView(Interface):
    """
    view interface
    """

    def  block_fields():
        """ Returns fields to block"""

    def  render_fields():
        """ Returns fields to render"""

class DexterityView(DefaultView, BrowserView):
    """
    Customizable browser view
    """
    @property
    def block_fields(self):
        return self.request.get('block_fields', ('IBasic.title', 'IBasic.description', 'title', 'description'))
    
    @property
    def render_fields(self):
        return  self.request.get('render_fields', '')
    
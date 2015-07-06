from zope import schema
from zope.interface import Interface
from z3c.form import interfaces
from z3c.form.interfaces import IFileWidget
from zope.interface import alsoProvides
from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider
from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider

from plone.formwidget.namedfile.widget import INamedImageWidget, NamedImageWidget

from collective.z3cform.datagridfield import DataGridFieldFactory 
from collective.z3cform.datagridfield.registry import DictRow


from plone.formwidget.namedfile.widget import NamedImageWidget


from zope.i18nmessageid import MessageFactory

_ = MessageFactory('medialog.dexterityview')


class IDexterityViewLayer(Interface):
    """A layer specific to medialog.dexterityview
        """




class DexterityNamedImageWidget(NamedImageWidget):
    """A widget for a named image field that can be set to scales
    """
                
    @property
    def image_scale(self):
        return  'preview'




class IContentPair(form.Schema):
    content_type = schema.ASCIILine(
        title=_(u'content_type', 'Content type'), 
        required=False
    )
    
    block_fields = schema.ASCIILine(
        title=_(u'block_fields', 'Fields to block'),
        required=False
    )


class IDexterityViewSettings(form.Schema):
    """Adds settings to medialog.controlpanel
        """
    form.fieldset(
        'dexterity_view',
        label=_(u'Sexterity View'),
            fields=[
                    'content_pairs',
            ],
    )
    
    form.widget(content_pairs=DataGridFieldFactory)
    content_pairs = schema.List(
        title = _(u"content_pairs", 
            default=u"Content type and fields blocked"),
        value_type=DictRow(schema=IContentPair),
    )
                
alsoProvides(IDexterityViewSettings, IMedialogControlpanelSettingsProvider)



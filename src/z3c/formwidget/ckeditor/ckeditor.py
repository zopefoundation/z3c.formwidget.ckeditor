##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""CKEditor Widget implementation
"""
import simplejson as json
import zope.component
import zope.interface
import zope.schema.interfaces
from z3c.form.browser import textarea
from z3c.form.interfaces import IFieldWidget
from z3c.form.interfaces import IFormLayer
from z3c.form.widget import FieldWidget
from zope.viewlet.viewlet import JavaScriptViewlet

from z3c.formwidget.ckeditor import interfaces


@zope.interface.implementer_only(interfaces.ICKEditorWidget)
class CKEditorWidget(textarea.TextAreaWidget):

    klass = 'CKEditorWidget'
    config = None

    def update(self):
        super().update()
        if self.config is None:
            self.configString = '{}'
        elif isinstance(self.config, str):
            self.configString = str(self.config)
        elif isinstance(self.config, dict):
            self.configString = json.dumps(self.config)
        else:
            raise ValueError('Invalid config object', self.config)


@zope.component.adapter(interfaces.IRichText, IFormLayer)
@zope.interface.implementer(IFieldWidget)
def CKEditorFieldWidget(field, request):
    """IFieldWidget factory for CKEditorWidget."""
    return FieldWidget(field, CKEditorWidget(request))


def CKEditorFieldWidgetFactory(config=None):
    """Create a CKEditorFieldWidget from a given config."""

    @zope.component.adapter(interfaces.IRichText, IFormLayer)
    @zope.interface.implementer(IFieldWidget)
    def CKEditorFieldWidget(field, request):
        widget = CKEditorWidget(request)
        widget.config = config
        return FieldWidget(field, widget)

    return CKEditorFieldWidget


CKEditorJSViewlet = JavaScriptViewlet('ckeditor/ckeditor.js')

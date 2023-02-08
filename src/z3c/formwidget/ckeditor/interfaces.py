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
"""CKEditor Widget interfaces
"""
import zope.schema
import zope.schema.interfaces
from z3c.form.interfaces import ITextAreaWidget
from zope.viewlet.interfaces import IViewletManager


class IJavaScript(IViewletManager):
    """JavaScript viewlet manager."""


class IRichText(zope.schema.interfaces.IText):
    """A text field that contains rich-text markup in HTML."""


class ICKEditorWidget(ITextAreaWidget):
    """CKEditor widget."""

    config = zope.schema.Field(
        title='Configuration',
        description=(
            'CKEditor Configuration. `None` refers to no configuration, a '
            'string represents a variable name to a config object, and a '
            'dictionary an actual configuration object that is encoded using '
            'JSON. All other object types will cause a `ValueError`.'),
        default=None,
        required=False)

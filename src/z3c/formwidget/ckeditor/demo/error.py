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
"""Error Reporting.
"""
import transaction
from zope.app.appsetup.bootstrap import ensureUtility
from zope.app.appsetup.bootstrap import getInformationFromEvent
from zope.error.error import RootErrorReportingUtility
from zope.error.interfaces import IErrorReportingUtility


def errorSubscriber(event):
    """Subscriber to the IDataBaseOpenedEvent

    Create utility at that time if not yet present
    """

    db, connection, root, root_folder = getInformationFromEvent(event)

    ensureUtility(root_folder, IErrorReportingUtility, '',
                  RootErrorReportingUtility, copy_to_zlog=True,
                  _ignored_exceptions=('Unauthorized',))

    transaction.commit()
    connection.close()


globalErrorReportingUtility = RootErrorReportingUtility()
globalErrorReportingUtility.setProperties(20, True, ())

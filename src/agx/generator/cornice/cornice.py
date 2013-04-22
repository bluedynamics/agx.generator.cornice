# -*- coding: utf-8 -*-
from zope.interface import implements
import agx.generator.cornice
from agx.core.interfaces import IProfileLocation

class cornice(object):

    implements(IProfileLocation)
    name = 'cornice.profile.uml'
    package = agx.generator.cornice
# -*- coding: utf-8 -*-
from agx.test.cornice.myrestservice import MyRestService

def register():
    """register this generator
    """
    import agx.test.cornice
    from agx.core.config import register_generator
    register_generator(agx.test.cornice)
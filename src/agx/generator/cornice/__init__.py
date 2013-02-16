# -*- coding: utf-8 -*-
def register():
    """register this generator
    """
    import agx.generator.cornice
    from agx.core.config import register_generator
    register_generator(agx.generator.cornice)
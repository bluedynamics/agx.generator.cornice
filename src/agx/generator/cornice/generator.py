# -*- coding: utf-8 -*-
from agx.generator.pyegg.utils import (
    class_base_name,
    implicit_dotted_path,
)
from agx.core.util import (
    read_target_node,
    dotted_path,
)
from agx.core.interfaces import IScope
from agx.core import (
    handler,
    Scope,
    registerScope,
    token,
)
from node.ext.uml.interfaces import (
    IOperation,
    IClass,
    IPackage,
    IInterface,
    IInterfaceRealization,
    IDependency,
    IProperty,
    IAssociation,
)

@handler('create_service', 'uml2fs', 'connectorgenerator', 'cornice_service')
def create_service(self, source, target):
    print 'this is a cornice service:', source.name

@handler('handle_getter', 'uml2fs', 'connectorgenerator', 'getterscope')
def handle_getter(self, source, target):
    print 'this is a cornice getter:', source.name

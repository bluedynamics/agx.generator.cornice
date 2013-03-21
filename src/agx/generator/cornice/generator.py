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

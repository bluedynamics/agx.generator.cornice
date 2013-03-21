# -*- coding: utf-8 -*-
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

class PackagesAndEggsScope(Scope):

    def __call__(self, node):
        return node.stereotype('pyegg:pythonegg') is not None \
            or node.stereotype('pyegg:pymodule') is not None

registerScope('packagesandeggs', 'uml2fs', [IPackage], PackagesAndEggsScope)
registerScope('classesandpackages', 'uml2fs', [IClass,IPackage], Scope)

class cornicescope(Scope):

    def __call__(self, node):
        return 

registerScope('cornicescope', 'uml2fs', None, cornicescope)

class ServiceScope(Scope):

    def __call__(self, node):
        return node.stereotype('cornice:service') is not None

registerScope('cornice_service', 'uml2fs', [IClass], ServiceScope)

class GETScope(Scope):

    def __call__(self, node):
        return node.stereotype('cornice:get') is not None

registerScope('getscope', 'uml2fs', [IOperation], GETScope)
registerScope('putscope', 'uml2fs', None, Scope)

class POSTScope(Scope):

    def __call__(self, node):
        return 

registerScope('postscope', 'uml2fs', None, POSTScope)
registerScope('deletescope', 'uml2fs', None, Scope)
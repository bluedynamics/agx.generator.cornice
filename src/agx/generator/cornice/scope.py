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
        return node.stereotype('pyegg:pythonegg') is not None or node.stereotype('pyegg:pymodule') is not None

registerScope('packagesandeggs', 'uml2fs', [IPackage], PackagesAndEggsScope)
registerScope('classesandpackages', 'uml2fs', [IClass,IPackage], Scope)

class ServiceScope(Scope):

    def __call__(self, node):
        return node.stereotype('cornice:service') is not None

registerScope('cornice_service', 'uml2fs', [IClass], ServiceScope)

class GETScope(Scope):

    def __call__(self, node):
        return node.stereotype('cornice:get') is not None

registerScope('getscope', 'uml2fs', [IOperation], GETScope)

class PUTScope(Scope):

    def __call__(self, node):
        return 

registerScope('putscope', 'uml2fs', None, PUTScope)

class POSTScope(Scope):

    def __call__(self, node):
        return 

registerScope('postscope', 'uml2fs', None, POSTScope)

class DELETEScope(Scope):

    def __call__(self, node):
        return 

registerScope('deletescope', 'uml2fs', None, DELETEScope)

class CorniceMethodScope(Scope):

    def __call__(self, node):
        return node.stereotype('cornice:get') is not None or node.stereotype('cornice:put') is not None or node.stereotype('cornice:delete') is not None or node.stereotype('cornice:post') is not None

registerScope('cornice_method', 'uml2fs', [IOperation], CorniceMethodScope)
# -*- coding: utf-8 -*-
import os
from agx.generator.pyegg.utils import (
    class_base_name,
    implicit_dotted_path,
    egg_source,
)
from agx.core.interfaces import IScope
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
from agx.core.util import (
    read_target_node,
    dotted_path,
    write_source_to_target_mapping,
)

# from agx.core.interfaces import IScope

from agx.core import (
    handler,
    token,
)
from node.ext.python import Decorator
from node.ext.python import Module
from node.ext.python import Attribute
from node.ext.python.utils import Imports
from node.ext.uml.utils import TaggedValues

# from node.ext.python.interfaces import IModule

DEBUG = True

def getservicename(source):
    tgv = TaggedValues(source)
    name = tgv.direct('name','cornice:service', source.name.lower())

    return name

def getservicepath(source):
    tgv = TaggedValues(source)
    name = tgv.direct('name', 'cornice:service', source.name.lower())
    path = tgv.direct('path', 'cornice:service', '/' + name)

    return path

@handler('create_service', 'uml2fs', 'hierarchygenerator', 'cornice_service')
def create_service(self, source, target):
    """create a module 'services.py' to hold the cornice services
    
    create a docstring at the top of the module.
    create an import statement (from cornice import Service).
    create an attribute of the name of the UML::Class
    and set it to a Service(with parameters)
    parameters are name = name of the
    """
    klass = read_target_node(source, target.target)
    module = klass.parent
    
    # create imports for cornice service
    imps = Imports(module)
    imps.set('cornice', 'Service')  # from cornice import Service
    
    #add the dep
    deps=token('setup_dependencies', True, deps=[])
    if not 'cornice' in deps.deps:
        deps.deps.append('cornice')
    
    # prepare for later: get name of the service
    servicename = getservicename(source)
    servicepath = getservicepath(source)
    
    # create an Attribute that will define a cornice service
    serviceattr = Attribute()
    serviceattr.targets = [source.name]  
    serviceattr.value = 'Service(name="%s", path="%s")' % (servicename, servicepath)
    serviceattr.__name__ = serviceattr.uuid
    
    # lets insert it after the class definition
    if not module.attributes(source.name):
        module.insertafter(serviceattr, klass)


@handler('reparent_cornice_functions', 'uml2fs', 'connectorgenerator',
         'cornice_service')
def reparent_cornice_functions(self, source, target):
    print 'reparenting methods of class ', source.name
    klass = read_target_node(source, target.target)
    module = klass.parent
    for func in klass.functions():
        print '    reparenting ', func.functionname
        klass.detach(func.name)
        funcs = module.functions(func.functionname)
        if not funcs:
            module.insertlast(func)
        else:
            # if already here, remap source/target
            oldfunc = funcs[0]
            sourcefunc = source.get(oldfunc.functionname, None)
            if sourcefunc:
                tok = token(str(sourcefunc.uuid), True, target=oldfunc)

def add_decorator(source, target, decname):
    tok = token(str(source.uuid), True, target=None)
    if tok.target:
        func = tok.target
    else:
        func = read_target_node(source, target.target)
        
    dec = Decorator(decname)
    dec.is_callable = True
    if not func.decorators(decname):
        func.insertfirst(dec)

@handler('handle_GET', 'uml2fs', 'connectorgenerator', 'getscope')
def handle_GET(self, source, target):
    servicename = source.parent.name
    decname = servicename + ".get"
    add_decorator(source, target, decname)

@handler('handle_PUT', 'uml2fs', 'connectorgenerator', 'putscope')
def handle_PUT(self, source, target):
    servicename = source.parent.name
    decname = servicename + ".put"
    add_decorator(source, target, decname)

@handler('handle_POST', 'uml2fs', 'connectorgenerator', 'postscope')
def handle_POST(self, source, target):
    servicename = source.parent.name
    decname = servicename + ".post"
    add_decorator(source, target, decname)

@handler('handle_DELETE', 'uml2fs', 'connectorgenerator', 'deletescope')
def handle_DELETE(self, source, target):
    servicename = source.parent.name
    decname = servicename + ".delete"
    add_decorator(source, target, decname)

@handler('purge_cornice_service_class', 'uml2fs', 'semanticsgenerator',
         'cornice_service')
def purge_cornice_service_class(self, source, target):
    klass = read_target_node(source, target.target)
    module = klass.parent
    module.detach(klass.name)

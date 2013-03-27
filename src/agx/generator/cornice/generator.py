# -*- coding: utf-8 -*-
#from agx.generator.pyegg.utils import (
    #class_base_name,
    #implicit_dotted_path,
#)
from agx.core.util import (
    read_target_node,
    #dotted_path,
)
#from agx.core.interfaces import IScope
from agx.core import (
    handler,
    #Scope,
    #registerScope,
    #token,
)
#from node.ext.uml.interfaces import (
    #IOperation,
    #IClass,
    #IPackage,
    #IInterface,
    #IInterfaceRealization,
    #IDependency,
    #IProperty,
    #IAssociation,
#)

#from node.ext.python.interfaces import IModule
DEBUG = True


@handler('create_service', 'uml2fs', 'connectorgenerator', 'cornice_service')
def create_service(self, source, target):
    """create a module 'services.py' to hold the cornice services
    """
    tgt = read_target_node(source, target.target)

    # some pseudo code of what shall be done:
    #
    # - wait for nodeification of the relevant class or module
    # - delete the class from the module
    # - create an Attribute node instead
    #    module[str(uuid.uuid4())] = Attribute(
    #                                    targets='foo',
    #                                    value='Service(params)'
    #
    # TODO: delete the 'original' class ... but how?
    #       the functions are still needed for the other handlers
    #del tgt.parent
    #tgt.clear()

    if DEBUG:  # pragma: no cover
        print "============= handler to create a Cornice Service ======="
        print "handling UML::Class %s" % tgt.classname

    # create (or reuse) a special module for cornice services
    if not 'services.py' in tgt.parent.parent:
        # the file has not been created yet
        if DEBUG:  # pragma: no cover
            print "services.py not found: creating it."
        from node.ext.python import Module
        servicesmodule = Module()
        tgt.parent.parent['services.py'] = servicesmodule
        # add a docstring
        from node.ext.python import Docstring
        docs = Docstring()
        docs.text = u'This module contains cornice services'
        servicesmodule['docstring-1'] = docs
    else:
        # the file already exists
        if DEBUG:  # pragma: no cover
            print "services.py exists. using it."
        servicesmodule = tgt.parent.parent['services.py']

    # create imports for cornice service
    from node.ext.python.utils import Imports
    imps = Imports(servicesmodule)
    imps.set('cornice', 'Service')  # from cornice import Service

    # prepare for later: get name of the service
    servicename = tgt.classname.lower()

    # # create an Attribute that will define a cornice service
    from node.ext.python import Attribute
    serviceattr = Attribute()
    serviceattr.targets = [servicename]  # name of attribute: Classname.lower()
    serviceattr.value = 'Service(name="foo", path="bar")'
    # # TODO: extract 'name' and 'path' from model
    import uuid
    servicesmodule[str(uuid.uuid4())] = serviceattr
    print "============= end handler create_service ================"


@handler('handle_GET', 'uml2fs', 'connectorgenerator', 'getscope')
def handle_GET(self, source, target):
    if DEBUG:  # pragma: no cover
        print "==== handler to create a GET method ===="
    tgt = read_target_node(source, target.target)
    #print tgt.printtree()
    #import pdb; pdb.set_trace()
    funcname = tgt.functionname.lower()

    # a decorator for the function
    from node.ext.python import Decorator
    #dec = Decorator('%s.get()') % funcname  # not works, grrr
    #dec = Decorator('foocorator')  # works! but is undesired :-/
    dec = Decorator(funcname)
    tgt['decorator-1'] = dec
    #insertbefore(dec, tgt)  # TODO: decorator shall be planted on function
    #print "========= end handler ========="


@handler('handle_PUT', 'uml2fs', 'connectorgenerator', 'putscope')
def handle_PUT(self, source, target):
    print "==== handler to create a PUT method ===="
    print "===== end of handler for PUT method ===="


@handler('handle_POST', 'uml2fs', 'connectorgenerator', 'postscope')
def handle_POST(self, source, target):
    print "==== handler to create a POST method ===="
    print "===== end of handler for POST method ===="


@handler('handle_DELETE', 'uml2fs', 'connectorgenerator', 'deletescope')
def handle_DELETE(self, source, target):
    print "==== handler to create a DELETE method ===="
    print "===== end of handler for DELETE method ===="

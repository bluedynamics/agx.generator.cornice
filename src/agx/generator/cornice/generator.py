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
    token,
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


@handler('create_service', 'uml2fs', 'hierarchygenerator', 'cornice_service',
         order=27)
def create_service(self, source, target):
    """create a module 'services.py' to hold the cornice services

    create a docstring at the top of the module.
    create an import statement (from cornice import Service).
    create an attribute of the name of the UML::Class
    and set it to a Service(with parameters)
    parameters are name = name of the
    """

    if DEBUG:  # pragma: no cover
        print "============= handler to create a Cornice Service ======="
        print "handling UML::Class %s" % source.name

    """ create (or reuse) a special module named 'services.py'
    for cornice services"""
    if not 'services.py' in target.anchor.parent:  # i.e. not already in target
        # the file has not been created yet
        if DEBUG:  # pragma: no cover
            print "services.py not found: creating it."
        from node.ext.python import Module
        servicesmodule = Module()  # create a file
        target.anchor.parent['services.py'] = servicesmodule
        if DEBUG:  # pragma: no cover
            print("here is the actual "
                  "servicesmodule.uuid: %s" % servicesmodule.uuid)
            print("and servicesmodule.path: %s" % servicesmodule.path)
        # add a docstring
        from node.ext.python import Docstring
        docs = Docstring()
        docs.text = u'This module contains cornice services'
        servicesmodule['docstring-0'] = docs
    else:
        # the file already exists
        if DEBUG:  # pragma: no cover
            print "services.py exists. using it."
        servicesmodule = target.anchor.parent['services.py']

    # create imports for cornice service
    from node.ext.python.utils import Imports
    imps = Imports(servicesmodule)
    imps.set('cornice', 'Service')  # from cornice import Service

    # prepare for later: get name of the service
    servicename = source.name  # tgt.classname.lower()
    # XXX TODO: the service name should be extracted from the model!
    # there are tagged values 'name' and 'path'
    # as long as they don't have values in the model, use default ones
    #import pdb; pdb.set_trace()

    # # create an Attribute that will define a cornice service
    from node.ext.python import Attribute
    serviceattr = Attribute()
    serviceattr.targets = [servicename]  # name of attribute: Classname.lower()
    serviceattr.value = 'Service(name="foo", path="bar")'
    # # TODO: extract 'name' and 'path' from model

    # service attribute is placed in services.py module
    if not servicesmodule.attributes(source.name):
        servicesmodule['servicename-attr-' + source.name] = serviceattr
#    servicesmodule.insertlineafter(serviceattr, '\n')

    # use a token to 'remember' the file for writing later?:
    # the GET, PUT, POST, DELETE handlers need to know where to attach to
    #from agx.core import token
    tok = token('cornice_service_module', True, the_uuid=servicesmodule.uuid)
    tok.the_path = servicesmodule.path
    print("the uuid: %s") % tok.the_uuid
    print("the path: %s") % tok.the_path

    # we need to store the index of child UML::Operations
    # that have cornice stereotypes on them.
    # to ind them later they have to go into the token
    #
    import node.ext.uml
    number_of_items = len(source.keys())
    print("found %s items in %s") % (number_of_items, source.name)
    for i in range(len(source.keys())):
        print('%s: %s of type %s') % (i,
                                      source.keys()[i],
                                      type(source.values()[i]))
        if isinstance(source.values()[i], node.ext.uml.classes.Operation):
            print("--yes, this is an operation. "
                  "find out if it has a stereotype!")
            #source.values()[i].printtree()
            #print("--source.values()[i]:  %s ") % source.values()[i]
            #print("--source.values()[i].stereotype:('cornice:get')  %s ") % source.values()[i].stereotype('cornice:get')
            if source.values()[i].stereotype('cornice:get'):
                print("--found a <<get>>")
            elif source.values()[i].stereotype('cornice:put'):
                print("--found a <<put>>")
            elif source.values()[i].stereotype('cornice:post'):
                print("--found a <<post>>")
            elif source.values()[i].stereotype('cornice:delete'):
                print("--found a <<delete>>")
            else:
                print("--found no stereotype.")
            #print("  %s ") % source.values()[i]
        #tok.the_operations = ['1', source.child()
    #(Pdb) source.keys().index('get_api_version')
    #2

#    import pdb
#    pdb.set_trace()

    # delete the original class from the tree, or at least mark it,
    # so it will not be generated as python module
    #
    # remove the original module from target:
    # (it was generated because a UML::Class inside a pyegg was found
    # and turned into a Python module of the same name, lowercase)
    # I want all 'services' into one module 'services.py'
    target.anchor.parent.detach(source.name.lower() + '.py')

    # try to end with a newline
    from node.ext.python import Block
    bloc = Block('\n')
    servicesmodule.insertlast(bloc)
    #servicesmodule['newline-1-' + source.name] = bloc
    #servicesmodule.insertlast(Block('''
    #
    # '''))
    # too bad -- trailing newlines are forbidden :-/
    # see devsrc/node.ext.python/src/node/ext/python/parser.py line 231

    if DEBUG:  # pragma: no cover
        print "============= end handler create_service ================"


@handler('handle_GET', 'uml2fs', 'connectorgenerator', 'getscope')
def handle_GET(self, source, target):
    """this handler is called for every stereotype <<get>>

    it should revisit the services.py module and add
    """
    if DEBUG:  # pragma: no cover
        print "==== handler to create a GET method ===="

    tok = token('cornice_service_module', False)
    servicemodules_path_in_target = tok.the_path
    #print("the uuid: %s") % tok.the_uuid
    print("the path: %s") % tok.the_path
    import os
    path = os.sep.join(servicemodules_path_in_target)
    print("the path, usable: %s") % path
    #servicemodule = tok.the_uuid  # does not work. how to get a node by uuid?
    from node.ext.python import Module
    servicemodule = Module(path)
    servicename = 'fooservice'  # tgt.parent.name.lower()
    #
    #import pdb; pdb.set_trace()
    # a decorator for the function
    from node.ext.python import Decorator
    #dec = Decorator('%s.get()') % funcname  # not works, grrr
    #dec = Decorator('foocorator')  # works! but is undesired :-/
    dec = Decorator("get." + servicename + '()')
    servicemodule['decorator-1'] = dec
    print("gave it a decorator: %s") % dec
    #servicemodule['decorator-1'] = dec
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

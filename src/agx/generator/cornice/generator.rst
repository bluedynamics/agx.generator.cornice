Test agx.generator.cornice
==========================

We would like to start with a fresh setup, no generated files. We delete them::

    >>> import os
    >>> import shutil
    >>> 
    >>> #print(os.path.abspath(datadir))
    >>> if os.path.exists(os.path.join(datadir, 'cornice.example')):
    ...     shutil.rmtree(os.path.join(datadir, 'cornice.example'))

Setup configuration and emulate main routine::

    >>> from zope.configuration.xmlconfig import XMLConfig

    >>> import agx.core
    >>> XMLConfig('configure.zcml', agx.core)()

    >>> from agx.core.main import parse_options

    >>> import os

Choose a model to use for testing::

    >>> modelpath = os.path.join(datadir, 'cornice.example.model.uml')

Where is the pyegg profile?
    >>> import pkg_resources
    >>> pyeggsubpath = 'profiles/pyegg.profile.uml'
    >>> eggprofilepath = \
    ...     pkg_resources.resource_filename('agx.generator.pyegg', pyeggsubpath)

Where is the cornice profile?
    >>> profilepath = os.path.join(datadir, '..', '..',
    ...                            'profiles', 'cornice.profile.uml')

Combine the UML model, PyEgg Profile and Cornice Profile

    >>> modelpaths = [modelpath, eggprofilepath, profilepath]

Where should stuff be generated?

    >>> outdir = os.path.join(datadir, 'cornice.example')
    >>> controller = agx.core.Controller()
    >>> target = controller(modelpaths, outdir)
    >>> target
    <Directory object '/.../agx.generator.cornice/src/agx/generator/cornice/testing/data/cornice.example' at ...>

    >>> target.printtree()
    <class 'node.ext.directory.directory.Directory'>: .../cornice.example
      <class 'node.ext.directory.directory.Directory'>: src
        <class 'node.ext.directory.directory.Directory'>: cornice
          <class 'node.ext.directory.directory.Directory'>: example
            <class 'node.ext.directory.directory.Directory'>: services
	    ...

Well, discard the rest, ok?
              <class 'node.ext.python.nodes.Module'>: [1:11] - -1
                <class 'node.ext.python.nodes.Block'>: [?:?] - 0
                <class 'node.ext.python.nodes.Class'>: [2:11] - 0
                  <class 'node.ext.python.nodes.Attribute'>: [4:4] - 1
                  <class 'node.ext.python.nodes.Attribute'>: [5:5] - 1
                  <class 'node.ext.python.nodes.Function'>: [7:8] - 1
                    <class 'node.ext.python.nodes.Block'>: [8:8] - 2
                  <class 'node.ext.python.nodes.Function'>: [10:11] - 1
                    <class 'node.ext.python.nodes.Block'>: [11:11] - 2
              <class 'node.ext.python.nodes.Module'>: [1:3] - -1
                <class 'node.ext.python.nodes.Block'>: [?:?] - 0
                <class 'node.ext.python.nodes.Import'>: [2:2] - 0
                <class 'node.ext.python.nodes.Import'>: [3:3] - 0
              <class 'node.ext.python.nodes.Module'>: [1:14] - -1
                <class 'node.ext.python.nodes.Block'>: [?:?] - 0
                <class 'node.ext.python.nodes.Class'>: [2:14] - 0
                  <class 'node.ext.python.nodes.Attribute'>: [4:4] - 1
                  <class 'node.ext.python.nodes.Attribute'>: [5:5] - 1
                  <class 'node.ext.python.nodes.Function'>: [7:8] - 1
                    <class 'node.ext.python.nodes.Block'>: [8:8] - 2
                  <class 'node.ext.python.nodes.Function'>: [10:11] - 1
                    <class 'node.ext.python.nodes.Block'>: [11:11] - 2
                  <class 'node.ext.python.nodes.Function'>: [13:14] - 1
                    <class 'node.ext.python.nodes.Block'>: [14:14] - 2
            <class 'node.ext.python.nodes.Module'>: [1:2] - -1
              <class 'node.ext.python.nodes.Block'>: [2:2] - 0
          <class 'node.ext.python.nodes.Module'>: [1:2] - -1
            <class 'node.ext.python.nodes.Block'>: [2:2] - 0
      <class 'node.ext.template.template.JinjaTemplate'>: README.rst
      <class 'node.ext.template.template.JinjaTemplate'>: MANIFEST.rst
      <class 'node.ext.template.template.JinjaTemplate'>: setup.py
      <class 'node.ext.template.template.JinjaTemplate'>: LICENSE.rst
      <class 'node.ext.directory.directory.Directory'>: cornice
        <class 'node.ext.python.nodes.Module'>: [1:1] - -1
          <class 'node.ext.python.nodes.Block'>: [?:?] - 0

Check for the existence of generated files and directories:

data/cornice.example
├── LICENSE.rst
├── MANIFEST.rst
├── README.rst
├── setup.py
└── src
    └── cornice
        ├── example
        │   ├── __init__.py
        │   └── services
        │       ├── apiversionservice.py
        │       ├── __init__.py
        │       ├── services.py
        │       └── userservice.py
        └── __init__.py


    >>> testpackage_path = os.path.join(datadir, 'cornice.example')
    >>> os.path.exists(os.path.join(testpackage_path, 'setup.py'))
    True
    >>> os.path.exists(os.path.join(testpackage_path, 'LICENSE.rst'))
    True
    >>> os.path.exists(os.path.join(testpackage_path, 'MANIFEST.rst'))
    True
    >>> os.path.exists(os.path.join(testpackage_path, 'README.rst'))
    True
    >>> os.path.exists(os.path.join(testpackage_path, 'setup.py'))
    True
    >>> os.path.isdir(os.path.join(testpackage_path, 'src'))
    True
    >>> os.path.isdir(os.path.join(testpackage_path, 'src', 'cornice'))
    True
    >>> os.path.exists(os.path.join(testpackage_path, 'src', 'cornice', '__init__.py'))
    True
    >>> os.path.isdir(os.path.join(testpackage_path, 'src', 'cornice', 'example'))
    True
    >>> os.path.exists(os.path.join(testpackage_path, 'src', 'cornice', 'example', '__init__.py'))
    True
    >>> os.path.isdir(os.path.join(testpackage_path, 'src', 'cornice', 'example', 'services'))
    True
    >>> os.path.exists(os.path.join(testpackage_path, 'src', 'cornice', 'example', 'services', '__init__.py'))
    True

There are two more files to expect, but only because I have not managed to program the handlers properly ;-)

    >>> os.path.exists(os.path.join(testpackage_path, 'src', 'cornice', 'example', 'services', 'apiversionservice.py'))
    True
    >>> os.path.exists(os.path.join(testpackage_path, 'src', 'cornice', 'example', 'services', 'userservice.py'))
    True

Actually, the generated services should go into one file services.py

    >>> os.path.exists(os.path.join(testpackage_path, 'src', 'cornice', 'example', 'services', 'services.py'))
    True

    >>> servicesfile = os.path.join(testpackage_path, 'src', 'cornice', 'example', 'services', 'services.py')
    >>> with open(servicesfile, 'r') as the_file:
    ...     lines = the_file.readlines()


The necessary import should be there...

    >>> 'from cornice import Service\n' in lines
    True

and the generated services, too

    >>> 'apiversionservice = Service(name="foo", path="bar")\n' in lines
    True
    >>> 'userservice = Service(name="foo", path="bar")' in lines
    True



Cleanup: Delete the generated directory:

    >>> if os.path.exists(os.path.join(datadir, 'cornice.example')):
    ...     shutil.rmtree(os.path.join(datadir, 'cornice.example'))


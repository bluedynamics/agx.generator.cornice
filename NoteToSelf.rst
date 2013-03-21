Some notes about Cornice Generator re-generation
------------------------------------------------

the cornice generator is itself modeled and generated.

the model is agx.generator.cornice/model/agx.generator.cornice{.di|.notation|.uml}
and it can be generated when in top level folder by issuing::

  agx model/agx.generator.cornice -o .


when trying to model it this way (calling agx on the .agx file)::

  agx model/agx.generator.cornice.uml.agx

it tries to generate into model/ AND it fails::

  (agx.dev)christoph@s3:~/Code/test_AGX_from_source/agx.dev/devsrc/agx.generator.cornice$ agx model/agx.generator.cornice.uml.agx 
  INFO  AGX 1.0a2 - (c) BlueDynamics Alliance, http://bluedynamics.com, GPL 2
  INFO  Generator started at 13:41:21 2013-03-21.
  INFO  generating model: /home/christoph/Code/test_AGX_from_source/agx.dev/devsrc/agx.generator.cornice/model/agx.generator.cornice.uml
  INFO  using profiles: ['/home/christoph/Code/test_AGX_from_source/agx.dev/devsrc/agx.generator.pyegg/src/agx/generator/pyegg/profiles/pyegg.profile.uml', '/home/christoph/Code/test_AGX_from_source/agx.dev/devsrc/agx.generator.zca/src/agx/generator/zca/profiles/zca.profile.uml', '/home/christoph/Code/test_AGX_from_source/agx.dev/devsrc/agx.generator.generator/src/agx/generator/generator/profiles/generator.profile.uml']
  INFO  generating into: /home/christoph/Code/test_AGX_from_source/agx.dev/devsrc/agx.generator.cornice/model
  Traceback (most recent call last):
    File "/home/christoph/Code/test_AGX_from_source/agx.dev/bin/agx", line 49, in <module>
      sys.exit(agx.dev.main.run())
    File "/home/christoph/Code/test_AGX_from_source/agx.dev/src/agx/dev/main.py", line 15, in run
      agx.core.main.run()
    File "/home/christoph/Code/test_AGX_from_source/agx.dev/devsrc/agx.core/src/agx/core/main.py", line 292, in run
      controller(modelpaths, outdir)
    File "/home/christoph/Code/test_AGX_from_source/agx.dev/devsrc/agx.core/src/agx/core/_api.py", line 48, in __call__
      target = processor(source, target)
    File "/home/christoph/Code/test_AGX_from_source/agx.dev/devsrc/agx.core/src/agx/core/_api.py", line 70, in __call__
      generator(source, targethandler)
    File "/home/christoph/Code/test_AGX_from_source/agx.dev/devsrc/agx.core/src/agx/core/_api.py", line 165, in __call__
      self._dispatch([source])
    File "/home/christoph/Code/test_AGX_from_source/agx.dev/devsrc/agx.core/src/agx/core/_api.py", line 171, in _dispatch
      dispatcher(child, self.target)
    File "/home/christoph/Code/test_AGX_from_source/agx.dev/devsrc/agx.core/src/agx/core/_api.py", line 267, in __call__
      if not scope(source):
    File "/home/christoph/Code/test_AGX_from_source/agx.dev/devsrc/agx.core/src/agx/core/_api.py", line 247, in __call__
      if iface.providedBy(node):
  AttributeError: 'NoneType' object has no attribute 'providedBy'
  (agx.dev)christoph@s3:~/Code/test_AGX_from_source/agx.dev/devsrc/agx.generator.cornice$




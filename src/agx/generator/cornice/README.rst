=====================
agx.generator.cornice
=====================

handler setup
=============

The profile diagram shows a cornice related UML extension,
see agx.generator.cornice/src/agx/generator/cornice/profiles/cornice.profile.di


Stereotype <<service>>
----------------------

I want to be able to model a cornice service as UML::Class,
with (at least) two properties:

 * name: a name for the service (like pyramid routes have names)
 * path: the URL extension of the service that it will 'listen' on
         (much like a pyramid route has a pattern)

The generator shall transform the service class into a statement like so
(where 'Service' is imported from cornice)::

   myservice = Service(
       name='myservicename',
       path='/path/to/service',
       description='some description of my service')


see examples in example app:
 
https://github.com/C3S/c3s.app.restapi/blob/master/src/c3s/api/views.py#L98
https://github.com/C3S/c3s.app.restapi/blob/master/src/c3s/api/views.py#L126
https://github.com/C3S/c3s.app.restapi/blob/master/src/c3s/api/views.py#L208


Stereotypes <<get>>, <<put>>, <<post>>, <<delete>>
--------------------------------------------------

The services modeled as described above shall also carry UML::Operations,
some of which may be given a stereotype <<get>>, <<put>>, <<post>>, <<delete>>.

The UML::Operations without stereotype are to become normal functions, usable as
utility functions or validators.

The UML::Operations *with* one of the stereotypes shall become functions and
get a *decorator* attached to them::

   # a GET call: what a browser does when calling a URL
   @api_version.get()
   def get_info(request):
       """Returns API version in JSON."""
       return {'API version': '0.1dev'}

   @users.put(validators=unique)
   def create_user(request):
       """Adds a new user."""
       user = request.validated['user']
       # do something ...
       _USERS[user['name']] = user['token']
       return {  # return something
           'api-version': api_ver,
           'token': '%s-%s' % (user['name'], user['token'])}


see examples in 
https://github.com/C3S/c3s.app.restapi/blob/master/src/c3s/api/views.py#L106 #GET
https://github.com/C3S/c3s.app.restapi/blob/master/src/c3s/api/views.py#L130 #GET
https://github.com/C3S/c3s.app.restapi/blob/master/src/c3s/api/views.py#L140 #PUT
https://github.com/C3S/c3s.app.restapi/blob/master/src/c3s/api/views.py#L168 #DELETE
https://github.com/C3S/c3s.app.restapi/blob/master/src/c3s/api/views.py#L247 #GET
https://github.com/C3S/c3s.app.restapi/blob/master/src/c3s/api/views.py#L263 #POST

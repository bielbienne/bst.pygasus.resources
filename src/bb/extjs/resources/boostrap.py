import fanstatic

from grokcore import component

from bb.extjs.core.interfaces import IApplicationContext

from bb.extjs.wsgi.interfaces import IRequest
from bb.extjs.wsgi.interfaces import IRootDispatcher


@component.implementer(IRootDispatcher)
class BootstrapEntryPoint(component.MultiAdapter):
    """ generate a boostrap.js with all
        required class-path-mappings.
    """
    component.name('bootstrap')
    component.adapts(IApplicationContext, IRequest)
    
    def __init__(self, context, request):
        self.context = context
        self.request = request
    
    def __call__(self):
        self.request.response.content_type='application/javascript'
        self.request.response.write("""
        Ext.Loader.addClassPathMappings({
          "Ext": "fanstatic/extjs/src/",
          "bielbienne.iptt.store": "fanstatic/iptt/store",
          "bielbienne.iptt.model": "fanstatic/iptt/model",
          "bielbienne.iptt.view": "fanstatic/iptt/view",
          "bielbienne.iptt.controller": "fanstatic/iptt/controller",

          "scaffolding.store": "scaffolding/store",
          "scaffolding.model": "scaffolding/model",
          "scaffolding.form": "scaffolding/form",
          "scaffolding.grid": "scaffolding/grid",
          "scaffolding.editgrid": "scaffolding/editgrid"

        });

        """)



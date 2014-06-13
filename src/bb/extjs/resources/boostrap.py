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
          "bielbienne.iptt.store": "scaffolding/store",
          "bielbienne.iptt.model": "scaffolding/model",
          "bielbienne.iptt.form": "scaffolding/form",
          "bielbienne.iptt.grid": "scaffolding/grid",
          "bielbienne.iptt.editgrid": "scaffolding/editgrid"

        });

        """)



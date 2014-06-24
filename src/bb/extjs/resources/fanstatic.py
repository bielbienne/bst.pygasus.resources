import fanstatic

from js.extjs import extjs as resource_extjs

from grokcore import component
from bb.extjs.wsgi.interfaces import IRequest
from bb.extjs.wsgi.interfaces import IRootDispatcher
from bb.extjs.wsgi.events import IPreRequestProcessingEvent
from bb.extjs.core.interfaces import IApplicationContext


@component.implementer(IRootDispatcher)
class FanstaticEntryPoint(component.MultiAdapter):
    """ 
    """
    component.name('fanstatic')
    component.adapts(IApplicationContext, IRequest)
    
    def __init__(self, context, request):
        self.context = context
        self.request = request
    
    def __call__(self):
        
        library = fanstatic.get_library_registry()
        publisher = fanstatic.Publisher(library)

        # skip first element in url before we
        # send it to original fanstatic publisher
        self.request.path_info_pop()
        response = publisher(self.request)
        self.request.response.status=response.status
        self.request.response.headerlist=response.headerlist
        self.request.response.app_iter=response.app_iter


@component.subscribe(IApplicationContext, IPreRequestProcessingEvent)
def initalize_fanstatic(context, event):
        needed = fanstatic.init_needed(debug=True)
        context.resources.need()

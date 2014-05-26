import fanstatic

from js import extjs as resource_extjs

from bb.extjs.core import extjs
from bb.extjs.wsgi.interfaces import IRootDispatcher
from bb.extjs.wsgi.interfaces import IRequest
from bb.extjs.wsgi.interfaces import IResponse



@extjs.implementer(IRootDispatcher)
class FanstaticEntryPoint(extjs.MultiAdapter):
    """ 
    """
    extjs.name('fanstatic')
    extjs.adapts(IRequest, IResponse)
    
    def __init__(self, request, response):
        self.request = request
        self.response = response
    
    def __call__(self):
        
        needed = fanstatic.init_needed()
        resource_extjs.basic.need()
        library = fanstatic.get_library_registry()
        publisher = fanstatic.Publisher(library)

        # skip first element in url before we
        # send it to original fanstatic publisher
        self.request.path_info_pop()
        response = publisher(self.request)
        self.response.status=response.status
        self.response.headerlist=response.headerlist
        self.response.app_iter=response.app_iter

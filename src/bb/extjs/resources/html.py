import fanstatic
from genshi.core import Markup
from bb.extjs.core import ext
from bb.extjs.core.interfaces import IApplicationContext

from bb.extjs.wsgi.interfaces import IRequest
from bb.extjs.wsgi.interfaces import IRootDispatcher

from bb.extjs.resources import loader


@ext.implementer(IRootDispatcher)
class HtmlEntryPoint(ext.MultiAdapter):
    """ generate a index html. This html site will than
        load extjs framework with css and run the
        application.
    """
    ext.name('index')
    ext.adapts(IApplicationContext, IRequest)
    
    tmpl = loader.load('index.html')
    
    def __init__(self, context, request):
        self.context = context
        self.request = request
    
    def __call__(self):
        resources = fanstatic.get_needed()
        stream = self.tmpl.generate(resources=Markup(resources.render()))
        self.request.response.mimetype='text/html'
        self.request.response.write(stream.render('html', doctype='html'))

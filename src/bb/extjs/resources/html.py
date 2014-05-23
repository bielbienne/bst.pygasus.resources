from bb.extjs.core import extjs
from bb.extjs.wsgi.interfaces import IRootDispatcher
from bb.extjs.wsgi.interfaces import IRequest
from bb.extjs.wsgi.interfaces import IResponse
from bb.extjs.resources import loader


@extjs.implementer(IRootDispatcher)
class HtmlEntryPoint(extjs.MultiAdapter):
    """ generate a index html. This html site will than
        load extjs framework with css and run the
        application.
    """
    extjs.name('bb.extjs.core.htmlentrypoint')
    extjs.adapts(IRequest, IResponse)
    
    target = '/'
    
    tmpl = loader.load('index.html')
    
    def __init__(self, request, response):
        self.request = request
        self.response = response
    
    def __call__(self):
        stream = self.tmpl.generate(links=None)
        self.response.mimetype='text/html'
        self.response.set_data(stream.render('html', doctype='html'))

from zope.interface import Interface
from zope.interface import Attribute



class IClassPathMappings(Interface):
    """ This subscriber tells Extjs how the class
        mapping should looks like.
    """
    
    name = Attribute('name space of moduel eg "bielbienne.iptt.gird"')
    path = Attribute('path to eg "fanstatic/iptt/grid')
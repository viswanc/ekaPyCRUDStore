
__plugin_name__ = 'python.crud.store.sqlalchemy'
__keywords__ = 'eka SQLAlchemy CRUD Store'
__author__ = 'Viswanath Chidambaram'
__email__ = 'viswanc@thoughtworks.com'
__version__ = '0.0.1'

from eka.classes.node import node
from eka.plugins import define

@define('python.crud.store.sqlalchemy')
class store(node):
  def __init__(self, Structure, Scopes):
    node.__init__(self, Structure, Scopes)

  def build(self):
    from os.path import dirname
    from eka.classes.builders.jinja import jinjaBuilder

    Structure = self.Structure

    buildTgt = '%s/store' % Structure['buildBase']
    buildSrc = '%s/res/store' % dirname(__file__)

    return jinjaBuilder().build(buildSrc, buildTgt, Structure)

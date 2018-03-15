
__plugin_name__ = 'python.crud.store.sqlalchemy'
__keywords__ = 'eka SQLAlchemy CRUD Store'
__author__ = 'Viswanath Chidambaram'
__email__ = 'viswanc@thoughtworks.com'
__version__ = '0.0.1'

from eka.classes.node import node
from eka.plugins import define

TypeMap = {

  'string': 'Unicode',
  'number': 'Float',
  # 'number': 'Integer', #Pending: Check whether could safely be ignored. If so inculde the possible values in the schema.
  'boolean': 'Boolean', #Pending
  # 'REAL': 'REAL', #Pending
  # 'BLOB': 'BLOB', #Pending
  # 'array': 'Json' #Pending
  # 'object': 'Json' #Pending
  # 'null': 'None' #Pending
}

@define('python.crud.store.sqlalchemy')
class store(node):
  def __init__(self, Structure, Scopes):
    node.__init__(self, Structure, Scopes)

  def standardizeProperties(self):
    for Resource in self.Structure['props'].values():
      Resource.setdefault('persist', True)

      for Field in Resource['props'].values():
        Field.setdefault('type', 'string')
        Field.setdefault('persist', True)
        Field.setdefault('crud.store.type', TypeMap[Field['type']]) # #Pending: Remove unnecessary fields after processing.

  def build(self):
    from os.path import dirname
    from eka.classes.builders.jinja import jinjaBuilder

    Structure = self.Structure

    buildTgt = '%s/store' % Structure['buildBase']
    buildSrc = '%s/res/store' % dirname(__file__)

    return jinjaBuilder().build(buildSrc, buildTgt, Structure)

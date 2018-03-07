
__plugin_name__ = 'python.crud.store.sqlalchemy'
__keywords__ = 'eka SQLAlchemy CRUD Store'
__author__ = 'Viswanath Chidambaram'
__email__ = 'viswanc@thoughtworks.com'
__version__ = '0.0.1'

from eka.classes.node import node
from eka.classes.ymlParser import parseYML
from eka.plugins import define

# Data
Definitions = parseYML(r"""
""")

# Helpers
def getSchemaExtension(className):
  Schema = {'definitions': Definitions}
  Schema.update(Definitions[className])

  return Schema

@define('python.crud.store.sqlalchemy')
class store(node):
  pass

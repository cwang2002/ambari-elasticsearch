from resource_management.libraries.functions.version import format_hdp_stack_version, compare_versions
from resource_management import *

# server configurations
config = Script.get_config()

dockerImage = config['configurations']['elasticsearch-config']['image']
containerName = config['configurations']['elasticsearch-config']['name']

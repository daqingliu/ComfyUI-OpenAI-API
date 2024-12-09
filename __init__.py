# __init__.py

from .openai_node import OpenAI_API

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "OpenAI_API": OpenAI_API
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "OpenAI_API": "OpenAI API Node"
}

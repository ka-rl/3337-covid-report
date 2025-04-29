from traitlets.config import get_config

c = get_config()
c.TagRemovePreprocessor.enabled = True
c.TagRemovePreprocessor.remove_input_tags = ['hide_input']
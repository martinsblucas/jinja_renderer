import os
import logging
from fire import Fire
from fire.core import FireError
from jinja2 import Environment, FileSystemLoader, TemplateError


logger = logging.getLogger(__name__)


class JinjaRender(object):
    """
    Render a Jinja template in the terminal
    """
    def render(self, template_path, **kwargs):
        """ 
          Render a Jinja template in the terminal 

          :param template_path: The Jinja template path
          :param kwargs: The template variables
        """
        if not os.path.exists(template_path):
            raise FireError(f'{template_path} not exists')
        if not os.path.isfile(template_path):
            raise FireError(f'{template_path} is not a file')
        loader = FileSystemLoader(searchpath=os.path.dirname(template_path))
        env = Environment(loader=loader)
        template = env.get_template(os.path.basename(template_path))
        return template.render(**kwargs)


if __name__ == '__main__':
    try:
        Fire(JinjaRender)
    except (FireError, TemplateError) as e:
        logger.error(str(e))

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from polls_cms_integration.models import PollPluginModel
from django.utils.translation import ugettext


@plugin_pool.register_plugin # register plugin
class PollPluginPublisher(CMSPluginBase):
    model = PollPluginModel #model where plugin data are saved
    module = ugettext('Polls')
    name = ugettext('Poll Plugin') # name of the plugin in the interface
    render_template = "polls_cms_integration/poll_plugin.html"

    def render(self,context,instance,placeholder):
        context.update({'instance':instance})
        return context
from paste.deploy.converters import asbool
from fedmsg.consumers import FedmsgConsumer
import ..models as m

log = logging.getLogger("moksha.hub")
class FUSSConsumer(FedmsgConsumer):
    topic = 'org.fedoraproject.*'
    def __init__(self, hub):
        self.hub = hub
        self.DBSession = m.DBsession

        ENABLED = 'fedmsg.consumers.fuss.enabled'
        if not asbool(hub.config.get(ENABLED, False)):
            log.info('fedmsg.consumers.fuss disabled')
        return super(FUSSConsumer, self).__init__(hub)

    def consumer(self, msg):
        pass

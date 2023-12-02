import ujson

from uc_flow_nodes.service import NodeService
from uc_flow_schemas.flow import CredentialProtocol
from node.views.execute import ExecuteView
from node.views.info import InfoView

class Service(NodeService):
    class Routes(NodeService.Routes):
        Info = InfoView
        Execute = ExecuteView

import ujson
from typing import List, Tuple

from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.service import NodeService
from uc_flow_nodes.views import info, execute
from uc_flow_schemas import flow
from uc_flow_schemas.flow import Property, CredentialProtocol, RunState


class NodeType(flow.NodeType):
    id: str = 'd7ba194d-d757-431c-bf5d-023f42bdf121'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'uc-flow-node'
    is_public: bool = False
    displayName: str = 'uc-flow-node'
    icon: str = '<svg><text x="8" y="50" font-size="50">😎</text></svg>'
    description: str = 'uc-flow-node service'
    properties: List[Property] = [
        Property(
            displayName='first_text_field',
            name='first_text_field',
            type=Property.Type.STRING,
            placeholder='Foo placeholder',
            description='Foo description',
            required=True,
            default='',
        ),
        Property(
            displayName='first_number_field',
            name='first_number_field',
            type=Property.Type.NUMBER,
            placeholder='Number placeholder',
            description='Number description',
            required=True,
            default=0,
        ),
        Property(
            displayName='number/text',
            name='return_type',
            type=Property.Type.BOOLEAN, 
            placeholder='Return type placeholder',
            description='Return type description',
            required=True,
            default=False,
        )
    ]


class InfoView(info.Info):
    class Response(info.Info.Response):
        node_type: NodeType


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            text_value = json.node.data.properties['first_text_field']
            number_value = json.node.data.properties['first_number_field']
            return_type = json.node.data.properties['return_type']

            try:
                text_value = float(text_value)
            except ValueError:
                raise ValueError("Нельзя перевести текст в число!")

            result = number_value + text_value

            if return_type:
                result = f'{int(result)}'
            else:
                result = int(result)

            await json.save_result({"result": result})
            json.state = RunState.complete

        except Exception as e:
            self.log.warning(f'Error {e}')
            await json.save_error({"error": str(e)})
            json.state = RunState.error

        return json


class Service(NodeService):
    class Routes(NodeService.Routes):
        Info = InfoView
        Execute = ExecuteView

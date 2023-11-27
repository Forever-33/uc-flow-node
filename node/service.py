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
        ),
        Property(
            displayName='Переключатель',
            name='switch_field',
            type=Property.Type.BOOLEAN,
            placeholder='Switch placeholder',
            description='Switch description',
            required=True,
            default=False,
        ),
        Property(
            displayName='Значение 1',
            name='dropdown_field_1',
            type=Property.Type.OPTIONS,
            options=[
                {"name": "Значение 1", "value": "value1"},
                {"name": "Значение 2", "value": "value2"},
            ],
            displayOptions={
                'show': {'switch_field': [True]},
            },
        ),
        Property(
            displayName='Значение 2',
            name='dropdown_field_2',
            type=Property.Type.OPTIONS,
            options=[
                {"name": "Значение 1", "value": "value1"},
                {"name": "Значение 2", "value": "value2"},
            ],
            displayOptions={
                'show': {'switch_field': [True]},
            },
        ),
        Property(
            displayName='Поле для ввода почты',
            name='email_field',
            type=Property.Type.STRING,
            placeholder='Email placeholder',
            description='Email description',
            displayOptions={
                'show': {
                    'switch_field': [True],
                    'dropdown_field_1': ['value1'],
                    'dropdown_field_2': ['value2'],
                },
            },
        ),
        Property(
            displayName='Поле для ввода даты и времени',
            name='datetime_field',
            type=Property.Type.DATETIME,
            placeholder='Datetime placeholder',
            description='Datetime description',
            displayOptions={
                'show': {
                    'switch_field': [True],
                    'dropdown_field_1': ['value1'],
                    'dropdown_field_2': ['value2'],
                },
            },
        ),

    ]


class InfoView(info.Info):
    class Response(info.Info.Response):
        node_type: NodeType


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            switch_field_value = json.node.data.properties['switch_field']
            dropdown_field_1_value = json.node.data.properties.get('dropdown_field_1')
            dropdown_field_2_value = json.node.data.properties.get('dropdown_field_2')
            email_field_value = json.node.data.properties.get('email_field')
            datetime_field_value = json.node.data.properties.get('datetime_field')
            text_value = json.node.data.properties['first_text_field']
            number_value = json.node.data.properties['first_number_field']
            return_type = json.node.data.properties['return_type']
            
            result_dict = {}

            try:
                text_value = float(text_value)
            except ValueError:
                raise ValueError("Нельзя перевести текст в число!")

            numeric_result = number_value + text_value

            if return_type:
                numeric_result = f'{int(numeric_result)}'
            else:
                numeric_result = int(numeric_result)
            
            if email_field_value is not None:
                result_dict['email_result'] = email_field_value
            if datetime_field_value is not None:
                result_dict['datetime_result'] = datetime_field_value

            result_dict['numeric_result'] = numeric_result

            await json.save_result(result_dict)
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
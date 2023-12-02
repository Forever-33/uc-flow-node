from uc_flow_schemas import flow
from uc_flow_schemas.flow import Property
from node.static.icon import ICON
from typing import List

class NodeType(flow.NodeType):
    id: str = '7849c909-6132-40d1-b259-be2cf3155816121'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'uc-flow-node'
    is_public: bool = False
    displayName: str = 'uc-flow-node'
    icon: str = ICON
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
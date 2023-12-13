
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
            displayName='Action',
            name='dropdown_action',
            type=Property.Type.OPTIONS,
            options=[
                {"name": "Авторизация", "value": "value1"},
                {"name": "Запрос", "value": "value2"},
            ],
        ),
        Property(
            displayName='Resource',
            name='dropdown_resource',
            type=Property.Type.OPTIONS,
            options=[
                {"name": "Customer", "value": "value3"},
            ],
            displayOptions={
                'show': {
                    'dropdown_action': ['value2'],
                },
            },
        ),
        Property(
            displayName='token_api',
            name='token_api',
            type=Property.Type.STRING,
            displayOptions={
                'show': {
                    'dropdown_resource': ['value3'],
                },
            },
        ),
        Property(
            displayName='Operation',
            name='dropdown_operation',
            type=Property.Type.OPTIONS,
            options=[
                {"name": "Index", "value": "value4"},
                {"name": "Create", "value": "value5"},
                {"name": "Update", "value": "value6"},
            ],
            displayOptions={
                'show': {
                    'dropdown_resource': ['value3'],
                },
            },
        ),
    ]
    
    credentials: List[flow.NodeType.Credential] = [
        flow.NodeType.Credential(name="alfacrm_api_auth", required=True, contextKey="auth_token")
    ]


# from uc_flow_schemas import flow
# from uc_flow_schemas.flow import Property
# from node.static.icon import ICON
# from typing import List

# class NodeType(flow.NodeType):
#     id: str = '7849c909-6132-40d1-b259-be2cf3155816121'
#     type: flow.NodeType.Type = flow.NodeType.Type.action
#     name: str = 'uc-flow-node'
#     is_public: bool = False
#     displayName: str = 'uc-flow-node'
#     icon: str = ICON
#     description: str = 'uc-flow-node service'
#     properties: List[Property] = [
#         Property(   
#             displayName='Action',
#             name='dropdown_action',
#             type=Property.Type.OPTIONS,
#             options=[
#                 {"name": "Авторизация", "value": "value1"},
#                 {"name": "Запрос", "value": "value2"},
#             ],
#         ),
#         Property(
#             displayName='Resource',
#             name='dropdown_resource',
#             type=Property.Type.OPTIONS,
#             options=[
#                 {"name": "Customer", "value": "value3"},
#             ],
#             displayOptions={
#                 'show': {
#                     'dropdown_action': ['value2'],
#                 },
#             },
#         ),
#         Property(
#             displayName='token_api',
#             name='token_api',
#             type=Property.Type.STRING,
#             displayOptions={
#                 'show': {
#                     'dropdown_resource': ['value3'],
#                 },
#             },
#         ),
#         Property(
#             displayName='Operation',
#             name='dropdown_operation',
#             type=Property.Type.OPTIONS,
#             options=[
#                 {"name": "Index", "value": "value4"},
#                 {"name": "Create", "value": "value5"},
#                 {"name": "Update", "value": "value6"},
#             ],
#             displayOptions={
#                 'show': {
#                     'dropdown_resource': ['value3'],
#                 },
#             },
#         ),
#     ]
    
#     credentials: List[flow.NodeType.Credential] = [
#         flow.NodeType.Credential(name="alfacrm_api_auth", required=True, contextKey="auth_token")
#     ]
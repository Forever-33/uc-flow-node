import ujson
from uc_flow_nodes.views import execute
from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_schemas.flow import RunState, Property
from uc_http_requester.requester import Request, Response

class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            credentials = await json.get_credentials()
            base_url = credentials.data['hostname']
            api_key = credentials.data['api_key']
            email = credentials.data['email']
            dropdown_action = json.node.data.properties.get('dropdown_action')
            dropdown_operation = json.node.data.properties.get('dropdown_operation')

            token = None  # Инициализация переменной token

            if dropdown_action == 'value1':  # Авторизация
                request_data = Request(
                    url=f'https://{base_url}/v2api/auth/login',
                    json={'email': email, 'api_key': api_key},
                    headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
                    method=Request.Method.post,
                )

                response: Response = await request_data.execute()

                if response.is_success:
                    response_data = ujson.loads(response.content)
                    token = response_data.get('token', None)

                    if token:
                        # Если токен успешно получен, сохраняем его и устанавливаем состояние complete
                        await json.save_result(response_data)
                        json.node.data.properties['token'] = token
                        json.state = RunState.complete
                    else:
                        # Если токен не найден в ответе сервера, устанавливаем состояние error
                        self.log.warning("Токен не найден в ответе сервера.")
                        json.state = RunState.error
                        return json
                else:
                    # Если произошла ошибка при авторизации, устанавливаем состояние error
                    self.log.warning("Ошибка при авторизации.")
                    json.state = RunState.error
                    return json

            if dropdown_operation == 'value4' and token:  # Это Branch
                create_data = Request(
                    url=f'https://{base_url}/v2api/branch/index',
                    json={"is_active": 1, "page": 0},
                    headers={
                        'X-ALFACRM-TOKEN': token,
                        'Accept': 'application/json',
                        'Content-Type': 'application/json',
                    },
                    method=Request.Method.post,
                )

                create_response: Response = await create_data.execute()

                if create_response.is_success:
                    create_response_data = ujson.loads(create_response.content)
                    await json.save_result(create_response_data)
                    json.state = RunState.complete
                else:
                    self.log.warning("Ошибка при запросе на создание.")

            elif dropdown_operation == 'value4' and not token:
                # Если токен не существует, устанавливаем состояние error
                self.log.warning("Токен отсутствует. Сначала выполните авторизацию.")
                json.state = RunState.error

        except Exception as e:
            # Если произошла общая ошибка, устанавливаем состояние error
            self.log.warning(f'Ошибка {e}')
            await json.save_error({"error": str(e)})
            json.state = RunState.error

        return json



# import ujson
# from uc_flow_nodes.views import execute
# from uc_flow_nodes.schemas import NodeRunContext
# from uc_flow_schemas.flow import RunState, Property
# from uc_http_requester.requester import Request, Response


# class ExecuteView(execute.Execute):
#     async def post(self, json: NodeRunContext) -> NodeRunContext:
        
#         try:
#             credentials = await json.get_credentials()
#             base_url = credentials.data['hostname']
#             api_key = credentials.data['api_key']
#             email = credentials.data['email']
#             dropdown_action = json.node.data.properties.get('dropdown_action')
#             dropdown_operation = json.node.data.properties.get('dropdown_operation')

#             if dropdown_action == 'value1':  # Авторизация
#                 request_data = Request(
#                     url=f'https://{base_url}/v2api/auth/login',
#                     json={'email': email, 'api_key': api_key},
#                     headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
#                     method=Request.Method.post,
#                 )

#                 response: Response = await request_data.execute()

#                 if response.is_success:
#                     response_data = ujson.loads(response.content)
#                     token = response_data.get('token', None)

#                     if token:
#                         await json.save_result(response_data)
#                         json.node.data.properties['token'] = token
#                         json.state = RunState.complete
#                     else:
#                         self.log.warning("Токен не найден в ответе сервера.")
#                 else:
#                     self.log.warning("Ошибка при авторизации.")

#             if dropdown_operation == 'value4' and token:  
#                 create_data = Request(
#                     url=f'https://{base_url}/v2api/branch/index',
#                     json={"is_active": 1, "page": 0},
#                     headers={
#                         'X-ALFACRM-TOKEN': token,
#                         'Accept': 'application/json',
#                         'Content-Type': 'application/json',
#                     },
#                     method=Request.Method.post,
#                 )

#                 create_response: Response = await create_data.execute()

#                 if create_response.is_success:
#                     create_response_data = ujson.loads(create_response.content)
#                     await json.save_result(create_response_data)
#                     json.state = RunState.complete
#                 else:
#                     self.log.warning("Ошибка при запросе на создание.")
#             elif dropdown_operation == 'value4' and not token:
#                 self.log.warning("Токен отсутствует. Сначала выполните авторизацию.")

#         except Exception as e:
#             self.log.warning(f'Ошибка {e}')
#             await json.save_error({"error": str(e)})
#             json.state = RunState.error

#         return json







# import ujson
# import aiohttp
# from uc_flow_nodes.views import execute
# from uc_flow_nodes.schemas import NodeRunContext
# from uc_flow_schemas.flow import RunState

# class ExecuteView(execute.Execute):
#     async def post(self, json: NodeRunContext) -> NodeRunContext:
#         try:
#             # Получение данных из credentials
#             credentials = await json.get_credentials()
#             base_url = credentials.data['hostname']
#             auth_key = credentials.data['api_key']

#             # Отправка HTTP-запроса для авторизации
#             auth_url = f'https://{base_url}/v2api/auth/login'
#             auth_data = {'email': credentials.data['email'], 'api_key': auth_key}
#             auth_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

#             async with aiohttp.ClientSession() as session:
#                 async with session.post(auth_url, headers=auth_headers, json=auth_data) as auth_response:
#                     auth_result = await auth_response.json()
                    # auth_token = auth_result.get('token')

            
#             result_dict = {'auth_token': auth_token}
#             result_json = ujson.dumps(result_dict)
#             await json.save_result(result_json)
#             json.state = RunState.complete


#         except Exception as e:
#             self.log.warning(f'Error {e}')
#             await json.save_error({"error": str(e)})
#             json.state = RunState.error

#         return json




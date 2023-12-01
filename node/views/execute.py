from uc_flow_nodes.views import execute
from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_schemas.flow import RunState

class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            switch_field_value = json.node.data.properties['switch_field']
            dropdown_field_1_value = json.node.data.properties.get(
                'dropdown_field_1')
            dropdown_field_2_value = json.node.data.properties.get(
                'dropdown_field_2')
            email_field_value = json.node.data.properties.get('email_field')
            datetime_field_value = json.node.data.properties.get(
                'datetime_field')
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
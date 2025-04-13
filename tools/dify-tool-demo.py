from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin.entities.model.llm import LLMModelConfig
from dify_plugin.entities.model.message import SystemPromptMessage, UserPromptMessage

class DifyToolDemoTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        # model_info = tool_parameters['chat-model']
        # response = self.session.model.llm.invoke(
        #     model_config=LLMModelConfig(
        #         provider=model_info.get('provider'),
        #         model=model_info.get('model'),
        #         mode=model_info.get('mode'),
        #         completion_params=model_info.get('completion_params')
        #     ),
        #     prompt_messages=[
        #         SystemPromptMessage(content="你是一个风趣幽默的问答机器人，请根据用户的问题进行回答"),
        #         UserPromptMessage(content=tool_parameters['query']),
        #     ],
        #     stream=False
        # )
        result = tool_parameters['query']
        yield self.create_blob_message(result, meta={'mime_type': 'text/html', 'filename': 'result.html'})

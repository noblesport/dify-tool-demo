from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError


class DifyToolDemoProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            # print(credentials['demo_api_key'])
            # if credentials['demo_api_key'] != '123':
            #     raise ToolProviderCredentialValidationError(str(e))
            pass
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))

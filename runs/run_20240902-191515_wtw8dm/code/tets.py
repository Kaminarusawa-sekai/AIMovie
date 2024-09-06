
import agentscope
from agentscope.models import PostAPIChatWrapper
from agentscope.agents import DialogAgent, UserAgent
from agentscope.message import Msg



# model_config = {
#     "config_name": "gpt-4", # A unique name for the model config.
#     "model_type": "openai_chat",    # Choose from "openai_chat", "openai_dall_e", or "openai_embedding".

#     "model_name": "gpt-4",   # The model identifier used in the OpenAI API, such as "gpt-3.5-turbo", "gpt-4", or "text-embedding-ada-002".
#     "api_key": "d4259c15567e44809c9629fae89583f8",               # Your OpenAI API key. If unset, the environment variable OPENAI_API_KEY is used.
#     "organization": "xxx",          # Your OpenAI organization ID. If unset, the environment variable OPENAI_ORGANIZATION is used.
# }

model_config = {
    "config_name": "my_postapiwrapper_config",
    "model_type": "post_api_chat",

    # Required parameters
    "api_url": "https://aichatlanba.openai.azure.com",
    "headers": {
        # e.g. "Authorization": "Bearer xxx",
    },

    # Optional parameters
    "messages_key": "d4259c15567e44809c9629fae89583f8",
}


# 读取模型配置
agentscope.init(model_configs=model_config)

# 创建一个对话智能体和一个用户智能体
dialogAgent = DialogAgent(name="assistant", model_config_name="my_postapiwrapper_config", sys_prompt="You are a helpful ai assistant")
userAgent = UserAgent()
x=Msg("assitant", "Hi!")

a=dialogAgent(x)
print(a)
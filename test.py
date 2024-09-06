import agentscope
from agentscope.agents import DialogAgent, UserAgent
from agentscope.message import Msg


# 读取模型配置
agentscope.init(model_configs="./model_configs.json")

# 创建一个对话智能体和一个用户智能体
dialogAgent = DialogAgent(name="assistant", model_config_name="gpt-4", sys_prompt="You are a helpful ai assistant")
userAgent = UserAgent()
# 来自Alice的简单文本消息示例
message_from_alice = Msg("assistant", "Hi!")
a=dialogAgent(message_from_alice)
print(a)
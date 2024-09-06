import langchain
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain


EMBEDDING_URL = "https://aichatlanba.openai.azure.com/openai/deployments/text-embedding-3-large/embeddings?api-version=2023-05-15"
OPENAI_API_KEY = "d4259c15567e44809c9629fae89583f8"
OPENAI_API_TYPE = "azure"
OPENAI_API_VERSION = "2023-03-15-preview"
AZURE_ENDPOINT="https://aichatlanba.openai.azure.com/"


llm = AzureChatOpenAI(azure_endpoint=AZURE_ENDPOINT,
                          openai_api_version=OPENAI_API_VERSION,
                          openai_api_key=OPENAI_API_KEY,
                          azure_deployment="gpt-4o",
                          openai_api_type=OPENAI_API_TYPE,
                          streaming=True,
                          temperature=0.7)


def clip_paragraph(story):
    template="""/

    我的故事是：{story}

    你来充当一位有艺术气息的助理。

    ## 任务

    我用自然语言告诉你一个故事，你需要列举出你认为需要插入图画的句子,间隔3-8句均可。
    请分段返回你认为需要插入图画的句子和这句句子的主旨。
    请使用字典格式回复以下字段:
    "在这里写你认为需要生成的第n个句子":"","在这里写你认为第n个句子的主旨":""，中间以"\n"分隔。
    除此之外也不要添加任何内容,也不要出现json字样。


    """

    prompt=PromptTemplate.from_template(template)
    prompt.format(story=story)
    query="给我一列举关键词"
    chain=prompt|llm
    paragraph=chain.invoke(input=story)
    print(paragraph)
    return paragraph

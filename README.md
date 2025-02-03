# Perplexica-Python
The Perplexica Python library was created to call the Perplexica API
# Perplexica 使用文档

## Introduction 简介
Perplexica 是一个用于处理查询请求并获取消息和来源信息的类。它通过调用指定的 API 来实现这一功能。

## Usage 使用方法

### Initialization 初始化
首先，需要创建一个 `Perplexica` 类的实例。在初始化时，需要提供以下参数：

- **url**: The URL of the API. (API 的 URL)
- **chatModelProvider**: The provider of the chat model. (聊天模型的提供商)
- **chatModel**: The specific chat model to use. (使用的具体聊天模型)
- **embeddingModelProvider**: The provider of the embedding model. (嵌入模型的提供商)
- **embeddingModel**: The specific embedding model to use. (使用的具体嵌入模型)
- **optimizationMode**: The mode for optimization,可以选择 "speed" 或 "balanced". (优化模式，可选 "speed" 或 "balanced")
- **focusMode**: The focus mode for searching, options include "webSearch", "academicSearch", "writingAssistant", "wolframAlphaSearch", "youtubeSearch", "redditSearch". (搜索焦点模式，选项包括 "webSearch", "academicSearch", "writingAssistant", "wolframAlphaSearch", "youtubeSearch", "redditSearch")

Example 示例:
```bash
ython
perplexica = Perplexica(
url="http://localhost:3001/api/search",
chatModelProvider="ollama",
chatModel="deepseek-r1:1.5b",
embeddingModelProvider="ollama",
embeddingModel="deepseek-r1:1.5b",
optimizationMode="speed",
focusMode="webSearch"
)
```
### Searcher Start 搜索开始
调用 `searcherStart` 方法来发起一次查询请求。该方法接受两个参数：
- **query**: The query string you want to search for. (要搜索的查询字符串)
- **history** (optional): The history of previous queries and responses Optional(之前的查询和响应的历史记录 可选)

Example 示例:
```python
message, source = perplexica.searcherStart("What is AI?")
print(message)
print(source)
```
If a history parameter is provided, it should be included in the data dictionary as follows:
如果提供了 history 参数，则应将其包含在数据字典中如下所示：
```bash
history = [
  ["human", "What is Perplexica?"],
  ["assistant", "Perplexica is an AI-powered search engine..."]
]
message, source = perplexica.searcherStart("What is AI?",history)
print(message)
print(source)
```
### Parameters 参数
##### Input 输入参数

- url: String representing the API endpoint. 表示 API 端口的字符串
- chatModelProvider: String indicating the provider of the chat model. 表示聊天模型的提供商的字符串
- chatModel: String specifying the name of the chat model. 指定聊天模型名称的字符串
- embeddingModelProvider: String indicating the provider of the embedding model. 表示嵌入模型的提供商的字符串
- embeddingModel: String specifying the name of the embedding model. 指定嵌入模型名称的字符串
- optimizationMode: String defining the optimization strategy ("speed" or "balanced"). 定义优化策略的字符串（“speed”或“balanced”）
- focusMode: String setting the focus area for the search. 设置搜索焦点区域的字符串
->`webSearch`, `academicSearch`, `writingAssistant`,` wolframAlphaSearch`, `youtubeSearch`,` redditSearch.`
- query: String containing the user's query.包含用户提问的字符串
- history: Optional list containing past interactions.包含过去交互的可选列表

### Returned information 返回的信息
- message:  The main content of Perplexca 
- sources:  Search for sources 搜索来源

### The situation when an error occurs 出错时的情况
If the API returns a non-200 status code, an error message and status code will be printed.
如果 API 返回非 200 状态代码，则会打印错误消息和状态代码。

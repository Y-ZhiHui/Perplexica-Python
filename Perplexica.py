import requests


class Perplexica:
    def __init__(self, url, chatModelProvider, chatModel, embeddingModelProvider, embeddingModel, optimizationMode, focusMode):
        #define the URL for the API 定义API的URL
        self.url = url
        
        #The chatModel Setting 设置聊天模型
        self.chatModelProvider = chatModelProvider
        self.chatModel = chatModel
        
        #The embeddingModel Setting 设置嵌入模型
        self.embeddingModelProvider = embeddingModelProvider
        self.embeddingModel = embeddingModel
        
        #The optimizationMode Setting 设置质量
        self.optimizationMode = optimizationMode
        
        #The focusMode Setting 设置搜索焦点
        self.focusMode = focusMode
    
    def searcherStrart(self, query, history=None):
        #Processing requests 处理请求
        if history is None:
            
            data = {
                "chatModel": {
                    "provider": self.chatModelProvider,
                    "model": self.chatModel
                },
                "embeddingModel": {
                    "provider": self.embeddingModelProvider,
                    "model": self.embeddingModel
                },
                "optimizationMode": self.optimizationMode,
                "focusMode": self.focusMode,
                "query": query,
            }
            
        else:
            data = {
                "chatModel": {
                    "provider": self.chatModelProvider,
                    "model": self.chatModel
                },
                "embeddingModel": {
                    "provider": self.embeddingModelProvider,
                    "model": self.embeddingModel
                },
                "optimizationMode": self.optimizationMode,
                "focusMode": self.focusMode,
                "query": query,
                history: history
            }

        response = requests.post(self.url, json=data) #Send the request 发送请求
        
        if response.status_code == 200:

            result = response.json()
            message = result['message'] #Get the message 获取消息
            source = result['sources'] #Get the source 获取来源
            return message,source #Return the message and source 返回消息和来源

        else:
            print(f"Error: Received status code {response.status_code}") #Print the error code 打印错误代码
            print(response.text) #Print the error message 打印错误消息
            return None,None

if __name__ == "__main__":
    url = "http://localhost:3001/api/search"
    chatModel_provider = "ollama"
    chatModel_model = "deepseek-r1:1.5b"
    embeddingModel_provider = "ollama"
    embeddingModel_model = "deepseek-r1:1.5b"
    optimizationMode = "speed"
    focusMode = "webSearch" #webSearch, academicSearch, writingAssistant, wolframAlphaSearch, youtubeSearch, redditSearch.

    perplexica = Perplexica(url, chatModel_provider, chatModel_model, embeddingModel_provider, embeddingModel_model, optimizationMode, focusMode)
    query = "What is the Perplexica?"
    message, source = perplexica.searcherStrart(query)
    print(message)
# llama-index-simple-app

这个仓库提供了一个使用 LlamaIndex 和本地模型的入门级示例。LlamaIndex 是一个强大的工具，用于使用大型语言模型构建搜索索引和查询引擎。此示例演示了如何加载文档、设置本地嵌入模型和 LLM、创建索引以及执行查询。

此外，这个仓库还包括了使用自定义嵌入模型的说明。要开始使用：

1. 将 Hugging Face 嵌入模型仓库下载到本项目根目录。
2. 修改 `main.py` 文件，更新嵌入模型的路径。
3. 使用 Ollama 后台运行 `llama2-chinese` 模型。
4. 安装所需的包后，直接运行 `python main.py`。

这个设置将允许您在 LlamaIndex 应用程序中使用自定义中文语言模型进行嵌入和查询。`main.py` 中提供的示例将指导您完成设置索引和针对索引文档执行查询的过程。

## 特性

- 从指定目录加载文档。
- 使用 LlamaIndex 设置本地嵌入模型和 LLM。
- 从加载的文档创建索引。
- 在循环中执行查询并获得答案。

## 使用方法

1. 克隆仓库到本地机器。
2. 按照上述说明设置自定义嵌入模型。
3. 将您的文档放在 `data` 文件夹中。
4. 运行 `main.py` 以启动交互式查询循环。
5. 在提示符下输入您的问题，或输入 `exit` 以终止程序。

## 要求

- Python 3.x
- 所需的包（使用 `pip install -r requirements.txt` 安装）
- LlamaIndex 和 Ollama 模型（参考 LlamaIndex 文档以获取设置说明）
- 运行 `llama2-chinese` 模型的 Ollama 后台服务

## 贡献

欢迎贡献！请阅读 CONTRIBUTING.md 文件以获取如何为这个项目做出贡献的指导。

## 许可证

这个项目使用 MIT 许可证 - 详情请查看 LICENSE.md 文件。

REACT_PROMPT = """
{instructions}
TOOLS:
------

你可以使用以下工具：
{tools}
使用工具时，请使用以下格式
```
思考：我需要使用工具吗？{yes_or_no}
行动：要采取的行动，必须是{tool_name}其中之一
行动输入：该行动的输入参数
观察：行动的结果
```

当你有要回复给用户的内容，或者你不需要使用工具时，你必须使用以下格式：
```
思考：我需要使用工具吗？否
最终答案：[你的回复内容]
```


开始！

新的输入: {input}
{agent_scratchpad}

"""
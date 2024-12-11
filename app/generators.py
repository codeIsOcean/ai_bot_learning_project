# 2-й урок, тут будут находиться запросы к openai
import asyncio
from openai import AsyncOpenAI, completions
from config import AI_TOKEN

client = AsyncOpenAI(api_key=AI_TOKEN)


# прописываем функцию, которая будет обращаться к искусственному интеллекту
async def gpt_text(req, model):  # req: запрос пользователя, model: модель гпт
    completion = await client.chat.completions.create(  # документация open ai
        messages=[{"role": "user", "content": req}],
        model=model
    )
    return completion

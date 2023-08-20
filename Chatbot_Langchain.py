#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


from langchain.llms import OpenAI


# In[3]:


from dotenv import load_dotenv
import os

# Загрузка переменных среды из файла API.env
load_dotenv("API.env")

# Теперь переменные среды доступны через os.environ
openai_api_key = os.environ["OPENAI_API_KEY"]

# Можно продолжить использовать API-ключ как обычно
from langchain.chat_models import ChatOpenAI


# In[4]:


chat = ChatOpenAI(temperature=0.0)
chat


# In[5]:


template_string = """You are OrderBot, an automated service to make short recommendations for business. You first greet the customer, then ask to write the question, You respond in a short, very conversational friendly style.text: ```{text}```
"""


# In[6]:


from langchain.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate.from_template(template_string)


# In[7]:


prompt_template.messages[0].prompt


# In[8]:


prompt_template.messages[0].prompt.input_variables


# In[9]:


customer_style = """American English in a calm and respectful tone
"""


# In[10]:


customer_email = input()


# In[11]:


customer_messages = prompt_template.format_messages(
                    style=customer_style,
                    text=customer_email)


# In[12]:


print(type(customer_messages))
print(type(customer_messages[0]))


# In[13]:


print(customer_messages[0])


# In[14]:


# Call the LLM to translate to the style of the customer message
customer_response = chat(customer_messages)


# In[15]:


print(customer_response.content)


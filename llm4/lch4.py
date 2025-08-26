from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from MyLCH import getOpenAI, getGenAI

if __name__ == '__main__':
    openllm = getOpenAI()
    genllm = getGenAI()

    tools = load_tools(['wikipedia'], llm=openllm)

    agent = initialize_agent(
        tools=tools,
        llm=openllm,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=False
    )

    txt = "영화 [좀비딸]의 주연이 누구야? 2025년 8월25일 기준으로 개봉 이후 몇개월이 지났어? 한국어로 답해줘"
    print(agent.invoke(txt))
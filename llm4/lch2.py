from langchain.model_laboratory import ModelLaboratory
from MyLCH import getOpenAI, getGenAI

if __name__ == '__main__':
    openllm = getOpenAI()
    genllm = getGenAI()

    model_lab = ModelLaboratory.from_llms( [openllm, genllm] )
    model_lab.compare("영화 [좀비딸]의 주연이 누구야? 2025년 8월25일 기준으로 개봉 이후 몇개월이 지났어? 한국어로 답해줘")
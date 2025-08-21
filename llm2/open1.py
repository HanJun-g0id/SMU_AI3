from myllm.MyApi import openAiModelArg, makeMsg


def test(prompt):
    modelName = "gpt-4o"
    msg = makeMsg("너는 무서운 한국어 선생님 스타일로 대답해줘 ",prompt)
    result = openAiModelArg(modelName, msg)
    print(result)

if __name__ == '__main__':
    prompt = "우간다의 수도가 어디야"
    test(prompt)
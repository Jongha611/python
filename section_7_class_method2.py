# 제미니 씨가 제안한 예제 풀어보기

class AIModel:
    def __init__(self, name: str | None = None, parameters: str | None = None):
        self.name = name
        self.parameters = parameters
        self.status = "ready"
        
    def __repr__(self):
        return (
            f"이 모델의 이름은 {self.name}이고, "
            f"크기는 {self.parameters}, "
            f"현재 상태는 {self.status} 입니다."
        )
    
    def tune(self, parameters: str | None = None):
        if parameters is not None:
            self.parameters = parameters
            
        
class LanguageModel(AIModel):
    def __init__(self, name: str | None = None, parameters: str | None = None, dataset_size: str | None = None):
        super().__init__(name, parameters)
        self.dataset_size = dataset_size
        
    def __repr__(self):
        return (
            f"{super().__repr__()[:-4]}이고, "
            f"학습 데이터셋 크기는 {self.dataset_size} 입니다."
        )
    
    @classmethod
    def create_gpt_v1(cls):
        return cls(
            name="GPT-1",
            parameters="117M",
            dataset_size="4.5GB"
        )
        
        
gptv1 = LanguageModel.create_gpt_v1()     
print(gptv1)

gptv1.tune(parameters="150M")
print(gptv1)

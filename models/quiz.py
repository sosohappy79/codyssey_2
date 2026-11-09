class Quiz:
    """문제, 선택지, 정답, 힌트를 보관하는 개별 퀴즈 클래스입니다."""

    def __init__(self, question, choices, answer, hint="힌트가 없습니다."):
        self.question = str(question).strip()
        self.choices = [str(choice).strip() for choice in choices]
        self.answer = int(answer)
        self.hint = str(hint).strip()
        self._validate()

    def _validate(self):
        if not self.question:
            raise ValueError("문제 내용은 비워 둘 수 없습니다.")
        if len(self.choices) != 4:
            raise ValueError("선택지는 반드시 4개여야 합니다.")
        if any(not choice for choice in self.choices):
            raise ValueError("선택지 내용은 비워 둘 수 없습니다.")
        if self.answer not in (1, 2, 3, 4):
            raise ValueError("정답 번호는 1-4 중 하나여야 합니다.")
        if not self.hint:
            self.hint = "힌트가 없습니다."

    def display(self, number=None):
        if number is not None:
            print(f"\n[문제 {number}]")
        print(self.question)
        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")

    def is_correct(self, user_answer):
        return user_answer == self.answer

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            question=data["question"],
            choices=data["choices"],
            answer=data["answer"],
            hint=data.get("hint", "힌트가 없습니다."),
        )

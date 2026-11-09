from models.quiz import Quiz


class QuizGame:
    """퀴즈 게임의 실행과 메뉴를 담당하는 클래스입니다."""

    def __init__(self):
        self.quizzes = self._create_default_quizzes()
        self.best_score = None
        self.best_correct = 0
        self.best_total = 0

    @staticmethod
    def _create_default_quizzes():
        """Python 기초 및 프로그래밍 상식 주제의 기본 문제 10개를 생성합니다."""
        quiz_data = [
            (
                "Python 프로그래밍 언어를 처음 만든 사람은 누구인가요?",
                ["귀도 반 로섬", "제임스 고슬링", "브렌던 아이크", "데니스 리치"],
                1,
                "Python의 창시자로 잘 알려진 네덜란드 출신 개발자입니다.",
            ),
            (
                "Python에서 input() 함수가 기본적으로 반환하는 자료형은 무엇인가요?",
                ["int", "str", "bool", "list"],
                2,
                "사용자가 입력한 값은 숫자처럼 보여도 우선 문자 데이터로 전달됩니다.",
            ),
            (
                "여러 값을 순서대로 저장하고, 값을 변경할 수 있는 자료형은 무엇인가요?",
                ["tuple", "set", "list", "bool"],
                3,
                "대괄호 []를 사용해 만드는 대표적인 자료형입니다.",
            ),
            (
                "Python의 dict 자료형은 어떤 형태로 데이터를 저장하나요?",
                ["값만 저장", "키와 값의 쌍", "문자만 저장", "참/거짓만 저장"],
                2,
                "사전에서 단어와 뜻을 연결하는 방식과 비슷합니다.",
            ),
            (
                "len() 함수의 역할로 알맞은 것은 무엇인가요?",
                ["요소의 개수 확인", "자료형 변환", "화면 출력", "파일 삭제"],
                1,
                "문자열이나 리스트 등에 몇 개의 요소가 있는지 확인할 때 사용합니다.",
            ),
            (
                "두 값이 같은지 비교할 때 사용하는 연산자는 무엇인가요?",
                ["=", "!=", ">=", "=="],
                4,
                "대입 연산자 =를 두 번 이어서 씁니다.",
            ),
            (
                "while 반복문은 일반적으로 어떤 조건에서 반복하나요?",
                ["조건이 거짓일 때만", "항상 한 번만", "조건이 참인 동안", "파일이 있을 때만"],
                3,
                "while 뒤에 작성한 조건식을 계속 검사합니다.",
            ),
            (
                "Python에서 함수를 정의할 때 사용하는 키워드는 무엇인가요?",
                ["def", "class", "return", "import"],
                1,
                "function을 줄여 쓴 것처럼 함수 정의의 시작에 사용합니다.",
            ),
            (
                "try/except 구문의 주된 사용 목적은 무엇인가요?",
                ["반복 실행", "오류 처리", "클래스 생성", "화면 꾸미기"],
                2,
                "예외가 발생할 수 있는 코드를 감싸고, 문제가 생겼을 때 실행할 동작을 작성합니다.",
            ),
            (
                "JSON 형식은 주로 어떤 목적으로 사용하나요?",
                ["이미지 편집", "음악 재생", "데이터 저장 및 교환", "화면 해상도 변경"],
                3,
                "객체와 배열 형태로 데이터를 표현하는 가벼운 텍스트 형식입니다.",
            ),
        ]
        return [Quiz(question, choices, answer, hint) for question, choices, answer, hint in quiz_data]

    def _show_menu(self):
        print("\n" + "=" * 40)
        print("          🎯 나만의 퀴즈 게임 🎯")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)

    def _read_menu_choice(self):
        while True:
            value = input("선택: ").strip()
            if not value:
                print("⚠️ 빈 입력입니다. 1-5 사이의 숫자를 입력하세요.")
                continue
            try:
                choice = int(value)
            except ValueError:
                print("⚠️ 숫자를 입력하세요.")
                continue
            if 1 <= choice <= 5:
                return choice
            print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")

    def run(self):
        while True:
            self._show_menu()
            choice = self._read_menu_choice()
            if choice == 5:
                print("퀴즈 게임을 종료합니다.")
                break
            print("선택한 기능은 다음 단계에서 구현합니다.")

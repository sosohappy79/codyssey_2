import random
from datetime import datetime

from models.quiz import Quiz


class QuizGame:
    """퀴즈 게임의 실행과 메뉴를 담당하는 클래스입니다."""

    def __init__(self):
        self.quizzes = self._create_default_quizzes()
        self.best_score = None
        self.best_correct = 0
        self.best_total = 0
        self.history = []

    @staticmethod
    def _create_default_quizzes():
        """Python 기초 및 프로그래밍 상식 주제의 기본 문제 10개를 생성합니다."""
        quiz_data = [
            ("Python 프로그래밍 언어를 처음 만든 사람은 누구인가요?", ["귀도 반 로섬", "제임스 고슬링", "브렌던 아이크", "데니스 리치"], 1, "Python의 창시자로 잘 알려진 네덜란드 출신 개발자입니다."),
            ("Python에서 input() 함수가 기본적으로 반환하는 자료형은 무엇인가요?", ["int", "str", "bool", "list"], 2, "사용자가 입력한 값은 숫자처럼 보여도 우선 문자 데이터로 전달됩니다."),
            ("여러 값을 순서대로 저장하고, 값을 변경할 수 있는 자료형은 무엇인가요?", ["tuple", "set", "list", "bool"], 3, "대괄호 []를 사용해 만드는 대표적인 자료형입니다."),
            ("Python의 dict 자료형은 어떤 형태로 데이터를 저장하나요?", ["값만 저장", "키와 값의 쌍", "문자만 저장", "참/거짓만 저장"], 2, "사전에서 단어와 뜻을 연결하는 방식과 비슷합니다."),
            ("len() 함수의 역할로 알맞은 것은 무엇인가요?", ["요소의 개수 확인", "자료형 변환", "화면 출력", "파일 삭제"], 1, "문자열이나 리스트 등에 몇 개의 요소가 있는지 확인할 때 사용합니다."),
            ("두 값이 같은지 비교할 때 사용하는 연산자는 무엇인가요?", ["=", "!=", ">=", "=="], 4, "대입 연산자 =를 두 번 이어서 씁니다."),
            ("while 반복문은 일반적으로 어떤 조건에서 반복하나요?", ["조건이 거짓일 때만", "항상 한 번만", "조건이 참인 동안", "파일이 있을 때만"], 3, "while 뒤에 작성한 조건식을 계속 검사합니다."),
            ("Python에서 함수를 정의할 때 사용하는 키워드는 무엇인가요?", ["def", "class", "return", "import"], 1, "function을 줄여 쓴 것처럼 함수 정의의 시작에 사용합니다."),
            ("try/except 구문의 주된 사용 목적은 무엇인가요?", ["반복 실행", "오류 처리", "클래스 생성", "화면 꾸미기"], 2, "예외가 발생할 수 있는 코드를 감싸고, 문제가 생겼을 때 실행할 동작을 작성합니다."),
            ("JSON 형식은 주로 어떤 목적으로 사용하나요?", ["이미지 편집", "음악 재생", "데이터 저장 및 교환", "화면 해상도 변경"], 3, "객체와 배열 형태로 데이터를 표현하는 가벼운 텍스트 형식입니다."),
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
        print("5. 퀴즈 삭제")
        print("6. 점수 기록 히스토리")
        print("7. 종료")
        print("=" * 40)

    def _read_menu_choice(self):
        while True:
            value = input("선택: ").strip()
            if not value:
                print("⚠️ 빈 입력입니다. 1-7 사이의 숫자를 입력하세요.")
                continue
            try:
                choice = int(value)
            except ValueError:
                print("⚠️ 숫자를 입력하세요.")
                continue
            if 1 <= choice <= 7:
                return choice
            print("⚠️ 잘못된 입력입니다. 1-7 사이의 숫자를 입력하세요.")

    def _read_number(self, prompt, minimum, maximum):
        while True:
            value = input(prompt).strip()
            if not value:
                print("⚠️ 빈 입력입니다. 숫자를 입력하세요.")
                continue
            try:
                number = int(value)
            except ValueError:
                print("⚠️ 숫자만 입력할 수 있습니다.")
                continue
            if minimum <= number <= maximum:
                return number
            print(f"⚠️ {minimum}-{maximum} 사이의 숫자를 입력하세요.")

    def _read_answer(self, quiz):
        hint_used = False
        while True:
            value = input("정답 입력 (1-4, 힌트는 h): ").strip().lower()
            if not value:
                print("⚠️ 빈 입력입니다. 정답 번호를 입력하세요.")
                continue
            if value == "h":
                if hint_used:
                    print("⚠️ 이 문제에서는 이미 힌트를 사용했습니다.")
                else:
                    print(f"💡 힌트: {quiz.hint}")
                    hint_used = True
                continue
            try:
                answer = int(value)
            except ValueError:
                print("⚠️ 1-4 숫자 또는 h를 입력하세요.")
                continue
            if answer not in (1, 2, 3, 4):
                print("⚠️ 정답 번호는 1-4 중 하나입니다.")
                continue
            return answer, hint_used

    def _read_non_empty(self, prompt):
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("⚠️ 빈 입력은 사용할 수 없습니다. 다시 입력하세요.")

    def show_quizzes(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 40)
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"[{number}] {quiz.question}")
        print("-" * 40)

    def delete_quiz(self):
        if not self.quizzes:
            print("삭제할 퀴즈가 없습니다.")
            return
        self.show_quizzes()
        quiz_number = self._read_number(
            f"삭제할 퀴즈 번호 (1-{len(self.quizzes)}, 취소는 0): ",
            0,
            len(self.quizzes),
        )
        if quiz_number == 0:
            print("퀴즈 삭제를 취소했습니다.")
            return
        while True:
            confirmation = input("정말 삭제할까요? (y/n): ").strip().lower()
            if confirmation in ("y", "n"):
                break
            print("⚠️ y 또는 n을 입력하세요.")
        if confirmation == "y":
            deleted = self.quizzes.pop(quiz_number - 1)
            print(f"✅ 퀴즈를 삭제했습니다: {deleted.question}")
        else:
            print("퀴즈 삭제를 취소했습니다.")

    def add_quiz(self):
        print("\n📌 새로운 퀴즈를 추가합니다.")
        question = self._read_non_empty("문제를 입력하세요: ")
        choices = []
        for number in range(1, 5):
            choices.append(self._read_non_empty(f"선택지 {number}: "))
        answer = self._read_number("정답 번호 (1-4): ", 1, 4)
        hint = self._read_non_empty("힌트를 입력하세요: ")

        try:
            quiz = Quiz(question, choices, answer, hint)
        except ValueError as error:
            print(f"⚠️ 퀴즈를 추가하지 못했습니다: {error}")
            return
        self.quizzes.append(quiz)
        print("✅ 퀴즈가 추가되었습니다!")

    def play_quiz(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가하세요.")
            return

        quiz_pool = self.quizzes.copy()
        random.shuffle(quiz_pool)
        question_count = self._read_number(
            f"몇 문제를 풀까요? (1-{len(quiz_pool)}): ", 1, len(quiz_pool)
        )
        selected_quizzes = quiz_pool[:question_count]
        correct_count = 0
        hint_count = 0

        print(f"\n📝 퀴즈를 시작합니다! (총 {question_count}문제)")
        for number, quiz in enumerate(selected_quizzes, start=1):
            print("-" * 40)
            quiz.display(number)
            user_answer, hint_used = self._read_answer(quiz)
            if hint_used:
                hint_count += 1
            if quiz.is_correct(user_answer):
                correct_count += 1
                print("✅ 정답입니다!")
            else:
                print(f"❌ 오답입니다. 정답은 {quiz.answer}번입니다.")

        base_score = round(correct_count / question_count * 100)
        score = max(0, base_score - hint_count * 10)
        print("\n" + "=" * 40)
        print(f"🏆 결과: {question_count}문제 중 {correct_count}문제 정답!")
        print(f"힌트 사용: {hint_count}회 / 최종 점수: {score}점")
        print("=" * 40)
        self._record_game_result(question_count, correct_count, hint_count, score)

    def _record_game_result(self, question_count, correct_count, hint_count, score):
        """게임 기록을 남기고 최고 점수를 갱신합니다."""
        self.history.append(
            {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "question_count": question_count,
                "correct_count": correct_count,
                "hint_count": hint_count,
                "score": score,
            }
        )
        if self.best_score is None or score > self.best_score:
            self.best_score = score
            self.best_correct = correct_count
            self.best_total = question_count
            print("🎉 새로운 최고 점수입니다!")

    def show_best_score(self):
        if self.best_score is None:
            print("아직 퀴즈를 푼 기록이 없습니다.")
            return
        print(
            f"🏆 최고 점수: {self.best_score}점 "
            f"({self.best_total}문제 중 {self.best_correct}문제 정답)"
        )

    def show_history(self):
        if not self.history:
            print("아직 저장된 게임 기록이 없습니다.")
            return
        print(f"\n📚 게임 기록 (총 {len(self.history)}회)")
        print("-" * 65)
        for number, record in enumerate(reversed(self.history), start=1):
            print(
                f"{number}. {record['date']} | "
                f"{record['question_count']}문제 | "
                f"정답 {record['correct_count']}개 | "
                f"힌트 {record['hint_count']}회 | {record['score']}점"
            )
        print("-" * 65)

    def run(self):
        while True:
            self._show_menu()
            choice = self._read_menu_choice()
            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.show_quizzes()
            elif choice == 4:
                self.show_best_score()
            elif choice == 5:
                self.delete_quiz()
            elif choice == 6:
                self.show_history()
            elif choice == 7:
                print("퀴즈 게임을 종료합니다.")
                break
            else:
                print("선택한 기능은 다음 단계에서 구현합니다.")

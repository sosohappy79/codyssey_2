class QuizGame:
    """퀴즈 게임의 실행과 메뉴를 담당하는 클래스입니다."""

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

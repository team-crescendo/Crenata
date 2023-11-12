class CrenataException(Exception):
    """
    모든 예외의 부모 클래스입니다.
    """

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)

class Strings:
    REGISTER_COMPLETED = "가입이 완료되었습니다."
    SUCCESSFUL_EDIT = "성공적으로 수정되었습니다."
    TIMETABLE_LOADING = "시간표를 가져오는 중 입니다."
    TIMETABLE_LOADED = "시간표를 가져왔습니다."

    USER_NOT_FOUND = "가입되지 않은 사용자입니다."
    DUPLICATE_USER = "이미 가입된 사용자입니다."
    MEAL_NAME_NOT_FOUND = (
        "해당하는 식사 명을 찾을 수 없습니다. 조식, 중식, 석식 중에 다시 선택해 주시길"
        " 바랍니다."
    )
    TIMETABLE_NOT_FOUND = "시간표가 없습니다."

    USER_CANCELLED = "취소되었습니다."
    VIEW_TIMEOUT = "시간 초과되었습니다."
    NEED_SCHOOL_REGISTER = "학교를 먼저 등록해 주시기 바랍니다."
    DATE_PARSE_ERROR = (
        "날짜를 잘못 입력했습니다. YYYYMMDD 형식, 또는 '내일'로 입력해 주시길 바랍니다."
        " 예: 20220110, 내일"
    )
    INTERACTION_LOCKED = (
        "다른 명령어을 사용 중일 때는 해당 명령어를 사용할 수 없습니다."
    )

    MUST_BE_GREATER_THAN_ZERO = "학년 또는 반은 0보다 커야합니다."
    NOT_INTERACTED_USER = "다른 사용자의 상호작용은 사용할 수 없습니다."
    NEED_GRADE_AND_ROOM_ARGUMENT = "학년과 반을 입력해야 합니다."
    SCHOOL_INFO_NOT_FOUND = "학교 정보를 찾을 수 없습니다. " + NEED_SCHOOL_REGISTER

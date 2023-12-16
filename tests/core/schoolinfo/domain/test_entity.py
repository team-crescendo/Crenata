from crenata.core.schoolinfo.domain.entity import SchoolInfo


def test_school_info():
    school_info = SchoolInfo(
        name="테스트 초등학교",
        grade=6,
        room=1,
        edu_office_code="J10",
        standard_school_code="1234567",
        department=None,
        major=None,
    )

    assert school_info.name == "테스트 초등학교"
    assert school_info.grade == 6
    assert school_info.room == 1
    assert school_info.edu_office_code == "J10"
    assert school_info.standard_school_code == "1234567"
    assert school_info.department == None
    assert school_info.major == None

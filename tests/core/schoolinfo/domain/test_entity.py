from crenata.core.schoolinfo.domain.entity import SchoolInfo


def test_schoolinfo():
    school_info = SchoolInfo(
        school_name="테스트 초등학교",
        grade=6,
        room=1,
        edu_office_code="J10",
        standard_school_code="1234567",
        ORD_SC_NM=None,
        DDDEP_NM=None,
    )

    assert school_info.school_name == "테스트 초등학교"
    assert school_info.grade == 6
    assert school_info.room == 1
    assert school_info.edu_office_code == "J10"
    assert school_info.standard_school_code == "1234567"
    assert school_info.ORD_SC_NM == None
    assert school_info.DDDEP_NM == None

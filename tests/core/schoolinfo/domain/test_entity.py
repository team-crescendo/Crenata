from crenata.core.schoolinfo.domain.entity import SchoolInfo


def test_schoolinfo():
    school_info = SchoolInfo(
        school_name="테스트 초등학교",
        grade=6,
        room=1,
        ATPT_OFCDC_SC_CODE="J10",
        SD_SCHUL_CODE="7011911",
        ORD_SC_NM=None,
        DDDEP_NM=None,
    )

    assert school_info.school_name == "테스트 초등학교"
    assert school_info.grade == 6
    assert school_info.room == 1
    assert school_info.ATPT_OFCDC_SC_CODE == "J10"
    assert school_info.SD_SCHUL_CODE == "7011911"
    assert school_info.ORD_SC_NM == None
    assert school_info.DDDEP_NM == None

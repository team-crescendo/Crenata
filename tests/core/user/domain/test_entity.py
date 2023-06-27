from crenata.core.preferences.domain.entity import Preferences
from crenata.core.schoolinfo.domain.entity import SchoolInfo
from crenata.core.user.domain.entity import User


def test_user():
    preferences = Preferences(private=True, ephemeral=True)
    school_info = SchoolInfo(
        school_name="테스트 초등학교",
        grade=6,
        room=1,
        ATPT_OFCDC_SC_CODE="J10",
        SD_SCHUL_CODE="7011911",
        ORD_SC_NM=None,
        DDDEP_NM=None,
    )
    user = User(preferences=preferences, school_info=school_info)

    assert user.preferences.private == True
    assert user.preferences.ephemeral == True
    assert user.school_info.school_name == "테스트 초등학교"
    assert user.school_info.grade == 6
    assert user.school_info.room == 1
    assert user.school_info.ATPT_OFCDC_SC_CODE == "J10"
    assert user.school_info.SD_SCHUL_CODE == "7011911"
    assert user.school_info.ORD_SC_NM == None
    assert user.school_info.DDDEP_NM == None

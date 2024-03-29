from crenata.core.preferences.domain.entity import Preferences
from crenata.core.schoolinfo.domain.entity import SchoolInfo
from crenata.core.user.domain.entity import User


def test_user():
    preferences = Preferences(private=True, ephemeral=True)
    school_info = SchoolInfo(
        name="테스트 초등학교",
        grade=6,
        room=1,
        edu_office_code="J10",
        standard_school_code="7011911",
        department=None,
        major=None,
    )
    user = User(discord_id=123456789, preferences=preferences, school_info=school_info)

    assert user.discord_id == 123456789
    assert user.preferences.private == True
    assert user.preferences.ephemeral == True
    assert user.school_info
    assert user.school_info.name == "테스트 초등학교"
    assert user.school_info.grade == 6
    assert user.school_info.room == 1
    assert user.school_info.edu_office_code == "J10"
    assert user.school_info.standard_school_code == "7011911"
    assert user.school_info.department == None
    assert user.school_info.major == None

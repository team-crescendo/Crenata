from datetime import datetime

from crenata.core.school.domain.entity import School


def test_school():
    school = School(
        edu_office_code="J10",
        standard_school_code="1234567",
        name="테스트",
        english_name="test",
        kind="초등학교",
        coeducation="남녀공학",
        street_name_address="도로명주소",
        zip_code="12345",
        highschool_general_or_business="일반계고등학교",
        highschool_category="공업계고등학교",
        fax_number="02-1234-5678",
        telephone_number="02-1234-5678",
        homepage_address="http://test.com",
        founding_date=datetime(2021, 1, 1),
    )

    assert school.edu_office_code == "J10"
    assert school.standard_school_code == "1234567"
    assert school.name == "테스트"
    assert school.english_name == "test"
    assert school.kind == "초등학교"
    assert school.coeducation == "남녀공학"
    assert school.street_name_address == "도로명주소"
    assert school.zip_code == "12345"
    assert school.highschool_general_or_business == "일반계고등학교"
    assert school.highschool_category == "공업계고등학교"
    assert school.fax_number == "02-1234-5678"
    assert school.telephone_number == "02-1234-5678"
    assert school.homepage_address == "http://test.com"
    assert school.founding_date == datetime(2021, 1, 1)

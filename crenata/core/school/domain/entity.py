from dataclasses import dataclass
from datetime import datetime


@dataclass
class School:
    edu_office_code: str
    """시도교육청코드"""
    standard_school_code: str
    """표준학교코드"""

    name: str
    """학교명"""
    english_name: str
    """영문 학교명"""

    kind: str
    """학교종류명"""
    coeducation: str
    """남녀공학구분명"""

    street_name_address: str
    """도로명 주소"""
    zip_code: str
    """우편번호"""

    highschool_general_or_business: str
    """고등학교일반실업구분명"""
    highschool_category: str
    """고등학교구분명"""

    fax_number: str
    """팩스번호"""
    telephone_number: str
    """전화번호"""

    homepage_address: str
    """홈페이지 주소"""

    founding_date: datetime
    """설립일"""

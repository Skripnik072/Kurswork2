from unittest.mock import patch, MagicMock
from src.api_hh import HeadHunterAPI


def test_api_hh_load(vacancies):
    assert HeadHunterAPI.load_vacancies(vacancies,"Python") == {"items":[{"id":"93353083","premium":'false'}]}

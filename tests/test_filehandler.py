from src.filehandler import JSONSaver


def test_filehand_init(jsonsaver1):
    assert jsonsaver1.criteria == "Python Developer"
    assert jsonsaver1._JSONSaver__full_path == 'C:\\Users\\it-pc.ru\\PycharmProjects\\PythonPKW2\\tests\\data\\vacancie.json'
    assert jsonsaver1._JSONSaver__vacancies == []

from function import *
import pytest

class TestApp:
    def test_show_type_text(self):
        print('text:')
        show_type_of_text("Go until jurong point, crazy..")
        assert True

    def test_show_type_of_text(self):
        print('text:')
        show_type_of_text("FreeMsg Hey there darling it's been 3 week's now and no word back!", False)
        assert True

    def test_type(self):
        print('text: (give text and first word)')   
        give_type(type1='Yeah he got in at 2 and was v apologetic. ')
        assert True

    
    if __name__ == '__main__':
        print("run with 'pytest -v test_fungsi.py'")
        pytest.main

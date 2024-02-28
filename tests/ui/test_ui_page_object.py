from modules.ui.page_objects.sign_in_page import SignInPage
import pytest
import time



@pytest.mark.ui
def test_check_incorrect_username_page_object():
    sign_in_page = SignInPage()
    sign_in_page.go_to()
    sign_in_page.try_login("page_object@gmail.com", "wrong password")
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    

@pytest.mark.ui
def test_check_track_down_package():
    sign_in_page = SignInPage()
    sign_in_page.go_to_n()
    sign_in_page.enter_number_package("1")
    assert sign_in_page.check_title_n("Трекінг посилки | Nova Global") 
    
@pytest.mark.ui
def test_search_video_and_like():
    sign_in_page = SignInPage()
    sign_in_page.go_to_u()
    time.sleep(3)
    sign_in_page.search_video("гімн україни")
    time.sleep(3)
    current_url = sign_in_page.get_current_url()
    expected_url = "https://www.youtube.com/watch?v=Wx7vo__48oE"
    
    assert current_url == expected_url

    


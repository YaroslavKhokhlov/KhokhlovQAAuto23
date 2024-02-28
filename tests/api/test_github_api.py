import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 55
    assert 'become-qa-auto' in r['items'][0]['name'] 


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0
    

 
@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0

#Тест перевіряє наявність емоджі "fist" серед доступних на Гітхабі
@pytest.mark.api
def test_emojis_that_can_be_found(github_api):
    r = github_api.search_emojis ()
    emoji = "fist"
    assert emoji in r

#Тест перевіряє відстуність емоджі "yaroslav" серед досутпних на Гітхабі
@pytest.mark.api
def test_emojis_that_cant_be_found(github_api):
    r = github_api.search_emojis ()
    assert r.get ("yaroslav") is None


#Тест перевіряє, що для того, щоб заблокувати користувача необхідно бути авторизованим
@pytest.mark.api
def test_that_check_neceessary_of_authentication_to_block_user (github_api):
    username_to_block = "exp_user"
    user_r = github_api.user_block(username_to_block)
    assert user_r['message'] == 'Requires authentication'

#Тест, який перевіряє кількість можливих запитів, що залишились для неавтиризованих користувачів    
@pytest.mark.api
def test_limit_check (github_api):
    r = github_api.limit_check()
    assert r ["resources"]["core"]["remaining"] != 0
    
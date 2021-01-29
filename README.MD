# Code challenge
This project is a test automation challenge for [this Login page](https://financeiro.hostgator.com.br)  and its [CEP search web API](https://financeiro.hostgator.com.br/api/v3/checkout/cep/{CEP}). It uses Python, Pytest, Pipenv, Selenium and Chrome.

## Prerequisites
You must have Python, Git, Chrome browser and Chromedriver (for the respective version of Chrome)
installed on your system. Chromedriver must be on the path of your system and running configuration, 
depending on how you will run the tests.

## Getting started
Clone the repository and install the required dependencies with `pipenv install`.

## Running the tests
If running on a terminal, on the directory you cloned the project, first enter pipenv with `pipenv shell` 
and then run the tests with `python -m pytest` or `python -m pytest -v` to see the tests names.

If running with the -v argument, you should see something like this:

```
(hg-finance-app) marco@skynet:~/development/test_automation/hg-finance-app$ python -m pytest -v
============================================================================================== test session starts ===============================================================================================
platform linux -- Python 3.6.9, pytest-6.2.1, py-1.10.0, pluggy-0.13.1 -- /home/marco/.local/share/virtualenvs/hg-finance-app-fZ1UGZyO/bin/python
cachedir: .pytest_cache
rootdir: /home/marco/development/test_automation/hg-finance-app
plugins: bdd-4.0.2
collected 39 items                                                                                                                                                                                               

test/user_interface/steps_definitions/test_finance_app_feature.py::test_blank_email_and_blank_password PASSED                                                                                              [  2%]
test/user_interface/steps_definitions/test_finance_app_feature.py::test_valid_password_but_email_address_does_not_have__symbol PASSED                                                                      [  5%]
test/user_interface/steps_definitions/test_finance_app_feature.py::test_valid_password_but_email_address_is_blank_after__symbol PASSED                                                                     [  7%]
test/user_interface/steps_definitions/test_finance_app_feature.py::test_valid_email_but_password_is_not_typed PASSED                                                                                       [ 10%]
test/user_interface/steps_definitions/test_finance_app_feature.py::test_valid_email_but_password_is_invalid PASSED                                                                                         [ 12%]
test/user_interface/steps_definitions/test_finance_app_feature.py::test_valid_email_and_password_but_recaptcha_image_is_not_clicked_on PASSED                                                              [ 15%]
test/user_interface/steps_definitions/test_finance_app_feature.py::test_clicking_on_esqueceu_sua_senha_link PASSED                                                                                         [ 17%]
test/user_interface/steps_definitions/test_finance_app_feature.py::test_clicking_on_base_de_conhecimento_link PASSED                                                                                       [ 20%]
test/web_api/test_cep_search_api.py::TestGet::test_request_with_full_valid_cep[_test_data0] PASSED                                                                                                         [ 23%]
test/web_api/test_cep_search_api.py::TestGet::test_request_with_full_valid_cep[_test_data1] PASSED                                                                                                         [ 25%]
test/web_api/test_cep_search_api.py::TestGet::test_request_with_full_valid_cep[_test_data2] PASSED                                                                                                         [ 28%]
test/web_api/test_cep_search_api.py::TestGet::test_request_with_valid_cep_without_hyphen[_test_data0] PASSED                                                                                               [ 30%]
test/web_api/test_cep_search_api.py::TestGet::test_request_with_valid_cep_without_hyphen[_test_data1] PASSED                                                                                               [ 33%]
test/web_api/test_cep_search_api.py::TestGet::test_request_with_valid_cep_without_hyphen[_test_data2] PASSED                                                                                               [ 35%]
test/web_api/test_cep_search_api.py::TestGet::test_request_with_invalid_cep[_test_data0] PASSED                                                                                                            [ 38%]
test/web_api/test_cep_search_api.py::TestGet::test_request_with_invalid_cep[_test_data1] PASSED                                                                                                            [ 41%]
test/web_api/test_cep_search_api.py::TestGet::test_request_with_invalid_cep[_test_data2] PASSED                                                                                                            [ 43%]
test/web_api/test_cep_search_api.py::TestGet::test_request_with_invalid_cep[_test_data3] PASSED                                                                                                            [ 46%]
test/web_api/test_cep_search_api.py::TestGet::test_request_with_unexisting_cep[_test_data0] PASSED                                                                                                         [ 48%]
test/web_api/test_cep_search_api.py::TestGet::test_request_with_unexisting_cep[_test_data1] PASSED                                                                                                         [ 51%]
test/web_api/test_cep_search_api.py::TestGet::test_request_without_cep PASSED                                                                                                                              [ 53%]
test/web_api/test_cep_search_api.py::TestPost::test_request_with_full_valid_cep[88036-000] PASSED                                                                                                          [ 56%]
test/web_api/test_cep_search_api.py::TestPost::test_request_with_full_valid_cep[70165-900] PASSED                                                                                                          [ 58%]
test/web_api/test_cep_search_api.py::TestPost::test_request_with_full_valid_cep[68980-000] PASSED                                                                                                          [ 61%]
test/web_api/test_cep_search_api.py::TestPut::test_request_with_full_valid_cep[88036-000] PASSED                                                                                                           [ 64%]
test/web_api/test_cep_search_api.py::TestPut::test_request_with_full_valid_cep[70165-900] PASSED                                                                                                           [ 66%]
test/web_api/test_cep_search_api.py::TestPut::test_request_with_full_valid_cep[68980-000] PASSED                                                                                                           [ 69%]
test/web_api/test_cep_search_api.py::TestDelete::test_request_with_full_valid_cep[88036-000] PASSED                                                                                                        [ 71%]
test/web_api/test_cep_search_api.py::TestDelete::test_request_with_full_valid_cep[70165-900] PASSED                                                                                                        [ 74%]
test/web_api/test_cep_search_api.py::TestDelete::test_request_with_full_valid_cep[68980-000] PASSED                                                                                                        [ 76%]
test/web_api/test_cep_search_api.py::TestOptions::test_request_with_full_valid_cep[88036-000] PASSED                                                                                                       [ 79%]
test/web_api/test_cep_search_api.py::TestOptions::test_request_with_full_valid_cep[70165-900] PASSED                                                                                                       [ 82%]
test/web_api/test_cep_search_api.py::TestOptions::test_request_with_full_valid_cep[68980-000] PASSED                                                                                                       [ 84%]
test/web_api/test_cep_search_api.py::TestPatch::test_request_with_full_valid_cep[88036-000] PASSED                                                                                                         [ 87%]
test/web_api/test_cep_search_api.py::TestPatch::test_request_with_full_valid_cep[70165-900] PASSED                                                                                                         [ 89%]
test/web_api/test_cep_search_api.py::TestPatch::test_request_with_full_valid_cep[68980-000] PASSED                                                                                                         [ 92%]
test/web_api/test_cep_search_api.py::TestHead::test_request_with_full_valid_cep[88036-000] PASSED                                                                                                          [ 94%]
test/web_api/test_cep_search_api.py::TestHead::test_request_with_full_valid_cep[70165-900] PASSED                                                                                                          [ 97%]
test/web_api/test_cep_search_api.py::TestHead::test_request_with_full_valid_cep[68980-000] PASSED                                                                                                          [100%]
==================================================================================== 39 passed, 1 warning in 72.01s (0:01:12) ====================================================================================
```
### Scenarios
As requested on the code challenge document, these tests are broken down on user interface BDD tests and web API tests.
All possible scenarios found were covered. The user interface tests were designed to run with Selenium. 
They follow the Page Object Model to separate web element interactions
from the step definitions, what increases readability, maintainability and scalability. Most tests are negative as no 
valid user is available at this point. The web API tests use different sets of data to test the expected outcomes, based
on the information available.

## Built With

* [Python](https://www.python.org/) - Programming language
* [Pytest](https://docs.pytest.org/) - Test automation framework
* [Pipenv](https://pypi.org/project/pipenv/) - Dependency and virtual environment management
* [Selenium](https://www.selenium.dev/) - Browser automation

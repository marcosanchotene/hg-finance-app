import pytest
import requests

from resources import cep_search_api_test_data as test_data

URL = "https://financeiro.hostgator.com.br/api/v3/checkout/cep/"


class TestGet:

    @pytest.mark.parametrize("_test_data", test_data.get_valid_data)
    def test_request_with_full_valid_cep(self, _test_data):
        response = requests.get(URL + _test_data["get"])
        assert response.status_code == _test_data["http_status_code"]
        response_body = response.json()
        assert response_body["success"] is _test_data["success"]
        assert response_body["internal_code"] == _test_data["internal_code"]
        assert response_body["data"]["address1"] == _test_data["data"]["address1"]
        assert response_body["data"]["address2"] == _test_data["data"]["address2"]
        assert response_body["data"]["city"] == _test_data["data"]["city"]
        assert response_body["data"]["state"] == _test_data["data"]["state"]
        assert response_body["data"]["postCode"] == _test_data["data"]["postCode"]
        assert response_body["notifications"] == _test_data["notifications"]

    @pytest.mark.parametrize("_test_data", test_data.get_valid_data)
    def test_request_with_valid_cep_without_hyphen(self, _test_data):
        response = requests.get(URL + _test_data["data"]["postCode"])
        assert response.status_code == _test_data["http_status_code"]
        response_body = response.json()
        assert response_body["success"] is _test_data["success"]
        assert response_body["internal_code"] == _test_data["internal_code"]
        assert response_body["data"]["address1"] == _test_data["data"]["address1"]
        assert response_body["data"]["address2"] == _test_data["data"]["address2"]
        assert response_body["data"]["city"] == _test_data["data"]["city"]
        assert response_body["data"]["state"] == _test_data["data"]["state"]
        assert response_body["data"]["postCode"] == _test_data["data"]["postCode"]
        assert response_body["notifications"] == _test_data["notifications"]

    @pytest.mark.parametrize("_test_data", test_data.get_invalid_ceps)
    def test_request_with_invalid_cep(self, _test_data):
        response = requests.get(URL + _test_data["get"])
        assert response.status_code == _test_data["http_status_code"]
        response_body = response.json()
        assert response_body["success"] is _test_data["success"]
        assert response_body["internal_code"] == _test_data["internal_code"]
        assert response_body["data"] == _test_data["data"]
        assert response_body["notifications"] == _test_data["notifications"]

    @pytest.mark.parametrize("_test_data", test_data.get_unexisting_ceps)
    def test_request_with_unexisting_cep(self, _test_data):
        response = requests.get(URL + _test_data["get"])
        assert response.status_code == _test_data["http_status_code"]
        response_body = response.json()
        assert response_body["success"] is _test_data["success"]
        assert response_body["internal_code"] == _test_data["internal_code"]
        assert response_body["data"] == _test_data["data"]
        assert response_body["notifications"] == _test_data["notifications"]

    def test_request_without_cep(self):
        response = requests.get(URL + "")
        assert response.status_code == 405


class TestPost:

    @pytest.mark.parametrize("_test_data", test_data.other_valid_data)
    def test_request_with_full_valid_cep(self, _test_data):
        response = requests.post(URL + _test_data, "test")
        assert response.status_code == 405


class TestPut:

    @pytest.mark.parametrize("_test_data", test_data.other_valid_data)
    def test_request_with_full_valid_cep(self, _test_data):
        response = requests.put(URL + _test_data, "test")
        assert response.status_code == 405


class TestDelete:

    @pytest.mark.parametrize("_test_data", test_data.other_valid_data)
    def test_request_with_full_valid_cep(self, _test_data):
        response = requests.delete(URL + _test_data)
        assert response.status_code == 405


class TestOptions:

    @pytest.mark.parametrize("_test_data", test_data.other_valid_data)
    def test_request_with_full_valid_cep(self, _test_data):
        response = requests.options(URL + _test_data)
        assert response.status_code == 200


class TestPatch:

    @pytest.mark.parametrize("_test_data", test_data.other_valid_data)
    def test_request_with_full_valid_cep(self, _test_data):
        response = requests.patch(URL + _test_data, "test")
        assert response.status_code == 405


class TestHead:

    @pytest.mark.parametrize("_test_data", test_data.other_valid_data)
    def test_request_with_full_valid_cep(self, _test_data):
        response = requests.head(URL + _test_data)
        assert response.status_code == 200

from rest_framework.test import APITestCase

class ActionTest(APITestCase):

    def test_main(self):
        self.action_test()
        
        
    def action_test(self):
        
        url = "/action"
        response = self.client.get(url)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()["message"])

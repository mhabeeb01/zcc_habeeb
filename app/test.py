


try : 
    from routes import app
    import unittest

except Exception as e: 
    print("Some modules are missing {} ".format(e))


    class FlaskTest(unittest.TestCase):

        # Check for response 200
        def test_index(self):
            tester = app.test_client(self)
            response = tester.get("/fo")
            statuscode = response.status_code
            self.assertEqual(statuscode, 200)

        def test_index_content(self):
            tester = app.test_client(self)
            response = tester.get("/fo")
            self.assertEqual(response.content_type, "application/json")

        def test_index_data(self):
            tester = app.test_client(self)
            response = tester.get("/fo")
            self.assertTrue(b'Message' in response.data)

            
        if __name__ == "__main__":
            unittest.main()


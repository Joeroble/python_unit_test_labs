

""" TODO create a test case to test the following functions,

generate_url_for_question
 - check that the expected URL is returned for an example question. 

extract_answer_from_response
 - one test should create some example dictionaries that match the expected response from the API,
 and check that the correct answer is extracted and returned.
 - another test should create example dictionaries with a different structure to the one returned from the API, 
 and check that the function returns None. 

 TODO to think about - what else could you test about this program? 
 What types of expected and unexpected behavior might happen? You may be able to write tests for some 
 of your ideas now. We'll talk about ways to test other aspects of this program in class.

"""
import unittest
import functions_magic

class TestMagic8Ball(unittest.TestCase):

    def test_check_url_for_question(self):
       test_question = 'Is this question false?' 
       expected_generated_url = f'https://8ball.delegator.com/magic/JSON/{test_question}' 
       test_8_ball_url = functions_magic.generate_url_for_question(test_question)
       self.assertEqual(test_8_ball_url, expected_generated_url)

    def test_expected_response(self):
        test_question = 'Is this question false?' 
        expected_generated_url = f'https://8ball.delegator.com/magic/JSON/{test_question}' 
        response = functions_magic.make_request_to_magic_8_ball(expected_generated_url)
        extract_response = functions_magic.extract_answer_from_response(response)
        expected_respone_form  = {'magic':{'question': '', 'answer' : extract_response, 'type': ''}}
        self.assertEqual(expected_respone_form['magic']['answer'], extract_response)

    def test_dictionary_form_wrong_response(self): 
        response = {'toad': 'toads', 'wrong' : 'wrong_things'}
        extract_response = functions_magic.extract_answer_from_response(response)
        self.assertEqual(None, extract_response)
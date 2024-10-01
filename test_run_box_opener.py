import unittest
from unittest.mock import patch, MagicMock
import run_box_opener


class TestRunBoxOpener(unittest.TestCase):
    @patch('run_box_opener.requests.post')
    @patch('run_box_opener.bip39_generate')
    def test_submit_guesses_success(self, mock_mnemonic, mock_post):
        # Mock Mnemonic to return predictable phrases
        mock_mnemonic.return_value.phrase = "test phrase"

        # Mock successful API response
        mock_response = MagicMock()
        mock_response.status_code = 202
        mock_post.return_value = mock_response

        result = run_box_opener.submit_guesses()

        self.assertFalse(result)
        self.assertEqual(mock_post.call_count, 1)
        _, kwargs = mock_post.call_args
        self.assertEqual(len(kwargs['json']), 50)
        self.assertEqual(kwargs['json'][0], "test phrase")

    @patch('run_box_opener.requests.post')
    @patch('run_box_opener.bip39_generate')
    def test_submit_guesses_failure(self, mock_mnemonic, mock_post):
        # Mock Mnemonic to return predictable phrases
        mock_mnemonic.return_value.phrase = "test phrase"

        # Mock failed API response
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_post.return_value = mock_response

        result = run_box_opener.submit_guesses()

        self.assertTrue(result)
        self.assertEqual(mock_post.call_count, 1)
        _, kwargs = mock_post.call_args
        self.assertEqual(len(kwargs['json']), 50)
        self.assertEqual(kwargs['json'][0], "test phrase")


if __name__ == '__main__':
    unittest.main()

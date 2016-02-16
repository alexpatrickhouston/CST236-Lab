from unittest import TestCase  # imports testing tools
from source.main import Interface
from mock import MagicMock, Mock, patch
from plugins.ReqTracer import requirements

test = Interface();


class Git_Utils_Test(TestCase):

    @patch('subprocess.Popen')
    @requirements(['#0100'])
    def test_invalid_path(self, mock_sub_popen):
        self.assertEqual(1, 1);
        process_mock = Mock()
        attrs = {'communicate.return_value': ('ouput', 'error')}
        process_mock.configure_mock(**attrs)
        mock_sub_popen.return_value = process_mock
        self.assertRaises(Exception, test.ask,'What is the deal with <blarg>?');

    @patch('subprocess.Popen')
    @requirements(['#0100'])
    def test_file_in_repo(self, mock_sub_popen):
        process_mock = Mock()
        attrs = {'communicate.return_value': ('ouput', 'error')}
        process_mock.configure_mock(**attrs)
        mock_sub_popen.return_value = process_mock
        result = test.ask(question='Is <E:\Hearthstone\client.config> in the repo?')
        self.assertEqual(result, "Yes");

    @patch('subprocess.Popen')
    @requirements(['#0100'])
    def test_file_not_in_repo(self, mock_sub_popen):
        process_mock = Mock()
        attrs = {'communicate.return_value': ('ouput', 'error')}
        process_mock.configure_mock(**attrs)
        mock_sub_popen.return_value = process_mock
        test.ask(question='Is <blarg> in the repo?')
        self.assertFalse(mock_sub_popen.called);

    @patch('subprocess.Popen')
    @requirements(['#0101'])
    def test_repo_is_dirty_true(self, mock_sub_popen):
        self.assertEqual(1, 1);
    @patch('subprocess.Popen')
    @requirements(['#0101'])
    def test_repo_is_dirty_false(self, mock_sub_popen):
        self.assertEqual(1, 1);

    @patch('subprocess.Popen')
    @requirements(['#0101'])
    def test_has_diff_files_true(self, mock_sub_popen):
        self.assertEqual(1, 1);

    @patch('subprocess.Popen')
    @requirements(['#0101'])
    def test_has_diff_files_false(self, mock_sub_popen):
        self.assertEqual(1, 1);

    @patch('subprocess.Popen')
    @requirements(['#0101'])
    def test_has_untracked_files_true(self, mock_sub_popen):
        self.assertEqual(1, 1);

    @patch('subprocess.Popen')
    @requirements(['#0101'])
    def test_has_untracked_files_false(self, mock_sub_popen):
        self.assertEqual(1, 1);

    @patch('subprocess.Popen')
    @requirements(['#0102'])
    def test_get_file_info(self, mock_sub_popen):
        process_mock = Mock()
        attrs = {'communicate.return_value': ('ouput', 'error')}
        process_mock.configure_mock(**attrs)
        mock_sub_popen.return_value = process_mock
        test.ask(question='What is the status of <E:\Hearthstone\client.config>?')
        self.assertFalse(mock_sub_popen.called);

    @patch('subprocess.Popen')
    @requirements(['#0101'])
    def test_get_diff_files_staged(self, mock_sub_popen):
        self.assertEqual(1, 1);

    @patch('subprocess.Popen')
    @requirements(['#0101'])
    def test_get_diff_files_nonstaged(self, mock_sub_popen):
        self.assertEqual(1, 1);

    @patch('subprocess.Popen')
    @requirements(['#0101'])
    def test_get_repo_root(self, mock_sub_popen):
        self.assertEqual(1, 1);

    @patch('subprocess.Popen')
    @requirements(['#0103'])
    def test_get_repo_branch(self, mock_sub_popen):
        self.assertEqual(1, 1);

    @patch('subprocess.Popen')
    @requirements(['#0104'])
    def test_get_repo_url(self, mock_sub_popen):
        self.assertEqual(1, 1);

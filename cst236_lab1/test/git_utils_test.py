from unittest import TestCase  # imports testing tools
from source.main import Interface
from source import  main
from source.git_utils import get_repo_root, is_repo_dirty, has_diff_files, \
    has_untracked_files, get_diff_files, get_git_file_info,get_untracked_files, is_file_in_repo
from mock import MagicMock, Mock, patch
from plugins.ReqTracer import requirements
import os

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
        self.assertRaises(Exception, test.ask, 'What is the deal with <blarg>?');

    @patch('subprocess.Popen')
    @requirements(['#0100'])
    def test_file_in_repo(self, mock_sub_popen):
        process_mock = Mock()
        attrs = {'communicate.return_value': ('ouput', 'error')}
        process_mock.configure_mock(**attrs)
        mock_sub_popen.return_value = process_mock
        result = test.ask(question='Is <requirements.txt> in the repo?')
        self.assertTrue(mock_sub_popen.called);

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
    @requirements(['#0102'])
    def test_get_file_info(self, mock_sub_popen):
        process_mock = Mock()
        attrs = {'communicate.return_value': ('ouput', 'error')}
        process_mock.configure_mock(**attrs)
        mock_sub_popen.return_value = process_mock
        test.ask(question='What is the status of <requirements.txt>?')
        self.assertTrue(mock_sub_popen.called);

    @patch('subprocess.Popen')
    @requirements(['#0101'])
    def test_what_is_deal_valid(self, mock_sub_popen):
        process_mock = Mock()
        attrs = {'communicate.return_value': ('ouput', 'error')}
        process_mock.configure_mock(**attrs)
        mock_sub_popen.return_value = process_mock
        test.ask(question='What is the deal with <requirements.txt>?');
        self.assertTrue(mock_sub_popen.called);

    @patch('subprocess.Popen')
    @requirements(['#0103'])
    def test_get_repo_branch(self, mock_sub_popen):
        process_mock = Mock()
        attrs = {'communicate.return_value': ('ouput', 'error')}
        process_mock.configure_mock(**attrs)
        mock_sub_popen.return_value = process_mock
        test.ask(question='What branch is <test\main_test.py>?')
        self.assertTrue(mock_sub_popen.called);

    @patch('subprocess.Popen')
    @requirements(['#0103'])
    def test_in_repo(self, mock_sub_popen):
        process_mock = Mock()
        attrs = {'communicate.return_value': ('ouput', 'error')}
        process_mock.configure_mock(**attrs)
        mock_sub_popen.return_value = process_mock
        test.ask(question='Is <requirements.txt> in the repo?')
        self.assertTrue(mock_sub_popen.called);

    @patch('subprocess.Popen')
    @requirements(['#0104'])
    def test_get_repo_url(self, mock_sub_popen):
        process_mock = Mock()
        attrs = {'communicate.return_value': ('ouput', 'error')}
        process_mock.configure_mock(**attrs)
        mock_sub_popen.return_value = process_mock
        test.ask(question='Where did <Job_Story_Traces.txt> come from?')
        self.assertTrue(mock_sub_popen.called);

    @patch('subprocess.Popen')
    @requirements(['#0104'])
    def test_in_repo_changed(self, mock_sub_popen):
        process_mock = Mock()
        attrs = {'communicate.return_value': ('ouput', 'error')}
        process_mock.configure_mock(**attrs)
        mock_sub_popen.return_value = process_mock
        test.ask(question='What is the status of <requirements.txt>?')
        self.assertTrue(mock_sub_popen.called);

    @patch('subprocess.Popen')
    @requirements(['#0104'])
    def test_in_repo_root(self, mock_sub_popen):
        process_mock = Mock()
        attrs = {'communicate.return_value': ('ouput', 'error')}
        process_mock.configure_mock(**attrs)
        mock_sub_popen.return_value = process_mock
        get_repo_root("htmlcov\index.html")
        self.assertTrue(mock_sub_popen.called);

    @patch('subprocess.Popen')
    @requirements(['#0104'])
    def test_unchecked(self, mock_sub_popen):
        process_mock = Mock()
        attrs = {'communicate.return_value': ('ouput', 'error')}
        process_mock.configure_mock(**attrs)
        mock_sub_popen.return_value = process_mock
        test.ask(question='What is the status of <unchecked.txt>?')
        self.assertTrue(mock_sub_popen.called);

    @patch('source.git_utils.has_diff_files')
    @patch('source.git_utils.has_untracked_files')
    @requirements(['#0104'])
    def test_dirty_repo(self, mock_has_diff, mock_has_untracked):
        mock_has_untracked.return_value = False
        mock_has_diff.return_value = False
        is_repo_dirty("requirements.txt")

    @patch("source.git_utils.get_diff_files")
    def test_mod_locally(self, mock_get_diff):
        mock_get_diff.return_value = os.path.abspath("requirements.txt")
        get_git_file_info("requirements.txt")

    @patch("source.git_utils.get_diff_files")
    def test_not_in_repo(self, mock_get_diff):
        mock_get_diff.return_value = os.path.abspath("requirements.txt")
        is_file_in_repo("requirements.txt")

    @patch("source.git_utils.get_diff_files")
    def test_has_diff(self, mock_get_diff):
        mock_get_diff.return_value = []
        has_diff_files("requirements.txt")

    @patch("source.git_utils.is_repo_dirty")
    @patch("source.git_utils.get_diff_files")
    @patch("source.git_utils.get_untracked_files")
    def test_up_to_date(self,mock_dirty,mock_get_diff,mock_get_untracked):
        mock_get_diff.return_value = []
        mock_get_untracked.return_value = True
        mock_dirty.return_value =[]
        get_git_file_info("requirements.txt")


    @patch("source.git_utils.get_diff_files")
    @patch("source.git_utils.get_untracked_files")
    def test_git_untracked(self,mock_get_diff,mock_get_untracked):
        mock_get_diff.return_value = os.path.abspath("requirements.txt")
        mock_get_untracked.return_value = []
        print mock_get_untracked.return_value
        get_git_file_info("requirements.txt")



    @patch("source.git_utils.get_untracked_files")
    def test_untracked(self,mock_get_untracked):
        mock_get_untracked.return_value = os.path.abspath("requirements.txt")
        has_untracked_files("requirements.txt")

    @patch("source.git_utils.get_untracked_files")
    def test__no_untracked(self,mock_get_untracked):
        mock_get_untracked.return_value = []
        has_untracked_files("requirements.txt")
from unittest import TestCase  # imports testing tools
from source.main import Interface
from mock import MagicMock, Mock
import requirements
test = Interface();


class Git_Utils_Test(TestCase):
    @requirements(['#0100'])
    def test_valid_path(self):

    @requirements(['#0100'])
    def test_invalid_path(self):

    @requirements(['#0100'])
    def test_file_in_repo(self):

    @requirements(['#0100'])
    def test_file_not_in_repo(self):

    @requirements(['#0101'])
    def test_repo_is_dirty_true(self):

    @requirements(['#0101'])
    def test_repo_is_dirty_false(self):

    @requirements(['#0101'])
    def test_has_diff_files_true(self):

    @requirements(['#0101'])
    def test_has_diff_files_false(self):

    @requirements(['#0101'])
    def test_has_untracked_files_true(self):

    @requirements(['#0101'])
    def test_has_untracked_files_false(self):

    @requirements(['#0102'])
    def test_get_file_info(self):

    @requirements(['#0101'])
    def test_get_diff_files_staged(self):

    @requirements(['#0101'])
    def test_get_diff_files_nonstaged(self):

    @requirements(['#0101'])
    def test_get_repo_root(self):

    @requirements(['#0103'])
    def test_get_repo_branch(self):

    @requirements(['#0104'])
    def test_get_repo_url(self):




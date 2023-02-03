"""
Test custom django management commands

docu: https://docs.python.org/3/library/unittest.mock.html#where-to-patch
"""
from unittest.mock import patch  # mock db behavior

# helper-function to call command from name
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase  # base test class
from psycopg2 import OperationalError as Psycopg2Error


# for mocking check method of base-command class
@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test commands"""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting if db is ready."""
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    # adding patches from inside out!
    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for db when getting operational error."""
        patched_check.side_effect = [Psycopg2Error] * 2 + [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])

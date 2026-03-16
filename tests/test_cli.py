import pytest
from typer.testing import CliRunner
from manzh.cli import app

runner = CliRunner()

def test_app_help():
    """Test that the help command works."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    # Check for argument help text which is more reliably present
    assert "The manual page to translate" in result.stdout

def test_app_invalid_command():
    """Test that an invalid command returns an error."""
    # We mock fetch_man to avoid real man calls and API usage if needed, 
    # but for a basic test we just check if it handles non-existent commands.
    result = runner.invoke(app, ["nonexistentcommand"])
    assert result.exit_code == 1
    assert "Error: No manual entry" in result.stderr

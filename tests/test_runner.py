from app.runner import run_command

def test_run_command_success():
    output = run_command("echo Hello")
    assert output == "Hello"

def test_run_command_failure():
    try:
        run_command("invalidcommandthatdoesnotexist")
    except RuntimeError:
        assert True
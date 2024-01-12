from subprocess import PIPE, run
from unittest import TestCase

from secuplug import LS_LA, Command, SecuPlug


class Echo(SecuPlug):
    def __init__(self, command=Command("echo", ["Hello, World!"])):
        self._command = command

    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, value: list[str]):
        self._command.args += value

    @classmethod
    def _process_output(cls, output):
        print(output)

    @classmethod
    def _run_command(cls, command):
        result = run(
            str(command),
            shell=True,
            check=True,
            text=True,
            stdout=PIPE,
            stderr=PIPE,
        )
        return result.stdout

    def execute_command(self):
        output = self._run_command(self.command)
        self._process_output(output)


class TestSecuPlug(TestCase):
    def test_echo(self):
        echo = Echo()
        echo.execute_command()
        echo.command = ["Hello, World!"]
        echo.command = ["Hello, World!"]
        echo.execute_command()
        self.assertTrue(True)

    def test_ls_la(self):
        LS_LA().execute_command()
        self.assertTrue(True)

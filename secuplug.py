import subprocess
from abc import ABC, abstractmethod
from typing import override


class Command:
    """Constructor class for a command to be executed in the command line."""

    def __init__(self, command: str, args: list[str] = []):
        """
        Parameters:
        - command (str): The command to be executed.
        - args (list[str]): The arguments of the command.
        """
        self._command: str = command
        self._args: list[str] = args

    def __str__(self):
        return self._command + " " + " ".join(self._args) if self._args else ""


class SecuPlug(ABC):
    """
    Abstract base class for a plugin that runs a command in the command line
    and processes the output.

    Attributes:
    - None

    Methods:
    - _process_output(output): Abstract method to process the output of the command.
    - _run_command(command): Internal method to run a command in the command line.
    - execute(command): External method to execute a command and process the output.
    """

    @property
    @abstractmethod
    def command(self):
        """
        Abstract property for the command to be executed.
        """
        return Command("")

    @classmethod
    @abstractmethod
    def _process_output(cls, output):
        """
        Abstract method to process the output of the command.

        Parameters:
        - output (str): The output of the command.
        """
        pass

    @classmethod
    @abstractmethod
    def _run_command(cls, command: Command | str):
        """
        Internal method to run a command in the command line.

        Parameters:
        - command (Command | str): The command to be executed.

        Returns:
        - str: The output of the command.
        """
        try:
            result = subprocess.run(
                str(command),
                shell=True,
                check=True,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error running command: {e}")
            return ""

    
    @classmethod
    def execute_command(cls):
        """
        External method to execute a command and process the output.

        Parameters:
        - command (str): The command to be executed.
        """
        output = cls._run_command(cls.command)
        cls._process_output(output)


# Example usage of the abstract class
class LS_LA(SecuPlug):
    @property
    @override
    def command(self):
        return Command("ls", ["-l, -a"])

    @classmethod
    @override
    def _process_output(cls, output):
        print("Processing output:")
        print(output.upper())

    @classmethod
    @override
    def _run_command(cls, command):
        return super()._run_command(command)

    @classmethod
    @override
    def execute_command(cls):
        super().execute_command()

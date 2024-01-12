import subprocess
from abc import ABC, abstractmethod


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

    @property
    def command(self) -> str:
        return self._command

    @command.setter
    def command(self, value: str) -> None:
        self._command = value

    @property
    def args(self) -> list[str]:
        return self._args

    @args.setter
    def args(self, value: list[str]) -> None:
        self._args = value

    def __str__(self):
        return self._command + (" " + " ".join(self._args) if self._args else "")

    def __repr__(self) -> str:
        return f"Command(command={self._command}, args={self._args})"


class SecuTools:
    @staticmethod
    def find_string(text: str, string: str):
        """Finds all instances of a search string in a text.

        This is just an example...

        Args:
            text (str): The text to be searched.
            string (str): The search string.
        Returns:
            list[int]: All indices of the search string in the text. (-1 if not found)
        """
        res = []
        while (idx := text.find(string)):
            res.append(idx)
            text = text[idx + 1:]
        return res




class SecuPlug(ABC):
    """ Abstract SecuPlug class

    Abstract base class for a plugin that runs a command in the command line
    and processes the output.

    Attributes:
    - None

    Methods:
    - _process_output(output): Abstract method to process the output of the command.
    - _run_command(command): Internal method to run a command in the command line.
    - execute(command): External method to execute a command and process the output.
    """

    def __init__(self, command: Command = Command("")):
        self._command = command

    @property
    @abstractmethod
    def command(self):
        """
        Abstract property for the command to be executed.
        """
        return self._command

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

    def execute_command(self):
        """
        External method to execute a command and process the output.

        Parameters:
        - command (str): The command to be executed.
        """
        output = self._run_command(self.command)
        self._process_output(output)


# Example usage of the abstract class
class LS_LA(SecuPlug):
    @property
    def command(self):
        return Command("ls", ["-l", "-a"])

    @classmethod
    def _process_output(cls, output):
        print("Processing output:")
        print(output.upper())

    @classmethod
    def _run_command(cls, command):
        return super()._run_command(command)

    def execute_command(self):
        super().execute_command()

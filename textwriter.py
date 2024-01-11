from logging import getLogger
from typing import Self

logger = getLogger(__name__)

class TextWriter():
    """
    A class for building and writing Markdown text documents to a file.

    Attributes:
        name (str): The name of the file where the Markdown document will be written.
        endl (str): The end line character (default "\\n")

    Methods:
        __init__(self, name: str)
            Initializes a TextWriter object with the specified file name.

        add_header_one(self, header: str)
            Adds a level-one Markdown header to the document with the specified text.

        add_header_two(self, header: str)
            Adds a level-two Markdown header to the document with the specified text.

        add_header_three(self, header: str)
            Adds a level-three Markdown header to the document with the specified text.

        add_header_n(self, n:int, header: str)
            Adds a level-n Markdown header to the document with the specified text.           

        add_paragraph(self, text: str)
            Adds a Markdown paragraph to the document with the specified text.

        add_list(self, items: list[str], ordered: bool = False)
            Adds a Markdown list to the document with the specified items. If ordered is True,
            creates an ordered list; otherwise, creates an unordered list.

        add_code_block(self, code: str, language: str = "")
            Adds a code block to the document with the specified code and optional language.

        add_horizontal_rule(self)
            Adds a horizontal rule to the document.

        write_to_file(self)
            Writes the constructed Markdown document to the specified file.

    Example:
        ```python
        # Example usage of TextWriter class
        writer = TextWriter("example.md")
        writer.add_header_one("My Markdown Document")
        writer.add_paragraph("This is a sample Markdown document created using TextWriter.")
        writer.add_list(["Item 1", "Item 2", "Item 3"], ordered=True)
        writer.add_code_block("print('Hello, Markdown!')")
        writer.write_to_file()
        ```
    """
    def __init__(self, name: str, endl: str = "\n") -> None:
        """
        Initializes a TextWriter object with the specified file name.

        Parameters:
            name (str): The name of the file where the Markdown document will be written.
            endl (str): The end line character (default "\\n")
        """
        self._state = ""
        self._name = name
        self._endl = endl

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    def add_header_n(self, n: int, header: str, end: str | None = None) -> Self:
        self._state += f"{"#" * n}{header}{end if end else self._endl}"
        return self
    
    def add_header_one(self, header: str, end: str | None = None) -> Self:
        self._state += f"# {header}{end if end else self._endl}"
        return self

    def add_header_two(self, header: str, end: str | None = None) -> Self:
        self._state += f"## {header}{end if end else self._endl}"
        return self

    def add_header_three(self, header: str, end: str | None = None) -> Self:
        self._state += f"### {header}{end if end else self._endl}"
        return self

    def add_paragraph(self):
        self._state += f"{self._endl}"
        return self

    def add_horizontal_rule(self):
        self._state += f"---{self._endl}"
        return self

    def add_code_block(self, code: str, end: str | None = None) -> Self:
        self._state += f"```{end if end else self._endl}" + code + f"{end if end else self._endl}" + f"```{end if end else self._endl}"
        return self

    def add_list(self, items: list[str], ordered: bool = False, end: str | None = None) -> Self:
        if ordered:
            self._state += f"{end if end else self._endl}".join([f"{idx + 1}. {item}" for (idx, item) in enumerate(items)]) + f"{end if end else self._endl}"
        else:
            self._state += f"{end if end else self._endl}".join([f"- {item}" for item in items]) + f"{end if end else self._endl}"
        return self

    def write_to_file(self) -> None:
        with open(self._name, mode="w") as f:
            f.write(self._state)
            logger.info(msg=f"Text is written to the file: {self._name}")

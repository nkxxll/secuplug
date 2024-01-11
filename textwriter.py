from enum import Enum
from logging import getLogger

logger = getLogger(__name__)


class SyntaxHighlighting(Enum):
    """Is used to specify the language syntax highlighting of a code block."""

    APACHE = "apache"
    ARMASM = "armasm"
    BASH = "bash"
    C = "c"
    COFFEESCRIPT = "coffeescript"
    CPP = "cpp"
    CSHARP = "csharp"
    CSS = "css"
    D = "d"
    DIFF = "diff"
    GO = "go"
    HANDLEBARS = "handlebars"
    HASKELL = "haskell"
    HTTP = "http"
    INI = "ini"
    JAVA = "java"
    JAVASCRIPT = "javascript"
    JSON = "json"
    JULIA = "julia"
    KOTLIN = "kotlin"
    LESS = "less"
    LUA = "lua"
    MAKEFILE = "makefile"
    MARKDOWN = "markdown"
    NGINX = "nginx"
    NIM = "nim"
    OBJECTIVEC = "objectivec"
    PERL = "perl"
    PHP = "php"
    PLAINTEXT = "plaintext"
    PROPERTIES = "properties"
    PYTHON = "python"
    R = "r"
    RUBY = "ruby"
    RUST = "rust"
    SCALA = "scala"
    SCSS = "scss"
    SHELL = "shell"
    SQL = "sql"
    SWIFT = "swift"
    TYPESCRIPT = "typescript"
    X86ASM = "x86asm"
    XML = "xml"
    YAML = "yaml"


class TextWriter:
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

    def add_header_n(self, n: int, header: str, end: str | None = None) -> "TextWriter":
        self._state += f"{'#' * n} {header}{end if end is not None else self._endl}"
        self._state += f"{end if end is not None else self._endl}"
        return self

    def add_header_one(self, header: str, end: str | None = None) -> "TextWriter":
        self._state += f"# {header}{end if end is not None else self._endl}"
        self._state += f"{end if end is not None else self._endl}"
        return self

    def add_header_two(self, header: str, end: str | None = None) -> "TextWriter":
        self._state += f"## {header}{end if end is not None else self._endl}"
        self._state += f"{end if end is not None else self._endl}"
        return self

    def add_header_three(self, header: str, end: str | None = None) -> "TextWriter":
        self._state += f"### {header}{end if end is not None else self._endl}"
        self._state += f"{end if end is not None else self._endl}"
        return self

    def add_paragraph(self, text: str, end: str | None = None):
        self._state += text
        self._state += f"{end if end is not None else self._endl}"
        self._state += self._endl
        return self

    def add_horizontal_rule(self):
        self._state += f"---{self._endl}"
        return self

    def add_code_block(
        self, code: str, highlighting: str | SyntaxHighlighting | None = None
    ) -> "TextWriter":
        self._state += (
            "```"
            + (
                highlighting
                if isinstance(highlighting, str)
                else highlighting.value
                if isinstance(highlighting, SyntaxHighlighting)
                else ""
            )
            + self._endl
            + code
            + f"```{self._endl}"
        )
        return self

    def add_list(
        self, items: list[str], ordered: bool = False, end: str | None = None
    ) -> "TextWriter":
        if ordered:
            self._state += (
                f"{end if end is not None else self._endl}".join(
                    [f"{idx + 1}. {item}" for (idx, item) in enumerate(items)]
                )
                + f"{end if end is not None else self._endl}"
            )
        else:
            self._state += (
                f"{end if end is not None else self._endl}".join(
                    [f"- {item}" for item in items]
                )
                + f"{end if end is not None else self._endl}"
            )
        self._state += self._endl
        return self

    def write_to_file(self) -> None:
        with open(self._name, mode="w") as f:
            f.write(self._state)
            logger.info(msg=f"Text is written to the file: {self._name}")

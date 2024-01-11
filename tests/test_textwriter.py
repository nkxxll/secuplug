from unittest import TestCase

from textwriter import SyntaxHighlighting, TextWriter

FILE_PATH = "./tests/tw_test_files/"


class TestTextWriter(TestCase):
    def test_header_one(self):
        name = FILE_PATH + "test_header.txt"
        expected = "# This is a test\n\n"
        TextWriter(name).add_header_one("This is a test").write_to_file()
        with open(name, "r") as f:
            text = f.read()
        self.assertEqual(text, expected)

    def test_header_two(self):
        name = FILE_PATH + "test_header.txt"
        expected = "## This is a test\n\n"
        TextWriter(name).add_header_two("This is a test").write_to_file()
        with open(name, "r") as f:
            text = f.read()
        self.assertEqual(text, expected)

    def test_header_three(self):
        name = FILE_PATH + "test_header.txt"
        expected = "### This is a test\n\n"
        TextWriter(name).add_header_three("This is a test").write_to_file()
        with open(name, "r") as f:
            text = f.read()
        self.assertEqual(text, expected)

    def test_header_n(self):
        name = FILE_PATH + "test_header.txt"
        n = 5
        expected = "##### This is a test\n\n"
        TextWriter(name).add_header_n(n, "This is a test").write_to_file()
        with open(name, "r") as f:
            text = f.read()
        self.assertEqual(text, expected)

    def test_paragraph(self):
        name = FILE_PATH + "test_paragraph.txt"
        expected = "This is a test\n\n"
        TextWriter(name).add_paragraph("This is a test").write_to_file()
        with open(name, "r") as f:
            text = f.read()
        self.assertEqual(text, expected)

    def test_paragraph_end(self):
        name = FILE_PATH + "test_paragraph.txt"
        expected = "This is a testbla\nThis is a test\n"
        TextWriter(name).add_paragraph("This is a test", "bla").add_paragraph(
            "This is a test", end=""
        ).write_to_file()
        with open(name, "r") as f:
            text = f.read()
        self.assertEqual(text, expected)

    def test_horizontal_rule(self):
        name = FILE_PATH + "test_horizontal_rule.txt"
        expected = "---\n"
        TextWriter(name).add_horizontal_rule().write_to_file()
        with open(name, "r") as f:
            text = f.read()
        self.assertEqual(text, expected)

    def test_code_block(self):
        name = FILE_PATH + "test_code_block.txt"
        code = """for i in range(1):
    print(i)
"""
        expected = f"```\n{code}```\n"
        TextWriter(name).add_code_block(code).write_to_file()
        with open(name, "r") as f:
            text = f.read()
        self.assertEqual(text, expected)

    def test_list(self):
        name = FILE_PATH + "test_list.txt"
        items = ["test1", "test2", "test3"]
        expected = "- test1\n- test2\n- test3\n\n"
        TextWriter(name).add_list(items).write_to_file()
        with open(name, "r") as f:
            text = f.read()
        self.assertEqual(text, expected)

    def test_ordered_list(self):
        name = FILE_PATH + "test_list.txt"
        items = ["test1", "test2", "test3"]
        expected = "1. test1\n2. test2\n3. test3\n\n"
        TextWriter(name).add_list(items, True).write_to_file()
        with open(name, "r") as f:
            text = f.read()
        self.assertEqual(text, expected)

    def test_full_document(self):
        name = FILE_PATH + "test_full_document.txt"
        expected = r"""# This is a test

# My Arbitrary Markdown File

## Introduction

Welcome to my Markdown file! This document serves as a demonstration of various Markdown elements.

## Text Styling

*This text* is italicized, **this text** is bold, and ***this text*** is both.

## Lists

### Ordered List

1. First item
2. Second item
3. Third item

### Unordered List

- Apples
- Bananas
- Oranges

## Code

Inline code can be written like `var example = "Hello, Markdown!";`.

For a code block:

```python
def greet(name):
    print(f"Hello, {name}!")

greet("World")
```
"""

        TextWriter(name).add_header_one("This is a test").add_header_one(
            "My Arbitrary Markdown File"
        ).add_header_two("Introduction").add_paragraph(
            "Welcome to my Markdown file! This document serves as a demonstration of various Markdown elements."
        ).add_header_two("Text Styling").add_paragraph(
            "*This text* is italicized, **this text** is bold, and ***this text*** is both."
        ).add_header_two("Lists").add_header_three("Ordered List").add_list(
            ["First item", "Second item", "Third item"], True
        ).add_header_three("Unordered List").add_list(
            ["Apples", "Bananas", "Oranges"]
        ).add_header_two("Code").add_paragraph(
            'Inline code can be written like `var example = "Hello, Markdown!";`.'
        ).add_paragraph("For a code block:").add_code_block(
            r"""def greet(name):
    print(f"Hello, {name}!")

greet("World")
""",
            highlighting=SyntaxHighlighting.PYTHON,
        ).write_to_file()
        with open(name, "r") as f:
            text = f.read()
        self.assertEqual(text, expected)

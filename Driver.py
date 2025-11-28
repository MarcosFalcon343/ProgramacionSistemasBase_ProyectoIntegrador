from antlr4 import InputStream, CommonTokenStream

from src.MarkdownGrammarLexer import MarkdownGrammarLexer
from src.MarkdownGrammarParser import MarkdownGrammarParser
from src.MarkdownVisitor import MarkdownToHtmlVisitor


def convert_markdown_to_html(text: str) -> str:
    """Convierte un texto en Markdown a una cadena HTML usando ANTLR."""
    # Asegurar un salto de línea final para que el parser no falle al final de archivo
    if not text.endswith("\n"):
        text += "\n"
    lexer = MarkdownGrammarLexer(InputStream(text))
    token_stream = CommonTokenStream(lexer)
    parser = MarkdownGrammarParser(token_stream)
    tree = parser.doc()
    visitor = MarkdownToHtmlVisitor()
    return visitor.visit(tree)


def convert_file(input_path: str, output_path: str) -> None:
    """Lee un archivo Markdown y escribe el HTML resultante en otro archivo."""
    with open(input_path, "r", encoding="utf-8") as f:
        md_text = f.read()
    html = convert_markdown_to_html(md_text)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    convert_file("examples/valid/ejemplo1.md", "examples/expected/ejemplo1.html")
    convert_file("examples/valid/ejemplo2.md", "examples/expected/ejemplo2.html")
    convert_file("examples/valid/ejemplo3.md", "examples/expected/ejemplo3.html")
    convert_file("examples/valid/ejemplo4.md", "examples/expected/ejemplo4.html")
    convert_file("examples/valid/ejemplo5.md", "examples/expected/ejemplo5.html")
    convert_file("examples/valid/ejemplo6.md", "examples/expected/ejemplo6.html")
    convert_file("examples/valid/ejemplo7.md", "examples/expected/ejemplo7.html")
    convert_file("examples/valid/ejemplo8.md", "examples/expected/ejemplo8.html")
    convert_file("examples/valid/ejemplo9.md", "examples/expected/ejemplo9.html")
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable


def run(
    cmd: list[str],
    *,
    cwd: Path | None = None,
    input_text: str | None = None,
    expected_substrings: list[str] | None = None,
) -> str:
    result = subprocess.run(
        cmd,
        cwd=cwd or ROOT,
        input=input_text,
        text=True,
        capture_output=True,
        check=True,
    )
    output = result.stdout + result.stderr
    if expected_substrings:
        for token in expected_substrings:
            if token not in output:
                raise AssertionError(
                    f"Missing expected text {token!r} in output of {cmd!r}\n{output}"
                )
    return output


def test_lesson_1() -> None:
    solutions = ROOT / "lesson_code" / "lezione_1" / "soluzioni"

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)

        run(
            ["bash", str(solutions / "esercizio_1_percorsi.sh")],
            cwd=tmp_path,
            expected_substrings=["lezione1_lab/appunti", "appunti", "prove"],
        )
        assert (tmp_path / "lezione1_lab" / "appunti").is_dir()
        assert (tmp_path / "lezione1_lab" / "prove").is_dir()

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        run(
            ["bash", str(solutions / "esercizio_2_file.sh")],
            cwd=tmp_path,
            expected_substrings=["note_importanti.txt", "gatto", "limone"],
        )
        note_file = tmp_path / "lezione1_lab" / "appunti" / "note_importanti.txt"
        assert note_file.read_text() == "gatto\nlimone\n"

    output = run(
        [PYTHON, str(solutions / "hello.py")],
        expected_substrings=["Ciao Python", "Nella scatola c'e un limone.", "42"],
    )
    assert len(output.strip().splitlines()) == 3

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        output = run(
            ["bash", str(solutions / "esercizio_5_venv.sh")],
            cwd=tmp_path,
            expected_substrings=[".venv", "jupyter_core"],
        )
        assert (tmp_path / ".venv").is_dir()
        assert "site-packages" in output

        notebook_path = solutions / "test_notebook.ipynb"
        tmp_notebook = tmp_path / "test_notebook.ipynb"
        tmp_notebook.write_text(notebook_path.read_text(encoding="utf-8"), encoding="utf-8")

        run(
            [
                str(tmp_path / ".venv" / "bin" / "python"),
                "-m",
                "jupyter",
                "nbconvert",
                "--to",
                "notebook",
                "--execute",
                "test_notebook.ipynb",
                "--output",
                "executed.ipynb",
            ],
            cwd=tmp_path,
        )

        notebook = json.loads((tmp_path / "executed.ipynb").read_text(encoding="utf-8"))
        assert notebook["nbformat"] == 4
        assert notebook["cells"][0]["cell_type"] == "markdown"
        assert "Test notebook" in "".join(notebook["cells"][0]["source"])
        assert notebook["cells"][1]["cell_type"] == "code"
        assert "Notebook ok" in "".join(notebook["cells"][1]["source"])
        first_output = notebook["cells"][1]["outputs"][0]["text"]
        assert "Notebook ok" in "".join(first_output)
        assert notebook["cells"][2]["cell_type"] == "code"
        assert "3 * 5" in "".join(notebook["cells"][2]["source"])
        second_output = notebook["cells"][2]["outputs"][0]["data"]["text/plain"]
        assert "15" in "".join(second_output)


def test_lesson_2() -> None:
    examples = ROOT / "lesson_code" / "lezione_2" / "esempi"
    solutions = ROOT / "lesson_code" / "lezione_2" / "soluzioni"

    run(
        [PYTHON, str(examples / "variabili.py")],
        expected_substrings=["nome=Milo", "anni=4", "colore=grigio"],
    )
    run([PYTHON, str(examples / "numeri.py")], expected_substrings=["13", "1000"])
    run([PYTHON, str(examples / "booleani.py")], expected_substrings=["True", "False"])
    run(
        [PYTHON, str(examples / "if_else.py")],
        expected_substrings=["Abbastanza limoni", "Sedia verde"],
    )
    run(
        [PYTHON, str(examples / "liste.py")],
        expected_substrings=[
            "['Anna', 'Luca', 'Marco']",
            "['Anna', 'Luca', 'Marco', 'Nina']",
        ],
    )
    run([PYTHON, str(examples / "type_examples.py")], expected_substrings=["<class 'int'>"])

    run(
        [PYTHON, str(solutions / "problema_1_valutazione_limoni.py")],
        expected_substrings=["Pochi limoni"],
    )
    run(
        [PYTHON, str(solutions / "problema_2_macedonia_nomi.py")],
        expected_substrings=["Anna", "Marco", "4"],
    )
    run(
        [PYTHON, str(solutions / "problema_3_area_tappeto.py")],
        expected_substrings=["10"],
    )


def test_lesson_3() -> None:
    examples = ROOT / "lesson_code" / "lezione_3" / "esempi"
    solutions = ROOT / "lesson_code" / "lezione_3" / "soluzioni"

    run(
        [PYTHON, str(examples / "stringhe.py")],
        expected_substrings=["Milo grigio", "gatto verde", "GATTO VERDE"],
    )
    run(
        [PYTHON, str(examples / "liste_e_for.py")],
        expected_substrings=["['Luca', 'Marco']", "Nome: Anna", "5"],
    )
    run(
        [PYTHON, str(examples / "while_input.py")],
        input_text="1.5\n2.0\n-1\n",
        expected_substrings=["[1.5, 2.0]"],
    )
    run(
        [PYTHON, str(examples / "funzioni.py")],
        expected_substrings=["Ciao Milo", "10", "Ciao Nina"],
    )
    run(
        [PYTHON, str(examples / "dizionari.py")],
        expected_substrings=["scatola_1", "limone", "cucina"],
    )
    run(
        [PYTHON, str(examples / "import_math.py")],
        expected_substrings=["4.0", "5.0"],
    )
    run(
        [PYTHON, str(examples / "import_locale" / "main.py")],
        expected_substrings=["Ciao Milo"],
    )
    run(
        [PYTHON, str(examples / "try_except.py")],
        input_text="venti\n",
        expected_substrings=["Inserire un numero intero"],
    )

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        run(
            [PYTHON, str(examples / "file_testo.py")],
            cwd=tmp_path,
            expected_substrings=["gatto"],
        )
        assert (tmp_path / "note.txt").read_text(encoding="utf-8") == "gatto\n"

    run(
        [PYTHON, str(solutions / "problema_1_frase_stringhe.py")],
        expected_substrings=["Anna ha un limone verde."],
    )
    run(
        [PYTHON, str(solutions / "problema_2_macedonia_funzione.py")],
        expected_substrings=["Nome lungo", "Nomi lunghi: 1"],
    )
    run(
        [PYTHON, str(solutions / "problema_3_registro_numeri.py")],
        input_text="1.5\n2.0\n-1\n",
        expected_substrings=["Valori inseriti: 2", "[1.5, 2.0]"],
    )

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        run(
            [PYTHON, str(solutions / "problema_4_scheda_scatola_file.py")],
            cwd=tmp_path,
            expected_substrings=["cucina"],
        )
        content = (tmp_path / "scheda_scatola.txt").read_text(encoding="utf-8")
        assert "Nome: scatola_1" in content
        assert "Stanza: cucina" in content


def test_lesson_4() -> None:
    examples = ROOT / "lesson_code" / "lezione_4" / "esempi"
    solutions = ROOT / "lesson_code" / "lezione_4" / "soluzioni"

    run(
        [PYTHON, str(examples / "dizionari_intro.py")],
        expected_substrings=["Milo", "cucina", "limone"],
    )
    run(
        [PYTHON, str(examples / "errori_intro.py")],
        expected_substrings=["Numero valido: 23", "Numero non valido: venti"],
    )

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        run(
            [PYTHON, str(examples / "file_testo_intro.py")],
            cwd=tmp_path,
            expected_substrings=["Anna", "Luca", "Marco"],
        )
        content = (tmp_path / "macedonia.txt").read_text(encoding="utf-8")
        assert content == "Anna\nLuca\nMarco\n"

    run(
        [PYTHON, str(examples / "classe_gatto_base.py")],
        expected_substrings=[
            "Nina, anni 1, nero",
            "False",
            "Nina, anni 2, nero",
            "True",
            "Nina (nero)",
        ],
    )
    run(
        [PYTHON, str(examples / "classe_registro_gatti.py")],
        expected_substrings=["2"],
    )
    run(
        [PYTHON, str(examples / "ereditarieta_animali.py")],
        expected_substrings=["Bruno, 3 anni", "Bruno: marrone"],
    )

    run(
        [PYTHON, str(solutions / "problema_1_dizionario_scatola.py")],
        expected_substrings=["scatola_1", "limone", "cucina"],
    )

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        run(
            [PYTHON, str(solutions / "problema_2_macedonia_file.py")],
            cwd=tmp_path,
            expected_substrings=["Anna", "Luca", "Marco"],
        )
        content = (tmp_path / "macedonia.txt").read_text(encoding="utf-8")
        assert content == "Anna\nLuca\nMarco\n"

    run(
        [PYTHON, str(solutions / "problema_3_classe_gatto.py")],
        expected_substrings=[
            "Nina, anni 1, nero",
            "False",
            "Nina, anni 2, nero",
            "True",
        ],
    )
    run(
        [PYTHON, str(solutions / "problema_4_registro_gatti.py")],
        expected_substrings=[
            "Gatti adulti: 2",
            "Media anni: 3.0",
            "Otto, anni 4, bianco",
        ],
    )
    run(
        [PYTHON, str(solutions / "problema_5_ereditarieta_animali.py")],
        expected_substrings=["Bruno, 3 anni", "Bruno: marrone"],
    )


def main() -> None:
    test_lesson_1()
    test_lesson_2()
    test_lesson_3()
    test_lesson_4()
    print("All lesson checks passed.")


if __name__ == "__main__":
    main()

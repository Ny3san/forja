"""Verifica a coerência da Forja consigo mesma.

Roda com a biblioteca padrão do Python, sem instalar nada:

    python3 -m unittest discover -s tests -v

Cada teste aplica uma regra que a própria Forja exige dos projetos que analisa
ou cria: referências que existem, documentação que bate com o código, prosa sem
enchimento, tabelas íntegras.
"""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
README = ROOT / "README.md"
REFS = ROOT / "references"

# Arquivos de nomes que pertencem ao projeto do usuário, não à Forja.
PROJECT_FILES = {
    "AGENTS.md", "AGENTS.local.md", "CLAUDE.md", "CLAUDE.local.md",
    "README.md", "SKILL.md",
}

# O catálogo de padrões de IA mora aqui e cita as próprias palavras vetadas.
PATTERN_CATALOG = "escrita-humana.md"

# Raízes das palavras da linha "Palavras de IA" de escrita-humana.md.
# test_banned_stems_cover_catalog garante que a lista abaixo acompanha o catálogo.
BANNED_STEMS = [
    r"robust\w*", r"hol[ií]stic\w*", r"alavanc\w*", r"sinergi\w*",
    r"ecossistem\w*", r"jornada\w*", r"panorama\w*", r"cen[áa]rio atual",
    r"mergulh\w*", r"desvend\w*", r"cruciais|crucial", r"transformador\w*",
    r"de ponta",
]
BANNED_PHRASES = [
    r"é importante ressaltar", r"vale destacar", r"em suma",
    r"nos dias de hoje", r"ótima pergunta", r"espero ter ajudado",
    r"sem dúvida",
]
BANNED_ADVERBS = [r"realmente", r"simplesmente", r"absolutamente", r"extremamente"]

EMOJI = re.compile("[\U0001F300-\U0001FAFF\u2600-\u27BF\u2B50\u2705]")
NOT_X_IS_Y = re.compile(
    r"\b[Nn]ão é (?:apenas |só |somente )?[^.\n,]{1,60}, é\b"
)

OPTION = re.compile(r"--[a-z]+")
# Opções de ferramentas do usuário que a documentação menciona de passagem.
EXTERNAL_OPTIONS = {"--help", "--version"}
HEADING_NUM = re.compile(r"^## (\d+)\. (.+)$", re.M)


def md_files():
    files = [SKILL, README, *sorted(REFS.glob("*.md"))]
    agents = ROOT / "AGENTS.md"
    if agents.exists():
        files.append(agents)
    return files


def read(path):
    return path.read_text(encoding="utf-8")


def strip_fences(text):
    """Troca o conteúdo de blocos de código por linhas vazias, mantendo a numeração."""
    out, inside = [], False
    for line in text.split("\n"):
        if line.startswith("```"):
            inside = not inside
            out.append("")
        else:
            out.append("" if inside else line)
    return "\n".join(out)


def prose_lines(path):
    """Linhas de prosa (sem blocos de código e sem trechos entre crases)."""
    for number, line in enumerate(strip_fences(read(path)).split("\n"), 1):
        yield number, re.sub(r"`[^`]*`", "", line)


def parse_frontmatter(text):
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        return None
    fields, key = {}, None
    for line in match.group(1).split("\n"):
        if re.match(r"^[A-Za-z_-]+:", line):
            key, value = line.split(":", 1)
            value = value.strip()
            fields[key] = "" if value in (">", "|") else value.strip('"')
        elif key:
            fields[key] = (fields[key] + " " + line.strip()).strip()
    return fields


def skill_commands():
    """Comandos da tabela de SKILL.md, como `analisar`, `entender`, ..."""
    return re.findall(r"^\| `/([a-z-]+)", read(SKILL), re.M)


class Frontmatter(unittest.TestCase):
    def setUp(self):
        self.fields = parse_frontmatter(read(SKILL))

    def test_frontmatter_exists(self):
        self.assertIsNotNone(self.fields, "SKILL.md precisa começar com frontmatter YAML")

    def test_required_fields(self):
        self.assertEqual(self.fields.get("name"), "forja")
        self.assertEqual(self.fields.get("license"), "MIT")
        self.assertTrue(self.fields.get("description"), "description vazia")

    def test_description_fits_the_limit(self):
        size = len(self.fields["description"])
        self.assertLessEqual(size, 1024, f"description tem {size} caracteres; o limite é 1024")

    def test_description_names_every_command(self):
        description = self.fields["description"].lower()
        for command in skill_commands():
            with self.subTest(command=command):
                text = description + " " + self.fields.get("argument-hint", "")
                self.assertTrue(command in text, f"'{command}' não aparece na description nem no argument-hint")

    def test_no_unknown_keys(self):
        allowed = {"name", "description", "argument-hint", "license"}
        self.assertLessEqual(set(self.fields), allowed)

    def test_skill_md_stays_small(self):
        lines = len(read(SKILL).split("\n"))
        self.assertLessEqual(lines, 500, f"SKILL.md tem {lines} linhas; mova detalhes para references/")

    def test_license_file_is_mit(self):
        self.assertIn("MIT License", read(ROOT / "LICENSE"))

    def test_notice_covers_every_credited_project(self):
        credits = read(README).split("## Créditos", 1)[1].split("## Licença", 1)[0]
        notice = read(ROOT / "NOTICE")
        projects = set(re.findall(r"https://github\.com/([\w.-]+/[\w.-]+)", credits))
        self.assertTrue(projects, "README sem projetos creditados")
        for project in projects:
            with self.subTest(project=project):
                self.assertTrue(project in notice, f"NOTICE não cita {project}")
                after = notice.split(project, 1)[1]
                self.assertTrue(re.match(r"\)\nCopyright \(c\) \d{4} \S", after), f"falta a linha de copyright de {project}")


class References(unittest.TestCase):
    def test_every_reference_is_listed_in_skill_md(self):
        listed = set(re.findall(r"references/([\w.-]+\.md)", read(SKILL)))
        actual = {p.name for p in REFS.glob("*.md")}
        self.assertEqual(listed - actual, set(), "SKILL.md cita arquivo que não existe")
        self.assertEqual(actual - listed, set(), "arquivo em references/ que SKILL.md não carrega")

    def test_every_command_has_its_reference(self):
        for command in skill_commands():
            with self.subTest(command=command):
                self.assertTrue((REFS / f"{command}.md").exists())

    def test_md_names_inside_references_resolve(self):
        for path in REFS.glob("*.md"):
            for token in re.findall(r"`([\w.-]+\.md)`", read(path)):
                with self.subTest(file=path.name, token=token):
                    if token not in PROJECT_FILES:
                        self.assertTrue((REFS / token).exists(), f"{path.name} cita {token}")

    def test_relative_links_resolve(self):
        for path in md_files():
            for target in re.findall(r"\]\(([^)]+)\)", read(path)):
                if target.startswith(("http://", "https://", "#", "mailto:")):
                    continue
                with self.subTest(file=path.name, target=target):
                    self.assertTrue((path.parent / target.split("#")[0]).exists())

    def test_guide_index_matches_headings(self):
        for name in ("escrita-humana.md", "prompt-guide.md"):
            text = read(REFS / name)
            index = re.search(r"^Conteúdo: (.+)$", text, re.M)
            with self.subTest(file=name):
                self.assertIsNotNone(index, "falta a linha 'Conteúdo:'")
                entries = [e.strip() for e in index.group(1).split("·")]
                headings = HEADING_NUM.findall(text)
                self.assertEqual(len(entries), len(headings))
                for entry, (number, title) in zip(entries, headings):
                    self.assertTrue(
                        entry.lower().startswith(f"{number}. {title.lower()}"),
                        f"índice '{entry}' não bate com o título '{number}. {title}'",
                    )


class Documentation(unittest.TestCase):
    def test_readme_structure_matches_the_repository(self):
        block = re.search(r"## Estrutura\s+```text\n(.*?)```", read(README), re.S)
        self.assertIsNotNone(block, "README precisa de '## Estrutura' com um bloco text")
        documented = set()
        for line in block.group(1).split("\n")[1:]:
            name = re.sub(r"^[│├└─\s]+", "", line).split("#")[0].strip()
            if name:
                documented.add(name.rstrip("/"))
        actual = set()
        for p in ROOT.rglob("*"):
            parts = p.relative_to(ROOT).parts
            if any(part.startswith(".") or part == "__pycache__" for part in parts):
                continue
            actual.add(p.name)
        self.assertEqual(documented - actual, set(), "README cita o que não existe")
        self.assertEqual(actual - documented, set(), "README não lista o que existe")

    def test_every_command_is_documented_in_readme(self):
        readme = read(README)
        for command in skill_commands():
            with self.subTest(command=command):
                self.assertTrue(f"/{command}" in readme, f"README não cita /{command}")

    def test_options_are_documented_both_ways(self):
        hint = parse_frontmatter(read(SKILL)).get("argument-hint", "")
        declared = set(OPTION.findall(hint))
        self.assertTrue(declared, "argument-hint sem opções")
        for option in declared:
            with self.subTest(option=option):
                self.assertTrue(option in read(README), f"README não documenta {option}")
                self.assertTrue(
                    any(option in read(p) for p in REFS.glob("*.md")),
                    f"{option} não é implementada em nenhuma referência",
                )
        used = set()
        for path in md_files():
            used |= set(OPTION.findall(strip_fences(read(path))))
            used |= set(OPTION.findall(" ".join(re.findall(r"```.*?```", read(path), re.S))))
        self.assertEqual(used - declared - EXTERNAL_OPTIONS, set(), "opção usada na documentação e ausente do argument-hint")

    def test_command_and_option_tables_are_identical(self):
        def rows(path):
            # Só as tabelas de três colunas (comandos e opções); "Referências" tem duas.
            cells = re.compile(r"(?<!\\)\|")
            return {
                r.strip() for r in read(path).split("\n")
                if re.match(r"^\| `(/|--)", r) and len(cells.split(r.strip())) - 2 == 3
            }
        skill, readme = rows(SKILL), rows(README)
        self.assertEqual(skill - readme, set(), "linha do SKILL.md ausente ou diferente no README")
        self.assertEqual(readme - skill, set(), "linha do README ausente ou diferente no SKILL.md")


class Structure(unittest.TestCase):
    def test_markdown_tables_are_well_formed(self):
        split = re.compile(r"(?<!\\)\|")
        for path in md_files():
            columns = None
            for number, line in enumerate(strip_fences(read(path)).split("\n"), 1):
                if line.startswith("|"):
                    count = len(split.split(line.strip())) - 2
                    if columns is None:
                        columns = count
                    with self.subTest(file=path.name, line=number):
                        self.assertEqual(count, columns, f"{path.name}:{number} tem {count} colunas, esperava {columns}")
                else:
                    columns = None

    def test_code_fences_are_balanced(self):
        for path in md_files():
            with self.subTest(file=path.name):
                fences = [l for l in read(path).split("\n") if l.startswith("```")]
                self.assertEqual(len(fences) % 2, 0)

    def test_whitespace_hygiene(self):
        for path in [*md_files(), Path(__file__)]:
            text = path.read_bytes().decode("utf-8")
            with self.subTest(file=path.name):
                self.assertNotIn("\r", text, "use fim de linha LF")
                self.assertTrue(text.endswith("\n") and not text.endswith("\n\n"), "termine com uma única quebra de linha")
                for number, line in enumerate(text.split("\n"), 1):
                    self.assertEqual(line, line.rstrip(), f"{path.name}:{number} tem espaço no fim")
                    self.assertNotIn("\t", line, f"{path.name}:{number} tem tabulação")

    def test_repository_follows_its_own_create_project_standard(self):
        for name in ("AGENTS.md", ".editorconfig", ".gitignore", "LICENSE", "README.md"):
            with self.subTest(file=name):
                self.assertTrue((ROOT / name).exists(), f"falta {name}")
        agents = ROOT / "AGENTS.md"
        if agents.exists():
            self.assertLessEqual(len(read(agents).split("\n")), 150)


class Prose(unittest.TestCase):
    """A Forja aplica a si mesma o filtro de escrita-humana.md."""

    def lint(self, patterns, message, flags=re.I, exempt_catalog=True):
        regex = re.compile("|".join(f"(?<!\\w)(?:{p})(?!\\w)" for p in patterns), flags)
        for path in md_files():
            if exempt_catalog and path.name == PATTERN_CATALOG:
                continue
            for number, line in prose_lines(path):
                with self.subTest(file=path.name, line=number):
                    found = regex.search(line)
                    self.assertIsNone(found, f"{path.name}:{number} {message}: '{found.group(0) if found else ''}'")

    def test_no_ai_vocabulary(self):
        self.lint(BANNED_STEMS, "palavra de IA")

    def test_no_filler_phrases(self):
        self.lint(BANNED_PHRASES, "frase de preenchimento")

    def test_no_decorative_adverbs(self):
        self.lint(BANNED_ADVERBS, "advérbio de enfeite")

    def test_no_not_x_is_y(self):
        self.lint([NOT_X_IS_Y.pattern.replace(r"\b", "")], "construção 'não é X, é Y'", flags=0)

    def test_no_em_dash_outside_the_catalog(self):
        for path in md_files():
            if path.name == PATTERN_CATALOG:
                continue
            for number, line in prose_lines(path):
                with self.subTest(file=path.name, line=number):
                    self.assertNotIn("—", line, f"{path.name}:{number} usa travessão")

    def test_no_emoji_outside_the_catalog(self):
        for path in md_files():
            if path.name == PATTERN_CATALOG:
                continue
            for number, line in enumerate(read(path).split("\n"), 1):
                with self.subTest(file=path.name, line=number):
                    self.assertIsNone(EMOJI.search(line), f"{path.name}:{number} tem emoji")

    def test_banned_stems_cover_catalog(self):
        row = re.search(r"^\| Palavras de IA \| (.+?) \|", read(REFS / PATTERN_CATALOG), re.M)
        self.assertIsNotNone(row, "linha 'Palavras de IA' não encontrada")
        for term in [t.strip() for t in row.group(1).split(",")]:
            with self.subTest(term=term):
                self.assertTrue(
                    any(re.fullmatch(stem, term, re.I) or re.match(stem, term, re.I) for stem in BANNED_STEMS),
                    f"'{term}' está no catálogo e falta em BANNED_STEMS",
                )




if __name__ == "__main__":
    unittest.main()

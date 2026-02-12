import subprocess
import sys


def test_roda_como_modulo():
    # Rodar como o avaliador rodaria: "python -m dataviva_desafio"
    r = subprocess.run(
        [sys.executable, "-m", "dataviva_desafio"],
        capture_output=True,
        text=True,
    )
    assert r.returncode == 0

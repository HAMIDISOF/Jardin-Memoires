#!/usr/bin/env python3
"""
verifier_peschard.py
Usage:
  python3 verifier_peschard.py <fichier.html> <source.md>
  python3 verifier_peschard.py --dossier <html_dir> <md_dir>

Vérifie pour chaque paire HTML/MD :
  1. Conformité du contenu (ratio mots capsule vs source)
  2. Troncatures / placeholders (≠ ellipses légitimes dans les citations)
  3. Navigation : liens morts
  4. Citations : refs citées in-text vs. définies dans la capsule sources
"""

import sys, re, os
from pathlib import Path

try:
    from bs4 import BeautifulSoup
except ImportError:
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "beautifulsoup4",
                    "--break-system-packages", "-q"])
    from bs4 import BeautifulSoup

# Patterns de vrais placeholders (≠ ellipses philosophiques [...])
# On cible les métadescriptions du type "[texte complet de…]", "[suite…]", etc.
PLACEHOLDER_RE = re.compile(
    r'\[texte\b|\[Le texte\b|\[suite\b|\[résumé\b|\[passage\b'
    r'|\[citation tronquée|\[abrégé|\[fin de|\[début de|\[contenu|\[ici\b'
    r'|\[extrait\]|\[\.\.\.texte|\[\.\.\.suite',
    re.IGNORECASE
)

ANSI_OK   = '\033[92m✓\033[0m'
ANSI_WARN = '\033[93m⚠\033[0m'
ANSI_ERR  = '\033[91m✗\033[0m'
ANSI_B    = '\033[1m'
ANSI_R    = '\033[0m'

def icon(ok, warn=False):
    if ok:   return ANSI_OK
    if warn: return ANSI_WARN
    return ANSI_ERR


def check_file(html_path, md_path):
    print(f"\n{ANSI_B}{'─'*60}{ANSI_R}")
    print(f"  HTML : {html_path.name}")
    print(f"  MD   : {md_path.name}")
    print(f"{'─'*60}")

    html = html_path.read_text(encoding='utf-8')
    md   = md_path.read_text(encoding='utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    errors = []
    warnings = []

    # ── 1. Vrais placeholders (pas les ellipses […] de Peschard) ──
    placeholder_hits = PLACEHOLDER_RE.findall(html)
    if placeholder_hits:
        errors.append(f"Placeholders/résumés détectés : {placeholder_hits[:5]}")
        print(f"  {ANSI_ERR} Placeholders de résumé : {placeholder_hits[:5]}")
    else:
        print(f"  {ANSI_OK} Aucun placeholder de résumé")

    # ── 2. Ratio contenu (mots capsule HTML vs mots source MD) ──
    capsules   = soup.find_all('div', class_='capsule-content')
    html_words = len(' '.join(c.get_text(' ', strip=True) for c in capsules).split())
    md_words   = len(md.split())
    ratio      = html_words / md_words if md_words else 0

    ratio_ok   = ratio >= 0.85
    ratio_warn = 0.70 <= ratio < 0.85
    ri     = icon(ratio_ok, ratio_warn)
    status = "OK" if ratio_ok else ("PARTIEL (vérifier)" if ratio_warn else "CONTENU TRONQUÉ/RÉSUMÉ")
    print(f"  {ri} Mots HTML={html_words:5d} / MD={md_words:5d}  ratio={ratio:.2f}  → {status}")
    if not ratio_ok:
        msg = f"Ratio bas ({ratio:.2f}) — contenu HTML semble incomplet ou paraphrasé"
        (errors if ratio < 0.70 else warnings).append(msg)

    # ── 3. Navigation : liens morts ──
    navs = re.findall(r'<a href="([^"]+)" class="nav-btn">([^<]*)</a>', html)
    dead = [(h, l.strip()) for h, l in navs if h.strip() in ('#', '', 'javascript:void(0)')]
    if dead:
        for h, l in dead:
            errors.append(f"Lien de navigation mort : '{l}' → '{h}'")
            print(f"  {ANSI_ERR} Lien MORT : [{l}] → {h}")
    else:
        print(f"  {ANSI_OK} Pas de lien mort")
        for h, l in navs:
            print(f"       [{l.strip()}] → {h}")

    # ── 4. Citations : cohérence refs in-text ↔ capsule sources ──
    intext_ids = set(re.findall(r'href="#(ref\d+)"', html))
    sources_div = soup.find('div', class_='sources')
    if not sources_div:
        warnings.append("Aucune capsule .sources trouvée")
        print(f"  {ANSI_WARN} Pas de capsule .sources")
    else:
        defined_ids = set(re.findall(r'id="(ref\d+)"', str(sources_div)))
        missing = intext_ids - defined_ids
        extra   = defined_ids - intext_ids
        if missing:
            errors.append(f"Refs citées in-text SANS définition .sources : {sorted(missing)}")
            print(f"  {ANSI_ERR} Refs manquantes : {sorted(missing)}")
        else:
            nums = sorted(int(r[3:]) for r in defined_ids) if defined_ids else []
            print(f"  {ANSI_OK} Citations OK — refs {nums}")
        if extra:
            print(f"  {ANSI_WARN} Refs dans .sources non citées in-text : {sorted(extra)} (normal si continuation)")

    # ── Résumé final ──
    print()
    if errors:
        print(f"  {ANSI_ERR} {len(errors)} ERREUR(S) :")
        for e in errors: print(f"     • {e}")
    if warnings:
        print(f"  {ANSI_WARN} {len(warnings)} AVERTISSEMENT(S) :")
        for w in warnings: print(f"     • {w}")
    if not errors and not warnings:
        print(f"  {ANSI_OK} TOUT OK")
    return errors, warnings


def run_dossier(html_dir, md_dir):
    html_dir = Path(html_dir)
    md_dir   = Path(md_dir)
    html_files = sorted(html_dir.glob('*.html'))
    total_err = total_warn = 0
    print(f"\n{'═'*60}")
    print(f"  Vérif. dossier  {html_dir.name}  ←→  {md_dir.name}")
    print(f"{'═'*60}")
    for hf in html_files:
        mf = md_dir / (hf.stem + '.md')
        if not mf.exists():
            print(f"\n  {ANSI_WARN} Pas de MD pour {hf.name} (ignoré)")
            continue
        errs, warns = check_file(hf, mf)
        total_err  += len(errs)
        total_warn += len(warns)
    print(f"\n{'═'*60}")
    print(f"  TOTAL : {total_err} erreur(s), {total_warn} avertissement(s)")
    print(f"{'═'*60}\n")


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 3 and args[0] == '--dossier':
        run_dossier(args[1], args[2])
    elif len(args) == 2:
        from pathlib import Path as _P
        errs, warns = check_file(_P(args[0]), _P(args[1]))
        print()
    else:
        print(__doc__)
        sys.exit(1)

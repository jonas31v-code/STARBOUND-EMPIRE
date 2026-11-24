# Idle Space Empire

Jeu incrémental de gestion spatiale en HTML, style Kittens Game, inspiré de X4: Foundations et Melvor Idle.
Un personnage seul, un petit vaisseau, puis des employés, des stations, des flottes et un empire.

## Organisation du dépôt
| Dossier | Contenu |
|---|---|
| `docs/` | GDD (conception), TDD (technique), BDS (équilibrage), schémas de données, scripts de début de partie |
| `data/` | Données de jeu en JSON : la seule source des valeurs d'équilibrage |
| `tools/` | `validate.py` : vérifie les références, l'arbre technologique et les textes |
| `balancing/` | Prototype tableur de l'économie (formules reliées au BDS) |
| `prototype/` | Prototype jouable en une page (référence de comportement, à reconstruire selon le TDD) |

## Démarrer
1. `python3 tools/validate.py` : les données doivent être valides avant tout commit.
2. Lire `AGENTS.md`, puis les documents de `docs/` utiles à votre tâche.
3. Ouvrir `prototype/idle-space-empire.html` dans un navigateur pour voir le comportement attendu.

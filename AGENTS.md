# Consignes pour les IA et les développeurs

## Projet en bref
Jeu idle spatial en HTML. Sept phases : Survivant, Indépendant, Entrepreneur, Industriel, Armateur, Magnat, Puissance spatiale.
Chaque phase s'ajoute à la précédente. Solo, hors ligne plafonné à 24 h (extensible), prestige optionnel.

## Règles
1. **Les valeurs vivent dans `data/`**, jamais dans le code. Un identifiant publié n'est jamais renommé.
2. **Aucun chiffre ne change sans vérification** : tableur `balancing/` ou simulateur (à écrire, TDD 11). Un changement = une ligne de journal.
3. **Un seul paramètre à la fois** lors de l'équilibrage (BDS 1).
4. Lancer `python3 tools/validate.py` avant chaque commit.
5. Le cœur du jeu n'accède ni au DOM, ni à l'horloge système, ni au stockage (TDD 3).
6. Hors ligne : aucune perte irréversible (aucun vaisseau détruit, aucun événement destructeur).
7. Textes visibles uniquement dans `data/lang/`.

## État (v0.1)
- Fait : GDD v0.2, TDD v0.1, BDS v0.1, schémas JSON, pack de données (17 marchandises, 20 recettes, 11 modules, 10 vaisseaux, 52 technologies), tableur de prototype, prototype jouable (phases 1 à 4, chaîne de production, saturation du marché, raids pirates, flottes, Héritage).
- Rythme validé : phase 2 vers 17 min, phase 3 vers 1 h 20 pour un joueur actif.
- Maquettes des écrans : à ajouter dans `docs/maquettes/`.

## À faire
1. Reconstruire le jeu selon le TDD (TypeScript, Vite, cœur sans interface, sauvegarde IndexedDB).
2. Écrire le simulateur sans interface et les 8 scénarios du BDS 12.
3. Autres systèmes solaires (NAV-6), factions, diplomatie, conquête, arsenal, frégates, destroyers, porte-vaisseaux.
4. Décisions ouvertes : achat intermédiaire pour passer sous 20 min d'attente en phase 2, quantité de titane au départ, rendement d'un Mineur automatisé.

## Répartition conseillée des tâches
| Tâche | Modèle |
|---|---|
| Conception, équilibrage, revues | Modèle le plus fort |
| Code (architecture, systèmes) | Modèle de code |
| Données répétitives, tests, textes | Modèle économique |
| Arbitre | `tools/validate.py`, tableur et simulateur |

## Modèle de brief par tâche
« Projet : voir AGENTS.md. Tâche : <une phrase>. Documents à lire : <liste>. Contraintes : règles ci-dessus. Livrable : <fichiers>. Critère : `python3 tools/validate.py` passe. »

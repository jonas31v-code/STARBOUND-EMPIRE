# TDD – Idle Space Empire (v0.1)

Technical Design Document – document 2 sur 3 (GDD → TDD → BDS)

Public : équipe de développement. Ce document décrit comment réaliser techniquement le jeu défini dans le GDD v0.2 ; les numéros de section renvoient au GDD. Les valeurs d'équilibrage ne figurent pas ici : elles vivent dans des fichiers de données gérés par l'équipe d'équilibrage.

## 1. Objectifs techniques

1. Jeu entièrement côté navigateur, en solo, sans serveur (hébergement statique).
2. Toutes les valeurs d'équilibrage dans des fichiers de données, jamais dans le code.
3. Simulation fiable : mêmes résultats que le joueur soit présent ou absent.
4. Cœur du jeu indépendant de l'interface, pour pouvoir le lancer sans navigateur (simulateur d'équilibrage).
5. Sauvegardes durables, versionnées et migrables.
6. Contenu extensible : ajouter une marchandise, un module ou une technologie = ajouter une entrée de données.

## 2. Stack recommandée

| Domaine | Choix | Raison |
| --- | --- | --- |
| Langage | TypeScript (mode strict) | Beaucoup de structures de données ; le typage évite les erreurs |
| Build | Vite | Rapide, produit un site statique |
| Interface | HTML5 + CSS, composants légers (Preact ou JavaScript natif) | Interface en panneaux, pas de moteur de jeu |
| État | Un objet unique sérialisable | Sauvegarde simple, tests faciles |
| Données | JSON + validation par schéma (Zod) | Erreurs détectées au chargement |
| Stockage | IndexedDB (bibliothèque idb) + export/import de fichier | Plus fiable et plus gros que localStorage |
| Tests | Vitest | Tests unitaires et de simulation |
| Simulateur | Node.js, même code de cœur | Équilibrage sans navigateur |
| Hébergement | Statique | Pas de backend |

Navigateurs visés : dernières versions de Chrome, Firefox, Edge et Safari. Ordinateur d'abord ; tablette et mobile lisibles. L'équipe peut choisir JavaScript pur, mais le typage est recommandé.

## 3. Architecture

### 3.1 Couches

| Couche | Rôle | Règle |
| --- | --- | --- |
| Données (data/) | Définitions statiques en JSON | Lecture seule |
| Cœur (core/) | État et systèmes de simulation | Aucun accès au DOM, à l'horloge système ni au stockage |
| Services | Sauvegarde, horloge, langue | Seule couche qui touche le navigateur |
| Interface (ui/) | Affichage et commandes du joueur | Lit l'état, envoie des commandes, ne le modifie jamais directement |

### 3.2 Principes

- **État unique** (GameState) fait d'objets simples : pas de classes à méthodes, pas de références circulaires ; les relations passent par des identifiants.
- **Systèmes** = fonctions qui prennent l'état, les définitions et une durée, et mettent l'état à jour.
- **Commandes** : le joueur agit par commandes (acheter, affecter, lancer une recherche) que le cœur valide. Elles sont faciles à tester et à journaliser.
- **Événements** : un bus interne prévient l'interface et le journal (fin de production, vaisseau arrivé, succès).
- **Aléatoire** : générateur à graine, dont l'état est stocké dans la sauvegarde, pour des résultats reproductibles.

### 3.3 Modules du cœur

| Module | Responsabilité | GDD |
| --- | --- | --- |
| GameEngine | Horloge de simulation, ordre des systèmes | 3 |
| ResourceManager | Stocks, capacités, transferts | 8 |
| ProductionSystem | Modules, recettes, énergie | 9, 19 |
| CharacterSystem | Compétences, maîtrise, activité personnelle | 5 |
| EmployeeSystem | Recrutement, postes, salaires, expérience | 6 |
| FleetSystem | Vaisseaux, états, équipages, missions, flottes | 7, 20 |
| TradeSystem | Prix, routes, contrats | 8 |
| UniverseSystem | Systèmes, secteurs, stations | 11, 21 |
| FactionSystem | Relations, licences | 21 |
| CombatSystem | Résolution des combats | 10 |
| ResearchSystem | Technologies, files de recherche | 18 |
| EventSystem | Événements, journal, succès | 12 |
| OfflineSystem | Rattrapage hors ligne | 13 |
| PrestigeSystem | Réinitialisation et bonus permanents | 14 |
| SaveService | Persistance | – |

## 4. Données de jeu

Les fichiers du dossier data/ sont validés au démarrage.

| Fichier | Contenu | GDD |
| --- | --- | --- |
| goods.json | Marchandises : identifiant, famille, prix de référence | 19.2 |
| recipes.json | Recettes : module, entrées, sorties, durée, énergie, déblocage | 19.3 |
| modules.json | Modules : coût, temps de construction, énergie, personnel, stockage | 9 |
| ships.json | Classes : caractéristiques, emplacements, recette de construction, coût | 20 |
| equipment.json | Modules d'équipement Mk1 à Mk3 | 20.4 |
| technologies.json | Arbre : branche, palier, prérequis, coût, durée, effets | 18 |
| skills.json | Compétences, paliers, bonus, courbes d'expérience | 5 |
| employees.json | Raretés, noms, tables de génération | 6 |
| universe.json | Systèmes, secteurs, stations, gisements | 21.1 |
| factions.json | Factions, production, demande, paliers de relation | 21 |
| contracts.json, events.json | Gabarits de contrats et d'événements | 21.5 |
| achievements.json | Succès | 12 |

**Règles**

- Chaque entrée a un **identifiant stable** (chaîne en minuscules, par exemple iron\_ore). Il n'est jamais renommé après publication, car les sauvegardes s'y réfèrent.
- Les effets des technologies suivent un vocabulaire fermé : **unlock** (recette, module, vaisseau, onglet), **modifier** (cible, opération additive ou multiplicative, valeur) et **limit** (plafond hors ligne, nombre de files de recherche).
- Les textes visibles sont dans des fichiers de langue, avec l'identifiant comme clé ; le français est la langue par défaut.
- La validation échoue au chargement, avec un message clair, si un identifiant référencé n'existe pas ou si une marchandise n'est utilisée par aucune recette, technologie ou vaisseau (GDD 8.1).
- En développement, les fichiers se rechargent à chaud pour l'équilibrage.

## 5. État de jeu

| Bloc | Contenu |
| --- | --- |
| meta | Version de sauvegarde, identifiant, horodatage du dernier calcul (lastTick), temps de jeu total, graine aléatoire |
| player | Crédits, compétences (niveau, expérience, maîtrise par action), activité en cours, vaisseau personnel, équipement |
| stations | Modules construits (recette active, progression du cycle, état), stocks, personnel, énergie |
| fleet | Vaisseaux : classe, modules, état, coque, équipage, mission, position, carburant |
| employees | Profil, niveau, expérience, poste, salaire |
| research | Technologies terminées, files, progression |
| universe | Secteurs découverts, prix locaux, niveaux de risque |
| factions | Relation par faction, licences |
| contracts | Contrats actifs et disponibles |
| events | Journal et événements en cours |
| prestige | Points et bonus permanents |
| settings | Langue, notation des nombres, paramètres hors ligne |

L'état contient des valeurs et des identifiants, jamais des valeurs d'équilibrage recopiées depuis les données.

## 6. Boucle de simulation

Le temps de jeu avance à partir d'**horodatages**, jamais en comptant les secondes dans le navigateur.

```
à chaque seconde (et à chaque retour d'un onglet masqué) :
  maintenant = horloge.now()
  écoulé = maintenant - state.meta.lastTick
  si écoulé > seuil_de_rattrapage : lancer OfflineSystem (section 7)
  sinon : tant que écoulé >= 1 s : step(1 s) ; écoulé -= 1 s
  state.meta.lastTick = maintenant - écoulé
```

Ordre fixe des systèmes dans un pas :

1. Recherche
2. Production (énergie, puis modules)
3. Flotte (déplacements, extraction, chargement et déchargement)
4. Commerce (prix, contrats)
5. Employés (salaires)
6. Combat
7. Événements et succès

**Règles**

- Pas de simulation fixe de 1 seconde de jeu. L'affichage se met à jour à 4 images par seconde pour les valeurs.
- Les navigateurs ralentissent les minuteurs d'un onglet masqué : sans importance, car la simulation se rattrape avec l'horodatage.
- Chaque cycle (production, recherche, activité) garde un champ progress en secondes, pour pouvoir être interrompu puis repris.
- Un paramètre d'échelle de temps (1 par défaut, ×10 ou ×100 pour les tests) est prévu dès le départ.
- Si l'horloge système recule (écoulé négatif), on le traite comme 0 : aucun gain, aucune perte.

## 7. Simulation hors ligne

Spécification fonctionnelle : GDD 13.

1. **Durée** : écoulé = min(now - lastTick, plafond hors ligne). Le plafond vient de l'état (24 h au départ, augmenté par SCI-3, SCI-5 et SCI-7).
2. **Pas agrégés** : on découpe en pas de 60 s jusqu'à 6 h, puis de 300 s au-delà (réglable dans la configuration ; objectif : environ 1 500 pas au plus pour 24 h).
3. **Mêmes systèmes** que la simulation normale, avec dt égal à la taille du pas, mais en **mode hors ligne** : aucun événement destructeur, aucun combat déclenché, aucune perte de vaisseau (GDD 13, 20.6).
4. **Cycles courts** : un cycle plus court que le pas est traité par le nombre de cycles complets réalisables ; le temps restant est conservé dans progress.
5. **Bilan** : on collecte ressources produites, crédits gagnés, salaires payés, arrêts de production et recherches terminées pour l'écran de retour.

**Contraintes**

- Un rattrapage de 8 h doit donner le même résultat qu'une simulation en ligne de 8 h, à 2 % près sur les ressources totales (testé automatiquement, section 13).
- Les prix locaux reviennent vers leur prix de référence plutôt que de réagir à chaque transaction. L'efficacité hors ligne est un paramètre de configuration (BDS 11) : 100 % pour la production et la recherche, 90 % pour le commerce automatisé, 0 % pour l'activité personnelle.
- Le calcul tourne dans un **Web Worker** pour ne pas figer l'interface ; un indicateur de progression s'affiche au-delà d'une seconde.
- Le journal hors ligne est résumé : une ligne par type d'événement, pas une par pas.

## 8. Systèmes en détail

### 8.1 Production

Chaque module suit une machine à états : **inactif**, **en cours**, **bloqué** (entrée manquante, sortie pleine, énergie ou personnel insuffisant).

- Au démarrage d'un cycle : vérification des entrées, de l'énergie et du personnel ; consommation des entrées ; progress augmente.
- À la fin : dépôt des sorties dans le stock de la station ; s'il n'y a pas de place, le module se bloque.
- **Énergie** : par station, on compare production et demande. Si la demande dépasse la production, tous les modules tournent au ratio production / demande, et leurs cycles s'allongent d'autant.
- Les bonus (technologies, employés, maîtrise) modifient la durée, l'énergie ou la quantité produite, **jamais les ratios d'entrée** (GDD 19.1).

### 8.2 Commerce et prix

Prix local d'une marchandise dans une station (formule de départ, que le BDS pourra remplacer) :

```
ratio = stock / stock_cible
prix  = prix_reference * clamp(1.6 - 0.6 * ratio, 0.5, 2.0)
```

Un stock vide donne 1,6 fois le prix de référence, un stock égal à la cible donne 1,0 et un stock double de la cible donne 0,5.

- **Route commerciale** : le vaisseau va en A, charge (limité par son cargo, les stocks et les prix minimum et maximum), va en B, décharge et vend, puis revient. Durée du trajet = distance / vitesse. La quantité achetée est limitée par les crédits disponibles du joueur : la cargaison peut être partielle.
- Les **ordres conditionnels** (prix min/max, stocks minimums) sont évalués à chaque étape.
- Une station peut exiger une **licence** pour commercer (COM-7).
- La rentabilité d'une route est calculée à la demande, jamais stockée. Les stations non joueur consomment et produisent en continu selon factions.json, avec un stock cible et une consommation de base par famille de marchandises (BDS 3.3) ; cette simulation de fond fait partie du système de commerce.

### 8.3 Univers et flotte

- L'univers est un **graphe** : les secteurs sont des nœuds, les liaisons des arêtes avec une distance. Les plus courts chemins sont calculés à la création (Dijkstra) et mis en cache.
- Un vaisseau a pour position un secteur et une progression sur le trajet en cours (pas de coordonnées 2D).
- Une mission est une suite d'étapes : aller, charger, décharger, extraire, patrouiller.
- Le carburant se consomme pendant les trajets ; l'entretien (0,2 % du prix d'achat par heure d'activité) et les salaires d'équipage sont prélevés en continu (BDS 8). Un manque de carburant ou d'équipage immobilise le vaisseau (GDD 20.6).

### 8.4 Personnage et employés

- Les courbes d'expérience viennent de skills.json. La maîtrise est comptée par action. Une seule activité personnelle à la fois, qui avance par progress comme un cycle. Une activité lancée se répète automatiquement jusqu'à ce que le joueur en choisisse une autre, et le minage manuel est vendu directement à la station du secteur, sans passer par la soute du vaisseau.
- Les employés sont générés à partir de tables ; le marché de recrutement se renouvelle à intervalle fixe.
- Les salaires sont prélevés en continu. Si les crédits sont insuffisants, les employés non payés deviennent **inactifs** : pas de dette négative, pas de licenciement automatique.

### 8.5 Combat

Résolution automatique et **déterministe** (graine) :

- Rounds de 1 seconde de jeu ; chaque vaisseau tire sur une cible choisie selon la doctrine.
- Dégâts = armes × précision × (1 - réduction) ; les boucliers absorbent en premier et se régénèrent.
- Fin du combat : un camp est détruit ou en fuite, ou le nombre maximal de rounds est atteint.
- Entrée : deux listes de vaisseaux, une doctrine, un commandant. Sortie : un rapport (pertes, dégâts, butin).
- La résolution est une **fonction pure**, facile à tester. Les formules détaillées sont dans le BDS.

### 8.6 Recherche et modificateurs

- Une recherche à la fois au départ (deux avec SCI-6). Le coût est payé au démarrage ; la progression se compte en secondes.
- Les effets ne sont **jamais écrits en dur dans l'état** : ils se recalculent à partir de la liste des technologies terminées. On peut donc modifier l'équilibrage sans casser les sauvegardes.
- Valeur finale = base × (1 + somme des bonus additifs) × produit des multiplicateurs. Un pipeline unique sert pour technologies, maîtrise, employés, équipements et prestige. Le résultat est mis en cache et invalidé quand une source change.

## 9. Sauvegarde

- **IndexedDB**, trois emplacements plus une sauvegarde automatique.
- Enregistrement automatique toutes les 30 secondes, et lors du masquage de l'onglet ou de la fermeture.
- Format : JSON de l'état avec un en-tête (version de sauvegarde, version du jeu, horodatage, somme de contrôle).
- **Migrations** : une fonction par version (n vers n+1), testée. Une copie de secours est conservée avant chaque migration.
- **Export et import** par fichier JSON (éventuellement compressé et encodé en base64).
- Si un identifiant n'existe plus dans les données après un changement d'équilibrage, la migration le remplace ou le supprime proprement ; jamais de plantage.
- **Plusieurs onglets** : un verrou (Web Locks) empêche deux onglets d'écrire en même temps ; le second passe en lecture seule avec un message.

## 10. Interface

- Panneaux en onglets, débloqués progressivement (GDD 15).
- Les composants reçoivent des sélecteurs de l'état et des fonctions de commande. L'affichage se met à jour à 4 Hz, pas à chaque pas de simulation.
- Barre de ressources permanente : crédits, énergie, ressources principales, date de jeu, taux par seconde.
- Notation des nombres configurable : compacte (1,2 M), scientifique ou complète ; séparateurs selon la langue.
- Listes longues (marchandises, vaisseaux, employés) : tri, filtre et virtualisation au-delà de 200 lignes.
- Carte en SVG générée à partir de universe.json, sans moteur de rendu lourd.
- Accessibilité : navigation au clavier, contrastes suffisants, aucune information portée par la couleur seule, animations réduites selon la préférence du système.
- Écran de bilan au retour, journal et notifications non bloquantes.
- Français d'abord, structure prête pour l'anglais.

## 11. Outils pour l'équilibrage

À livrer avec le MVP :

1. **Simulateur sans interface (Node.js)** : exécute le cœur avec des scénarios scriptés (joueur actif 30 minutes et 2 heures, retour après 8 h et 24 h, profils commerce, industrie, combat) et produit des fichiers CSV (ressources, crédits, niveaux, technologies par minute).
2. **Console de debug**, désactivable en production : accélération du temps, ajout de crédits et de marchandises, déblocage d'une technologie, saut à une phase, import d'un état de test.
3. **Export de données** : un script transforme les JSON en tableur pour l'équipe d'équilibrage et réimporte leurs modifications.
4. **Rapports automatiques** : temps pour atteindre chaque phase, rentabilité de chaque recette et de chaque route type, répartition du temps de jeu par activité.
5. **Rechargement à chaud** des données en développement.

## 12. Performance

Profil de référence pour la v1 complète : 22 secteurs, 60 stations, 300 modules, 300 vaisseaux, 150 employés, 50 technologies.

| Mesure | Budget |
| --- | --- |
| Pas de simulation de 1 s | Moins de 5 ms |
| Rattrapage hors ligne de 24 h | Moins de 3 s, hors affichage |
| Affichage de l'interface principale | 60 images par seconde sur un ordinateur ordinaire |
| Taille d'une sauvegarde | Moins de 2 Mo |
| Chargement initial | Moins de 3 s sur une connexion ordinaire |

Pratiques : structures simples, pas d'allocation dans la boucle chaude, vaisseaux regroupés par secteur, aucun calcul de chemin dans la boucle (cache).

## 13. Tests et qualité

| Type | Cible | Critère |
| --- | --- | --- |
| Unitaires | Chaque système (production, prix, expérience, combat, recherche) | Cas nominaux et limites |
| Déterminisme | Même état, même graine, mêmes commandes | Résultat identique |
| Hors ligne contre en ligne | 8 h simulées des deux façons | Écart de 2 % au plus |
| Sauvegarde | Enregistrer puis recharger | État identique ; migration depuis chaque ancienne version |
| Données | Validation de tous les JSON | Aucune référence cassée, aucune marchandise inutile |
| Régression d'équilibrage | Scénarios du simulateur | Rapport comparé à la version précédente, écarts signalés |
| Interface | Parcours principaux | Tests de bout en bout sur les panneaux clés |

L'intégration continue lance le contrôle de style, les types, les tests et la validation des données à chaque envoi de code.

## 14. Jalons de développement

Alignés sur les phases du GDD (section 16).

| Jalon | Contenu | Critère d'acceptation |
| --- | --- | --- |
| J0 Socle | Projet, données et validation, état, boucle, sauvegarde, simulateur minimal | Une simulation de 24 h tourne dans le simulateur ; sauvegarde et chargement fonctionnent |
| J1 MVP | Personnage et compétences, ressources, extraction, premiers modules, recrutement, hors ligne, interface principale | Un joueur peut jouer 2 h, partir 8 h et revenir avec un bilan |
| J2 Économie | Vaisseaux, routes, commerce, stations, salaires, stocks | Une route automatique rentable tourne hors ligne ; la phase 3 du GDD est jouable |
| J3 Expansion | Plusieurs secteurs, exploration, factions, recherche avancée | Accès aux autres systèmes par les portes de saut ; relations fonctionnelles |
| J4 Militaire | Flottes, combat, escorte, piraterie, conquête | Combat déterministe testé ; conquête d'un secteur |
| J5 Endgame | Infrastructures, prestige, événements majeurs, succès | Prestige fonctionnel ; migrations testées |

Chaque jalon livre un build jouable, les données à jour, un rapport du simulateur et des notes de version pour l'équipe d'équilibrage.

## 15. Risques et questions ouvertes

- **Hors ligne par pas agrégés** : un écart avec la simulation en ligne est possible si les cycles sont courts. À mesurer dès J0.
- **Chaîne du moteur** : le titane est un goulot probable ; à suivre avec le simulateur.
- **Taille de l'état** : surveiller la sauvegarde quand la flotte grandit.
- **Interface** : Preact ou JavaScript natif, à décider par l'équipe avant J0.
- **Langues** : prévoir les fichiers de langue dès le départ pour éviter de réécrire les textes.
- **Décisions ouvertes du GDD** (section 22.1) : à trancher avant le BDS.

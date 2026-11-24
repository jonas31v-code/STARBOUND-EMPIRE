# GDD – Idle Space Empire (v0.2)

Game Design Document – document 1 sur 3 (GDD → TDD → BDS)

Public : équipe de game design et de développement. Les valeurs chiffrées sont des ordres de grandeur illustratifs ; elles seront fixées par le document d'équilibrage (BDS).

## 1. Vision

**Idle Space Empire** est un jeu incrémental de gestion spatiale, jouable dans un navigateur (HTML/JavaScript), en solo. Le joueur incarne un personnage seul, avec un petit vaisseau et presque aucune ressource, et construit peu à peu un empire : employés, vaisseaux automatisés, stations industrielles, flottes commerciales et militaires.

**Références et ce qu'on en retient**

- *Kittens Game* : ressources interdépendantes, population affectée à des postes, bâtiments, technologies, progression très longue.
- *Melvor Idle* : compétences individuelles, actions répétables, maîtrise par action, spécialisation.
- *X4: Foundations* : univers économique vivant, production et consommation, commerce automatisé, factions. On ne reproduit pas sa simulation 3D : tout est abstrait en secteurs, stations et routes.

**Piliers de design**

1. **Chaque phase s'ajoute à la précédente.** Le personnage et son petit vaisseau restent utiles même avec 50 transporteurs.
2. **L'automatisation se mérite.** Elle est une récompense de progression, pas un état initial.
3. **Interdépendance.** Le commerçant a besoin de l'industrie, l'industriel du transport, le militaire des produits des deux.
4. **Choix et coûts d'opportunité.** Un employé, un vaisseau ou un crédit investi à un endroit ne l'est pas ailleurs.
5. **L'argent est un moyen.** Les crédits ne suffisent jamais seuls : ressources, technologies, licences, personnel et capacité de stockage limitent aussi la progression.
6. **Lisibilité.** Beaucoup de données, mais une interface en panneaux claire.

## 2. Décisions de cadrage

| Sujet | Décision |
| --- | --- |
| Taille de l'univers | Une galaxie avec quelques systèmes solaires conçus à la main (pas de procédural en v1) |
| Économie | Prix dynamiques simples selon l'offre et la demande locales ; pas de simulation détaillée de chaque faction au départ |
| Combat | Automatique, avec préparation tactique et quelques ordres du joueur |
| Personnage | Reste au centre du jeu pendant toute la partie, avec des activités personnelles toujours rentables |
| Progression hors ligne | Plafond de 24 h, extensible par la recherche |
| Prestige | Optionnel, avec bonus permanents |
| Multijoueur | Solo uniquement |
| Interface | Panneaux façon Kittens Game, avec une carte spatiale simple dans un onglet |
| Complexité | Moyenne : quelques chaînes de production lisibles |

**Contenu cible de la v1 :** 15 à 20 marchandises, 3 à 4 systèmes solaires, 3 factions, 8 à 10 classes de vaisseaux.

## 3. Boucle de jeu

### 3.1 Boucle courte (secondes à minutes)

Le joueur lance une activité personnelle (miner, explorer, faire une mission, commercer à la main), gagne des ressources, des crédits et de l'expérience, puis dépense dans une amélioration, un équipement ou un recrutement.

### 3.2 Boucle moyenne (dizaines de minutes à heures)

Le joueur recrute des employés, achète des vaisseaux et les affecte à des tâches. Les revenus passifs (extraction, routes commerciales) financent les salaires et la croissance. Il doit gérer les stocks, les pénuries et les coûts d'entretien.

### 3.3 Boucle longue (jours à semaines)

Le joueur construit des stations, des chaînes de production et des flottes, explore de nouveaux systèmes, nouvelle faction après nouvelle faction, atteint des objectifs d'endgame et peut déclencher un prestige.

### 3.4 Principe idle

Le jeu doit rester intéressant quand le joueur est présent et quand il ferme l'onglet :

- **Niveau 1, activité personnelle (actif)** : compétences, exploration, missions, combat.
- **Niveau 2, automatisation (idle)** : employés et vaisseaux produisent, extraient, transportent.
- **Niveau 3, empire (idle)** : stations, flottes, territoires, guerre.

Le joueur ne doit jamais être obligé de cliquer toutes les secondes. Les actions manuelles restent intéressantes (bonus, vitesse, accès à du contenu unique) mais jamais obligatoires à long terme.

## 4. Progression en sept phases

| # | Phase | Situation du joueur | Déblocage principal |
| --- | --- | --- | --- |
| 1 | Survivant | Un personnage, un petit vaisseau, peu de crédits | Minage manuel, premières ventes |
| 2 | Indépendant | Exploration, minage, missions, commerce manuel | Compétences, premières technologies |
| 3 | Entrepreneur | Premiers employés, premiers vaisseaux automatisés | Recrutement, routes simples (COM-4 requis) |
| 4 | Industriel | Stations, chaînes de production, logistique | Modules, recettes, entrepôts |
| 5 | Armateur | Flottes commerciales et militaires | Chantier naval, commandants |
| 6 | Magnat | Plusieurs secteurs, plusieurs activités | Licences, diplomatie |
| 7 | Puissance spatiale | Territoires, grandes flottes, guerre | Conquête, mégastructures |

Chaque phase est débloquée par des **conditions explicites** (niveau de compétence, technologie, possession d'un bâtiment ou d'un vaisseau), jamais par un simple seuil de crédits. La phase 3 se déclenche au début du premier trajet automatique d'un vaisseau piloté par un employé. Aucune phase ne remplace la précédente.

## 5. Le personnage

Le personnage est le point de départ et reste utile pendant toute la partie.

### 5.1 Compétences

Sept compétences, regroupées en cinq catégories :

| Catégorie | Compétences |
| --- | --- |
| Navigation | Pilotage, Exploration |
| Industrie | Minage, Ingénierie |
| Économie | Commerce |
| Militaire | Combat, Commandement |
| Science | Recherche |

Chaque compétence possède un niveau général, de l'expérience, des actions spécifiques et des bonus par palier. Exemple pour le minage (valeurs illustratives) :

| Niveau | Déblocage |
| --- | --- |
| 1 | Extraction manuelle |
| 5 | Astéroïdes riches : minage manuel de silicium |
| 10 | Extraction spécialisée |
| 20 | Minerais rares |
| 30 | Extraction avancée |

### 5.2 Maîtrise (inspirée de Melvor Idle)

En plus du niveau de compétence, chaque **action** (par exemple miner du fer, livrer du cuivre) possède sa propre maîtrise, qui progresse avec la répétition et donne des bonus propres à cette action. Le joueur continue donc de progresser dans une activité même quand son niveau général est élevé.

### 5.3 Règles de progression

- Une seule activité personnelle à la fois, qui se répète automatiquement jusqu'à ce que le joueur en choisisse une autre ; le minage manuel est vendu directement à la station du secteur, sans passer par la soute du vaisseau.
- Le joueur choisit ce qu'il développe : pas de progression simultanée de toutes les compétences.
- Les compétences améliorent aussi l'empire : Commerce améliore les marges des routes, Commandement améliore les équipages, Recherche accélère les technologies.
- Le personnage peut piloter un vaisseau lui-même ou le laisser à un employé : c'est un arbitrage, pas un automatisme.

## 6. Employés et équipages

C'est le système central de la transition entre phase 2 et phase 3.

### 6.1 Catégories

| Type | Rôle |
| --- | --- |
| Employés | Production, recherche, gestion des stations |
| Équipages | Pilotage et fonctionnement des vaisseaux |
| Officiers | Commandement et bonus spécialisés |

### 6.2 Caractéristiques d'un employé

- Nom, compétence principale, spécialisation.
- Niveau et expérience.
- Salaire (versé en continu).
- Efficacité de travail.
- Rareté (commun, expérimenté, expert, légendaire).

Exemple : *Ingénieur industriel, niveau 12, rareté expérimenté, spécialité production, +25 % de production, -5 % de consommation d'énergie, salaire d'environ 1 620 crédits par heure (formule du BDS, section 5).*

### 6.3 Postes

Directeur de station, ingénieur, technicien, chercheur, pilote, commandant, responsable commercial. Un employé n'est pas aussi bon à tous les postes : sa compétence principale détermine son efficacité.

### 6.4 Règles

- Un employé occupe un seul poste à la fois.
- Les salaires sont une dépense continue : un empire trop grand pour ses revenus s'effondre.
- Les employés gagnent de l'expérience en travaillant.
- Le marché de recrutement se renouvelle régulièrement avec des profils différents.
- Un bon employé peut être gardé auprès du joueur (bonus sur ses activités) ou placé dans une usine : arbitrage volontaire.

## 7. Vaisseaux

### 7.1 Classes de la v1

| Classe | Usage |
| --- | --- |
| Éclaireur | Exploration |
| Mineur | Extraction automatisée |
| Transporteur S / M / L | Commerce, du petit au lourd |
| Chasseur | Combat léger |
| Corvette | Escorte |
| Frégate | Combat polyvalent |
| Destroyer | Puissance militaire |
| Porte-vaisseaux | Gestion de flotte (endgame) |

### 7.2 Caractéristiques

Coque, boucliers, vitesse, capacité de chargement, consommation de carburant, consommation d'énergie, équipage requis, armement, emplacements de modules.

### 7.3 Modes

- **Piloté** par le joueur : bénéficie des compétences du personnage, peut faire des missions et explorer.
- **Automatisé** : assigné à une route, une mine ou une station, il travaille seul avec un pilote employé.

Un vaisseau sans équipage suffisant ne peut pas fonctionner. Les vaisseaux automatisés coûtent du carburant, de l'entretien et des salaires.

## 8. Économie, marchandises et commerce

### 8.1 Marchandises

Cible v1 : **15 à 20** marchandises. Règle absolue : chaque marchandise doit servir à au moins une chaîne de production, une technologie, un bâtiment ou un équipement.

| Famille | Exemples |
| --- | --- |
| Matières premières | Minerai de fer, minerai de cuivre, silicium, carbone, glace, minerai de titane |
| Métaux raffinés | Acier, cuivre raffiné, alliage de titane |
| Chimie | Polymères |
| Électronique | Circuits |
| Industrie avancée | Composants mécaniques, moteurs, boucliers |
| Énergie | Électricité, carburant |
| Militaire | Munitions, missiles |
| Recherche | Données scientifiques |

Les crédits sont la monnaie ; les données scientifiques servent à la recherche.

### 8.2 Exemple de chaîne

Minerai de fer, cuivre, silicium et titane → acier, cuivre raffiné, circuits, alliage de titane → composants mécaniques → moteur spatial → utilisé pour fabriquer ou améliorer des vaisseaux, ou revendu.

### 8.3 Prix

Les prix sont dynamiques et locaux : ils montent quand le stock d'une station est bas, baissent quand il est saturé. Chaque marchandise a un prix de référence. Les écarts de prix entre stations créent les opportunités de commerce.

### 8.4 Commerce

Le joueur peut :

- acheter et vendre manuellement ;
- créer des routes commerciales automatiques entre deux stations ;
- définir des prix minimum et maximum, et des stocks minimums ;
- affecter des transporteurs à une station pour l'approvisionner. Une route achète dans la limite des crédits disponibles : sa cargaison est partielle si le joueur manque de crédits.

## 9. Industrie et stations

Une station est un ensemble de **modules** que le joueur achète et ajoute (pas de construction libre en v1).

| Module | Fonction |
| --- | --- |
| Mine | Extraction |
| Raffinerie | Transformation des minerais |
| Usine chimique | Composés chimiques, carburant |
| Usine électronique | Circuits, boucliers |
| Atelier mécanique | Composants mécaniques et moteurs (IND-7) |
| Arsenal | Munitions et missiles (MIL-6) |
| Centrale | Énergie : panneaux solaires dès le départ, centrale à carburant avec IND-6 |
| Entrepôt | Stockage |
| Laboratoire | Recherche |
| Chantier naval | Construction de vaisseaux |

Chaque module définit : coût de construction, temps de construction, besoin en énergie, besoin en personnel, production ou capacité. Chaque station a une **capacité de stockage limitée** ; une production sans place s'arrête, un manque d'intrant l'arrête aussi.

## 10. Combat et sécurité

Le combat est **résolu automatiquement** après préparation. Le joueur donne des ordres : attaquer, escorter, défendre une station, patrouiller, intercepter.

Le résultat dépend de : puissance et équipement des vaisseaux, qualité des équipages, compétence du commandant, doctrine tactique et composition de la flotte. Ce n'est jamais une simple comparaison de deux nombres : un bon contre-choix de composition doit pouvoir battre une flotte plus puissante.

Conséquences : dégâts de coque, réparations, pertes d'équipage, munitions consommées, coûts d'entretien.

**Priorité :** le combat arrive en phase 4 de développement. Les phases 1 à 3 n'incluent que des rencontres simples (pirates sur une route) pour valider le principe.

## 11. Univers et factions

- Une galaxie de quelques systèmes solaires, chacun divisé en secteurs.
- Chaque secteur possède : ressources, stations, routes, niveau de risque, faction dominante.
- Trois factions en v1 : une industrielle (métaux), une commerciale neutre, une pirate. Une faction militaire expansionniste peut venir en phase 4.
- Les relations avec une faction se gagnent par contrats, livraisons et missions. Elles débloquent des licences commerciales, des technologies et des marchés.
- La guerre et la conquête arrivent en phase 5 de développement.

## 12. Systèmes transversaux

| Système | Description |
| --- | --- |
| Recherche | Arbre technologique avec prérequis ; débloque bâtiments, vaisseaux, bonus, plafond hors ligne |
| Équipement | Amélioration du personnage et des vaisseaux |
| Missions | Transport, extraction, combat |
| Événements | Découvertes, attaques, pénuries, opportunités |
| Entretien | Salaires, réparations, carburant |
| Automatisation | Priorités, seuils, ordres programmés |
| Succès | Objectifs et récompenses |
| Journal | Historique des opérations et événements |

## 13. Progression hors ligne

Simulation obligatoire. À la reconnexion, le jeu calcule ce qui s'est passé depuis la dernière sauvegarde : extraction, transformation, routes, consommation d'énergie, salaires.

**Règles :**

- Plafond initial de **24 h**, augmentable par la recherche.
- Le calcul se fait à partir du **temps écoulé entre deux sauvegardes**, jamais en comptant les secondes dans le navigateur.
- Les contraintes s'appliquent : stocks saturés, manque de ressources, vaisseaux immobilisés, stations à l'arrêt.
- **Aucune perte irréversible** à cause d'un événement aléatoire hors ligne : au pire, une station est arrêtée ou un vaisseau immobilisé, jamais détruit.
- Un écran de bilan résume ce qui s'est passé pendant l'absence.

## 14. Prestige

Optionnel. Le joueur peut réinitialiser sa progression contre des bonus permanents (par exemple : vitesse d'apprentissage, qualité du marché de recrutement, plafond hors ligne). Le prestige ne bloque jamais l'accès au contenu principal.

## 15. Interface

Panneaux en onglets, façon Kittens Game et Melvor Idle, avec une barre de ressources permanente (crédits, énergie, ressources principales, date du jeu).

| Onglet | Contenu |
| --- | --- |
| Personnage | Compétences, équipement, activité en cours |
| Vaisseaux | Flotte, améliorations, affectations |
| Employés | Recrutement, postes, salaires |
| Industrie | Stations, modules, production |
| Commerce | Marchandises, prix, routes |
| Recherche | Technologies |
| Militaire | Flottes, ordres, doctrines |
| Univers | Carte simple, secteurs, factions, diplomatie |

Les onglets sont débloqués progressivement pour ne pas submerger le débutant.

## 16. Plan de développement

| Phase | Contenu |
| --- | --- |
| MVP | Personnage et compétences, ressources et production, extraction et fabrication, premiers bâtiments, recrutement, sauvegarde et hors ligne, interface principale |
| Économie | Vaisseaux, transport, commerce automatisé, routes, stations industrielles, stocks et salaires |
| Expansion | Plusieurs secteurs, exploration, factions, diplomatie, recherche avancée, ressources rares |
| Militaire | Flottes, combats automatiques, escorte, piraterie, conquête, guerres |
| Endgame | Grandes infrastructures, technologies avancées, prestige, événements majeurs |

Critère de passage : **la phase Économie doit déjà être amusante** avant de commencer l'Expansion.

## 17. Prochains documents

- **TDD** (équipe de développement) : architecture JavaScript modulaire, données de jeu en JSON séparées du code, sauvegarde locale (IndexedDB), moteur de simulation basé sur le temps écoulé.
- **BDS** (équipe d'équilibrage) : coûts, temps, productions, salaires, courbes d'expérience, prix de référence, puissances, et scénarios de test (joueur actif 30 min et 2 h, retour après 8 h et 24 h, profils commerce, industrie, combat).

Les chapitres détaillés (arbre de recherche, recettes, fiches de vaisseaux, univers et factions) sont rédigés dans les sections 18 à 21 (ajouts v0.2).

## 18. Arbre de recherche (ajout v0.2)

### 18.1 Principes

- Environ **50 technologies** en v1, réparties en **6 branches**, chacune en 5 paliers (T1 à T5) qui correspondent grosso modo aux phases de progression (T1 = phases 1-2, T2 = phase 3, T3 = phase 4, T4 = phases 5-6, T5 = phase 7).
- Chaque technologie a un identifiant (ex. NAV-3), des **prérequis** (dans la même branche ou dans une autre), un **coût** et un **temps de recherche**.
- Coût = **données scientifiques + crédits**, parfois une marchandise (ex. circuits pour l'électronique). Les valeurs exactes sont fixées par le BDS ; le GDD ne définit que l'ordre de grandeur par palier.
- Une technologie fait l'un de ces effets : **déblocage** (bâtiment, vaisseau, onglet, action), **bonus permanent** (pourcentage), ou **extension de limite** (plafond hors ligne, files de recherche).
- Au départ, **une seule recherche à la fois**. La recherche continue hors ligne.
- Les prerequis croisés entre branches sont voulus : ils forcent l'interdépendance entre commerce, industrie et militaire.
- Les données scientifiques proviennent de l'activité personnelle (exploration, scans), des laboratoires et de chercheurs employés : la recherche ne se résume donc pas à un délai d'attente.

| Palier | Phase | Ordre de grandeur du coût | Durée indicative |
| --- | --- | --- | --- |
| T1 | Survivant, Indépendant | très faible | secondes à minutes |
| T2 | Entrepreneur | faible | minutes à dizaines de minutes |
| T3 | Industriel | moyen | dizaines de minutes à heures |
| T4 | Armateur, Magnat | élevé | heures |
| T5 | Puissance spatiale | très élevé | heures à jours |

### 18.2 Branche Navigation (NAV)

| ID | Technologie | Prérequis | Palier | Effet |
| --- | --- | --- | --- | --- |
| NAV-1 | Cartographie de base | – | T1 | Débloque l'onglet Univers et la carte du système de départ |
| NAV-2 | Moteurs optimisés | – | T1 | Bonus de vitesse des vaisseaux |
| NAV-3 | Scanners longue portée | NAV-1 | T1 | Révèle le contenu des astéroïdes ; débloque l'Éclaireur |
| NAV-4 | Saut inter-secteurs | NAV-2, NAV-3 | T2 | Accès aux secteurs voisins |
| NAV-5 | Réservoirs étendus | NAV-2 | T2 | Réduit la consommation de carburant |
| NAV-6 | Portes de saut | NAV-4 | T3 | Accès aux autres systèmes solaires |
| NAV-7 | Navigation automatique avancée | NAV-5, NAV-6 | T4 | Routes longues sans pénalité de temps |
| NAV-8 | Exploration profonde | NAV-6, SCI-6 | T4 | Secteurs cachés et ressources rares |

### 18.3 Branche Industrie (IND)

| ID | Technologie | Prérequis | Palier | Effet |
| --- | --- | --- | --- | --- |
| IND-1 | Extraction mécanisée | – | T1 | Bonus de minage ; débloque le Mineur automatisé |
| IND-2 | Raffinage de base | IND-1 | T1 | Débloque le module Raffinerie |
| IND-3 | Stockage modulaire | IND-1 | T2 | Débloque le module Entrepôt |
| IND-4 | Électronique de base | IND-2 | T2 | Usine électronique ; circuits |
| IND-5 | Chimie des polymères | IND-2 | T2 | Usine chimique ; polymères |
| IND-6 | Stations modulaires | IND-3, IND-4 | T3 | Construction de stations à plusieurs modules, centrale |
| IND-7 | Alliages avancés | IND-4, IND-5 | T3 | Titane et alliages ; composants mécaniques |
| IND-8 | Chantier naval | IND-6, IND-7 | T3 | Module Chantier naval ; construction de vaisseaux |
| IND-9 | Efficacité énergétique | IND-6 | T4 | Réduit la consommation d'énergie des stations |
| IND-10 | Mégastructures industrielles | IND-8, IND-9 | T5 | Grandes infrastructures d'endgame |

### 18.4 Branche Commerce (COM)

| ID | Technologie | Prérequis | Palier | Effet |
| --- | --- | --- | --- | --- |
| COM-1 | Registre de marché | – | T1 | Affiche les prix des marchandises du secteur |
| COM-2 | Contrats de transport | COM-1 | T1 | Débloque les missions de transport |
| COM-3 | Transporteurs S | COM-1 | T1 | Achat de Transporteurs S |
| COM-4 | Routes commerciales | COM-2, COM-3 | T2 | Routes automatiques entre deux stations |
| COM-5 | Ordres conditionnels | COM-4 | T3 | Prix minimum et maximum, stocks minimums |
| COM-6 | Transporteurs M et L | COM-4, IND-7 | T3 | Achat de Transporteurs M et L |
| COM-7 | Licences commerciales | COM-5 | T4 | Accès aux marchés des factions |
| COM-8 | Analyse de marché | COM-5, SCI-4 | T4 | Prévision des prix et alertes de pénurie |

### 18.5 Branche Personnel (PER)

| ID | Technologie | Prérequis | Palier | Effet |
| --- | --- | --- | --- | --- |
| PER-1 | Recrutement | – | T1 | Onglet Employés et premiers recrutements |
| PER-2 | Formation | PER-1 | T2 | Bonus d'expérience des employés |
| PER-3 | Postes de direction | PER-2 | T3 | Débloque le poste de directeur de station |
| PER-4 | Agence de recrutement | PER-2 | T3 | Profils plus rares, marché renouvelé plus souvent |
| PER-5 | Corps d'officiers | PER-3 | T4 | Débloque commandants et bonus d'officier |
| PER-6 | Contrats long terme | PER-4 | T4 | Réduit les salaires |
| PER-7 | Délégation | PER-3, PER-6 | T5 | Règles par défaut pour automatiser les stations et flottes |

### 18.6 Branche Militaire (MIL)

| ID | Technologie | Prérequis | Palier | Effet |
| --- | --- | --- | --- | --- |
| MIL-1 | Armement de base | – | T1 | Armes du personnage ; débloque le Chasseur |
| MIL-2 | Blindage renforcé | MIL-1 | T2 | Bonus de coque |
| MIL-3 | Boucliers | MIL-1, IND-4, IND-5 | T2 | Boucliers pour vaisseaux |
| MIL-4 | Tactique de flotte | MIL-2 | T3 | Ordres d'escorte et de patrouille ; débloque la Corvette |
| MIL-5 | Frégates | MIL-3, MIL-4 | T3 | Débloque la Frégate |
| MIL-6 | Munitions et missiles | MIL-5, IND-7 | T4 | Production de munitions et de missiles |
| MIL-7 | Destroyers | MIL-6 | T4 | Débloque le Destroyer |
| MIL-8 | Doctrines | MIL-4, PER-5 | T4 | Choix de doctrine de flotte |
| MIL-9 | Porte-vaisseaux | MIL-7, IND-8 | T5 | Débloque le Porte-vaisseaux |
| MIL-10 | Guerre de conquête | MIL-8, MIL-9 | T5 | Attaque de stations et de secteurs ennemis |

### 18.7 Branche Science et Empire (SCI)

| ID | Technologie | Prérequis | Palier | Effet |
| --- | --- | --- | --- | --- |
| SCI-1 | Méthode scientifique | – | T1 | Onglet Recherche et données scientifiques via l'activité personnelle (offerte par le tutoriel au niveau 2 de Minage) |
| SCI-2 | Laboratoire de base | SCI-1 | T1 | Débloque le module Laboratoire |
| SCI-3 | Archivage hors ligne | SCI-2 | T2 | Plafond hors ligne passe de 24 h à 36 h |
| SCI-4 | Analyse des données | SCI-2 | T2 | Bonus de production de données scientifiques |
| SCI-5 | Archivage avancé | SCI-3, IND-6 | T3 | Plafond hors ligne à 48 h |
| SCI-6 | Programmes de recherche | SCI-4 | T3 | Deux recherches en parallèle |
| SCI-7 | Archivage orbital | SCI-5 | T4 | Plafond hors ligne à 72 h |
| SCI-8 | Héritage | SCI-6, SCI-5 | T4 | Débloque le prestige |
| SCI-9 | Technologies expérimentales | SCI-6, SCI-8 | T5 | Bonus d'endgame et technologies spéciales |

Les plafonds hors ligne (36 h, 48 h, 72 h) sont des exemples à valider avec l'équipe d'équilibrage.

### 18.8 Points d'attention

- **Pas de branche obligatoire** pour atteindre une phase : chaque phase doit pouvoir être atteinte par plus d'un chemin (par exemple, un joueur très commerce et un joueur très industrie).
- **Goulots à surveiller en équilibrage** : IND-4 (utilisée par IND-6, MIL-3), IND-7 (utilisée par COM-6, MIL-6) et SCI-6 (utilisée par NAV-8, SCI-9) sont des technologies charnières.
- **Pas de technologie purement numérique** : au moins un tiers des technologies doivent débloquer une action, un bâtiment ou un vaisseau, pas seulement un pourcentage.
- **Coûts en données scientifiques** : si le joueur n'a pas de source de données avant le laboratoire (SCI-2), la phase 2 peut se bloquer. À vérifier dans le scénario de test du joueur actif de 30 minutes.
- **Respec** : non prévu en v1. La recherche est permanente, ce qui simplifie l'équilibrage.

## 19. Recettes de production (ajout v0.2)

### 19.1 Principes

- **19 marchandises** en v1 (hors crédits). Chacune sert à au moins une recette, un vaisseau, une technologie ou une consommation (énergie, combat).
- Un module exécute **une recette à la fois**. Le joueur peut changer la recette active ; le cycle en cours se termine d'abord.
- Un cycle consomme les entrées au démarrage et produit les sorties à la fin. Si une entrée manque, si le stock de sortie est plein ou si l'énergie est insuffisante, le module **s'arrête et le signale** ; il ne perd rien.
- Les transformations ont des **pertes** (par exemple 3 unités en entrée pour 2 en sortie) afin que l'extraction reste toujours utile.
- Les employés et les technologies augmentent la production ou réduisent la durée et l'énergie. Ils **ne modifient jamais les ratios d'entrée**.
- Quantités, durées et énergies ci-dessous sont **illustratives** : le BDS les fixera. Durées en secondes de jeu avant bonus ; énergie en unités d'électricité par cycle.
- Personnel : 1 employé pour une mine, une raffinerie, une usine chimique, une centrale ou un entrepôt ; 2 pour une usine électronique, un atelier mécanique, un arsenal ou un laboratoire ; 3 pour un chantier naval.

### 19.2 Liste des marchandises

| Famille | Marchandises |
| --- | --- |
| Matières premières (6) | Minerai de fer, minerai de cuivre, silicium, carbone, glace, minerai de titane |
| Métaux raffinés (3) | Acier, cuivre raffiné, alliage de titane |
| Chimie (1) | Polymères |
| Électronique (1) | Circuits |
| Industrie avancée (3) | Composants mécaniques, moteurs spatiaux, boucliers |
| Énergie (2) | Électricité, carburant |
| Militaire (2) | Munitions, missiles |
| Recherche (1) | Données scientifiques |

### 19.3 Recettes par module

**Mine**

| Recette | Entrées | Sorties | Durée | Énergie | Déblocage |
| --- | --- | --- | --- | --- | --- |
| Extraction de fer | – | 10 minerai de fer | 30 s | 2 | IND-1 |
| Extraction de cuivre | – | 10 minerai de cuivre | 30 s | 2 | IND-1 |
| Extraction de silicium | – | 8 silicium | 30 s | 2 | IND-1 |
| Extraction de carbone | – | 8 carbone | 30 s | 2 | IND-1 |
| Extraction de glace | – | 8 glace | 30 s | 2 | IND-1 |
| Extraction de titane | – | 4 minerai de titane | 45 s | 3 | IND-1 et Minage niveau 10 |

La disponibilité de chaque gisement dépend du secteur : tous les secteurs ne proposent pas toutes les matières.

**Raffinerie**

| Recette | Entrées | Sorties | Durée | Énergie | Déblocage |
| --- | --- | --- | --- | --- | --- |
| Acier | 3 minerai de fer + 1 carbone | 2 acier | 20 s | 3 | IND-2 |
| Cuivre raffiné | 3 minerai de cuivre | 2 cuivre raffiné | 20 s | 3 | IND-2 |
| Alliage de titane | 3 minerai de titane + 1 acier + 1 carbone | 2 alliage de titane | 40 s | 4 | IND-7 |

**Usine chimique**

| Recette | Entrées | Sorties | Durée | Énergie | Déblocage |
| --- | --- | --- | --- | --- | --- |
| Polymères | 2 carbone + 1 glace | 2 polymères | 25 s | 3 | IND-5 |
| Carburant | 2 glace + 1 carbone | 3 carburant | 20 s | 3 | IND-5 |

**Usine électronique**

| Recette | Entrées | Sorties | Durée | Énergie | Déblocage |
| --- | --- | --- | --- | --- | --- |
| Circuits | 2 silicium + 1 cuivre raffiné | 1 circuit | 30 s | 4 | IND-4 |
| Boucliers | 2 circuits + 1 polymères | 1 bouclier | 50 s | 5 | MIL-3 et IND-5 |

**Atelier mécanique** (nouveau module, déblocage IND-7)

| Recette | Entrées | Sorties | Durée | Énergie | Déblocage |
| --- | --- | --- | --- | --- | --- |
| Composants mécaniques | 2 acier + 1 cuivre raffiné | 1 composant mécanique | 35 s | 5 | IND-7 |
| Moteurs spatiaux | 2 composants mécaniques + 1 circuit + 1 alliage de titane | 1 moteur | 60 s | 6 | IND-7 |

**Arsenal** (nouveau module, déblocage MIL-6)

| Recette | Entrées | Sorties | Durée | Énergie | Déblocage |
| --- | --- | --- | --- | --- | --- |
| Munitions | 1 acier + 1 cuivre raffiné | 10 munitions | 15 s | 3 | MIL-6 |
| Missiles | 2 acier + 1 circuit + 1 carburant | 2 missiles | 40 s | 5 | MIL-6 |

**Laboratoire**

| Recette | Entrées | Sorties | Durée | Énergie | Déblocage |
| --- | --- | --- | --- | --- | --- |
| Analyse de base | 2 silicium | 2 données scientifiques | 60 s | 3 | SCI-2 |
| Analyse avancée | 1 circuit + 1 silicium | 6 données scientifiques | 60 s | 4 | SCI-4 et IND-4 |

**Production d'énergie**

| Recette | Entrées | Sorties | Durée | Déblocage |
| --- | --- | --- | --- | --- |
| Panneaux solaires | – | 12 électricité | 30 s | Disponible dès le départ (production variable selon le secteur) |
| Centrale à carburant | 1 carburant | 30 électricité | 30 s | IND-6 |

### 19.4 Exemple de chaîne complète : un moteur spatial

Un moteur demande 2 composants mécaniques, 1 circuit et 1 alliage de titane. En remontant jusqu'aux matières premières, la chaîne coûte environ :

| Matière première | Quantité par moteur |
| --- | --- |
| Minerai de fer | 6,75 |
| Minerai de cuivre | 4,5 |
| Silicium | 2 |
| Carbone | 2,75 |
| Minerai de titane | 1,5 |

Cette chaîne traverse **quatre modules** (mine, raffinerie, usine électronique, atelier mécanique), ce qui illustre bien l'interdépendance voulue entre extraction, industrie et logistique.

### 19.5 Construction de vaisseaux

Avant le chantier naval (IND-8), les vaisseaux sont **achetés en crédits** à un chantier de faction. Le chantier naval permet de les **construire à partir de marchandises**, ce qui revient moins cher mais demande une chaîne industrielle. Il faut aussi la technologie de la classe concernée.

| Vaisseau | Technologie | Composants méc. | Moteurs | Circuits | Alliages | Boucliers | Acier |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Éclaireur | NAV-3 | 4 | 1 | 2 | 0 | 0 | 10 |
| Mineur | IND-1 | 6 | 1 | 2 | 0 | 0 | 15 |
| Transporteur S | COM-3 | 6 | 1 | 2 | 0 | 0 | 12 |
| Transporteur M | COM-6 | 15 | 2 | 4 | 3 | 0 | 30 |
| Transporteur L | COM-6 | 40 | 4 | 8 | 10 | 0 | 80 |
| Chasseur | MIL-1 | 5 | 1 | 2 | 0 | 1 | 15 |
| Corvette | MIL-4 | 12 | 2 | 4 | 4 | 2 | 30 |
| Frégate | MIL-5 | 30 | 3 | 8 | 10 | 4 | 60 |
| Destroyer | MIL-7 | 80 | 6 | 20 | 30 | 10 | 150 |
| Porte-vaisseaux | MIL-9 | 200 | 12 | 50 | 100 | 25 | 400 |

En plus des marchandises, chaque construction coûte des **crédits** et du **temps** (valeurs dans le BDS), et le vaisseau demande un équipage pour fonctionner.

### 19.6 Corrections appliquées dans le reste du GDD

- **Section 8.1** : retirer l'hydrogène et les capteurs ; ajouter le minerai de titane et l'alliage de titane. La liste finale est celle du 19.2.
- **Arbre de recherche, IND-4** : l'effet devient « usine électronique et circuits » (sans capteurs).
- **Arbre de recherche, MIL-3** : ajouter IND-5 aux prérequis (les boucliers demandent des polymères).
- **Section 9** : ajouter les modules **Atelier mécanique** (IND-7) et **Arsenal** (MIL-6). Les panneaux solaires sont disponibles dès le départ ; la centrale à carburant arrive avec IND-6.
- **Section 17** : l'arbre de recherche, les recettes, les fiches de vaisseaux et l'univers sont rédigés (sections 18 à 21).

### 19.7 Points d'attention pour l'équilibrage

- **Le titane est le goulot du milieu de partie** : il est nécessaire aux alliages, donc aux moteurs et aux grands vaisseaux. À vérifier : sa disponibilité par secteur et le moment où le joueur peut le miner.
- **Composants mécaniques et circuits** sont utilisés presque partout : leur prix de référence sera décisif pour la rentabilité du commerce.
- **Boucle énergie** : une centrale à carburant consomme du carburant. Le rendement (1 carburant pour 30 électricité) doit rester largement positif par rapport au coût de production du carburant.
- **Scénario de test à ajouter** : temps nécessaire pour produire un premier moteur à partir de zéro, pour un joueur actif pendant 2 heures.
- **Pas de sous-produits ni de déchets en v1** : à envisager plus tard si la profondeur manque.

## 20. Vaisseaux : fiches détaillées (ajout v0.2)

### 20.1 Principes

- Toutes les valeurs sont en **unités arbitraires** et servent à comparer les classes entre elles ; le BDS fixera les chiffres définitifs.
- Un vaisseau est défini par sa **classe**, ses **modules** installés, son **équipage** et son **état**.
- Il est soit **piloté** par le joueur, soit **automatisé** avec un pilote employé (voir section 7).
- Un vaisseau sans l'équipage minimum **ne peut pas partir**. Avec l'équipage au complet, il gagne un petit bonus d'efficacité ; un équipage expérimenté améliore vitesse, précision ou consommation selon son poste.
- Les classes sont débloquées par recherche (section 18) et construites ou achetées (section 19.5).

### 20.2 Caractéristiques de base

| Classe | Coque | Boucliers | Vitesse | Cargo | Équipage min. | Emplacements de modules |
| --- | --- | --- | --- | --- | --- | --- |
| Éclaireur | 100 | 20 | 10 | 10 | 1 | 2 |
| Mineur | 150 | 10 | 4 | 80 | 1 | 2 |
| Transporteur S | 120 | 20 | 6 | 100 | 1 | 2 |
| Transporteur M | 400 | 80 | 5 | 500 | 3 | 3 |
| Transporteur L | 1 500 | 300 | 3 | 2 500 | 8 | 4 |
| Chasseur | 200 | 60 | 12 | 10 | 1 | 2 |
| Corvette | 600 | 200 | 8 | 50 | 4 | 3 |
| Frégate | 2 000 | 800 | 6 | 100 | 12 | 5 |
| Destroyer | 8 000 | 3 000 | 4 | 200 | 40 | 8 |
| Porte-vaisseaux | 20 000 | 8 000 | 2 | 500 | 100 | 12 |

### 20.3 Rôle, armement et coûts

| Classe | Rôle | Emplacements d'armes | Consommation de carburant | Entretien par heure (cr) | Prix d'achat (cr) |
| --- | --- | --- | --- | --- | --- |
| Éclaireur | Exploration, scans, missions rapides | 0 | 1 | 9 | 4 600 |
| Mineur | Extraction automatisée | 0 | 2 | 11 | 5 700 |
| Transporteur S | Petites routes commerciales | 0 | 2 | 11 | 5 500 |
| Transporteur M | Routes intermédiaires | 1 | 6 | 32 | 16 100 |
| Transporteur L | Fret lourd entre systèmes | 2 | 15 | 106 | 53 100 |
| Chasseur | Combat léger, interception | 2 | 2 | 15 | 7 400 |
| Corvette | Escorte et patrouille | 4 | 6 | 46 | 22 900 |
| Frégate | Combat polyvalent | 8 | 14 | 117 | 58 700 |
| Destroyer | Puissance militaire | 16 | 40 | 354 | 176 800 |
| Porte-vaisseaux | Commandement de flotte | 10 | 60 | 1 200 | 600 000 |

Les prix d'achat viennent du BDS (section 8) : ils se calculent à partir de la valeur des marchandises de construction. L'entretien est de 0,2 % du prix d'achat par heure d'activité. Le porte-vaisseaux possède en plus des **hangars** : il peut transporter jusqu'à 20 petits vaisseaux (éclaireurs, chasseurs, mineurs, transporteurs S) qui profitent de son commandant.

### 20.4 Modules d'équipement

Chaque emplacement reçoit un module. Trois niveaux de qualité : **Mk1** (disponible tôt), **Mk2** (palier T3) et **Mk3** (paliers T4 et T5).

| Module | Effet |
| --- | --- |
| Propulseur | Bonus de vitesse |
| Générateur de bouclier | Bonus de boucliers |
| Blindage | Bonus de coque |
| Arme | Dégâts, type (laser, cinétique, missiles) |
| Soute | Capacité de chargement |
| Scanner | Portée et précision de détection |
| Foreuse | Vitesse d'extraction (Mineur et minage manuel du vaisseau personnel) |
| Atelier de réparation | Répare coque et modules en route |
| Quartiers d'équipage | Réduit l'usure de l'équipage |
| Hangar | Accueille de petits vaisseaux (porte-vaisseaux uniquement) |

Choisir un module, c'est renoncer à un autre : un transporteur très blindé transporte moins, un mineur très foré est plus vulnérable.

### 20.5 Affectations

Un vaisseau automatisé reçoit une **mission** : route commerciale, extraction, approvisionnement d'une station, patrouille, escorte, défense de station, exploration automatique (Éclaireur, à partir de NAV-8). Le joueur peut reprendre le contrôle d'un vaisseau à tout moment ; l'affectation est alors suspendue.

### 20.6 États et entretien

| État | Signification |
| --- | --- |
| À quai | Amarré, disponible |
| En route | Se déplace, en mission |
| Au combat | Engagé dans une rencontre |
| Endommagé | Coque basse, performances réduites |
| Immobilisé | Carburant, équipage ou énergie manquant |

- Les vaisseaux s'usent avec l'activité ; les réparations se font à quai contre des crédits et de l'acier.
- **Hors ligne, aucun vaisseau n'est détruit.** Au pire, il est endommagé ou immobilisé. Une perte définitive n'est possible que lors d'un combat auquel le joueur a participé ou qu'il a lancé en étant présent.
- Chaque vaisseau coûte du **carburant**, des **salaires d'équipage** et de l'**entretien**. Une flotte trop grande pour ses revenus s'immobilise progressivement.

### 20.7 Escadrons et flottes

- Un **escadron** regroupe jusqu'à 5 vaisseaux sous un commandant.
- Une **flotte** regroupe plusieurs escadrons ; le nombre maximal dépend de la compétence **Commandement** du personnage et des officiers disponibles (PER-5).
- La composition compte : un escadron équilibré (ligne, escorte, soutien) bénéficie de bonus, un escadron composé d'un seul type n'en a pas.

### 20.8 Points d'attention

- Le **Transporteur S** doit être rentable très tôt : c'est le premier vaisseau automatisé du joueur et il conditionne la transition vers la phase 3.
- L'**écart de puissance** entre Frégate et Destroyer est volontairement grand ; à vérifier qu'il n'écrase pas les stratégies fondées sur la quantité de petits vaisseaux.
- Le **porte-vaisseaux** ne doit pas être strictement meilleur que plusieurs destroyers : il apporte du commandement, pas de la puissance brute.

## 21. Univers et factions (ajout v0.2)

Les noms ci-dessous sont des **noms de travail**.

### 21.1 Systèmes solaires de la v1

| Système | Phase d'accès | Secteurs | Faction dominante | Particularités |
| --- | --- | --- | --- | --- |
| Aurore | Départ | 5 | Ligue Marchande d'Altaïr | Ressources de base, sécurité relative, un peu de titane en bordure |
| Ferrum | À partir de NAV-6 (portes de saut) | 6 | Consortium Ferrum | Métaux abondants, titane, industrie lourde |
| Ceinture Noire | À partir de NAV-6 | 5 | Clans de la Ceinture Noire (pirates) | Dangereux, ressources rares, trafic illégal |
| Vanguard | Phase 4 de développement | 6 | Directoire Vanguard | Militaire, chantiers de guerre, conflits entre factions |

**Contrainte importante** : le titane doit être accessible dans le système de départ (secteurs de bordure, quantités limitées), car les alliages (IND-7) arrivent avant les portes de saut (NAV-6).

Chaque secteur possède : ressources disponibles, stations, routes, niveau de risque (échelle de 0 à 10, voir BDS 9), faction dominante et opportunités d'exploitation.

### 21.2 Les factions

**Ligue Marchande d'Altaïr** (commerciale, neutre)

- Philosophie : le commerce avant tout, jamais en guerre ouverte.
- Produit : circuits, polymères, carburant. Achète presque tout, à prix modéré.
- Rôle pour le joueur : faction de départ, premiers contrats de transport, premières licences commerciales.

**Consortium Ferrum** (industrielle)

- Philosophie : maîtriser la production de métaux et de composants.
- Produit : acier, alliages de titane, composants mécaniques. A besoin de glace, de carbone et de circuits.
- Rôle pour le joueur : source de titane et d'alliages, contrats d'approvisionnement, accès au chantier naval de faction.

**Clans de la Ceinture Noire** (pirates)

- Philosophie : prendre ce qui passe.
- Pas d'économie légale : leurs repaires achètent munitions, missiles et carburant à prix élevé, et vendent à bas prix des marchandises détournées.
- Rôle pour le joueur : source de risque sur les routes, de missions de combat et de marché noir ; les attaquer rapporte des récompenses mais détériore ses relations avec eux, sans effet sur les autres factions.

**Directoire Vanguard** (militaire expansionniste, phase 4)

- Philosophie : accroître son territoire par la force.
- Produit : munitions, missiles, boucliers. A besoin d'alliages, de composants mécaniques et de moteurs.
- Rôle pour le joueur : contrats militaires, fournitures de guerre, premiers conflits entre factions.

### 21.3 Production et demande par faction

| Faction | Produit | A besoin de |
| --- | --- | --- |
| Ligue Marchande | Circuits, polymères, carburant | Acier, composants mécaniques, silicium |
| Consortium Ferrum | Acier, alliages, composants mécaniques | Glace, carbone, circuits |
| Clans de la Ceinture Noire | Marchandises détournées (variable) | Munitions, missiles, carburant |
| Directoire Vanguard | Munitions, missiles, boucliers | Alliages, composants mécaniques, moteurs |

Ces profils créent des opportunités de commerce naturelles : le joueur peut acheter chez l'un ce que l'autre manque.

### 21.4 Relations

- Échelle de **-100 à +100** pour chaque faction, avec cinq paliers : Hostile, Méfiant, Neutre, Amical, Allié.
- **Gains** : contrats terminés, livraisons, missions, aide en cas d'attaque.
- **Pertes** : attaque de ses vaisseaux ou stations, contrebande, échec de contrats.
- **Effets** : prix d'achat et de vente, accès aux licences (COM-7), accès aux chantiers navals de faction, accès aux technologies et plans spécifiques, passage sécurisé ou hostile dans les secteurs.
- Les relations évoluent lentement ; un joueur absent ne perd pas ses relations hors ligne.

### 21.5 Contrats et événements

| Type | Contenu |
| --- | --- |
| Contrat de transport | Livrer une marchandise d'une station à une autre |
| Contrat d'approvisionnement | Fournir une quantité régulière à une station |
| Contrat d'extraction | Extraire une quantité de matière donnée |
| Contrat d'escorte | Protéger un convoi |
| Contrat de combat | Détruire des pirates ou défendre un secteur |

Événements possibles : pénurie dans un secteur, surproduction, attaque pirate, blocus, découverte, tension entre factions. Un événement peut modifier les prix et créer une opportunité ou un risque, mais ne détruit jamais une partie de la progression du joueur.

### 21.6 Conflits (phase 4 de développement)

- Les guerres entre factions sont **abstraites** : elles modifient la demande en munitions, missiles et vaisseaux, les routes disponibles et le niveau de risque d'un secteur.
- Le joueur peut **soutenir** un camp (fournitures, escorte, combat), **rester neutre** ou **profiter** de la guerre par le commerce.
- La conquête de secteurs (MIL-10) est la mécanique d'endgame : un secteur conquis reste dans l'empire du joueur et produit des ressources, avec coût d'entretien et risque de contre-attaque.

### 21.7 Points d'attention

- **Pas de faction à bloquer le jeu** : le joueur doit pouvoir progresser sans soutenir aucune faction en particulier, mais en choisissant un camp il gagne des avantages.
- **Hostilité modérée des pirates** au début : les attaques sur les routes doivent rester une contrainte, jamais une cause de blocage.
- **Équilibrage économique** : tester que le commerce entre factions reste rentable sans qu'une seule route domine toutes les autres.
- **Univers à la main** : chaque secteur doit être écrit dans un fichier de données séparé (ressources, stations, faction, risque), pour que l'équilibrage puisse l'ajuster sans toucher au code.

## 22. État du document et prochaines étapes

Le GDD v0.2 couvre l'ensemble du jeu pour la v1 : toutes les sections sont rédigées et cohérentes entre elles. Il reste à produire le TDD pour les développeurs et le BDS pour l'équilibrage.

| Version | Contenu |
| --- | --- |
| v0.1 | Vision, décisions de cadrage, boucles de jeu, progression, personnage, employés, vaisseaux, économie, industrie, combat, factions, hors ligne, prestige, interface, plan de développement |
| v0.2 | Arbre de recherche (18), recettes de production (19), fiches de vaisseaux (20), univers et factions (21), corrections de cohérence (sections 8, 9, 17, 18) |

### 22.1 Décisions ouvertes avant le BDS

- **Titane dans le système de départ** : choisir les secteurs de bordure et les quantités (21.1).
- **Plafonds hors ligne** : valider 24 h, puis 36, 48 et 72 h selon la recherche (18.7).
- **Rentabilité du Transporteur S** : c'est le premier vaisseau automatisé, il conditionne la transition vers la phase 3 (20.8).
- **Équilibre entre petits et gros vaisseaux** : Frégate, Destroyer et porte-vaisseaux (20.8).
- **Noms définitifs** des factions et des systèmes (21).

### 22.2 Suite

1. **TDD** : architecture JavaScript modulaire, données de jeu en JSON séparées du code, sauvegarde locale, moteur de simulation basé sur le temps écoulé.
2. **BDS** : coûts, durées, productions, salaires, courbes d'expérience, prix de référence, puissances et scénarios de test (voir section 17).
3. **Relecture croisée** du GDD par les deux équipes avant de figer la v1.

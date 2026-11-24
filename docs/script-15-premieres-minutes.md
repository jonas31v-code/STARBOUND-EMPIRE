# Script des 15 premières minutes – Idle Space Empire (v0.1)

Document complémentaire au GDD v0.2, au TDD v0.1 et au BDS v0.1

Public : game design, développement, équilibrage. Ce document décrit ce que le joueur voit et fait de la minute 0 à la minute 15, avec les valeurs du BDS, puis projette le temps nécessaire pour atteindre la phase 3. En écrivant le script, j'ai relevé plusieurs écarts avec les autres documents : ils sont listés en section 6. Statut : les deux premiers leviers de la section 5 (scan de 10 données, COM-3 au palier T1) sont validés, et les corrections de la section 6 sont reportées dans le GDD, le TDD et le BDS. La cible d'entrée en phase 3 est passée à 1 h 30, puis à 1 h 20 après les correctifs de la phase 2.

## 1. Objectifs du début de partie

- Faire comprendre la boucle courte en moins de 2 minutes : miner, vendre, progresser.
- Chaque minute apporte un retour visible : une barre qui avance, des crédits, un niveau, un déblocage.
- Les onglets arrivent un à un (GDD 15) : seul l'onglet Personnage est visible au départ.
- Toujours une action utile possible : le joueur n'est jamais bloqué.
- Une activité lancée **se répète automatiquement** jusqu'à ce que le joueur en choisisse une autre ; il n'a pas à cliquer à chaque cycle (GDD 3.4).
- Tutoriel léger : un objectif affiché en une ligne, des notifications non bloquantes, aucune fenêtre qui interrompt le jeu avant le bilan de la minute 15.
- À la minute 15, le joueur a essayé trois types d'activité (minage, exploration, recherche), vu le marché local et terminé deux technologies.

## 2. Valeurs utilisées

| Élément | Valeur | Source |
| --- | --- | --- |
| Crédits de départ | 500 | BDS 2 |
| Minage manuel (fer) | Cycle de 20 s, 4 minerai vendus 10 cr pièce, soit 40 cr, 4 XP | BDS 2 |
| Exploration (scan) | Cycle de 60 s, **10 données** (valeur proposée, voir 5), 12 XP | Modifié par rapport au BDS |
| XP pour passer du niveau n au suivant | 60 × 1,18 à la puissance (n - 1) : niveau 2 à 60 XP, niveau 3 à 131 XP cumulés | BDS 6 |
| Première recherche (IND-1) | 12 données, 300 cr, 2 min | BDS 7, facteur 1 |
| Deuxième recherche (PER-1) | 12 données, 300 cr, 2 min | BDS 7, facteur 1 |
| Effet d'IND-1 | +10 % d'extraction manuelle (valeur proposée) | À définir dans le BDS |
| SCI-1 (méthode scientifique) | **Offerte** par le tutoriel (0 donnée, 0 cr) | Exception de tutoriel |

## 3. Déroulé minute par minute

| Temps | Action du joueur | Ce qui se passe | Déblocage ou objectif | Crédits |
| --- | --- | --- | --- | --- |
| 0:00 | Lit l'introduction (trois lignes) et appuie sur Miner | Un cycle de 20 s démarre, avec une barre de progression | Objectif 1 : Minez 10 minerais | 500 |
| 0:20 à 1:00 | Regarde l'activité se répéter | Chaque cycle : +4 minerai vendu à la station voisine (+40 cr) et +4 XP |  | 620 |
| 1:00 | Objectif 1 atteint (12 minerais) | L'onglet Commerce apparaît avec les prix locaux | Objectif 2 : Atteignez le niveau 2 de Minage | 620 |
| 1:00 à 5:00 | Continue de miner (12 cycles) |  |  | 1 100 |
| 5:00 | Niveau 2 de Minage (60 XP) | L'ordinateur de bord (SCI-1) se débloque : onglet Recherche et activité Exploration | Objectif 3 : Lancez un scan | 1 100 |
| 5:00 à 7:00 | Passe en exploration : 2 scans | +10 données par scan, soit 20 données |  | 1 100 |
| 7:00 | Choisit sa première recherche | Le jeu propose trois technologies de départ : IND-1, COM-1, PER-1 ; IND-1 est suggérée | Recherche lancée (12 données, 300 cr, 2 min) | 800 |
| 7:00 à 10:00 | Retourne au minage (9 cycles) | À 9:00, IND-1 se termine : +10 % d'extraction | Objectif 4 : Terminez une deuxième recherche | 1 170 |
| 10:00 à 11:00 | Un scan de plus | Il manque 4 données pour PER-1 ; on a 8 + 10 = 18 données |  | 1 170 |
| 11:00 | Lance PER-1 (Recrutement) | 12 données, 300 cr, 2 min |  | 870 |
| 11:00 à 15:00 | Mine (12 cycles) | À 13:00, PER-1 se termine : l'onglet Employés apparaît (vide, avec un aperçu) ; vers 13:40, niveau 3 de Minage |  | 1 400 |
| 15:00 | Bilan de tutoriel | La phase 2 « Indépendant » est atteinte : fenêtre courte de bilan, puis objectifs de la phase 2 | Conditions : Minage niveau 3 et 2 technologies terminées | 1 400 |

Les crédits de la dernière colonne sont cumulés après chaque étape, arrondis à la dizaine.

## 4. Interface pendant les 15 premières minutes

- **Minute 0** : barre de ressources réduite à deux valeurs (crédits, carburant), onglet Personnage seul, activité en cours avec sa barre.
- **Un objectif visible** en permanence sous la barre de ressources, remplacé dès qu'il est atteint.
- **Le journal** (GDD 12) enregistre les événements importants mais n'est pas obligatoire pour comprendre le jeu.
- **Notifications non bloquantes** pour les déblocages (onglet, recherche terminée).
- **Une seule fenêtre** s'interpose : le bilan de la minute 15.
- **Les onglets** apparaissent dans cet ordre : Personnage (0:00), Commerce (1:00), Recherche (5:00), Employés (13:00).

## 5. Projection jusqu'à la phase 3

La phase 3 demande un employé et un vaisseau automatisé (GDD 4). Concrètement : recruter un employé (1 500 cr), acheter un Transporteur S (5 500 cr) et avoir la technologie des routes commerciales (COM-4). Cela passe par COM-1, COM-2, COM-3 et COM-4, en plus d'IND-1 et PER-1.

**Besoin total** : 240 données scientifiques et 13 000 cr (techs : 300 × 4 pour les quatre paliers T1 et 2 400 × 2 pour COM-3 et COM-4 ; employé 1 500 ; Transporteur S 5 500).

Le joueur alterne minage (131 cr par minute avec IND-1) et exploration. Les recherches tournent en arrière-plan.

| Hypothèse | Exploration nécessaire | Minage nécessaire | Entrée en phase 3 |
| --- | --- | --- | --- |
| Valeurs actuelles du BDS (scan de 2,5 données) | 96 min | 95 min | environ 3 h 10 |
| Scan de 10 données | 24 min | 95 min | environ 2 h |
| Scan de 10 données, et COM-3 déplacée au palier T1 (12 données, 300 cr) | 16 min | 79 min | environ 1 h 35 |
| Idem, et minage manuel à 5 minerai par cycle (9 000 cr/h) | 16 min | 63 min | environ 1 h 20 |

La cible du BDS est **1 h 15, plus ou moins 25 %**, soit de 56 min à 1 h 34. Avec les valeurs actuelles, la phase 3 arrive donc plus de deux fois trop tard.

**Recommandation** : appliquer les deux premiers leviers (scan de 10 données, COM-3 au palier T1), ce qui donne environ 1 h 35, à la limite de la tolérance. Le troisième (5 minerai par cycle) ramène à 1 h 20 et peut être ajouté si le simulateur confirme que le rythme reste trop lent.

## 6. Écarts relevés dans les autres documents

1. **Production de données (BDS 2 et 7)** : l'exploration à 150 données par heure est beaucoup trop lente pour les technologies de palier T2. Proposition : 600 par heure (10 par scan).
2. **Achats typiques de la phase 1 (BDS 2)** : le BDS cite l'Éclaireur (4 600 cr), alors que le joueur n'a que 1 400 cr à la minute 15. À remplacer par les deux premières technologies (600 cr au total).
3. **SCI-1 offerte** : la technologie qui débloque l'exploration produit des données, mais elle coûterait des données que le joueur n'a pas encore. Elle doit être offerte par le tutoriel (à ajouter au BDS 7 et au GDD 18.7).
4. **Minage manuel et soute** : le vaisseau de départ a une soute de 10 unités (GDD 20.2), mais le minage manuel produit 4 unités par cycle. Pour éviter les trajets, le minage manuel est **vendu directement à la station voisine**, sans limite de soute. À écrire dans le GDD 5 et le TDD 8.4.
5. **IND-1** : l'effet « bonus de minage » n'a pas de valeur dans le BDS. Proposition : +10 % d'extraction manuelle.
6. **Rendement d'un Mineur automatisé** : ni le GDD ni le BDS ne donnent la quantité extraite par un vaisseau Mineur. C'est indispensable pour la phase 3 ; à définir.
7. **Saturation par le minage manuel** : 720 minerais par heure contre 600 de consommation par station (BDS 3.3). Le stock monte de 120 unités par heure ; à vérifier dans les scénarios S1 et S2.
8. **COM-4 pour la phase 3** : un vaisseau n'est « automatisé » qu'avec les routes commerciales. La condition de la phase 3 doit citer COM-4 explicitement (GDD 4).

## 7. Ce que le joueur doit ressentir

| Moment | Sensation recherchée |
| --- | --- |
| 1 min | J'ai gagné de l'argent et un onglet s'est ouvert |
| 5 min | Je progresse : premier niveau, un nouvel outil |
| 7 min | Je fais un choix : trois recherches possibles |
| 13 min | Le jeu s'ouvre : les employés arrivent |
| 15 min | J'ai un objectif clair pour la suite |

## 8. Suite

- Valider les leviers de la section 5 et les corrections de la section 6, puis les reporter dans le BDS, le GDD et le TDD.
- Écrire le script de la phase 2 (minutes 15 à environ 95) : alternance minage et exploration, premier employé, premier Transporteur S, première route automatique.
- Construire le prototype tableur de l'économie, qui permettra de vérifier ces projections.

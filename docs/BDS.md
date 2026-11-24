# BDS – Idle Space Empire (v0.1)

Balancing Design Specification – document 3 sur 3 (GDD → TDD → BDS)

Public : équipe d'équilibrage. Ce document fixe les **valeurs de départ** du jeu, les **formules** qui les relient et les **scénarios** qui permettent de les vérifier. Les valeurs sont calculées pour être cohérentes entre elles ; le simulateur du TDD (section 11) sert à les corriger. Les numéros de section renvoient au GDD v0.2 et au TDD v0.1.

Notations : cr = crédits ; u = unité de marchandise ; h = heure de jeu ; VA = valeur ajoutée = valeur des sorties moins valeur des entrées.

## 1. Méthode

1. **Ordre de réglage** : prix de référence, valeur ajoutée, coûts des modules, rythme des phases, expérience, recherche, vaisseaux, combat, hors ligne.
2. On règle d'abord les **relations** (rapports de prix, retours sur investissement), puis l'échelle globale.
3. **Un seul paramètre à la fois.** Chaque modification est notée dans un journal : date, paramètre, ancienne et nouvelle valeur, raison, résultat du simulateur.
4. Les valeurs vivent dans les fichiers data/ (TDD 4). Ce document donne les formules ; l'export tableur (TDD 11) donne les valeurs courantes.

## 2. Rythme visé

| Phase | Entrée dans la phase (temps actif cumulé) | Calendrier (2 h actives par jour) | Revenu net visé en fin de phase | Achats typiques |
| --- | --- | --- | --- | --- |
| 1 Survivant | 0 | Jour 1 | 7 000 cr/h (travail manuel) | Deux premières technologies (600 cr) |
| 2 Indépendant | 15 min | Jour 1 | 14 000 cr/h | Technologies COM, Foreuse Mk1 (900), Transporteur S (5 500), premier employé (1 500) |
| 3 Entrepreneur | 1 h 20 | Jour 1 | 25 000 cr/h | Mines (6 800), raffinerie (3 800), laboratoire (6 000) |
| 4 Industriel | 6 h | Jour 3 | 100 000 cr/h | Stations, chantier naval (60 000) |
| 5 Armateur | 25 h | Jour 12 | 400 000 cr/h | Frégates (58 700), destroyers (176 800) |
| 6 Magnat | 80 h | Jour 40 | 1 500 000 cr/h | Licences, grandes flottes |
| 7 Puissance spatiale | 200 h | Jour 100 | 6 000 000 cr/h | Porte-vaisseaux (600 000), conquête |

Fin de la v1 : environ 400 h de jeu actif (jour 200). **Tolérance : plus ou moins 25 %** sur chaque entrée de phase.

**Valeurs de départ** : 500 cr, vaisseau de départ de classe Éclaireur (non vendable), 100 unités de carburant, aucune marchandise, toutes les compétences au niveau 1.

**Activités personnelles de départ**

| Activité | Cycle | Résultat | XP |
| --- | --- | --- | --- |
| Minage manuel (fer) | 20 s | 4 minerai de fer, soit 40 cr (7 200 cr/h), vendus directement à la station du secteur ; dès le niveau 5 de Minage, minage de silicium possible (4 silicium, soit 56 cr par cycle) | 4 par cycle (720 par heure) |
| Mission de transport | 90 s | 12 unités fournies par le client, récompense = 115 % de leur valeur (environ 92 cr par minute pour le fer, soit 70 % du minage) | 720 par heure |
| Exploration (scan) | 60 s | 10 données scientifiques (600 par heure) | 720 par heure |

## 3. Économie

### 3.1 Prix de référence

Les matières premières ont un prix fixé. Les autres marchandises suivent une règle : **prix = (valeur des entrées / quantité produite) × 1,6**, soit une marge de transformation de 60 %. On calcule dans l'ordre des paliers et on arrondit à l'unité.

| Marchandise | Prix (cr) | Calcul |
| --- | --- | --- |
| Minerai de fer | 10 | Fixé |
| Minerai de cuivre | 12 | Fixé |
| Silicium | 14 | Fixé |
| Carbone | 8 | Fixé |
| Glace | 6 | Fixé |
| Minerai de titane | 40 | Fixé |
| Acier | 30 | (3 × 10 + 8) / 2 × 1,6 |
| Cuivre raffiné | 29 | (3 × 12) / 2 × 1,6 |
| Alliage de titane | 126 | (3 × 40 + 30 + 8) / 2 × 1,6 |
| Polymères | 18 | (2 × 8 + 6) / 2 × 1,6 |
| Carburant | 11 | (2 × 6 + 8) / 3 × 1,6 |
| Circuits | 91 | (2 × 14 + 29) × 1,6 |
| Composants mécaniques | 142 | (2 × 30 + 29) × 1,6 |
| Moteurs spatiaux | 802 | (2 × 142 + 91 + 126) × 1,6 |
| Boucliers | 320 | (2 × 91 + 18) × 1,6 |
| Munitions | 9 | (30 + 29) / 10 × 1,6 |
| Missiles | 130 | (2 × 30 + 91 + 11) / 2 × 1,6 |

Hors marché : l'électricité a un coût interne de 0,3 cr par unité ; les données scientifiques valent environ 14 cr l'unité (coût du silicium) mais ne s'échangent pas.

### 3.2 Valeur ajoutée par heure (module à 100 % d'utilisation)

| Recette | Cycle | VA par cycle (cr) | VA par heure (cr) |
| --- | --- | --- | --- |
| Extraction de fer | 30 s | 100 | 12 000 |
| Extraction de cuivre | 30 s | 120 | 14 400 |
| Extraction de silicium | 30 s | 112 | 13 440 |
| Extraction de carbone | 30 s | 64 | 7 680 |
| Extraction de glace | 30 s | 48 | 5 760 |
| Extraction de titane | 45 s | 160 | 12 800 |
| Acier | 20 s | 22 | 3 960 |
| Cuivre raffiné | 20 s | 22 | 3 960 |
| Alliage de titane | 40 s | 94 | 8 460 |
| Polymères | 25 s | 14 | 2 016 |
| Carburant | 20 s | 13 | 2 340 |
| Circuits | 30 s | 34 | 4 080 |
| Composants mécaniques | 35 s | 53 | 5 450 |
| Moteurs spatiaux | 60 s | 301 | 18 060 |
| Boucliers | 50 s | 120 | 8 640 |
| Munitions | 15 s | 31 | 7 440 |
| Missiles | 40 s | 98 | 8 820 |

**Point d'attention** : l'extraction rapporte deux à quatre fois plus que la transformation de palier 2. Trois leviers sont prévus : la profondeur de marché (3.3), le nombre de gisements par secteur, et la marge de transformation (60 % au départ, à relever si l'extraction domine).

### 3.3 Profondeur de marché

Prix local : formule du TDD 8.2, c'est-à-dire prix de référence × clamp(1,6 - 0,6 × stock / stock cible, 0,5, 2,0).

| Famille | Stock cible par station | Consommation de base par station |
| --- | --- | --- |
| Matières premières | 2 000 u | 600 u/h |
| Métaux raffinés | 1 000 u | 250 u/h |
| Chimie et électronique | 800 u | 150 u/h |
| Industrie avancée | 300 u | 30 u/h |
| Militaire | 300 u | 40 u/h |

- Hors ligne, les stocks reviennent vers leur cible avec une demi-vie de 2 h.
- Une mine de fer produit 1 200 u/h : deux mines saturent une station. Le joueur est ainsi poussé à raffiner et à transporter. Le minage manuel (720 u/h) dépasse déjà la consommation d'une station (600 u/h) : à vérifier dans les scénarios S1 et S2.
- **Vérification** : une mine qui vend toute sa production à une seule station ne doit plus être rentable à plein régime à partir de la troisième mine.

### 3.4 Commerce et routes

- Route de départ : aller de 4 min, cycle complet de 10 min, soit 6 cycles par heure. Une route achète dans la limite des crédits disponibles : la cargaison est partielle au début.
- Profit par heure = cycles par heure × cargo × prix d'achat × marge - salaires - carburant - entretien.
- **Marge brute visée** : 20 à 30 % du prix d'achat, sur la marchandise la plus rentable accessible.
- **Retour sur investissement visé** : Transporteur S 3 h, Transporteur M 6 h, Transporteur L 12 h.
- Contrats : récompense de 115 % de la valeur des marchandises ; prime de 10 % après 5 livraisons d'un même contrat d'approvisionnement.

## 4. Modules et stations

Formule : **coût = (VA par heure × 0,8 - exploitation par heure) × retour visé**. L'exploitation regroupe les salaires et l'énergie (0,3 cr par unité). Le facteur 0,8 représente la perte de valeur due au marché.

| Module | Personnel | Retour visé | Coût (cr) | Acier | Temps de construction |
| --- | --- | --- | --- | --- | --- |
| Panneaux solaires | 0 | – | 800 | 5 | 2 min |
| Mine | 1 | 45 min | 6 800 | 45 | 9 min |
| Raffinerie | 1 | 1,5 h | 3 800 | 25 | 6 min |
| Usine chimique | 1 | 2 h | 2 200 | 15 | 4 min |
| Usine électronique | 2 | 2 h (circuits) | 4 200 | 28 | 6 min |
| Atelier mécanique | 2 | 1 h (moteurs) | 13 000 | 87 | 16 min |
| Arsenal | 2 | 2 h | 10 500 | 70 | 13 min |
| Laboratoire | 2 | – | 6 000 | 40 | 8 min |
| Centrale à carburant | 1 | – | 3 000 | 20 | 5 min |
| Entrepôt | 1 | – | 2 000 | 13 | 3,5 min |
| Chantier naval | 3 | – | 60 000 | 400 | 53 min |

- **Acier de construction** = coût / 150, arrondi.
- **Temps de construction** = 120 s × (coût / 1 000) à la puissance 0,8.
- **Plusieurs exemplaires** : le n-ième module du même type dans une station coûte le coût de base × 1,15 à la puissance (n - 1).
- Capacités : stockage de base de 2 000 u par station, +5 000 u par entrepôt. Un panneau solaire produit 1 440 électricité par heure.
- **À surveiller** : l'atelier mécanique et l'arsenal ont une recette bien moins rentable que l'autre (composants mécaniques : retour d'environ 4 h).

## 5. Employés et équipages

- **Salaire par heure** = 500 × (1 + 0,12 × (niveau - 1)) × multiplicateur de rareté.
- **Raretés** : Commun ×1 (70 % du marché), Expérimenté ×1,4 (22 %), Expert ×2,2 (7 %), Légendaire ×4 (1 %).
- **Efficacité** = 1,5 % × (niveau - 1), plafonnée à 30 %, plus un bonus de rareté : 0, +8, +20 ou +40 points.
- **Recrutement** = 3 × le salaire horaire. Le marché propose 6 profils et se renouvelle toutes les 2 h.
- **Expérience** : 0,25 XP par seconde de travail, même courbe que le personnage (section 6). Niveau 10 en environ 1,3 h, niveau 20 en 8 h, niveau 30 en 45 h, hors ligne compris.
- **Équipage** : un membre coûte 60 % du salaire d'un employé de même niveau, soit 300 cr/h au niveau 1.

**Règle de design** : un employé de rareté supérieure n'est rentable que si le bonus multiplié par la VA du poste dépasse le surcoût de salaire. Un Expert de niveau 12 contre un Commun de niveau 12 coûte 1 390 cr/h de plus (2 550 contre 1 160) pour 20 points d'efficacité en plus : +2 400 cr/h sur une mine de fer, mais seulement +790 cr/h sur une raffinerie d'acier. Sur ce poste, l'expert n'est pas rentable.

## 6. Compétences

**XP pour passer du niveau n au suivant = 60 × 1,18 à la puissance (n - 1).** Niveau maximum : 50.

| Niveau | XP cumulée | Temps actif visé | XP par heure à viser dans la tranche |
| --- | --- | --- | --- |
| 5 | 313 | 25 min | environ 760 (niveaux 1 à 10) |
| 10 | 1 145 | 1,5 h |  |
| 20 | 7 400 | 6 h | environ 1 400 (niveaux 10 à 40) |
| 30 | 40 200 | 30 h |  |
| 40 | 211 600 | 150 h | environ 3 600 (niveaux 40 à 50) |
| 50 | 1 109 000 | 400 h |  |

- XP par cycle d'une action = XP par heure visé × durée du cycle / 3 600.
- Chaque niveau donne +1 % d'efficacité à l'activité concernée (plafond +50 %), plus les déblocages du GDD 5.1.
- **Maîtrise par action** : niveaux 1 à 20, XP du niveau n = 200 × 1,3 à la puissance (n - 1), bonus de +2 % de rendement par niveau (plafond +40 %).

## 7. Recherche

Formules par palier p (de 1 à 5), avec un facteur propre à chaque technologie :

- Données = 12 × 8 à la puissance (p - 1) × facteur (de 1 à 3).
- Crédits = 300 × 8 à la puissance (p - 1) × facteur (de 1 à 3).
- Durée = 2 min × 6 à la puissance (p - 1) × facteur (de 0,5 à 1,5).

| Palier | Nombre | Données | Crédits | Durée | Totaux (facteur moyen) |
| --- | --- | --- | --- | --- | --- |
| T1 | 12 | 12 à 36 | 300 à 900 | 1 à 3 min | 288 données, 7 200 cr |
| T2 | 11 | 96 à 288 | 2 400 à 7 200 | 6 à 18 min | 2 100 données, 52 800 cr |
| T3 | 12 | 768 à 2 304 | 19 200 à 57 600 | 36 à 108 min | 18 400 données, 460 800 cr |
| T4 | 12 | 6 144 à 18 432 | 153 600 à 460 800 | 3,6 à 10,8 h | 147 500 données, 3,7 M cr |
| T5 | 5 | 49 152 à 147 456 | 1 228 800 à 3 686 400 | 21,6 à 64,8 h | 491 500 données, 12,3 M cr |

**Production de données** : exploration manuelle 600 par heure ; laboratoire avec analyse de base 120 par heure ; avec analyse avancée (SCI-4 et IND-4) 360 par heure. Il faut environ 7 laboratoires avancés pour tenir le rythme des paliers T4 et T5. SCI-1 est offerte par le tutoriel (0 donnée, 0 crédit). COM-3 (Transporteurs S) est au palier T1 : 12 données, 300 cr. Effet d'IND-1 : +10 % d'extraction manuelle.

## 8. Vaisseaux

Règle : **prix d'achat auprès d'une faction = facteur de classe × valeur des marchandises de construction** (GDD 19.5, aux prix de référence). Le coût en crédits de construction au chantier naval est de 20 % du prix d'achat. Construire revient ainsi à 37 à 60 % du prix d'achat.

| Classe | Valeur des marchandises | Facteur | Prix d'achat | Crédits de construction |
| --- | --- | --- | --- | --- |
| Éclaireur | 1 852 | 2,5 | 4 600 | 920 |
| Mineur | 2 286 | 2,5 | 5 700 | 1 140 |
| Transporteur S | 2 196 | 2,5 | 5 500 | 1 100 |
| Transporteur M | 5 376 | 3 | 16 100 | 3 220 |
| Transporteur L | 13 276 | 4 | 53 100 | 10 620 |
| Chasseur | 2 464 | 3 | 7 400 | 1 480 |
| Corvette | 5 716 | 4 | 22 900 | 4 580 |
| Frégate | 11 734 | 5 | 58 700 | 11 740 |
| Destroyer | 29 472 | 6 | 176 800 | 35 360 |
| Porte-vaisseaux | 75 174 | 8 | 600 000 | 120 000 |

**Frais courants par heure** : entretien = 0,2 % du prix d'achat ; équipage = 300 cr par membre ; carburant = consommation du GDD 20.3 × 11 cr (levier : multiplier par 10 si l'économie manque d'un puits à crédits).

| Classe | Frais par heure (cr) |
| --- | --- |
| Transporteur S | 333 |
| Transporteur L | 2 670 |
| Frégate | 3 870 |
| Destroyer | 12 800 |
| Porte-vaisseaux | 31 900 |

Réparation : 25 % du prix d'achat × fraction de coque perdue, plus de l'acier. Rendement d'un Mineur automatisé (valeur proposée) : 5 unités par cycle de 30 s, soit 600 u/h, jusqu'à remplissage de la soute (80 u), puis trajet de livraison à la station. Équipement du vaisseau personnel : Foreuse Mk1, 900 cr, +15 % d'extraction manuelle, débloquée au niveau 6 de Minage (retour d'environ 45 min).

## 9. Combat

**Valeurs de départ**

- Arme Mk1 : 12 dégâts par seconde par emplacement ; Mk2 ×1,5 ; Mk3 ×2,2. Précision de base 80 %.
- Régénération des boucliers : 1 % du maximum par seconde, après 10 s sans dégâts.
- Combat limité à 120 rounds d'une seconde.

**Puissance de référence** = racine carrée de (DPS efficace × points de vie totaux), où les points de vie sont la coque plus les boucliers.

| Classe | DPS efficace (Mk1) | Points de vie | Puissance | Puissance par crédit (× 1 000) |
| --- | --- | --- | --- | --- |
| Chasseur | 19,2 | 260 | 71 | 9,6 |
| Corvette | 38,4 | 800 | 175 | 7,7 |
| Frégate | 76,8 | 2 800 | 464 | 7,9 |
| Destroyer | 153,6 | 11 000 | 1 300 | 7,4 |
| Porte-vaisseaux | 96 | 28 000 | 1 640 | 2,7 |

Règle : pour les quatre classes de combat, la puissance par crédit reste à plus ou moins 30 % de la même valeur. Le porte-vaisseaux se justifie par ses hangars et son commandement, pas par sa puissance brute.

**Modificateurs**

| Source | Effet |
| --- | --- |
| Commandant | +1,5 % de DPS par niveau de Commandement (maximum +45 %) |
| Équipage au complet | +5 % |
| Composition équilibrée (ligne, escorte, soutien) | +20 % de points de vie effectifs |
| Doctrine offensive | +15 % de DPS, -10 % de points de vie |
| Doctrine défensive | -10 % de DPS, +15 % de points de vie |

**Pirates** : puissance d'un raid = 100 × 1,35 à la puissance du niveau de risque du secteur (0 à 10). Risque 3 : environ 246 ; risque 5 : environ 448 ; risque 10 : environ 2 000.

**Pertes** : un vaisseau à 0 de coque est perdu avec 70 % de probabilité ; sinon il est immobilisé et récupérable. **Jamais hors ligne** (GDD 13).

**Objectifs à vérifier au simulateur** : à puissance égale, 50 % de victoires plus ou moins 10 ; à puissance ×1,5, au moins 85 % ; à ×2, au moins 95 %.

## 10. Factions

| Palier | Relation | Prix d'achat | Prix de vente | Accès |
| --- | --- | --- | --- | --- |
| Hostile | -100 à -51 | +25 % | -20 % | Amarrage refusé |
| Méfiant | -50 à -11 | +10 % | -10 % | Standard |
| Neutre | -10 à +24 | 0 | 0 | Standard |
| Amical | +25 à +59 | -5 % | +5 % | Licences de niveau 1 |
| Allié | +60 à +100 | -10 % | +10 % | Plans spéciaux, chantier de faction |

| Action | Variation |
| --- | --- |
| Contrat de transport terminé | +2 |
| Contrat d'approvisionnement terminé | +3 |
| Contrat d'escorte terminé | +4 |
| Contrat de combat terminé | +5 |
| Échec d'un contrat | -3 |
| Attaque d'un vaisseau | -10 |
| Attaque d'une station | -25 |

Pas de dérive des relations hors ligne.

## 11. Hors ligne

- **Plafond** : 24 h au départ, 36 h (SCI-3), 48 h (SCI-5), 72 h (SCI-7).
- **Production et recherche** : 100 % de l'efficacité en ligne. **Commerce automatisé** : 90 % (aléas de marché simplifiés). **Activité personnelle** : 0 %.
- Aucun événement destructeur ; les événements de marché hors ligne sont limités à plus ou moins 10 % de prix.
- **Indicateur** : le revenu horaire hors ligne vaut entre 80 et 100 % du revenu horaire en ligne pour une même configuration.
- Aucune pénalité de rendement en v1. Si un joueur très passif progresse trop vite, on resserre les capacités de stockage plutôt que d'ajouter une pénalité.

## 12. Scénarios de test

| Scénario | Comportement | Résultat attendu |
| --- | --- | --- |
| S1 Actif 30 min | Minage manuel puis premiers achats | Phase 2 vers 15 min ; niveau de Minage proche de 5 |
| S2 Actif 2 h | Automatisation progressive | Phase 3 vers 1 h 20 ; au moins 1 employé et 1 vaisseau automatisé ; revenu net d'au moins 15 000 cr/h |
| S3 Retour après 8 h (suite de S2) | Aucune action pendant l'absence | Gain égal à 8 fois le revenu horaire, à plus ou moins 10 % ; aucune perte ; au moins une recherche terminée |
| S4 Retour après 24 h | Plafond atteint | Aucune perte ; stocks saturés signalés ; au moins 3 achats possibles au retour |
| S5 Joueur commerce | Routes et contrats | Phase 4 à 6 h, plus ou moins 25 % |
| S6 Joueur industrie | Chaînes de production | Chantier naval entre 20 h et 30 h |
| S7 Joueur militaire | Combat et escortes | Première corvette avant 15 h, première frégate avant 30 h ; frégate gagnante à plus de 85 % contre un raid de risque 3 |
| S8 Joueur passif | 5 min par jour pendant 14 jours | Atteint au moins la phase 3 ; aucun blocage de plus de 24 h |

## 13. Indicateurs et seuils d'alerte

| Indicateur | Seuil d'alerte | Signification |
| --- | --- | --- |
| Entrée dans une phase | Écart de plus de 25 % à la cible | Rythme à revoir |
| Temps sans achat possible (joueur actif) | Plus de 20 min | Blocage de progression |
| Part du revenu net par activité (commerce, extraction, industrie, combat) | Une seule activité au-dessus de 60 % | Stratégie dominante |
| Retour sur investissement d'un vaisseau commercial | Hors de 0,5 à 2 fois la cible | Prix ou marge à revoir |
| Écart de retour entre deux stratégies comparables | Plus de 2 fois | Déséquilibre |
| Part des salaires dans la VA d'une station | Hors de 10 à 40 % | Salaires à revoir |
| Puissance par crédit (classes de combat) | Écart de plus de 30 % | Combat à revoir |
| Revenu hors ligne par rapport au revenu en ligne | Moins de 80 % ou plus de 100 % | Hors ligne à revoir |
| Marchandises jamais produites par le joueur type | Plus de 3 | Marchandise inutile |
| Stock saturé plus de la moitié du temps | Un module au moins | Stockage ou demande à revoir |

## 14. Corrections à reporter dans les autres documents

- **GDD 6.2** : l'exemple de salaire (250 cr/h) est remplacé par la formule de la section 5.
- **GDD 20.3** : le « coût d'achat relatif » est remplacé par le tableau de la section 8.
- **TDD 8.2** : la formule de prix est inchangée ; les paramètres de marché (stock cible, consommation) viennent de la section 3.3.
- Les **recettes du GDD 19** sont conservées telles quelles ; si l'extraction domine (3.2), on ajuste d'abord la marge ou la demande, pas les recettes.

## 15. Questions ouvertes

- Rapport entre extraction et transformation (3.2) : à mesurer dès la première version du simulateur.
- Rentabilité du Transporteur S sur la meilleure route de départ (3.4) : cible de 3 h à valider.
- Puits à crédits en fin de partie : l'entretien et les salaires suffisent-ils, ou faut-il un puits supplémentaire (carburant ×10, licences) ?
- Quantité de titane dans le système de départ (GDD 22.1).
- Combat : ces valeurs dépendent de la résolution réelle du TDD 8.5 ; les courbes de victoire sont à vérifier une fois le simulateur de combat écrit.

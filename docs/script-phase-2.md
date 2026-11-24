# Script de la phase 2 (minutes 15 à 95) – Idle Space Empire (v0.1)

Suite du script des 15 premières minutes. Complément au GDD v0.2, au TDD v0.1, au BDS v0.1 et au prototype tableur.

Public : game design, développement, équilibrage. Ce document décrit ce que fait le joueur entre la phase 2 (Indépendant) et la phase 3 (Entrepreneur), avec les valeurs validées : scan de 10 données, COM-3 au palier T1, minage manuel de 4 minerais par cycle. Il relève aussi les périodes où le joueur n'a rien à acheter, et propose des correctifs.

## 1. Point de départ (minute 15)

| Élément | Valeur |
| --- | --- |
| Crédits | 1 400 |
| Données scientifiques | 6 |
| Technologies terminées | SCI-1 (offerte), IND-1, PER-1 |
| Niveau de Minage | 3 |
| Revenu du minage | 132 cr par minute (4 minerais par cycle de 20 s, +10 % avec IND-1) |
| Exploration | 10 données par scan de 60 s |

**Objectif de la phase 2 : entrer en phase 3**, c'est-à-dire avoir un employé et un Transporteur S automatisé sur une route commerciale (COM-4).

**Besoin restant** : 126 données (COM-1, COM-2, COM-3 à 12 chacune, COM-4 à 96, moins les 6 déjà en poche) et 10 300 cr (COM-1, COM-2, COM-3 à 300 chacune, COM-4 à 2 400, employé 1 500, Transporteur S 5 500). Les recherches tournent en arrière-plan : 2 min pour les trois premières, 12 min pour COM-4.

## 2. Plan de jeu de référence (avant correctifs)

| Temps | Action du joueur | Déblocage | Crédits | Données |
| --- | --- | --- | --- | --- |
| 15:00 | Passe en exploration |  | 1 400 | 6 |
| 16:00 | Lance COM-1 (12 données, 300 cr) | Registre de marché à 18:00 | 1 100 | 4 |
| 16:00 à 18:00 | Continue d'explorer |  | 1 100 | 24 |
| 18:00 | Lance COM-2 (12 données, 300 cr) | Contrats de transport à 20:00 | 800 | 12 |
| 18:00 à 20:00 | Continue d'explorer |  | 800 | 32 |
| 20:00 | Lance COM-3 (12 données, 300 cr) | Transporteur S à 22:00 | 500 | 20 |
| 20:00 à 28:00 | Explore (8 scans) ; niveau 3 d'Exploration vers 23:00 |  | 500 | 100 |
| 28:00 à 42:30 | Retourne au minage | Niveau 4 de Minage vers 35:00 | 2 410 | 100 |
| 42:30 | Lance COM-4 (96 données, 2 400 cr) | Routes commerciales à 54:30 | 10 | 4 |
| 43:00 | Niveau 5 de Minage | Voir proposition A | 80 | 4 |
| 42:30 à 54:00 | Mine pour financer l'employé | Niveau 6 vers 52:40 | 1 530 | 4 |
| 54:00 | Recrute le premier employé (1 500 cr) | Employé disponible | 30 | 4 |
| 54:00 à 95:30 | Mine pour financer le Transporteur S | Niveaux 7, 8 et 9 vers 64:00, 77:30 et 93:30 | 5 510 | 4 |
| 95:30 | Achète le Transporteur S (5 500 cr), lui affecte l'employé et lance une route | Phase 3 | 10 | 4 |

Résultat : **phase 3 vers 1 h 35**, ce que confirme la feuille Rythme du prototype tableur. Les critères du BDS sont respectés (cible 1 h 30, tolérance de 25 %).

## 3. Ce que le joueur voit pendant la phase 2

- **COM-1, Registre de marché** : l'onglet Commerce affiche les prix de toutes les marchandises du secteur, plus seulement ceux du fer.
- **COM-2, Contrats de transport** : une liste de contrats apparaît dans l'onglet Commerce.
- **COM-3, Transporteurs S** : l'onglet Vaisseaux s'ouvre et propose le Transporteur S à 5 500 cr, chez un chantier de la Ligue Marchande.
- **COM-4, Routes commerciales** : le joueur peut programmer un aller-retour entre deux stations.
- **Employés** : l'onglet propose six profils ; un employé de niveau 1 commun coûte 1 500 cr à recruter et 500 cr/h de salaire.
- **Objectif visible** en permanence, comme dans les 15 premières minutes : chaque étape du tableau devient l'objectif du moment.

## 4. Première route conseillée et trésorerie

La meilleure marchandise accessible à ce stade est le **silicium** (14 cr l'unité). Un Transporteur S transporte 100 unités, soit 1 400 cr de marchandise par aller. Avec une marge de 25 % et un cycle de 10 minutes (6 par heure) :

| Élément | Valeur par heure |
| --- | --- |
| Marge brute | 6 × 100 × 14 × 25 % = 2 100 cr |
| Salaire du pilote | 500 cr |
| Entretien et carburant | environ 33 cr |
| **Revenu net** | **environ 1 570 cr** |

Retour sur investissement du vaisseau : environ 3,5 h, pour une cible du BDS de 3 h. Avec le minage manuel (7 900 cr/h), le joueur atteint environ 9 500 cr/h, proche des 10 000 cr/h visés en fin de phase 2.

**Problème de trésorerie** : après l'achat du Transporteur S et le recrutement, il reste environ 10 cr. Or la première cargaison coûte jusqu'à 1 400 cr. Il faut donc qu'une route **achète dans la limite des crédits disponibles** (cargaison partielle au début) ou que la Ligue Marchande avance la première cargaison. Voir la section 8.

## 5. Temps morts

Le BDS 13 déclenche une alerte au-delà de **20 minutes sans achat possible**.

| Période | Durée | Ce que le joueur attend |
| --- | --- | --- |
| 28:00 à 42:30 | 14,5 min | 2 400 cr pour COM-4 |
| 42:30 à 54:00 | 11,5 min | 1 500 cr pour l'employé |
| 54:00 à 95:30 | **41,5 min** | 5 500 cr pour le Transporteur S |

Les deux premières périodes sont acceptables, avec des niveaux de compétence en chemin. La troisième est une longue période de minage sans rien à acheter : c'est le principal risque d'abandon du début de partie.

## 6. Propositions (adoptées, voir section 10)

**A. Le niveau 5 de Minage débloque le minage manuel de silicium** (GDD 5.1, « astéroïdes riches »). Le silicium vaut 14 cr contre 10 pour le fer : 185 cr par minute au lieu de 132. Le joueur sent la récompense d'un niveau, et la phase 3 arrive vers **1 h 20** au lieu de 1 h 35.

**B. Un équipement intermédiaire pour le vaisseau personnel** : *Foreuse Mk1*, 900 cr, +15 % d'extraction manuelle, débloquée au niveau 6 de Minage. Son retour est d'environ 45 minutes, comme celui d'une mine (BDS 4). Effet net sur le rythme : proche de zéro, mais il coupe la longue attente.

**C. Une route qui achète dans la limite des crédits disponibles** (voir 4).

**Effet combiné de A et B** : la plus longue période sans achat passe de 41,5 à environ 26 minutes. Pour passer sous 20 minutes, il faudrait un second achat intermédiaire, à définir avec l'équipe d'équilibrage.

**Recommandation** : adopter A, B et C.

## 7. Ce qui n'est pas modélisé

- Le bonus de +1 % d'efficacité par niveau de compétence (BDS 6) : il raccourcirait la phase 2 de 3 à 4 minutes.
- La durée de COM-4, qui peut varier de 6 à 18 minutes selon son facteur.
- Le salaire de l'employé payé pendant l'attente du Transporteur S : environ 350 cr, soit 3 minutes de plus. Alternative : acheter le vaisseau avant de recruter le pilote.
- La saturation du marché : le minage manuel (720 unités par heure) dépasse la consommation d'une station (600).

## 8. Écarts et décisions (tranchés en section 10)

1. **Niveau 5 de Minage** : valider la proposition A (déblocage du silicium) ou choisir un autre effet.
2. **Foreuse Mk1** : valider l'équipement, son prix et son niveau de déblocage, et l'ajouter au BDS 8 ou 9 ; le GDD 20.4 décrit les modules de vaisseau, mais pas ceux du personnage.
3. **Route et trésorerie** : choisir entre cargaison limitée par les crédits et avance de la Ligue Marchande ; l'inscrire au GDD 8.4 et au TDD 8.2.
4. **Déclencheur de la phase 3** : proposer de le fixer au début du premier trajet automatique, pas à son achèvement.
5. **Missions de transport manuelles** (COM-2) : le BDS ne donne que la récompense (115 % de la valeur des marchandises), pas la quantité transportée ni qui fournit les marchandises. À définir, car cette activité pourrait battre le minage en rendement.
6. **Ordre d'achat** : recruter le pilote avant ou après le vaisseau (section 7).

## 9. Suite

- Valider les décisions de la section 8, puis les reporter dans les autres documents.
- Mettre à jour la feuille Rythme du prototype pour modéliser les propositions A et B.
- Écrire les maquettes des écrans principaux (barre de ressources, onglets, bilan hors ligne).

## 10. Correctifs adoptés et plan révisé

Les propositions A, B et C ont été adoptées, et les six décisions de la section 8 sont tranchées.

| N° | Décision |
| --- | --- |
| 1 | Le niveau 5 de Minage débloque le minage manuel de silicium (56 cr par cycle au lieu de 40). |
| 2 | Foreuse Mk1 : 900 cr, +15 % d'extraction manuelle, débloquée au niveau 6 de Minage. C'est un module du vaisseau personnel (GDD 20.4). |
| 3 | Une route achète dans la limite des crédits disponibles : cargaison partielle au début. |
| 4 | La phase 3 se déclenche au début du premier trajet automatique d'un vaisseau piloté par un employé. |
| 5 | Mission de transport manuelle : 12 unités fournies par le client, récompense de 115 % de leur valeur, soit environ 92 cr par minute pour le fer. C'est 70 % du minage : une activité alternative, pas dominante. |
| 6 | Ordre d'achat : le Transporteur S d'abord, le pilote ensuite. Aucun salaire n'est payé pendant l'attente, et le recrutement du pilote déclenche la phase 3. |

### Plan révisé à partir de la minute 28

Les minutes 15 à 28 sont inchangées (exploration, COM-1, COM-2, COM-3).

| Temps | Action du joueur | Déblocage | Crédits après |
| --- | --- | --- | --- |
| 28:00 à 42:25 | Mine du fer (132 cr par minute) |  | 2 400 avant l'achat |
| 42:25 | Lance COM-4 (96 données, 2 400 cr) | Routes commerciales à 54:25 | 0 |
| 43:05 | Niveau 5 de Minage | Minage de silicium : 185 cr par minute | environ 90 |
| 52:45 | Niveau 6 de Minage, achat de la Foreuse Mk1 (900 cr) | +15 % : 213 cr par minute | environ 980 |
| 74:00 | Achète le Transporteur S (5 500 cr) |  | environ 0 |
| 81:05 | Recrute le pilote (1 500 cr) et lance la première route | **Phase 3** | environ 0 |

Résultat : **phase 3 vers 1 h 21**, soit 14 minutes de gagnées sur le plan de référence (1 h 35). La feuille « Phase 2 (A+B) » du prototype tableur reproduit ce calcul.

### Temps morts après correctifs

| Période | Durée | Ce que le joueur attend |
| --- | --- | --- |
| 28:00 à 42:25 | 14,4 min | COM-4 (2 400 cr) |
| 42:25 à 52:45 | 10,3 min | Foreuse Mk1 (900 cr) |
| 52:45 à 74:00 | 21,3 min | Transporteur S (5 500 cr) |
| 74:00 à 81:05 | 7,1 min | Pilote (1 500 cr) |

La plus longue attente passe de 41,5 à 21,3 minutes : juste au-dessus du seuil de 20 minutes du BDS 13. **Question ouverte** : ajouter un achat intermédiaire entre la Foreuse Mk1 et le Transporteur S (par exemple une Foreuse Mk2 au niveau 7 de Minage) pour passer sous 20 minutes.

### Effets sur les autres valeurs

- En fin de phase 2, le minage rapporte environ 12 750 cr/h (213 cr par minute) et la route d'environ 1 570 cr/h, soit **environ 14 300 cr/h**. La cible du BDS pour la fin de la phase 2 passe de 10 000 à 14 000 cr/h.
- La cible d'entrée en phase 3 passe de 1 h 30 à **1 h 20**.
- Reports effectués : GDD 4, 5.1, 8.4 et 20.4 ; BDS 2, 3.4 et 8 ; TDD 8.2 ; prototype tableur.

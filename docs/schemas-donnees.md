# Schémas de données JSON – Idle Space Empire (v0.1)

Complément au TDD v0.1 (section 4). Public : équipe de développement, équipe d'équilibrage.

Ce document décrit chaque fichier du dossier data/ : ses champs, ses règles et un exemple réel avec les valeurs du BDS v0.1. Les valeurs d'équilibrage étant dans ces fichiers, l'équipe d'équilibrage peut les modifier sans toucher au code.

## 1. Conventions

- Chaque fichier est un objet `{ "version": 1, "entries": [ ... ] }`. Les fichiers qui ont des paramètres globaux ajoutent d'autres clés au même niveau (par exemple `families` dans goods.json).
- **Identifiants** : chaînes en minuscules avec tirets bas (iron\_ore), sauf les technologies qui gardent leur code du GDD (COM-3). Un identifiant est unique dans son fichier et **n'est jamais renommé** après publication.
- **Unités** : durées en secondes de jeu, prix en crédits entiers, pourcentages en décimaux (0.15 pour 15 %), distances en minutes de trajet à la vitesse 1.
- **Quantités** : toujours `{ "item": "<id marchandise>", "qty": <nombre> }`.
- **Textes visibles** : jamais dans ces fichiers. Ils sont dans lang/fr.json, avec les clés `<fichier>.<id>.name` et `<fichier>.<id>.desc` (par exemple `ships.transporter_s.name`).
- **Références** : un champ qui cite un autre identifiant doit pointer vers une entrée existante ; la validation échoue sinon (TDD 4).
- Dans les tableaux ci-dessous : **R** = champ obligatoire, **O** = optionnel.

### 1.1 Identifiants des marchandises

iron\_ore, copper\_ore, silicon, carbon, ice, titanium\_ore, steel, refined\_copper, titanium\_alloy, polymers, fuel, circuits, mechanical\_parts, engines, shields, ammo, missiles. L'électricité (`electricity`) et les données scientifiques (`data`) sont des ressources, non échangées sur le marché. Les crédits s'appellent `credits`.

### 1.2 Effets (vocabulaire fermé)

Un effet est un objet de l'un des trois types suivants. Il sert aux technologies, aux équipements, aux niveaux de compétence et au prestige.

| Type | Forme | Sens |
| --- | --- | --- |
| unlock | `{ "type": "unlock", "kind": "recipe", "id": "steel" }` | Débloque un élément. `kind` vaut recipe, module, ship, equipment, activity, contract, tab ou feature. |
| modifier | `{ "type": "modifier", "target": "production.speed", "op": "add", "value": 0.10 }` | Modifie une valeur. `op` vaut add (bonus additif en pourcentage) ou mul (multiplicateur). |
| limit | `{ "type": "limit", "key": "offline_cap_hours", "value": 36 }` | Fixe une limite. Clés : offline\_cap\_hours, research\_slots. |

Valeur finale = base × (1 + somme des bonus add) × produit des multiplicateurs mul (TDD 8.6).

Cibles de modifier admises en v1 : manual\_mining.yield, production.speed, production.output, production.energy, ship.speed, ship.fuel\_use, ship.cargo, research.speed, employee.xp, employee.salary, skill.xp, combat.damage, combat.hull.

## 2. Fichiers de marchandises et de production

### 2.1 goods.json

| Champ | Type | Description |
| --- | --- | --- |
| id | texte (R) | Identifiant de la marchandise |
| family | texte (R) | Famille de marché : raw, refined, chem\_elec, advanced ou military |
| basePrice | entier (R) | Prix de référence en crédits (BDS 3.1) |
| tradable | booléen (R) | Vrai si la marchandise s'échange sur le marché |

La clé `families` donne, par famille, le stock cible et la consommation de base par station (BDS 3.3).

```json
{
  "version": 1,
  "families": {
    "raw": { "stockTarget": 2000, "baseConsumption": 600 },
    "refined": { "stockTarget": 1000, "baseConsumption": 250 }
  },
  "entries": [
    { "id": "iron_ore", "family": "raw", "basePrice": 10, "tradable": true },
    { "id": "steel", "family": "refined", "basePrice": 30, "tradable": true }
  ]
}
```

### 2.2 recipes.json

| Champ | Type | Description |
| --- | --- | --- |
| id | texte (R) | Identifiant de la recette |
| module | texte (R) | Module qui l'exécute (modules.json) |
| inputs | liste de quantités (R) | Entrées ; liste vide pour une extraction |
| outputs | liste de quantités (R) | Sorties |
| duration | nombre (R) | Durée du cycle en secondes |
| energy | nombre (R) | Électricité consommée par cycle |
| unlock | texte (O) | Technologie qui la débloque ; absent si disponible dès le départ |
| requires | objet (O) | Condition de compétence : `{ "skill": "mining", "level": 10 }` |

```json
{
  "version": 1,
  "entries": [
    {
      "id": "steel", "module": "refinery",
      "inputs": [ { "item": "iron_ore", "qty": 3 }, { "item": "carbon", "qty": 1 } ],
      "outputs": [ { "item": "steel", "qty": 2 } ],
      "duration": 20, "energy": 3, "unlock": "IND-2"
    },
    {
      "id": "mine_titanium", "module": "mine",
      "inputs": [],
      "outputs": [ { "item": "titanium_ore", "qty": 4 } ],
      "duration": 45, "energy": 3, "unlock": "IND-1",
      "requires": { "skill": "mining", "level": 10 }
    }
  ]
}
```

### 2.3 modules.json

| Champ | Type | Description |
| --- | --- | --- |
| id | texte (R) | Identifiant du module |
| staff | entier (R) | Personnel nécessaire |
| cost | objet (R) | `{ "credits": <n>, "items": [quantités] }` |
| buildTime | nombre (R) | Temps de construction en secondes |
| costGrowth | nombre (O) | Hausse de coût par exemplaire supplémentaire dans une station (1.15 par défaut) |
| storage | entier (O) | Capacité de stockage ajoutée |
| energyOutput | nombre (O) | Électricité produite par cycle de 30 s (panneaux solaires) |
| unlock | texte (O) | Technologie qui le débloque |

```json
{
  "version": 1,
  "entries": [
    {
      "id": "refinery", "staff": 1,
      "cost": { "credits": 3800, "items": [ { "item": "steel", "qty": 25 } ] },
      "buildTime": 349, "costGrowth": 1.15, "unlock": "IND-2"
    },
    {
      "id": "warehouse", "staff": 1,
      "cost": { "credits": 2000, "items": [ { "item": "steel", "qty": 13 } ] },
      "buildTime": 209, "storage": 5000, "unlock": "IND-3"
    }
  ]
}
```

## 3. Fichiers de vaisseaux et d'équipement

### 3.1 ships.json

| Champ | Type | Description |
| --- | --- | --- |
| id | texte (R) | Identifiant de la classe |
| hull, shield, speed, cargo | nombres (R) | Caractéristiques de base (GDD 20.2) |
| crewMin | entier (R) | Équipage minimum |
| moduleSlots, weaponSlots | entiers (R) | Emplacements de modules et d'armes |
| fuelUse | nombre (R) | Carburant consommé par heure d'activité |
| buyPrice | entier (R) | Prix d'achat auprès d'une faction |
| build | objet (O) | Construction au chantier naval : `{ "credits": <n>, "items": [quantités] }` |
| upkeepRate | nombre (O) | Entretien par heure en part du prix d'achat (0.002 par défaut) |
| hangar | entier (O) | Nombre de petits vaisseaux accueillis |
| unlock | texte (O) | Technologie qui débloque la classe |

```json
{
  "version": 1,
  "entries": [
    {
      "id": "transporter_s",
      "hull": 120, "shield": 20, "speed": 6, "cargo": 100,
      "crewMin": 1, "moduleSlots": 2, "weaponSlots": 0, "fuelUse": 2,
      "buyPrice": 5500,
      "build": { "credits": 1100, "items": [
        { "item": "mechanical_parts", "qty": 6 }, { "item": "engines", "qty": 1 },
        { "item": "circuits", "qty": 2 }, { "item": "steel", "qty": 12 } ] },
      "unlock": "COM-3"
    }
  ]
}
```

### 3.2 equipment.json

| Champ | Type | Description |
| --- | --- | --- |
| id | texte (R) | Identifiant de l'équipement |
| slot | texte (R) | Type d'emplacement : thruster, shield, armor, weapon, cargo, scanner, drill, repair, quarters ou hangar |
| tier | entier (R) | Niveau de qualité : 1, 2 ou 3 (Mk1 à Mk3) |
| cost | objet (R) | `{ "credits": <n> }`, avec `items` si besoin |
| effects | liste d'effets (R) | Effets de l'équipement (1.2) |
| unlock | objet ou texte (O) | Technologie, ou condition de compétence `{ "skill": "mining", "level": 6 }` |
| damagePerSecond | nombre (O) | Dégâts par seconde, pour une arme |

```json
{
  "version": 1,
  "entries": [
    {
      "id": "drill_mk1", "slot": "drill", "tier": 1,
      "cost": { "credits": 900 },
      "effects": [ { "type": "modifier", "target": "manual_mining.yield", "op": "add", "value": 0.15 } ],
      "unlock": { "skill": "mining", "level": 6 }
    },
    {
      "id": "laser_mk1", "slot": "weapon", "tier": 1,
      "cost": { "credits": 1500 }, "damagePerSecond": 12,
      "effects": [], "unlock": "MIL-1"
    }
  ]
}
```

## 4. Fichiers de progression

### 4.1 technologies.json

| Champ | Type | Description |
| --- | --- | --- |
| id | texte (R) | Code du GDD (COM-3) |
| branch | texte (R) | navigation, industry, commerce, staff, military ou science |
| tier | entier (R) | Palier de 1 à 5 |
| prerequisites | liste de textes (R) | Technologies requises ; liste vide si aucune |
| cost | objet (R) | `{ "data": <n>, "credits": <n> }` |
| duration | nombre (R) | Durée en secondes |
| effects | liste d'effets (R) | Effets (1.2) |
| free | booléen (O) | Vrai si offerte (SCI-1) ; ignore le coût |

Les coûts suivent la formule du BDS 7 ; le fichier contient les valeurs déjà calculées.

```json
{
  "version": 1,
  "entries": [
    {
      "id": "COM-3", "branch": "commerce", "tier": 1,
      "prerequisites": [ "COM-1" ],
      "cost": { "data": 12, "credits": 300 }, "duration": 120,
      "effects": [ { "type": "unlock", "kind": "ship", "id": "transporter_s" } ]
    },
    {
      "id": "SCI-3", "branch": "science", "tier": 2,
      "prerequisites": [ "SCI-2" ],
      "cost": { "data": 96, "credits": 2400 }, "duration": 720,
      "effects": [ { "type": "limit", "key": "offline_cap_hours", "value": 36 } ]
    }
  ]
}
```

### 4.2 skills.json

| Champ | Type | Description |
| --- | --- | --- |
| id | texte (R) | Identifiant de la compétence |
| category | texte (R) | navigation, industry, economy, military ou science |
| xp | objet (R) | `{ "base": 60, "growth": 1.18 }` : XP du niveau n = base × growth puissance (n - 1) |
| maxLevel | entier (R) | Niveau maximum (50) |
| levelBonus | objet (R) | `{ "target": <cible>, "perLevel": 0.01, "cap": 0.50 }` |
| milestones | liste (O) | `{ "level": <n>, "effects": [effets] }` : déblocages par niveau |
| actions | liste (R) | Actions manuelles de la compétence |
| mastery | objet (O) | `{ "base": 200, "growth": 1.3, "maxLevel": 20, "bonusPerLevel": 0.02, "cap": 0.40 }` |

Une action : `id`, `cycle` (secondes), `xp`, `outputs`, `sellDirect` (vrai : vendu à la station du secteur sans passer par la soute), `requires` (niveau de compétence, optionnel).

```json
{
  "version": 1,
  "entries": [
    {
      "id": "mining", "category": "industry",
      "xp": { "base": 60, "growth": 1.18 }, "maxLevel": 50,
      "levelBonus": { "target": "manual_mining.yield", "perLevel": 0.01, "cap": 0.50 },
      "milestones": [
        { "level": 5, "effects": [ { "type": "unlock", "kind": "activity", "id": "mine_silicon" } ] },
        { "level": 6, "effects": [ { "type": "unlock", "kind": "equipment", "id": "drill_mk1" } ] }
      ],
      "actions": [
        { "id": "mine_iron", "cycle": 20, "xp": 4, "sellDirect": true,
          "outputs": [ { "item": "iron_ore", "qty": 4 } ] },
        { "id": "mine_silicon", "cycle": 20, "xp": 4, "sellDirect": true,
          "outputs": [ { "item": "silicon", "qty": 4 } ], "requires": { "level": 5 } }
      ]
    }
  ]
}
```

### 4.3 employees.json

Ce fichier est un objet unique de paramètres (pas de liste `entries`) :

| Champ | Type | Description |
| --- | --- | --- |
| baseSalary, salaryGrowth | nombres (R) | Salaire de base par heure et hausse par niveau (BDS 5) |
| efficiencyPerLevel, efficiencyCap | nombres (R) | Efficacité par niveau et plafond |
| hireMultiple | nombre (R) | Coût de recrutement en multiple du salaire horaire |
| marketSize, refreshSeconds | nombres (R) | Profils proposés et durée avant renouvellement |
| xpPerSecond | nombre (R) | XP gagnée par seconde de travail |
| rarities | liste (R) | `{ id, salaryMult, efficiencyBonus, marketShare }` |
| roles | liste de textes (R) | Postes possibles |

```json
{
  "version": 1,
  "baseSalary": 500, "salaryGrowth": 0.12,
  "efficiencyPerLevel": 0.015, "efficiencyCap": 0.30,
  "hireMultiple": 3, "marketSize": 6, "refreshSeconds": 7200, "xpPerSecond": 0.25,
  "rarities": [
    { "id": "common", "salaryMult": 1, "efficiencyBonus": 0, "marketShare": 0.70 },
    { "id": "expert", "salaryMult": 2.2, "efficiencyBonus": 0.20, "marketShare": 0.07 }
  ],
  "roles": [ "pilot", "engineer", "technician", "researcher", "commander", "trade_manager", "station_director" ]
}
```

## 5. Fichiers d'univers

### 5.1 universe.json

| Champ | Type | Description |
| --- | --- | --- |
| systems | liste (R) | Systèmes solaires : `id`, `unlock` (technologie d'accès, optionnelle) |
| sectors | liste (R) | Secteurs, voir ci-dessous |

Un secteur : `id`, `system`, `faction`, `risk` (0 à 10), `deposits` (liste de `{ item, richness }`), `stations` (liste de `{ id, faction }`), `links` (liste de `{ to, distance }`), `start` (vrai pour le secteur de départ, optionnel).

```json
{
  "version": 1,
  "systems": [ { "id": "aurore" }, { "id": "ferrum", "unlock": "NAV-6" } ],
  "sectors": [
    {
      "id": "aurore_1", "system": "aurore", "faction": "altair_league", "risk": 2, "start": true,
      "deposits": [ { "item": "iron_ore", "richness": 1.0 }, { "item": "silicon", "richness": 0.8 }, { "item": "ice", "richness": 1.0 } ],
      "stations": [ { "id": "aurore_1_hub", "faction": "altair_league" } ],
      "links": [ { "to": "aurore_2", "distance": 4 }, { "to": "aurore_3", "distance": 4 } ]
    }
  ]
}
```

### 5.2 factions.json

| Champ | Type | Description |
| --- | --- | --- |
| id | texte (R) | Identifiant de la faction |
| produces | liste de textes (R) | Marchandises produites par ses stations |
| demands | liste de textes (R) | Marchandises qu'elle demande |
| relationLevels | liste (R) | `{ id, min, max, buyMod, sellMod, access }` ; `access` est une liste de textes |
| relationEvents | objet (R) | Variation de relation par action (BDS 10) |

```json
{
  "version": 1,
  "entries": [
    {
      "id": "altair_league",
      "produces": [ "circuits", "polymers", "fuel" ],
      "demands": [ "steel", "mechanical_parts", "silicon" ],
      "relationLevels": [
        { "id": "hostile", "min": -100, "max": -51, "buyMod": 0.25, "sellMod": -0.20, "access": [ "dock_denied" ] },
        { "id": "neutral", "min": -10, "max": 24, "buyMod": 0, "sellMod": 0, "access": [] }
      ],
      "relationEvents": { "transport_done": 2, "supply_done": 3, "ship_attacked": -10, "station_attacked": -25 }
    }
  ]
}
```

## 6. Fichiers de contenu dynamique

### 6.1 contracts.json

Champs : `id`, `type` (transport, supply, extraction, escort ou combat), `unlock` (technologie), `params` (selon le type), `duration` (secondes), `relation` (gain de relation), `weight` (poids dans le tirage).

```json
{
  "version": 1,
  "entries": [
    {
      "id": "transport_basic", "type": "transport", "unlock": "COM-2",
      "params": { "units": 12, "rewardMult": 1.15 },
      "duration": 90, "relation": 2, "weight": 10
    }
  ]
}
```

### 6.2 events.json

Champs : `id`, `type` (market, pirate, discovery ou faction), `weight`, `conditions` (`phaseMin`, `riskMin`, optionnels), `offlineAllowed` (vrai si l'événement peut survenir hors ligne), `effect` (selon le type). **Règle** : un événement destructeur doit avoir `offlineAllowed` à faux (GDD 13).

```json
{
  "version": 1,
  "entries": [
    {
      "id": "ore_shortage", "type": "market", "weight": 5,
      "conditions": { "phaseMin": 3 }, "offlineAllowed": true,
      "effect": { "good": "iron_ore", "priceMod": 0.10, "duration": 3600 }
    }
  ]
}
```

### 6.3 achievements.json

Champs : `id`, `condition` (`{ "type": "phase", "value": 3 }`, types admis : phase, credits, tech, skill\_level, ship\_count), `reward` (un effet ou `{ "type": "credits", "value": 500 }`).

```json
{
  "version": 1,
  "entries": [
    { "id": "first_route", "condition": { "type": "phase", "value": 3 }, "reward": { "type": "credits", "value": 500 } }
  ]
}
```

## 7. Configuration globale (config.json)

```json
{
  "version": 1,
  "timeScale": 1,
  "stepSeconds": 1,
  "autosaveSeconds": 30,
  "offline": {
    "baseCapHours": 24, "stepSeconds": 60, "longStepSeconds": 300, "longStepAfterHours": 6,
    "efficiency": { "production": 1.0, "research": 1.0, "trade": 0.9, "personalActivity": 0.0 }
  },
  "market": { "priceSlope": 0.6, "priceBase": 1.6, "priceMin": 0.5, "priceMax": 2.0, "offlineHalfLifeHours": 2 },
  "economy": { "transformMargin": 1.6, "electricityCost": 0.3, "marketLossFactor": 0.8 },
  "start": { "credits": 500, "fuel": 100, "ship": "scout", "sector": "aurore_1" }
}
```

## 8. Règles de validation supplémentaires

En plus des règles du TDD 4 :

- Le graphe des technologies ne contient aucun cycle.
- Le palier d'une technologie est supérieur ou égal à celui de chacun de ses prérequis.
- Toute recette cite un module, des marchandises et une technologie existants.
- Un événement destructeur n'a jamais `offlineAllowed` à vrai.
- La somme des `marketShare` des raretés vaut 1.
- Les paliers de relation d'une faction couvrent -100 à +100 sans trou ni chevauchement.
- Chaque clé de texte attendue (`<fichier>.<id>.name`) existe dans lang/fr.json.

## 9. Pour démarrer

1. Créer le dossier data/ avec un fichier par section de ce document, rempli avec toutes les valeurs du GDD et du BDS (17 marchandises, 17 recettes, 11 modules, 10 vaisseaux, 52 technologies).
2. Écrire les schémas de validation (Zod) à partir des tableaux ci-dessus.
3. Brancher la validation sur l'intégration continue (TDD 13).
4. Faire relire le contenu par l'équipe d'équilibrage avant le jalon J0.

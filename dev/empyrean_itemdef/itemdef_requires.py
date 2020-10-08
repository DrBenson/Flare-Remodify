#!/usr/bin/env python

from itemdef_itemtype import ItemType

requires1 = []
# (stat, initial_value, value_per_level, initial_level)
requires1.insert(ItemType.MELEE_HEAD,      ("defense",  7, 2, 5))
requires1.insert(ItemType.RANGED_HEAD,     ("defense",  6, 2, 5))
requires1.insert(ItemType.MENT_HEAD,       ("defense",  5, 2, 5))
requires1.insert(ItemType.MELEE_CHEST,     ("defense",  4, 2, 4))
requires1.insert(ItemType.RANGED_CHEST,    ("defense",  3, 2, 4))
requires1.insert(ItemType.MENT_CHEST,      ("defense",  2, 2, 4))
requires1.insert(ItemType.MELEE_LEGS,      ("defense",  4, 2, 4))
requires1.insert(ItemType.RANGED_LEGS,     ("defense",  3, 2, 4))
requires1.insert(ItemType.MENT_LEGS,       ("defense",  2, 2, 4))
requires1.insert(ItemType.MELEE_FEET,      ("defense",  4, 2, 4))
requires1.insert(ItemType.RANGED_FEET,     ("defense",  3, 2, 4))
requires1.insert(ItemType.MENT_FEET,       ("defense",  2, 2, 4))
requires1.insert(ItemType.MELEE_HANDS,     ("defense",  4, 2, 4))
requires1.insert(ItemType.RANGED_HANDS,    ("defense",  3, 2, 4))
requires1.insert(ItemType.MENT_HANDS,      ("defense",  2, 2, 4))
requires1.insert(ItemType.MELEE_ARTIFACT,  ("defense",  4, 2, 4))
requires1.insert(ItemType.RANGED_ARTIFACT, ("defense",  3, 2, 4))
requires1.insert(ItemType.MENT_ARTIFACT,   ("defense",  2, 2, 4))
requires1.insert(ItemType.MELEE_WEAPON,    ("physical", 2, 2, 2))
requires1.insert(ItemType.RANGED_WEAPON,   ("offense",  2, 2, 2))
requires1.insert(ItemType.MENT_WEAPON,     ("mental",   2, 2, 2))
requires1.insert(ItemType.SHIELD,          ("defense",  3, 2, 3))
requires1.insert(ItemType.FIRE_RING,       ("",         0, 0, 0))
requires1.insert(ItemType.ICE_RING,        ("",         0, 0, 0))
requires1.insert(ItemType.SHOCK_RING,      ("",         0, 0, 0))
requires1.insert(ItemType.DARK_RING,       ("",         0, 0, 0))
requires1.insert(ItemType.XP_RING,         ("",         0, 0, 0))
requires1.insert(ItemType.GOLD_RING,       ("",         0, 0, 0))
requires1.insert(ItemType.ITEM_RING,       ("",         0, 0, 0))

requires2 = []
requires2.insert(ItemType.MELEE_HEAD,      ("physical", 2, 1, 4))
requires2.insert(ItemType.RANGED_HEAD,     ("offense",  3, 1, 4))
requires2.insert(ItemType.MENT_HEAD,       ("mental",   4, 1, 4))
requires2.insert(ItemType.MELEE_CHEST,     ("physical", 2, 1, 4))
requires2.insert(ItemType.RANGED_CHEST,    ("offense",  3, 1, 4))
requires2.insert(ItemType.MENT_CHEST,      ("mental",   4, 1, 4))
requires2.insert(ItemType.MELEE_LEGS,      ("physical", 2, 1, 4))
requires2.insert(ItemType.RANGED_LEGS,     ("offense",  3, 1, 4))
requires2.insert(ItemType.MENT_LEGS,       ("mental",   4, 1, 4))
requires2.insert(ItemType.MELEE_FEET,      ("physical", 2, 1, 4))
requires2.insert(ItemType.RANGED_FEET,     ("offense",  3, 1, 4))
requires2.insert(ItemType.MENT_FEET,       ("mental",   4, 1, 4))
requires2.insert(ItemType.MELEE_HANDS,     ("physical", 2, 1, 4))
requires2.insert(ItemType.RANGED_HANDS,    ("offense",  3, 1, 4))
requires2.insert(ItemType.MENT_HANDS,      ("mental",   4, 1, 4))
requires2.insert(ItemType.MELEE_ARTIFACT,  ("physical", 2, 1, 4))
requires2.insert(ItemType.RANGED_ARTIFACT, ("offense",  3, 1, 4))
requires2.insert(ItemType.MENT_ARTIFACT,   ("mental",   4, 1, 4))
requires2.insert(ItemType.MELEE_WEAPON,    ("",         0, 0, 0))
requires2.insert(ItemType.RANGED_WEAPON,   ("",         0, 0, 0))
requires2.insert(ItemType.MENT_WEAPON,     ("",         0, 0, 0))
requires2.insert(ItemType.SHIELD,          ("",         0, 0, 0))
requires2.insert(ItemType.FIRE_RING,       ("",         0, 0, 0))
requires2.insert(ItemType.ICE_RING,        ("",         0, 0, 0))
requires2.insert(ItemType.SHOCK_RING,      ("",         0, 0, 0))
requires2.insert(ItemType.DARK_RING,       ("",         0, 0, 0))
requires2.insert(ItemType.XP_RING,         ("",         0, 0, 0))
requires2.insert(ItemType.GOLD_RING,       ("",         0, 0, 0))
requires2.insert(ItemType.ITEM_RING,       ("",         0, 0, 0))

# level requirements
# (initial_value, value_per_level, initial_level)
requires3 = []
requires3.insert(ItemType.MELEE_HEAD,      (0, 0, 0))
requires3.insert(ItemType.RANGED_HEAD,     (0, 0, 0))
requires3.insert(ItemType.MENT_HEAD,       (0, 0, 0))
requires3.insert(ItemType.MELEE_CHEST,     (0, 0, 0))
requires3.insert(ItemType.RANGED_CHEST,    (0, 0, 0))
requires3.insert(ItemType.MENT_CHEST,      (0, 0, 0))
requires3.insert(ItemType.MELEE_LEGS,      (0, 0, 0))
requires3.insert(ItemType.RANGED_LEGS,     (0, 0, 0))
requires3.insert(ItemType.MENT_LEGS,       (0, 0, 0))
requires3.insert(ItemType.MELEE_FEET,      (0, 0, 0))
requires3.insert(ItemType.RANGED_FEET,     (0, 0, 0))
requires3.insert(ItemType.MENT_FEET,       (0, 0, 0))
requires3.insert(ItemType.MELEE_HANDS,     (0, 0, 0))
requires3.insert(ItemType.RANGED_HANDS,    (0, 0, 0))
requires3.insert(ItemType.MENT_HANDS,      (0, 0, 0))
requires3.insert(ItemType.MELEE_ARTIFACT,  (0, 0, 0))
requires3.insert(ItemType.RANGED_ARTIFACT, (0, 0, 0))
requires3.insert(ItemType.MENT_ARTIFACT,   (0, 0, 0))
requires3.insert(ItemType.MELEE_WEAPON,    (0, 0, 0))
requires3.insert(ItemType.RANGED_WEAPON,   (0, 0, 0))
requires3.insert(ItemType.MENT_WEAPON,     (0, 0, 0))
requires3.insert(ItemType.SHIELD,          (0, 0, 0))
requires3.insert(ItemType.FIRE_RING,       (2, 1, 4))
requires3.insert(ItemType.ICE_RING,        (2, 1, 4))
requires3.insert(ItemType.SHOCK_RING,      (2, 1, 4))
requires3.insert(ItemType.DARK_RING,       (2, 1, 4))
requires3.insert(ItemType.XP_RING,         (2, 1, 4))
requires3.insert(ItemType.GOLD_RING,       (2, 1, 4))
requires3.insert(ItemType.ITEM_RING,       (2, 1, 4))


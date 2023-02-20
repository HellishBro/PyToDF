# ITEMS
class ItemEnum:
    STONE = "stone"
    EMERALD = "emerald"
    LAPIS_LAZULI = "lapis_lazuli"
    COBBLESTONE = "cobblestone"

# CODE GEN
class Code:
    B_BLOCK = "block"
    B_BRACKET = "bracket"
    B_KILLABLE = "killable"

    B_EVENT = "event"
    B_PLAYER_ACTION = "player_action"
    B_ENTITY_EVENT = "entity_event"
    B_ENTITY_ACTION = "entity_action"
    B_GAME_ACTION = "game_action"
    B_IF_GAME = "if_game"
    B_CALL_FUNC = "call_func"
    B_START_PROC = "start_process"
    B_IF_ENTITY = "if_entity"
    B_IF_VAR = "if_var"
    B_PROCESS = "process"
    B_SELECT_OBJ = "select_obj"
    B_ELSE = "else"
    B_REPEAT = "repeat"
    B_FUNCTION = "func"
    B_CONTROL = "control"
    B_VAR = "set_var"
    B_IF_PLAYER = "if_player"

    B_SUB_SELECT_OBJ = "select_obj"
    B_SUB_REPEAT = "repeat"

    BRACKET_OPEN = "open"
    BRACKET_CLOSE = "close"
    BRACKET_IF = "norm"
    BRACKET_REPEAT = "repeat"

    VAR_GLOBAL = "unsaved"
    VAR_SAVED = "saved"
    VAR_LOCAL = "local"

    ITEM = "item"
    TAG = "bl_tag"
    VAR = "var"
    SOUND = "snd"
    NUM = "num"
    TEXT = "txt"
    LOCATION = "loc"
    VECTOR = "vec"
    GAME_VALUE = "g_val"
    POTION = "pot"
    PARTICLE = "part"


# Actions
class Actions:
    class Control:
        WAIT = "Wait"
        RETURN = "Return"
        END = "End"
        CONTINUE = "Skip"
        BREAK = "StopRepeat"
    class Var:
        SET_TO = "="
        RAND_CHOICE = "RandomValue"
        DEL_REGEX = "PurgeVars"

        ADD = "+"
        SUB = "-"
        MULT = "x"
        DIV = "/"
        MOD = "%"
        INC = "+="
        DEC = "-="
        POW = "Exponent"
        ROOT = "Root"
        LOG = "Logarithm"
        NUM_FROM_STR = "ParseNumber"
        ABS = "AbsoluteValue"
        CLAMP = "ClampNumber"
        WRAP = "WrapNumber"
        AVG = "Average"
        RAND = "RandomNumber"
        ROUND = "RoundNumber"
        NORMALLY_DISTRIBUTED_RAND = "NormalRandom"
        SINE = "Sine"
        COS = "Cosine"
        TAN = "Tangent"
        PERLIN = "PerlinNoise"
        VORONOI = "VoronoiNoise"
        WORLEY = "WorleyNoise"
        BITWISE = "Bitwise"

        SET_TEXT = "Text"
        REPLACE_TEXT = "ReplaceText"
        REMOVE_TEXT = "RemoveText"
        TRIM_TEXT = "TrimText"
        SPLIT_TEXT = "SplitText"
        JOIN_TEXT = "JoinText"
        SET_CASE = "SetCase"
        TRANSLATE_COLOR_CODE = "TranslateColors"
        TEXT_LEN = "TextLength"
        TEXT_REPEAT = "RepeatText"
        FORMAT_TIME = "FormatTime"

        GET_LOC_COORDS = "GetCoord"
        SET_LOC_COORDS = "SetCoord"
        SET_ALL_COORDS = "SetAllCoords"
        SHIFT_ON_AXIS = "ShiftOnAxis"
        SHIFT_ON_ALL_AXIS = "ShiftAllAxis"
        SHIFT_LOC_DIRECTION = "ShiftInDirection"
        SHIFT_LOC_ALL_DIR = "ShiftAllDirections"
        SHIFT_TOWARD_TARGET = "ShiftToward"
        SHIFT_ON_VECTOR = "ShiftOnVector"
        GET_LOC_DIRECTION = "GetDirection"
        SET_LOC_DIRECTION = "SetDirection"
        SHIFT_LOC_ROTATION = "ShiftRotation"
        FACE_LOCATION = "FaceLocation"
        ALIGN_LOCATION = "AlignLoc"
        SET_TO_DISTANCE = "Distance"
        SET_CENTER = "GetCenterLoc"
        SET_RANDOM = "RandomLoc"

        GET_I_MATERIAL = "GetItemType"
        GET_I_NAME = "GetItemName"
        GET_I_LORE = "GetItemLore"
        GET_I_LORE_LINE = "GetItemLoreLine"
        GET_I_STACK_SIZE = "GetItemAmount"
        GET_I_MAX_SIZE = "GetMaxItemAmount"
        GET_I_DURABILITY = "GetItemDura"
        GET_I_ENCHANTS = "GetItemEnchants"
        GET_I_HEAD_OWNER = "GetHeadOwner"
        GET_I_BOOK_TEXT = "GetBookText"
        GET_I_CUSTOM_TAG = "GetItemTag"
        GET_ALL_TAGS = "GetAllItemTags"
        GET_I_POTION_EFFECTS = "GetItemEffects"
        GET_I_RARITY = "GetItemRarity"
        GET_COMPASS_LODESTONE = "GetLodestoneLoc"
        GET_I_COLOR = "GetItemColor"
        GET_I_ATTR = "GetItemAttribute"
        SET_I_MATERIAL = "SetItemType"
        SET_I_NAME = "SetItemName"
        SET_I_LORE = "SetItemLore"
        SET_I_STACK_SIZE = "SetItemAmount"
        SET_I_DURABILITY = "SetItemDura"
        SET_I_BREAKABLE = "SetBreakability"
        SET_I_ENCHANTS = "SetItemEnchants"
        ADD_I_ENCHANT = "AddItemEnchant"
        REMOVE_I_ENCHANT = "RemoveItemEnchant"
        SET_HEAD_TEXTURE = "SetHeadTexture"
        SET_I_BOOK_TEXT = "SetBookText"
        SET_I_CUSTOM_TAG = "SetItemTag"
        REMOVE_I_CUSTOM_TAG = "RemoveItemTag"
        SET_CUSTOM_MODEL = "SetModelData"
        SET_I_POTION_EFFECTS = "SetItemEffects"
        SET_I_VISIBLE_FLAGS = "SetItemFlags"
        SET_PLACABLE = "SetCanPlaceOn"
        SET_BREAKABLE = "SetCanDestroy"
        SET_COMPASS_LODESTONE = "SetLodestoneLoc"
        SET_I_COLOR = "SetItemColor"
        SET_I_ATTR = "SetItemAttribute"
        SET_MAP_TEXTURE = "SetMapTexture"
    class Player:
        GIVE_ITEMS = "GiveItems"
        SET_HOTBAR_ITEMS = "SetHotbar"
        SET_INVENTORY_ITEMS = "SetInventory"
        SET_SLOT_ITEM = "SetSlotItem"
        SET_EQUIPMENT_ITEM = "SetEquipment"
        SET_ARMOR_ITEMS = "SetArmor"
        REPLACE_ITEMS = "ReplaceItems"
        REMOVE_ITEMS = "RemoveItems"
        CLEAR_ITEMS = "ClearItems"
        CLEAR_INV = "ClearInv"
        SET_CURSOR_ITEM = "SetCursorItem"
        SAVE_CURR_INV = ""
        LOAD_SAVED_INV = ""
        SET_ITEM_COOLDOWN = "SetItemCooldown"


# PLAYER EVENTS
class PlayerEvent:
    JOIN = "Join"
    LEAVE = "Leave"
    CMD = "Command"
    RC = "RightClick"
    LC = "LeftClick"
    RC_ENTITY = "player_right_click_entity"
    RC_PLAYER = "player_right_click_player"
    PLACE_BLOCK = "player_place_block"
    BREAK_BLOCK = "player_break_block"
    SWAP_HANDS = "player_swap_hands"
    CHANGE_SLOT = "player_change_slot"
    WALK = "player_walk"
    JUMP = "player_jump"
    SNEAK = "player_sneak"
    UNSNEAK = "player_unsneak"
    START_SPRINT = "player_start_sprint"
    STOP_SPRINT = "player_stop_sprinting"
    START_FLIGHT = "player_start_flight"
    STOP_FLIGHT = "player_stop_flight"
    RIPTIDE = "player_riptide"
    DISMOUNT = "player_dismount"
    HORSE_JUMP = "player_horse_jump"
    VEHICLE_JUMP = "player_vehicle_jump"
    CLICK_MENU_SLOT = "player_click_menu_slot"
    CLICK_INV_SLOT = "player_click_inventory_slot"
    PICK_UP_ITEM = "player_pick_up_item"
    DROP_ITEM = "player_drop_item"
    CONSUME_ITEM = "player_consume_item"
    BREAK_ITEM = "player_break_item"
    CLOSE_INV = "player_close_inventory"
    FISH = "player_fish"
    TAKE_DAMAGE = "player_take_damage"
    DAMAGE_PLAYER = "player_damage_player"
    DAMAGE_ENTITY = "player_damage_entity"
    ENTITY_DAMAGE_PLAYER = "entity_damage_player"
    HEAL = "player_heal"
    SHOOT_BOW = "player_shoot_bow"
    SHOOT_PROJECTILE = "player_shoot_projectile"
    PROJECTILE_HIT = "player_projectile_hit"
    PROJECTILE_DAMAGE_PLAYER = "projectile_damage_player"
    POTION_CLOUD_IMBUE_PLAYER = "potion_cloud_imbue_player"
    DEATH = "player_death"
    KILL_PLAYER = "player_kill_player"
    KILL_MOB = "player_kill_mob"
    MOB_KILL_PLAYER = "mob_kill_player"
    RESPAWN = "player_respawn"

# ENTITY EVENTS
class EntityEvent:
    DAMAGE_ENTITY = "entity_damage_entity"
    KILL_ENTITY = "entity_kill_entity"
    TAKE_DAMAGE = "entity_take_damage"
    PROJECTILE_DAMAGE_ENTITY = "projectile_damage_entity"
    PROJECTILE_KILL_ENTITY = "projectile_kill_entity"
    DEATH = "entity_death"
    VEHICLE_TAKE_DAMAGE = "vehicle_take_damage"
    BLOCK_FALL = "block_fall"
    FALLING_BLOCK_LAND = "falling_block_land"

# FINAL
ConstantDict = {}
def genDict(enum, parent=None):
    for item in dir(enum):
        if not item.startswith("__"):
            data = getattr(enum, item)
            if type(data) == type:
                genDict(data, enum.__name__)
            else:
                if parent:
                    ConstantDict[f"{parent}.{enum.__name__}.{item}"] = data
                else:
                    ConstantDict[f"{enum.__name__}.{item}"] = data

enums = [
    ItemEnum,
    Code,
    Actions,
    PlayerEvent,
    EntityEvent
]
for enum in enums:
    genDict(enum)

print(ConstantDict)

# ~ STATES
# ----------------------------------
START = "start"
INFO = "info"
CANCEL = "cancel"

# > CONSTANTES PARA CATEGORIA DE MOTOS 

NAKED = "naked"
SCOOTER = "scooter"
CRUCERO = "crucero"
CHOOPER = "chooper"
CUSTOM = "custom"
SIDECAR = "sidecar"
TOURING = "touring"
RACER = "racer"
TRIAL = "trial"

SHOW_MOTO_NAKED = "show_moto_naked"
SHOW_MOTO_SCOOTER = "show_moto_scooter"
SHOW_MOTO_CRUCERO = "show_moto_crucero"
SHOW_MOTO_CHOOPER = "show_moto_chooper"
SHOW_MOTO_CUSTOM = "show_moto_custom"
SHOW_MOTO_SIDECAR = "show_moto_sidecar"
SHOW_MOTO_TOURING = "show_moto_touring"
SHOW_MOTO_RACER = "show_moto_racer"
SHOW_MOTO_TRIAL = "show_moto_trial"


# ~ USMOTOS PRODUCTOS
PRODUCTS = "products"
MOTORCYCLE = "motorcycle"
ACCESORIES = "accesories"
PROMOTIONS = "promotions"

CATEGORYS_MOTO = "categorys_moto"

CATEGORY_MOTORCYCLE = "category_motorcycle"

CATEGORYS_M = "categorys_m"

LIST_ASISTENCIAS = "list_asistencias"

# ----------------------------------

# ~ TRIGGERS
# ----------------------------------
SHOW_START = "show_start"
SHOW_INFO = "show_info"
SHOW_LOGIN = "show_login"

START_DESTROY = "start_destroy"
ADD_CEDULA_DESTROY = "add_cedula_destroy"


SHOW_MISSION = "show_mission"
SHOW_VIEW = "show_view"
SHOW_SCHEDULE = "show_schedule"
SHOW_ADDRESS = "show_address"


MISSION = "mission"
VIEW = "view"
SCHEDULE = "schedule"
ADDRESS = "address"

SHOW_INFORMATION = "show_information"
INFORMATION_BUSINESS = "information_business"

# MOTOS 
SHOW_PRODUCTS = "show_products"
SHOW_MOTORCYCLES = "show_motorcycles"
SHOW_ACCESORIES = "show_accessories"
SHOW_PROMOTIONS = "show_promotions"

SHOW_REPARACION = "show_reparacion"

SHOW_CATEGORY_MOTORCYCLE = "show_category_motorcycle"

SHOW_ASISTENCIAS = "show_asistencias"
# ----------------------------------
# ~ CONDITIONS
# ----------------------------------
HAS_SESSION = "has_session"

HAS_USER = "has_user"


PROCESS_USER = "process_user"
ADD_CEDULA = "add_cedula"

# ~ STATES CONFIG
# ----------------------------------

states = [
    START, INFO,
    PRODUCTS, MOTORCYCLE, ACCESORIES, PROMOTIONS, CATEGORY_MOTORCYCLE,
    CATEGORYS_MOTO, MOTORCYCLE , SHOW_MOTO_NAKED, SHOW_MOTO_SCOOTER , SHOW_MOTO_CRUCERO,
    SHOW_MOTO_CHOOPER, SHOW_MOTO_CUSTOM, SHOW_MOTO_SIDECAR, SHOW_MOTO_TOURING, SHOW_MOTO_RACER, SHOW_MOTO_TRIAL,
    SHOW_PROMOTIONS, SHOW_ACCESORIES, PROCESS_USER, LIST_ASISTENCIAS, SHOW_MISSION ,SHOW_VIEW,
    SHOW_SCHEDULE, SHOW_ADDRESS ,SHOW_INFORMATION, INFORMATION_BUSINESS
]

# ~ TRANSITIONS
# ----------------------------------


transitions = [

    { # ------ USMOTOS TRANSICIONES ------
        'source': START, 'dest': PRODUCTS,
        'trigger': SHOW_PRODUCTS,
        'after': 'render_' + PRODUCTS,  # Reply
        'conditions': []
    },

    {
        'source': PRODUCTS, 'dest': START,
        'trigger': CANCEL,
        'after': 'render_' + START,  # Reply
        'conditions': []
    },

    {
        'source': START, 'dest': INFO,
        'trigger': SHOW_INFO,
        'after': 'render_' + INFO,  # Reply
        'conditions': []
    },

    {
        'source': PRODUCTS, 'dest': START,
        'trigger': CANCEL,
        'after': 'render_' + START,  # Reply
        'conditions': []
    },
    
    {
        'source': PRODUCTS, 'dest': CATEGORY_MOTORCYCLE,
        'trigger': SHOW_CATEGORY_MOTORCYCLE,
        'after': 'render_' + CATEGORYS_MOTO,  # Reply
        'conditions': []
    },

    {
        'source': CATEGORY_MOTORCYCLE, 'dest': START,
        'trigger': CANCEL,
        'after': 'render_' + START,  # Reply
        'conditions': []
    },

    {
        'source': CATEGORY_MOTORCYCLE, 'dest': SHOW_MOTO_NAKED,
        'trigger': NAKED,
        'after': 'render_' + SHOW_MOTO_NAKED,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_MOTO_NAKED, 'dest': CATEGORYS_MOTO,
        'trigger': CATEGORYS_M,
        'after': 'render_' + CATEGORYS_MOTO,  # Reply
        'conditions': []
    },

    {
        'source': CATEGORYS_MOTO, 'dest': START,
        'trigger': CANCEL,
        'after': 'render_' + START,  # Reply
        'conditions': []
    },

    {
        'source': CATEGORYS_MOTO, 'dest': SHOW_MOTO_NAKED,
        'trigger': NAKED,
        'after': 'render_' + SHOW_MOTO_NAKED,  # Reply
        'conditions': []
    },

    {
        'source': CATEGORY_MOTORCYCLE, 'dest': SHOW_MOTO_SCOOTER,
        'trigger': SCOOTER,
        'after': 'render_' + SHOW_MOTO_SCOOTER,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_MOTO_SCOOTER, 'dest': CATEGORYS_MOTO,
        'trigger': CATEGORYS_M,
        'after': 'render_' + CATEGORYS_MOTO,  # Reply
        'conditions': []
    },

    {
        'source': CATEGORYS_MOTO, 'dest': SHOW_MOTO_SCOOTER,
        'trigger': SCOOTER,
        'after': 'render_' + SHOW_MOTO_SCOOTER,  # Reply
        'conditions': []
    },

    {
        'source': CATEGORY_MOTORCYCLE, 'dest': SHOW_MOTO_CRUCERO,
        'trigger': CRUCERO,
        'after': 'render_' + SHOW_MOTO_CRUCERO,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_MOTO_CRUCERO, 'dest': CATEGORYS_MOTO,
        'trigger': CATEGORYS_M,
        'after': 'render_' + CATEGORYS_MOTO,  # Reply
        'conditions': []
    },

    {
        'source': CATEGORYS_MOTO, 'dest': SHOW_MOTO_CRUCERO,
        'trigger': CRUCERO,
        'after': 'render_' + SHOW_MOTO_CRUCERO,  # Reply
        'conditions': []
    },

    {
        'source': CATEGORY_MOTORCYCLE, 'dest': SHOW_MOTO_CHOOPER,
        'trigger': CHOOPER,
        'after': 'render_' + SHOW_MOTO_CHOOPER,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_MOTO_CHOOPER, 'dest': CATEGORYS_MOTO,
        'trigger': CATEGORYS_M,
        'after': 'render_' + CATEGORYS_MOTO,  # Reply
        'conditions': []
    },

    {
        'source': CATEGORYS_MOTO, 'dest': SHOW_MOTO_CHOOPER,
        'trigger': CHOOPER,
        'after': 'render_' + SHOW_MOTO_CHOOPER,  # Reply
        'conditions': []
    },

    {
        'source': CATEGORY_MOTORCYCLE, 'dest': SHOW_MOTO_CUSTOM,
        'trigger': CUSTOM,
        'after': 'render_' + SHOW_MOTO_CUSTOM,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_MOTO_CUSTOM, 'dest': CATEGORYS_MOTO,
        'trigger': CATEGORYS_M,
        'after': 'render_' + CATEGORYS_MOTO,  # Reply
        'conditions': []
    },

    {
        'source': CATEGORYS_MOTO, 'dest': SHOW_MOTO_CUSTOM,
        'trigger': CUSTOM,
        'after': 'render_' + SHOW_MOTO_CUSTOM,  # Reply
        'conditions': []
    },

    {
        'source': CATEGORY_MOTORCYCLE, 'dest': SHOW_MOTO_SIDECAR,
        'trigger': SIDECAR,
        'after': 'render_' + SHOW_MOTO_SIDECAR,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_MOTO_SIDECAR, 'dest': CATEGORYS_MOTO,
        'trigger': CATEGORYS_M,
        'after': 'render_' + CATEGORYS_MOTO,  # Reply
        'conditions': []
    },

    {
        'source': CATEGORYS_MOTO, 'dest': SHOW_MOTO_SIDECAR,
        'trigger': SIDECAR,
        'after': 'render_' + SHOW_MOTO_SIDECAR,  # Reply
        'conditions': []
    },

    {
        'source': CATEGORY_MOTORCYCLE, 'dest': SHOW_MOTO_TOURING,
        'trigger': TOURING,
        'after': 'render_' + SHOW_MOTO_TOURING,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_MOTO_SIDECAR, 'dest': CATEGORYS_MOTO,
        'trigger': CATEGORYS_M,
        'after': 'render_' + CATEGORYS_MOTO,  # Reply
        'conditions': []
    },

    {
        'source': CATEGORYS_MOTO, 'dest': SHOW_MOTO_SIDECAR,
        'trigger': SIDECAR,
        'after': 'render_' + SHOW_MOTO_SIDECAR,  # Reply
        'conditions': []
    },

    {
        'source': CATEGORY_MOTORCYCLE, 'dest': SHOW_MOTO_TOURING,
        'trigger': TOURING,
        'after': 'render_' + SHOW_MOTO_TOURING,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_MOTO_TOURING, 'dest': CATEGORYS_MOTO,
        'trigger': CATEGORYS_M,
        'after': 'render_' + CATEGORYS_MOTO,  # Reply
        'conditions': []
    },

    {
        'source': CATEGORYS_MOTO, 'dest': SHOW_MOTO_TOURING,
        'trigger': TOURING,
        'after': 'render_' + SHOW_MOTO_TOURING,  # Reply
        'conditions': []
    },

    {
        'source': CATEGORY_MOTORCYCLE, 'dest': SHOW_MOTO_RACER,
        'trigger': RACER,
        'after': 'render_' + SHOW_MOTO_RACER,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_MOTO_RACER, 'dest': CATEGORYS_MOTO,
        'trigger': CATEGORYS_M,
        'after': 'render_' + CATEGORYS_MOTO,  # Reply
        'conditions': []
    },

    {
        'source': CATEGORYS_MOTO, 'dest': SHOW_MOTO_RACER,
        'trigger': RACER,
        'after': 'render_' + SHOW_MOTO_RACER,  # Reply
        'conditions': []
    },

    {
        'source': CATEGORY_MOTORCYCLE, 'dest': SHOW_MOTO_TRIAL,
        'trigger': TRIAL,
        'after': 'render_' + SHOW_MOTO_TRIAL,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_MOTO_TRIAL, 'dest': CATEGORYS_MOTO,
        'trigger': CATEGORYS_M,
        'after': 'render_' + CATEGORYS_MOTO,  # Reply
        'conditions': []
    },

    {
        'source': CATEGORYS_MOTO, 'dest': SHOW_MOTO_TRIAL,
        'trigger': TRIAL,
        'after': 'render_' + SHOW_MOTO_TRIAL,  # Reply
        'conditions': []
    },
    {
        'source': SHOW_MOTO_NAKED, 'dest': START,
        'trigger': START,
        'after': 'render_' + START,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_MOTO_SCOOTER, 'dest': START,
        'trigger': START,
        'after': 'render_' + START,  # Reply
        'conditions': []
    },


    {
        'source': SHOW_MOTO_CRUCERO, 'dest': START,
        'trigger': START,
        'after': 'render_' + START,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_MOTO_CHOOPER, 'dest': START,
        'trigger': START,
        'after': 'render_' + START,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_MOTO_CUSTOM, 'dest': START,
        'trigger': START,
        'after': 'render_' + START,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_MOTO_SIDECAR, 'dest': START,
        'trigger': START,
        'after': 'render_' + START,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_MOTO_CRUCERO, 'dest': START,
        'trigger': START,
        'after': 'render_' + START,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_MOTO_TOURING, 'dest': START,
        'trigger': START,
        'after': 'render_' + START,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_MOTO_RACER, 'dest': START,
        'trigger': START,
        'after': 'render_' + START,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_MOTO_TRIAL, 'dest': START,
        'trigger': START,
        'after': 'render_' + START,  # Reply
        'conditions': []
    },


    # PROMOTIONS
    {
        'source': PRODUCTS, 'dest': PROMOTIONS,
        'trigger': SHOW_PROMOTIONS,
        'after': 'render_' + PROMOTIONS,  # Reply
        'conditions': []
    },

    {
        'source': PROMOTIONS, 'dest': START,
        'trigger': START,
        'after': 'render_' + START,  # Reply
        'conditions': []
    },

    {
        'source': PRODUCTS, 'dest': ACCESORIES,
        'trigger': SHOW_ACCESORIES,
        'after': 'render_' + ACCESORIES,  # Reply
        'conditions': []
    },

    {
        'source': ACCESORIES, 'dest': START,
        'trigger': START,
        'after': 'render_' + START,  # Reply
        'conditions': []
    },


    {
        'source': ACCESORIES, 'dest': PRODUCTS,
        'trigger': PRODUCTS,
        'after': 'render_' + PRODUCTS,  # Reply
        'conditions': []
    },

    # Para Asistencia Mecanica

    {
        'source': START, 'dest': PROCESS_USER,
        'trigger': SHOW_REPARACION,
        'after': 'render_' + PROCESS_USER,  # Reply
        'conditions': []
    },

    {
        'source': PROCESS_USER, 'dest': PROCESS_USER,
        'trigger': ADD_CEDULA,
        'after': 'render_' + PROCESS_USER,  # Reply
        'conditions': [HAS_USER]
    },

    {
        'source': PROCESS_USER, 'dest': LIST_ASISTENCIAS,
        'trigger': SHOW_ASISTENCIAS,
        'after': 'render_' + LIST_ASISTENCIAS,  # Reply
        'conditions': []
    },

    {
        'source': PROCESS_USER, 'dest': START,
        'trigger': START_DESTROY,
        'after': 'render_' + START,  # Reply
        'conditions': []
    },


    {
        'source': LIST_ASISTENCIAS, 'dest': START,
        'trigger': START_DESTROY,
        'after': 'render_' + START,  # Reply
        'conditions': []
    },

    {
        'source': LIST_ASISTENCIAS, 'dest': PROCESS_USER,
        'trigger': ADD_CEDULA_DESTROY,
        'after': 'render_' + PROCESS_USER,  # Reply
        'conditions': [HAS_USER]
    },


    # informacion de la empresa

    {
        'source': START, 'dest': SHOW_INFORMATION,
        'trigger': INFORMATION_BUSINESS,
        'after': 'render_' + SHOW_INFORMATION,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_INFORMATION, 'dest': SHOW_MISSION,
        'trigger': MISSION,
        'after': 'render_' + SHOW_MISSION,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_MISSION, 'dest': SHOW_INFORMATION,
        'trigger': INFORMATION_BUSINESS,
        'after': 'render_' + SHOW_INFORMATION,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_INFORMATION, 'dest': SHOW_VIEW,
        'trigger': VIEW,
        'after': 'render_' + SHOW_VIEW,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_VIEW, 'dest': SHOW_INFORMATION,
        'trigger': INFORMATION_BUSINESS,
        'after': 'render_' + SHOW_INFORMATION,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_INFORMATION, 'dest': SHOW_ADDRESS,
        'trigger': ADDRESS,
        'after': 'render_' + SHOW_ADDRESS,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_ADDRESS, 'dest': SHOW_INFORMATION,
        'trigger': INFORMATION_BUSINESS,
        'after': 'render_' + SHOW_INFORMATION,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_INFORMATION, 'dest': SHOW_SCHEDULE,
        'trigger': SCHEDULE,
        'after': 'render_' + SHOW_SCHEDULE,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_SCHEDULE, 'dest': SHOW_INFORMATION,
        'trigger': INFORMATION_BUSINESS,
        'after': 'render_' + SHOW_INFORMATION,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_INFORMATION, 'dest': START,
        'trigger': START,
        'after': 'render_' + START,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_ADDRESS, 'dest': START,
        'trigger': START,
        'after': 'render_' + START,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_SCHEDULE, 'dest': START,
        'trigger': START,
        'after': 'render_' + START,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_VIEW, 'dest': START,
        'trigger': START,
        'after': 'render_' + START,  # Reply
        'conditions': []
    },

    {
        'source': SHOW_MISSION, 'dest': START,
        'trigger': START,
        'after': 'render_' + START,  # Reply
        'conditions': []
    }

]
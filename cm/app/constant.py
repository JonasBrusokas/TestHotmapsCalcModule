
CELERY_BROKER_URL_DOCKER = 'amqp://admin:mypass@rabbit:5672/'
CELERY_BROKER_URL_LOCAL = 'amqp://localhost/'


CM_REGISTER_Q = 'rpc_queue_CM_register' # Do no change this value

CM_NAME = 'CM - Scale heat and cool density maps'
RPC_CM_ALIVE= 'rpc_queue_CM_ALIVE' # Do no change this value
RPC_Q = 'rpc_queue_CM_compute' # Do no change this value
CM_ID = 1 # CM_ID is defined by the enegy research center of Martigny (CREM)
PORT_LOCAL = int('500' + str(CM_ID))
PORT_DOCKER = 80

#TODO ********************setup this URL depending on which version you are running***************************

CELERY_BROKER_URL = CELERY_BROKER_URL_DOCKER
PORT = PORT_DOCKER

#TODO ********************setup this URL depending on which version you are running***************************

TRANFER_PROTOCOLE ='http://'
INPUTS_CALCULATION_MODULE = [ # <<< HERE we describe the
    {'input_name': 'Multiplication factor',
     'input_type': 'input',
     'input_parameter_name': 'multiplication_factor', # <<< INTERNAL NAME
     'input_value': '1',
     'input_priority': 0,
     'input_unit': '',
     'input_min': 0,
     # CM_ID is provided by the HT developers? (previously: CREM, now: ...?)
     'input_max': 10, 'cm_id': CM_ID  # Do no change this value
     },
]


SIGNATURE = {

    "category": "Demand",

    # This is sets up which data is available
    "authorized_scale": ["LAU 2", "Hectare"], # TODO: from dh_economic_assessment
    "description_link": "", # NOTE: same as 'wiki_url' ???
    "cm_name": CM_NAME,
    "wiki_url": "https://wiki.hotmaps.hevs.ch/en/CM-Scale-heat-and-cool-density-maps", #
    "layers_needed": [], # <<< NOTE IMPORTANT! Which layers are available to the calculation module?
    # It is not clear how to get the layer names. Mustafa always asked Crem colleagues

    # Raster types / layer types
    # "heat" can have multiple impl.
    # WE DO NOT HAVE A CENTRALIZED REPO FOR IDENTIFIERS (e.g. "heat_tot_curr_density" for layer or "heat" for type)
        # TODO: we would really like to have a centralized repository

    # NOTE: integration is not principally very difficult UNLESS you have special requests
    # e.g. running Gurobi, Cython

    # NOTE: THIS IS NOT AVAILABLE (data from the HT) DURING DEVELOPMENT
    # FOR LOCAL VERSION - WE NEED TO PASS THINGS MANUALLY
    "type_layer_needed": [
        {"type": "heat", "description": "Choose a heat demand density layer."}
    ],
    "type_vectors_needed": [],
    "cm_url": "Do not add something",
    "cm_description": "This calculation module allows to scale the heat demand density layer up or down.",
    "cm_id": CM_ID,
    'inputs_calculation_module': INPUTS_CALCULATION_MODULE
}

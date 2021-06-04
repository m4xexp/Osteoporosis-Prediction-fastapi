import json
import base64
import numpy as np
class arrEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            if obj.flags['C_CONTIGUOUS']:
                obj_data = obj.data
            else:
                cont_obj = np.ascontiguousarray(obj)
                assert(cont_obj.flags['C_CONTIGUOUS'])
                obj_data = cont_obj.data
            ## data_b64 = base64.b64encode(obj_data)
            ## converting to base64 and returning a dictionary did not work
            ## return dict(__ndarray__ = data_b64, dtype = str(obj.dtype), shape = obj.shape)
            return obj.tolist()  ## instead, utilize numpy builtin tolist() method
        try:
            my_dict = obj.__dict__   ## <-- ERROR raised here
        except TypeError:
            pass
        else:
            return my_dict
        return json.JSONEncoder.default(self, obj)
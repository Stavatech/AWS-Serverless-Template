import json, pickle


class SerializableObject(object):
    def pickle(self):
        return pickle.dumps(self)
    
    def to_JSON(self):
        return json.dumps(self, default=lambda o: self._try(o), sort_keys=True, indent=4, separators=[",", ":"])
    
    def to_dict(self):
        return json.loads(self.to_JSON())
    
    def _try(self, field):
        try:
            return vars(field)
        except:
            return str(field)
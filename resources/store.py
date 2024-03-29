from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message':'Store is not found'},404

    def post(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return {'message':'A store with a name "{}" already exists.'.format(name)},400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message":"An error occered while creating the store"},500
        return store.json()


    def delete(self,name):
        store  = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {"message":"The Store is Deleted."}


class StoreList(Resource):
    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}


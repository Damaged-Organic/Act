import dispatcher from "../dispatcher";

import * as centersConstants from "../constants/centersConstants";

class CentersProvider{

    constructor(){
        this.store = {};
    }
    setStore(store){
        this.store = store;
    }
    handleAction(action){
        switch(action.type){
            case centersConstants.LOAD_CENTERS_START:

                this.store.handleLoadCenterStart(action.payload);
                this.store.emit("change");

                break;
            case centersConstants.LOAD_CENTERS_END:

                this.store.handleLoadCenterEnd(action.payload);
                this.store.emit("change");

                break;
            case centersConstants.LOAD_CENTERS_ERROR:

                this.store.handleLoadCenterError(action.payload);
                this.store.emit("change");

                break;
        }
    }

}

const centersProvider = new CentersProvider();

dispatcher.register((action) => {
    centersProvider.handleAction(action);
});

export default centersProvider;
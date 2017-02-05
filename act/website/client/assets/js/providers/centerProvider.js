import dispatcher from "../dispatcher";

import * as centerConstants from "Constants/centerConstants";

class CenterProvider{

    constructor(){
        this.store = {};        
    }
    setStore(store){
        this.store = store;
    }
    handleAction(action){
        switch(action.type){
            case centerConstants.LOAD_CENTER_START:
                
                this.store.handleLoadStart(action.payload);
                this.store.emit("change");

                break;
            case centerConstants.LOAD_CENTER_END:
                
                this.store.handleLoadEnd(action.payload);
                this.store.emit("change");

                break;
            case centerConstants.LOAD_CENTER_ERROR:

                this.store.handleLoadError(action.payload);
                this.store.emit("change");

                break;
        }
    }

}

const centerProvider = new CenterProvider();

dispatcher.register((action) => {
    centerProvider.handleAction(action);
});

export default centerProvider;
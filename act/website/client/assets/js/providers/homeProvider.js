import dispatcher from "../dispatcher";

import * as homeConstants from "../constants/homeConstants";

class HomeProvider{

    constructor(){
        this.store = {};
    }
    setStore(store){
        this.store = store;
    }
    handleAction(action){
        switch(action.type){
            case homeConstants.LOAD_HOME_START:

                this.store.handleLoadStart(action.payload);
                this.store.emit("change");
                
                break;
            case homeConstants.LOAD_HOME_END:
                
                this.store.handleLoadEnd(action.payload);
                this.store.emit("change");

                break;
            case homeConstants.LOAD_HOME_ERROR:

                this.store.handleLoadError(action.payload);
                this.store.emit("change");

                break;
        }
    }

}

const homeProvider = new HomeProvider();

dispatcher.register((action) => {
    homeProvider.handleAction(action);
});

export default homeProvider;
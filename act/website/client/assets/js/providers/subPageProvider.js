import dispatcher from "../dispatcher";

import * as subPageConstants from "Constants/subPageConstants";

class SubPageProvider{

    constructor(){
        this.store = {};
    }
    setStore(store){
        this.store = store;
    }
    handleAction(action){
        switch(action.type){
            case subPageConstants.LOAD_SUBPAGE_START:
                
                this.store.handleLoadStart(action.payload);
                this.store.emit("change");

                break;
            case subPageConstants.LOAD_SUBPAGE_END:

                this.store.handleLoadEnd(action.payload);
                this.store.emit("change");
                
                break;
            case subPageConstants.LOAD_SUBPAGE_ERROR:

                this.store.handleLoadError(action.payload);
                this.store.emit("change");
                
                break;
        }
    }

}

const subPageProvider = new SubPageProvider();

dispatcher.register((action) => {
    subPageProvider.handleAction(action);
});

export default subPageProvider;
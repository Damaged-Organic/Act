import dispatcher from "../dispatcher";

import * as projectConstants from "Constants/projectConstants";

class ProjectProvider{

    constructor(){
        this.store = {};
    }
    setStore(store){
        this.store = store;
    }
    handleAction(action){
        switch(action.type){
            case projectConstants.LOAD_PROJECT_START:
                
                this.store.handleLoadStart(action.payload);
                this.store.emit("change");

                break;
            case projectConstants.LOAD_PROJECT_END:

                this.store.handleLoadEnd(action.payload);
                this.store.emit("change");

                break;
            case projectConstants.LOAD_PROJECT_ERROR:
                
                this.store.handleLoadError(action.payload);
                this.store.emit("change");

                break;
        }
    }

}

const projectProvider = new ProjectProvider();

dispatcher.register((action) => {
    projectProvider.handleAction(action);
});

export default projectProvider;
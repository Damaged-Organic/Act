import dispatcher from "../dispatcher";

import * as eventConstants from "Constants/eventConstants";

class EventProvider{

    constructor(){
        this.store = {};
    }
    setStore(store){
        this.store = store;
    }
    handleAction(action){
        switch(action.type){
            case eventConstants.LOAD_EVENT_START:
                
                this.store.handleLoadStart(action.payload);
                this.store.emit("change");

                break;
            case eventConstants.LOAD_EVENT_END:
                
                this.store.handleLoadEnd(action.payload);
                this.store.emit("change");

                break;
            case eventConstants.LOAD_EVENT_ERROR:
                
                this.store.handleLoadError(action.payload);
                this.store.emit("change");

                break;
        }
    }

}

const eventProvider = new EventProvider();

dispatcher.register((action) => {
    eventProvider.handleAction(action);
});

export default eventProvider;
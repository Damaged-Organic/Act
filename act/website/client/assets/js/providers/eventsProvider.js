import dispatcher from "../dispatcher";

import * as eventsConstants from "Constants/eventsConstants";

class EventsProvider{

    constructor(){
        this.store = {};
    }
    setStore(store){
        this.store = store;
    }
    handleAction(action){
        switch(action.type){
            case eventsConstants.LOAD_EVENTS_START:

                this.store.handleLoadStart(action.payload);
                this.store.emit("change");

                break;
            case eventsConstants.LOAD_EVENTS_END:

                this.store.handleLoadEnd(action.payload);
                this.store.emit("change");

                break;
            case eventsConstants.LOAD_EVENTS_ERROR:

                this.store.handleLoadError(action.payload);
                this.store.emit("change");

                break;
        }
    }

}

const eventsProvider = new EventsProvider();

dispatcher.register((action) => {
    eventsProvider.handleAction(action);
});

export default eventsProvider;
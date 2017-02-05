import dispatcher from "../dispatcher";

import * as connectConstants from "Constants/connectConstants";

class ConnectProvider{

    constructor(){
        this.store = {};
    }
    setStore(store){
        this.store = store;
    }
    handleAction(action){
        switch(action.type){
            case connectConstants.LOAD_CONNECT_START:

                this.store.handleLoadStart(action.payload);
                this.store.emit("change");

                break;
            case connectConstants.LOAD_CONNECT_END:

                this.store.handleLoadEnd(action.payload);
                this.store.emit("change");

                break;
            case connectConstants.LOAD_CONNECT_ERROR:

                this.store.handleLoadError(action.payload);
                this.store.emit("change");

                break;
            case connectConstants.SEND_CONNECT_START:

                this.store.handleSendStart(action.payload);
                this.store.emit("change");

                break;
            case connectConstants.SEND_CONNECT_END:

                this.store.handleSendEnd(action.payload);
                this.store.emit("change");

                break;
            case connectConstants.SEND_CONNECT_ERROR:

                this.store.handleSendError(action.payload);
                this.store.emit("change");

                break;
        }
    }

}

const connectProvider = new ConnectProvider();

dispatcher.register((action) => {
    connectProvider.handleAction(action);
});

export default connectProvider;
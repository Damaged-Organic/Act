import dispatcher from "../dispatcher";

import * as subscribeConstants from "Constants/subscribeConstants";

class SubscribeProvider{

    constructor(store = {}){
        this.store = store;
    }
    setStore(store){
        this.store = store;
    }
    handleAction(action){

        switch(action.type){
            case subscribeConstants.LOAD_SUBSCRIBE_START:

                this.store.handleLoadStart(action.payload);
                this.store.emit("change");

                break;
            case subscribeConstants.LOAD_SUBSCRIBE_END:

                this.store.handleLoadEnd(action.payload);
                this.store.emit("change");

                break;
            case subscribeConstants.LOAD_SUBSCRIBE_ERROR:

                this.store.handleLoadError(action.payload);
                this.store.emit("change");

                break;
            case subscribeConstants.CHECK_SUBSCRIBE_START:

                this.store.handleCheckSubscriberStart(action.payload);
                this.store.emit("change");

                break;
            case subscribeConstants.CHECK_SUBSCRIBE_END:

                this.store.handleCheckSubscriberEnd(action.payload);
                this.store.emit("change");

                break;
            case subscribeConstants.CHECK_SUBSCRIBE_ERROR:

                this.store.handleCheckSubscriberError(action.payload);
                this.store.emit("change");

                break;
            case subscribeConstants.CONFIRM_SUBSCRIBE_START:

                this.store.handleConfirmSubscribeStart(action.payload);
                this.store.emit("change");

                break;
            case subscribeConstants.CONFIRM_SUBSCRIBE_END:

                this.store.handleConfirmSubscribeEnd(action.payload);
                this.store.emit("change");

                break;
            case subscribeConstants.CONFIRM_SUBSCRIBE_ERROR:

                this.store.handleConfirmSubscribeError(action.payload);
                this.store.emit("change");

                break;
            case subscribeConstants.CHECK_UNSUBSCRIBE_START:

                this.store.handleCheckUnsubscribeStart(action.payload);
                this.store.emit("change");

                break;
            case subscribeConstants.CHECK_UNSUBSCRIBE_END:

                this.store.handleCheckUnsubscribeEnd(action.payload);
                this.store.emit("change");

                break;
            case subscribeConstants.CHECK_UNSUBSCRIBE_ERROR:

                this.store.handleCheckUnsubscribeError(action.payload);
                this.store.emit("change");

                break;
            case subscribeConstants.CONFIRM_UNSUBSCRIBE_START:

                this.store.handleConfirmUnsubscribeStart(action.payload);
                this.store.emit("change");

                break;
            case subscribeConstants.CONFIRM_UNSUBSCRIBE_END:

                this.store.handleConfirmUnsubscribeEnd(action.payload);
                this.store.emit("change");

                break;
            case subscribeConstants.CONFIRM_UNSUBSCRIBE_ERROR:

                this.store.handleConfirmUnsubscribeError(action.payload);
                this.store.emit("change");

                break;
        }

    }

}

const subscribeProvider = new SubscribeProvider();

dispatcher.register((action) => {
    subscribeProvider.handleAction(action);
});

export default subscribeProvider;
import dispatcher from "../dispatcher";

import * as aboutConstants from "Constants/aboutConstants";

class AboutProvider{

    constructor(){
        this.store = {};
    }
    setStore(store){
        this.store = store;
    }
    handleAction(action){
        switch(action.type){
            case aboutConstants.LOAD_ABOUT_START:

                this.store.handleLoadStart(action.payload);
                this.store.emit("change");

                break;
            case aboutConstants.LOAD_ABOUT_END:

                this.store.handleLoadEnd(action.payload);
                this.store.emit("change");

                break;
            case aboutConstants.LOAD_ABOUT_ERROR:

                this.store.handleLoadError(action.payload);
                this.store.emit("change");

                break;
        }
    }

}

const aboutProvider = new AboutProvider();

dispatcher.register((action) => {
    aboutProvider.handleAction(action);
});

export default aboutProvider;
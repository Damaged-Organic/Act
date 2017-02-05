import dispatcher from "../dispatcher";

import * as projectsConstants from "Constants/projectsConstants";

class ProjectsProvider{

    constructor(){
        this.store = {};
    }
    setStore(store){
        this.store = store;
    }
    handleAction(action){
        switch(action.type){
            case projectsConstants.LOAD_PROJECTS_START:
                
                this.store.handleLoadStart(action.payload);
                this.store.emit("change");

                break;
            case projectsConstants.LOAD_PROJECTS_END:
                
                this.store.handleLoadEnd(action.payload);
                this.store.emit("change");

                break;
            case projectsConstants.LOAD_PROJECTS_ERROR:
                
                this.store.handleLoadError(action.payload);
                this.store.emit("change");

                break;
        }
    }

}

const projectsProvider = new ProjectsProvider();

dispatcher.register((action) => {
    projectsProvider.handleAction(action);
});

export default projectsProvider;
import { EventEmitter } from "events";

import ProjectProvider from "Providers/projectProvider";

class ProjectStore extends EventEmitter{

    constructor(){
        super();
        
        this.data = {
            loading: false,
            metadata: {},
            sponsors: [],
            socials: [],
            project: {},
            centers: [],
            contacts: [],
            disclaimer: {},
            error: {}
        }
    }
    handleLoadStart(data){
        this.data.loading = data.loading;
    }
    handleLoadEnd(data){
        this.data.loading = data.loading;
        this.data.metadata = data.metadata;
        this.data.sponsors = data.sponsors;
        this.data.socials = data.socials;
        this.data.project = data.project;
        this.data.centers = data.centers;
        this.data.contacts = data.contacts;
        this.data.disclaimer = data.disclaimer;
    }
    handleLoadError(data){
        this.data.loading = data.loading;
        this.data.error = data.error;
    }
    isLoading(){
        return this.data.loading;
    }
    getMetaData(){
        return this.data.metadata;
    }
    getSponsors(){
        return this.data.sponsors;
    }
    getSocials(){
        return this.data.socials;
    }
    getProject(){
        return this.data.project;
    }
    getCenters(){
        return this.data.centers;
    }
    getContacts(){
        return this.data.contacts;
    }
    getDisclaimer(){
        return this.data.disclaimer;
    }
    getAll(){
        return this.data;
    }

}

const projectStore = new ProjectStore();

ProjectProvider.setStore(projectStore);

export default projectStore;
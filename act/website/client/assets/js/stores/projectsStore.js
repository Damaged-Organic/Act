import { EventEmitter } from "events";

import ProjectsProvider from "Providers/projectsProvider";

class ProjectsStore extends EventEmitter{

    constructor(){
        super();
        
        this.data = {
            loading: false,
            metadata: {},
            sponsors: [],
            socials: [],
            projects: {},
            categories: [],
            centers: [],
            contacts: [],
            disclaimer: {}
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
        this.data.projects = data.projects;
        this.data.categories = data.categories;
        this.data.centers = data.centers;
        this.data.contacts = data.contacts;
        this.data.disclaimer = data.disclaimer;
    }
    handleLoadError(data){
        this.data.loading = data.loading;
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
    getProjects(){
        return this.data.projects;
    }
    getCategories(){
        return this.data.categories;
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

const projectsStore = new ProjectsStore();

ProjectsProvider.setStore(projectsStore);

export default projectsStore;
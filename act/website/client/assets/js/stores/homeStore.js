import { EventEmitter } from "events";

import HomeProvider from "../providers/homeProvider";

class HomeStore extends EventEmitter{

    constructor(){
        super();

        this.data = {
            loading: false,
            metadata: {},
            sponsors: [],
            socials: [],
            intro: {},
            centers: [],
            activities: [],
            projects: {},
            events: {},
            disclaimer: {},
            contacts: [],
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
        this.data.intro = data.intro;
        this.data.centers = data.centers;
        this.data.activities = data.activities;
        this.data.projects = data.projects;
        this.data.events = data.events;
        this.data.disclaimer = data.disclaimer;
        this.data.contacts = data.contacts;
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
    getIntro(){
        return this.data.intro;
    }
    getCenters(){
        return this.data.centers;
    }
    getActivities(){
        return this.data.activities;
    }
    getProjects(){
        return this.data.projects;
    }
    getEvents(){
        return this.data.events;
    }
    getDisclaimer(){
        return this.data.disclaimer;
    }
    getContacts(){
        return this.data.contacts;
    }
    getAll(){
        return this.data;
    }

}

const homeStore = new HomeStore();

HomeProvider.setStore(homeStore);

export default homeStore;
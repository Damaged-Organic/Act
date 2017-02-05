import { EventEmitter } from "events";

import EventsProvider from "Providers/eventsProvider";

class EventsStore extends EventEmitter{

    constructor(){
        super();
        
        this.data = {
            loading: false,
            metadata: {},
            sponsors: [],
            socials: [],
            events: {},
            categories: [],
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
        this.data.events = data.events;
        this.data.categories = data.categories;
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
    getEvents(){
        return this.data.events;
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

const eventsStore = new EventsStore();

EventsProvider.setStore(eventsStore);

export default eventsStore;
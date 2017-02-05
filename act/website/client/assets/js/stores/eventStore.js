import { EventEmitter } from "events";

import EventProvider from "Providers/eventProvider";

class EventStore extends EventEmitter{

    constructor(){
        super();

        this.data = {
            loading: false,
            metadata: {},
            sponsors: [],
            socials: [],
            _event: {},
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
        this.data._event = data._event;
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
    getEvent(){
        return this.data._event;
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

const eventStore = new EventStore();

EventProvider.setStore(eventStore);

export default eventStore;


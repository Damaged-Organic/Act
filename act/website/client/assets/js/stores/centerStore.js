import { EventEmitter } from "events";

import CenterProvider from "Providers/centerProvider";

class CenterStore extends EventEmitter{

    constructor(){
        super();
        
        this.data = {
            loading: false,
            metadata: {},
            sponsors: [],
            socials: [],
            center: {},
            cities: [],
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
        this.data.center = data.center;
        this.data.cities = data.cities;
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
    getCenter(){
        return this.data.center;
    }
    getCities(){
        return this.data.cities;
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

const centerStore = new CenterStore();

CenterProvider.setStore(centerStore);

export default centerStore;
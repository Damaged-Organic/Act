import { EventEmitter } from "events";

import SubPageProvider from "Providers/subPageProvider";

class SubPageStore extends EventEmitter{

    constructor(){
        super();
        
        this.data = {
            loading: false,
            metadata: {},
            sponsors: [],
            socials: [],
            subPage: {},
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
        this.data.subPage = data.subPage;
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
    getSubPage(){
        return this.data.subPage;
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

const subPageStore = new SubPageStore();

SubPageProvider.setStore(subPageStore);

export default subPageStore;
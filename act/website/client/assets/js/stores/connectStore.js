import { EventEmitter } from "events";

import ConnectProvider from "Providers/connectProvider";

class ConnectStore extends EventEmitter{

    constructor(){
        super();
        
        this.data = {
            loading: false,
            metadata: {},
            sponsors: [],
            socials: [],
            centers: [],
            contacts: [],
            disclaimer: {},
            form: {
                loading: false,
                hasErrors: false,
                hasMessage: false,
                errors: {},
            },
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
        this.data.centers = data.centers;
        this.data.contacts = data.contacts;
        this.data.disclaimer = data.disclaimer;
    }
    handleLoadError(data){
        this.data.loading = data.loading;
        this.data.error = data.error;
    }
    handleSendStart(data){
        this.data.form.loading = data.loading;
    }
    handleSendEnd(data){
        this.data.form.loading = data.loading;
        this.data.form.hasMessage = data.hasMessage;
        this.data.form.hasErrors = data.hasErrors;
    }
    handleSendError(data){
        this.data.form.loading = data.loading;
        this.data.form.hasMessage = data.hasMessage;
        this.data.form.hasErrors = data.hasErrors;
        this.data.form.errors = data.error;
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
    getWorksheets(){
        return this.data.worksheets;
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

    getForm(){
        return this.data.form;
    }

}

const connectStore = new ConnectStore();

ConnectProvider.setStore(connectStore);

export default connectStore;
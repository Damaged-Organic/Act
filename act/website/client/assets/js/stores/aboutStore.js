import { EventEmitter } from "events";

import AboutProvider from "Providers/aboutProvider";

class AboutStore extends EventEmitter{

    constructor(){
        super();
        
        this.data = {
            loading: false,
            metadata: {},
            sponsors: [],
            socials: [],
            activities: [],
            aboutContent: {},
            centers: [],
            contacts: [],
            participants: [],
            partners: [],
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
        this.data.activities = data.activities;
        this.data.centers = data.centers;
        this.data.contacts = data.contacts;
        this.data.participants = data.participants;
        this.data.partners = data.partners;
        this.data.disclaimer = data.disclaimer;

        this.data.aboutContent = this.mergeContent(data.aboutContent, data.goalContent);
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
    getActivities(){
        return this.data.activities;
    }
    getAboutContent(){
        return this.data.aboutContent;
    }
    getCenters(){
        return this.data.centers;
    }
    getContacts(){
        return this.data.contacts;
    }
    getParticipants(){
        return this.data.participants;
    }
    getPartners(){
        return this.data.partners;
    }
    getDisclaimer(){
        return this.data.disclaimer;
    }
    getAll(){
        return this.data;
    }
    mergeContent(intro, goal){
        return {
            intro,
            goal
        }
    }

}

const aboutStore = new AboutStore();

AboutProvider.setStore(aboutStore);

export default aboutStore;

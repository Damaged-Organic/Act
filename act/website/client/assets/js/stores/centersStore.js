import { EventEmitter } from "events";

import CentersProvider from "../providers/centersProvider";

class CentersStore extends EventEmitter{

    constructor(){
        super();
        
        this.data = {
            loading: false,
            metadata: {},
            sponsors: [],
            socials: [],
            centers: [],
            error: {}
        }
    }
    handleLoadCenterStart(data){
        this.data.loading = data.loading;
    }
    handleLoadCenterEnd(data){
        this.data.loading = data.loading;
        this.data.metadata = data.metadata;
        this.data.sponsors = data.sponsors;
        this.data.socials = data.socials;
        this.data.centers = data.centers;
    }
    handleLoadCenterError(data){
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
    getCenters(){
        return this.data.centers;
    }
    getAll(){
        return this.data;
    }

}

const centersStore = new CentersStore();

CentersProvider.setStore(centersStore);

export default centersStore;
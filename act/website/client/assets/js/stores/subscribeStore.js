import { EventEmitter } from "events";

import SubscribeProvider from "Providers/subscribeProvider";

class SubscribeStore extends EventEmitter{

    constructor(){
        super();
        
        this.data = {
            loading: false,
            isChecked: false,
            isConfirmed: false,
            email: "",
            error: ""
        }
    }
    handleLoadStart(data){
        this.data.loading = data.loading;
    }
    handleLoadEnd(data){
        this.data.loading = data.loading;
        this.data.email = data.email;
        this.data.error = data.error;
    }
    handleLoadError(data){
        this.data.loading = data.loading;
        this.data.email = data.email;
        this.data.error = data.error;
    }
    handleCheckSubscriberStart(data){
        this.data.loading = data.loading;
    }
    handleCheckSubscriberEnd(data){
        this.data.loading = data.loading;
        this.data.isChecked = data.isChecked;
        this.data.email = data.email;
    }
    handleCheckSubscriberError(data){
        this.data.loading = data.loading;
        this.data.isChecked = data.isChecked;
        this.data.error = data.error;
    }
    handleConfirmSubscribeStart(data){
        this.data.loading = data.loading;
    }
    handleConfirmSubscribeEnd(data){
        this.data.loading = data.loading;
        this.data.isConfirmed = data.isConfirmed;
        this.data.email = data.email;
    }
    handleConfirmSubscribeError(data){
        this.data.loading = data.loading;
        this.data.isConfirmed = data.isConfirmed;
        this.data.error = data.error;
    }
    handleCheckUnsubscribeStart(data){
        this.data.loading = data.loading;
    }
    handleCheckUnsubscribeEnd(data){
        this.data.loading = data.loading;
        this.data.isChecked = data.isChecked;
        this.data.email = data.email;
    }
    handleCheckUnsubscribeError(data){
        this.data.loading = data.loading;
        this.data.isChecked = data.isChecked;
        this.data.error = data.error;
    }
    handleConfirmUnsubscribeStart(data){
        this.data.loading = data.loading;
    }
    handleConfirmUnsubscribeEnd(data){
        this.data.loading = data.loading;
        this.data.isConfirmed = data.isConfirmed;
        this.data.email = data.email;
    }
    handleConfirmUnsubscribeError(data){
        this.data.loading = data.loading;
        this.data.isConfirmed = data.isConfirmed;
        this.data.error = data.error;
    }
    isLoading(){
        return this.data.loading;
    }
    isChecked(){
        return this.data.isChecked;
    }
    isConfirmed(){
        return this.data.isConfirmed;
    }
    hasErrors(){
        return this.data.error ? true : false;
    }
    isSuccessfull(){
        return this.data.email ? true : false;
    }
    getEmail(){
        return this.data.email;
    }
    getAll(){
        return this.data;
    }

}

const subscribeStore = new SubscribeStore();

SubscribeProvider.setStore(subscribeStore);

export default subscribeStore;
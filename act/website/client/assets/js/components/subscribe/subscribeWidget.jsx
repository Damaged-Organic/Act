import React, { Component } from "react";
import { translate } from "react-i18next";
import autoBind from "autobind-decorator";

import * as subscribeActions from "Actions/subscribeActions";
import SubscribeStore from "Stores/subscribeStore";

@autoBind
class SubscribeWidget extends Component{

    constructor(props){
        super(props);
        
        this.state = {
            isActive: false,
            isLoading: SubscribeStore.isLoading(),
            hasErrors: SubscribeStore.hasErrors(),
            isSuccessfull: SubscribeStore.isSuccessfull(),
            email: ""
        }
    }
    componentWillMount(){
        SubscribeStore.on("change", this.handleStoreChange);
    }
    componentWillUnmount(){
        SubscribeStore.removeListener("change", this.handleStoreChange);
    }
    handleStoreChange(){
        this.setState({
            isLoading: SubscribeStore.isLoading(),
            hasErrors: SubscribeStore.hasErrors(),
            isSuccessfull: SubscribeStore.isSuccessfull()
        });
    }
    toggleActive(e){
        e.preventDefault();

        this.setState({ isActive: !this.state.isActive });
    }
    handleChangeEmail(e){
        this.setState({ email: e.target.value });
    }
    submitForm(e){
        e.preventDefault();

        if(this.state.isLoading) return;

        subscribeActions.subscribe({
            email: this.state.email
        });

        this.clearForm();
    }
    clearForm(){
        this.setState({
            email: ""
        });
    }
    render(){
        return(
            <div id="subscribe-widget-holder" class={ this.state.isActive ? "__active" : "" }>
                <div class="btn-subscribe" onClick={ (e) => this.toggleActive(e) }>
                    <span>{ this.props.t("buttons:subscribe") }</span>
                </div>
                <div class="inner">
                    { 
                        this.state.isSuccessfull
                            ? <p class="success-holder">{ this.props.t("forms:subscribe.success") }</p>
                            : <p>{ this.props.t("subscribeText") }</p>
                    }
                    <form method="POST" encType="application/x-www-form-urlencoded" id="subscribe-form" onSubmit={ (e) => this.submitForm(e) }>
                        <input
                            type="email"
                            name="email"
                            value={ this.state.email }
                            placeholder={ this.props.t("forms:subscribe.email") }
                            id="subscribe-form-email"
                            onChange={ (e) => this.handleChangeEmail(e) }
                        />
                        {
                            this.state.hasErrors
                                ? <span class="error-holder">{ this.props.t("forms:subscribe.error") }</span>
                                : null
                        }
                    </form>
                </div>
                { this.state.isLoading ? <span class="subscribe-loader"></span> : null }
            </div>
        );
    }

}

export default translate(["common", "forms", "buttons"])(SubscribeWidget);
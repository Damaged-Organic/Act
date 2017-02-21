import React, { Component } from "react";
import { Link } from "react-router";
import { translate } from "react-i18next";
import autoBind from "autobind-decorator";

import generateUrl from "Router/generateUrl";

import * as subscribeActions from "Actions/subscribeActions";
import SubscribeStore from "Stores/subscribeStore";

import Logo from "Pages/header/logo";

import Loader from "Components/loader";

@autoBind
class Unsubscribe extends Component{

    constructor(props){
        super(props);
        
        this.state = {
            isLoading: false,
            isChecked: false,
            isConfirmed: false,
            hasErrors: false,
            email: ""
        }
    }
    componentWillMount(){
        SubscribeStore.on("change", this.handleStoreChange);
    }
    componentDidMount(){
        let {id, hash} = this.props.params;

        subscribeActions.checkUnsubscriber(id, hash);
    }
    componentWillUnmount(){
        SubscribeStore.removeListener("change", this.handleStoreChange);
    }
    handleStoreChange(){
        this.setState({
            isLoading: SubscribeStore.isLoading(),
            isChecked: SubscribeStore.isChecked(),
            isConfirmed: SubscribeStore.isConfirmed(),
            email: SubscribeStore.getEmail()
        })
    }
    handleConfirm(e){
        e.preventDefault();

        if(this.state.isLoading) return;

        let id = this.props.params.id,
            hash = this.props.params.hash,
            email = this.state.email;

        if(!id || !hash || !email) return;

        subscribeActions.confirmUnsubscribe(id, hash, email);
    }
    renderButtons(){
        return(
            <div class="btns-holder">
                <div class="btn-cancel bordered">
                    <Link to={ generateUrl("home") }>{ this.props.t("buttons:cancel") }</Link>
                </div>
                <div class="btn-confirm" onClick={(e) => this.handleConfirm(e)}>
                    <span>{ this.props.t("buttons:unsubscribe") }</span>
                </div>
            </div>
        );
    }
    renderBackButton(){
        return(
            <div class="btns-holder">
                <div class="btn-back">
                    <Link to={ generateUrl("home") }>{ this.props.t("buttons:toHome") }</Link>
                </div>
            </div>
        );
    }
    render(){
        let isLoading = this.state.isLoading,
            isChecked = this.state.isChecked,
            isConfirmed = this.state.isConfirmed;

        return(
            <div id="page" class="__unsubscribe">
                <header id="header">
                    <Logo />
                </header>
                <main id="content">
                    <section class="container unsubscribe-holder">
                        <div class="inner">
                            <span class="upper-divider"></span>
                            <h1>{ this.props.t("headlines:subscribition.unsubscribe") }</h1>
                            {
                                isConfirmed && !isLoading
                                    ? <p class="success">{ this.props.t("confirmUnsubscribeSuccess") }</p>
                                    : null
                            }
                            {
                                !isChecked && !isConfirmed && !isLoading
                                    ? <p class="error">{ this.props.t("confirmUnsubscribeError") }</p>
                                    : null
                            }
                            {
                                isChecked && !isConfirmed
                                    ? this.renderButtons()
                                    : this.renderBackButton()
                            }
                        </div>
                    </section>
                </main>
                <Loader isLoading={ isLoading } />
            </div>
        );
    }

}

export default translate(["common", "headlines", "buttons"])(Unsubscribe);
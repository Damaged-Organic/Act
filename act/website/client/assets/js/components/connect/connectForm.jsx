import React, { Component } from "react";
import autoBind from "autobind-decorator";
import { translate } from "react-i18next";

import * as connectActions from "Actions/connectActions";
import ConnectStore from "Stores/connectStore";

@autoBind
class ConnectForm extends Component{

    constructor(props){
        super(props);
        
        this.state = {
            loading: false,
            hasErrors: false,
            fullName: "",
            residence: "",
            email: "",
            phone: "",
            personalLink: "",
            problem: false,
            problemDescription: "",
            activity: false,
            activityDescription: "",
            message: "",
            errors: {},
        }
    }
    componentWillMount(){
        ConnectStore.on("change", this.handleStoreChange);
    }
    componentWillUnmount(){
        ConnectStore.removeListener("change", this.handleStoreChange);
    }
    handleFullName(e){
        this.setState({ fullName: e.target.value });
    }
    handleResidence(e){
        this.setState({ residence: e.target.value });
    }
    handleEmail(e){
        this.setState({ email: e.target.value });
    }
    handlePhone(e){
        this.setState({ phone: e.target.value });
    }
    handlePersonalLink(e){
        this.setState({ personalLink: e.target.value });
    }
    handleProblem(e){
        let isChecked = (e.target.value === "false") ? true : false;

        this.setState({
            problem: isChecked,
            problemDescription: ""
        });
    }
    handleProblemDescription(e){
        this.setState({ problemDescription: e.target.value });
    }
    handleActivity(e){
        let isChecked = (e.target.value === "false") ? true : false;

        this.setState({
            activity: isChecked,
            activityDescription: ""
        });
    }
    handleActivityDescription(e){
        this.setState({ activityDescription: e.target.value });
    }
    handleSubmit(e){
        e.preventDefault();

        if(this.state.loading) return;
        
        connectActions.sendForm({
            "full_name": this.state.fullName,
            "residence": this.state.residence,
            "email": this.state.email,
            "phone": this.state.phone,
            "personal_link": this.state.personalLink,
            "problem": this.state.problem ? "true" : "",
            "problem_description": this.state.problemDescription,
            "activity": this.state.activity ? "true" : "",
            "activity_description": this.state.activityDescription
        });

        window.scrollTo(0, 0);
    }
    handleStoreChange(){
        let form = ConnectStore.getForm();
        
        if(!form.hasErrors){

            this.setState({
                loading: form.loading,
                hasErrors: form.hasErrors,
                fullName: "",
                residence: "",
                email: "",
                phone: "",
                personalLink: "",
                problem: false,
                problemDescription: "",
                activity: false,
                activityDescription: "",
                message: form.hasMessage ? this.props.t("forms:connect.message") : "",
                errors: form.errors
            });

        } else{

            this.setState({
                loading: form.loading,
                hasErrors: form.hasErrors,
                errors: form.errors
            });
        }

    }
    handleClose(e){
        e.preventDefault();
        
        this.setState({ message: "" });
    }
    renderLoading(){
        return(
            <div id="loading-holder" class={ this.state.loading ? "active" : null }>
                <div class="svg-holder">
                    <svg version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 60">
                        <defs>
                            <linearGradient id="gradient">
                                <stop offset="5%"  stopColor="#95212a" />
                                <stop offset="95%" stopColor="#4a87b1" />
                            </linearGradient>
                        </defs>
                        <circle cx="30" cy="30" r="28.5" stroke="url(#gradient)" />
                    </svg>
                </div>
            </div>
        );
    }
    renderErrors(errors){
        return errors.map((error, index) => <span key={ index } class="error-holder">{ error }</span>);
    }
    renderMessage(){
        return(
            <div class="success-holder">
                <p>{ this.state.message }</p>
                <span class="close icon-close" onClick={(e) => this.handleClose(e)}></span>
            </div>
        );
    }
    render(){
        return(
            <form method="POST" onSubmit={(e) => this.handleSubmit(e)} encType="application/x-www-form-urlencoded" id="connect-form" ref="connectForm">
                { this.state.message ? this.renderMessage() : null }
                <div class="input-holder">
                    <label for="connect-fullname">{ this.props.t("forms:connect.fullName") }</label>
                    <input
                        type="text"
                        name="full_name"
                        value={ this.state.fullName }
                        onChange={(e) => this.handleFullName(e)}
                        id="connect-fullname"
                        ref="fullName"
                    />
                    {
                        (this.state.hasErrors && this.state.errors.full_name && this.state.errors.full_name.length > 0)
                            ? this.renderErrors(this.state.errors.full_name)
                            : null
                    }
                </div>
                <div class="input-holder">
                    <label for="connect-residence">{ this.props.t("forms:connect.residence") }</label>
                    <input
                        type="text"
                        name="residence"
                        value={ this.state.residence }
                        onChange={(e) => this.handleResidence(e)}
                        id="connect-residence"
                        ref="residence"
                    />
                    {
                        (this.state.hasErrors && this.state.errors.residence && this.state.errors.residence.length > 0)
                            ? this.renderErrors(this.state.errors.residence)
                            : null
                    }
                </div>
                <div class="input-holder">
                    <label for="connect-email">{ this.props.t("forms:connect.email") }</label>
                    <input
                        type="email"
                        name="email"
                        value={ this.state.email }
                        onChange={(e) => this.handleEmail(e)}
                        id="connect-email"
                        ref="email"
                    />
                    {
                        (this.state.hasErrors && this.state.errors.email && this.state.errors.email.length > 0)
                            ? this.renderErrors(this.state.errors.email)
                            : null
                    }
                </div>
                <div class="input-holder">
                    <label for="connect-phone">{ this.props.t("forms:connect.phone") }</label>
                    <input
                        type="tel"
                        name="phone"
                        value={ this.state.phone }
                        onChange={(e) => this.handlePhone(e)}
                        id="connect-phone"
                        ref="phone"
                    />
                    {
                        (this.state.hasErrors && this.state.errors.phone && this.state.errors.phone.length > 0)
                            ? this.renderErrors(this.state.errors.phone)
                            : null
                    }
                </div>
                <div class="input-holder">
                    <label for="connect-link">{ this.props.t("forms:connect.personalLink") }</label>
                    <input
                        type="url"
                        name="personal_link"
                        value={ this.state.personalLink }
                        onChange={(e) => this.handlePersonalLink(e)}
                        id="connect-link"
                        ref="personalLink"
                    />
                    {
                        (this.state.hasErrors && this.state.errors.personal_link && this.state.errors.personal_link.length > 0)
                            ? this.renderErrors(this.state.errors.personal_link)
                            : null
                    }
                </div>
                <div class="input-holder">
                    <input
                        type="checkbox"
                        name="problem"
                        value={ this.state.problem }
                        onChange={(e) => this.handleProblem(e)}
                        id="connect-problem"
                        ref="problem"
                    />
                    <label for="connect-problem">
                        <span class="checkbox-holder"></span>
                        <p>{ this.props.t("forms:connect.problem") }</p>
                    </label>
                </div>
                <div class={this.state.problem ? "input-holder" : "input-holder disabled"}>
                    <label for="connect-problem-description">{ this.props.t("forms:connect.problemDescription") }</label>
                    <input
                        type="text"
                        name="problem_description"
                        value={ this.state.problemDescription }
                        onChange={(e) => this.handleProblemDescription(e)}
                        id="connect-problem-description"
                        ref="problemDescription"
                    />
                    {
                        (this.state.hasErrors && this.state.errors.problem_description && this.state.errors.problem_description.length > 0)
                            ? this.renderErrors(this.state.errors.problem_description)
                            : null
                    }
                </div>
                <div class="input-holder">
                    <input
                        type="checkbox"
                        name="activity"
                        value={ this.state.activity }
                        onChange={(e) => this.handleActivity(e)}
                        id="connect-activity"
                        ref="activity"
                    />
                    <label for="connect-activity">
                        <span class="checkbox-holder"></span>
                        <p>{ this.props.t("forms:connect.activity") }</p>
                    </label>
                </div>
                <div class={ this.state.activity ? "input-holder" : "input-holder disabled" }>
                    <label for="connect-activity-description">{ this.props.t("forms:connect.activityDescription") }</label>
                    <input
                        type="text"
                        name="activity_description"
                        value={ this.state.activityDescription }
                        onChange={(e) => this.handleActivityDescription(e)}
                        id="connect-activity-description"
                        ref="activityDescription"
                    />
                    {
                        (this.state.hasErrors && this.state.errors.activity_description && this.state.errors.activity_description.length > 0)
                            ? this.renderErrors(this.state.errors.activity_description)
                            : null
                    }
                </div>
                <button type="submit">
                    <span>{ this.props.t("forms:connect.submit") }</span>
                </button>
                { this.renderLoading() }
            </form>
        );
    }

}

export default translate(["forms"])(ConnectForm);
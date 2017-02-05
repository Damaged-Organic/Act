import React, { Component } from "react";
import { Link } from "react-router";
import { translate } from "react-i18next";

import Logo from "Pages/header/logo";

@translate(["common", "buttons"])
class NotFound extends Component{

    constructor(props){
        super(props);
        
    }
    render(){
        return(
            <div id="page" class="__not-found">
                <Logo />
                <div class="inner">
                    <span class="upper-divider"></span>
                    <h1>{ this.props.t("notFound.title") }</h1>
                    <p>{ this.props.t("notFound.text") }</p>
                    <div class="btn-back">
                        <Link to="">{ this.props.t("buttons:toHome") }</Link>
                    </div>
                </div>
                <div class="error-number-holder">
                    <span>{ this.props.t("notFound.number") }</span>
                </div>
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

}

export default NotFound;
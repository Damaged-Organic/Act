import React, { Component } from "react";
import { translate } from "react-i18next";

import ConnectForm from "./connectForm";

@translate(["headlines"])
class ConnectComponent extends Component{

    constructor(props){
        super(props);

    }
    render(){
        return(
            <section class="container connect-holder extra-padding-top">
                <div class="inner">
                    <span class="upper-divider"></span>
                    <h1>{ this.props.t("headlines:connect") }</h1>
                    <ConnectForm />
                </div>
            </section>
        );
    }

}

export default ConnectComponent;
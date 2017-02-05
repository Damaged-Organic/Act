import React, { Component } from "react";
import { Link } from "react-router";
import { translate } from "react-i18next";

import generateUrl from "Router/generateUrl";

@translate(["buttons"], {wait: true})
class ConnectButton extends Component{

    constructor(props){
        super(props);
        
    }
    render(){
        return(
            <div class="btn-connect">
                <Link to={ generateUrl("connect") }>{ this.props.t("buttons:connect") }</Link>
            </div>
        );
    }

}

export default ConnectButton;
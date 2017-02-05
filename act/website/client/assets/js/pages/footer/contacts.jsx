import React, { Component } from "react";
import { translate } from "react-i18next";

import clearPhone from "Utils/clearPhone";

@translate(["headlines"])
class Contacts extends Component{

    constructor(props){
        super(props);
        
    }
    shouldComponentUpdate(nextProps, nextState){
        if(nextProps.contacts.length > 0){
            return true;
        }
        return false;
    }
    render(){
        let contacts = this.props.contacts[0] || {};

        return(
            <div class="item">
                <span class="upper-divider"></span>
                <h3>{ this.props.t("headlines:footer.contactInfo") }</h3>
                <ul>
                    <li><a href={ "mailto:"+ contacts.email }>{ contacts.email }</a></li>
                    <li><a href={ "tel:"+ clearPhone(contacts.phone) }>{ contacts.phone }</a></li>
                </ul>
            </div>
        );
    }

}

export default Contacts;
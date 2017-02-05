import React, { Component } from "react";

import clearPhone from "Utils/clearPhone";

class Contacts extends Component{

    constructor(props){
        super(props);
        
    }
    render(){
        let contacts = this.props.contacts[0] || {};

        return(
            <div class="contacts-holder">
                <a href={ "mailto:" + contacts.email }>{ contacts.email }</a>
                <a href={ "tel:" + clearPhone(contacts.phone) }>{ contacts.phone }</a>
            </div>
        );
    }

}

export default Contacts;
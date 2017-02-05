import React, { Component } from "react";

import LinkCenters from "./linkCenters";
import LinkMenu from "./linkMenu";
import Contacts from "./contacts";
import LinkSocials from "./linkSocials";
import Disclaimer from "./disclaimer";
import Developers from "./developers";
import Copyright from "./copyright";

class Footer extends Component{

    constructor(props){
        super(props);


    }
    render(){
        let centers = this.props.centers,
            socials = this.props.socials,
            contacts = this.props.contacts,
            disclaimer = this.props.disclaimer;
        
        return(
            <div id="footer">
                <div class="inner">
                    <LinkCenters centers={ centers } />
                    <LinkMenu />
                    <Contacts contacts={ contacts } />
                    <LinkSocials socials={ socials } />
                    <Disclaimer disclaimer={ disclaimer } />
                </div>
                <footer>
                    <Developers />
                    <Copyright />
                </footer>
            </div>
        );
    }

}

export default Footer;
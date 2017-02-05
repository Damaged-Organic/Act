import React, { Component } from "react";
import { Link } from "react-router";
import { translate } from "react-i18next";

@translate(["headlines"], {wait: true})
class LinkSocials extends Component{

    constructor(props){
        super(props);
        
    }
    renderSocial(){
        let socials = this.props.socials;

        return socials.map((social) => <li key={ social.id }><Link to={ social.link } target="_blank">{ social.title }</Link></li>);
    }
    render(){
        return(
            <div class="item">
                <span class="upper-divider"></span>
                <h3>{ this.props.t("headlines:footer.socials") }</h3>
                <ul>
                    { this.renderSocial() }
                </ul>
            </div>
        );
    }

}

export default LinkSocials;
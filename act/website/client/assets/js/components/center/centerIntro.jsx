import React, { Component } from "react";
import { translate } from "react-i18next";

import clearPhone from "Utils/clearPhone";

@translate(["center"])
class CenterIntro extends Component{

    constructor(props){
        super(props);
        
    }
    shouldComponentUpdate(nextProps, nextState){
        return Object.keys(nextProps.center).length > 0 ? true : false;
    }
    render(){
        let isMobile = this.props.isMobile,
            center = this.props.center,
            city = center.city || {},
            photo = city.photo || {},
            contact = center.contact || {},
            projectCount = center.projects ? center.projects.length : 0,
            eventCount = center.events ? center.events.length : 0,
            styles = {};

        if(!isMobile){
            styles = {
                "backgroundImage": "url("+ photo.original +")",
                "backgroundRepeat": "no-repeat",
                "backgroundPosition": "50% 50%",
                "backgroundSize": "cover"
            };
        }

        return(
            <section class="container intro-holder extra-padding-top" style={ styles }>
                <span class="address-holder">{ contact.address }</span>
                <div class="contact-holder">
                    <div class="social-link">
                        <a href={ contact.social_link || "" } target="_blank">{ this.props.t("center:buttons.socialLink") }</a>
                    </div>
                    <a href={ clearPhone(contact.phone) }>{ contact.phone }</a>
                    <a href={"mailto:"+ contact.email }>{ contact.email }</a>
                </div>
                <div class="info-holder">
                    <span class="upper-divider"></span>
                    <h1>{ city.name }</h1>
                    <p>{ center.short_description }</p>
                </div>
                <span class="projects-count-holder">{ this.props.t("center:projectsInCenter", {count: projectCount}) }</span>
                <span class="events-count-holder">{ this.props.t("center:eventsInCenter", {count: eventCount}) }</span>
            </section>
        );
    }

}

export default CenterIntro;
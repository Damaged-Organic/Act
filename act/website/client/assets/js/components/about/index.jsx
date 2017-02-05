import React, { Component } from "react";

import Contacts from "./contacts";
import Intro from "./intro";
import Centers from "./centers";
import Goal from "./goal";
import Participants from "./participants";
import Partners from "./partners";

class AboutComponent extends Component{

    constructor(props){
        super(props);
        
    }
    shouldComponentUpdate(nextProps, nextState){
        let isReady = (nextProps.centers.length > 0) && (nextProps.activities.length > 0) && (nextProps.participants.length > 0);

        return isReady ? true : false;
    }
    render(){
        let isMobile = this.props.isMobile,
            contacts = this.props.contacts,
            centers = this.props.centers,
            activities = this.props.activities,
            intro = this.props.aboutContent.intro || {},
            goal = this.props.aboutContent.goal || {},
            participants = this.props.participants,
            partners = this.props.partners,
            location = this.props.location;

        return(
            <div class="container about-holder extra-padding-top">
                <Contacts contacts={ contacts } />
                <div class="inner">
                    <Intro intro={ intro } />
                    <Centers centers={ centers } isMobile={ isMobile } />
                    <Goal goal={ goal } activities={ activities } />
                    <Participants participants={ participants } />
                    <Partners partners={ partners } />
                </div>
            </div>
        );
    }

}

export default AboutComponent;
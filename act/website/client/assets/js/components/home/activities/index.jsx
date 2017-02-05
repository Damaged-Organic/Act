import React, { Component } from "react";
import { translate } from "react-i18next";

import Activity from "./activity";

@translate(["headlines"])
class Activities extends Component{

    constructor(){
        super();
    }
    shouldComponentUpdate(nextProps, nextState){
        return (nextProps.activities.length > 0) ? true : false;
    }
    renderActivity(){
        let activities = this.props.activities;

        return activities.map((activity) => <Activity key={ activity.id } activity={ activity } />);
    }
    render(){
        return(
            <section class="container home-activities-holder">
                <div class="inner">
                    <span class="upper-divider"></span>
                    <h2>{ this.props.t("headlines:home.activities") }</h2>
                    <div class="activities">
                        { this.renderActivity() }    
                    </div>
                </div>
            </section>
        );
    }

}

export default Activities;


import React, { Component } from "react";
import { translate } from "react-i18next";

import Activity from "./activity";

@translate(["headlines"])
class Goal extends Component{

    constructor(props){
        super(props);
        
    }
    shouldComponentUpdate(nextProps, nextState){
        if(nextProps.activities.length > 0 && Object.keys(nextProps.goal).length > 0){
            return true;
        }
        return false;
    }
    renderActivities(activities){
        return activities.map((activity) => <Activity key={ activity.id } activity={ activity } />)
    }
    render(){
        let goal = this.props.goal,
            activities = this.props.activities;

        return(
            <section class="container goal-holder">
                <span class="upper-divider"></span>
                <h2>{ this.props.t("headlines:about.goal") }</h2>
                <p>{ goal.text }</p>
                <div class="activities-holder">
                    <ul>
                        { this.renderActivities(activities) }
                    </ul>
                </div>
            </section>
        );
    }

}

export default Goal;
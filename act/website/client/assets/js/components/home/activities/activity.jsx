import React, { Component } from "react";

class Activity extends Component{

    constructor(props){
        super(props);
        
    }
    render(){
        let activity = this.props.activity,
            iconClassName = "icon icon-"+ activity.icon;

        return(
            <div class="item">
                <span class={ iconClassName }></span>
                <p>{ activity.title }</p>
            </div>
        );
    }

}

export default Activity;
import React, { Component } from "react";

class Activity extends Component{

    constructor(props){
        super(props);
        
    }
    render(){
        let activity = this.props.activity,
            iconClass = "icon icon-" + activity.icon; 

        return(
            <li>
                <span class={ iconClass }></span>
                <p>{ activity.title }</p>
            </li>
        );
    }

}

export default Activity;
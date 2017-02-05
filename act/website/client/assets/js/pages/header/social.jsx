import React, { Component } from "react";

class Social extends Component{

    constructor(props){
        super(props);
        
    }
    render(){
        let social = this.props.social,
            socialIconClassName = "icon icon-" + social.icon;

        return(
            <li>
                <a href={ social.link } target="_blank">
                    <span class={ socialIconClassName }></span>
                </a>
            </li>
        );
    }

}

export default Social
import React, { Component } from "react";
import { translate } from "react-i18next";

@translate(["common"])
class DisableLandscapeView extends Component{

    constructor(props){
        super(props);
        
    }
    render(){
        return(
            <div id="landscape-holder">
                <p>{ this.props.t("landscape") }</p>
            </div>
        );
    }

}

export default DisableLandscapeView;
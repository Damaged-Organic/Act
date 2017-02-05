import React, { Component } from "react";
import { translate } from "react-i18next";

@translate(["common"])
class Copyright extends Component{

    constructor(props){
        super(props);
        
    }
    render(){
        return(
            <small>{ this.props.t("copyright") } <a href="http://cheersunlimited.com.ua" target="_blank">{ this.props.t("studio") }</a></small>
        );
    }

}

export default Copyright;
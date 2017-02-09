import React, { Component } from "react";
import { translate } from "react-i18next";

import { staticPath } from "Settings";

@translate(["common"])
class Developers extends Component{

    constructor(props){
        super(props);

    }
    render(){
        return(
            <a href="http://cheersunlimited.com.ua" target="_blank">
               <figure>
                    <img src={ staticPath("/images/cheers-logo.png") } alt={ this.props.t("studio") } />
                </figure>
            </a>
        );
    }

}

export default Developers;

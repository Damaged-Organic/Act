import React, { Component } from "react";
import { Link } from "react-router";

import { staticPath } from "Settings";
import generateUrl from "Router/generateUrl";

class Logo extends Component{

    constructor(props){
        super(props);

    }
    render(){
        return(
            <Link to={ generateUrl("home") } class="logo">
                <img src={ staticPath("/images/logo.png") } alt="Act" />
            </Link>
        );
    }

}

export default Logo;

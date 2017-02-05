import React, { Component } from "react";
import { Link } from "react-router";

import generateUrl from "Router/generateUrl";

class Logo extends Component{

    constructor(props){
        super(props);

    }
    render(){
        return(
            <Link to={ generateUrl("home") } class="logo">
                <img src="static/website/build/images/logo.png" alt="Дий" />
            </Link>
        );
    }

}

export default Logo;

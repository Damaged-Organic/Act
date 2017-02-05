import React, { Component } from "react";

import Meta from "Meta/common";

import DisableLandscapeView from "Components/disableLandscapeView";

class Layout extends Component{

    constructor(props){
        super(props);
        
    }
    render(){
        return(
            <div id="layout">
                <Meta />
                { this.props.children }
                <DisableLandscapeView />
            </div>
        );
    }

}

export default Layout;
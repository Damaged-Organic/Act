import React, { Component } from "react";

import Center from "./center";

class CentersComponent extends Component{

    constructor(props){
        super(props);
    }
    renderCenter(){
        return this.props.centers.map((center) => {
            return <Center key={ center.id } center={ center } isMobile={ this.props.isMobile } />
        });
    }
    render(){
        return(
            <section class="container centers-holder extra-padding-top">
                { this.renderCenter() }
            </section>
        );
    }
}

export default CentersComponent;
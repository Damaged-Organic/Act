import React, { Component } from "react";

import Center from "./center";

class Centers extends Component{

    constructor(props){
        super(props);
        
    }
    renderCenters(){
        return this.props.centers.map((center) => <Center key={ center.id } center={ center } isMobile={ this.props.isMobile } />);
    }
    render(){
        return(
            <section class="container centers-holder">
                { this.renderCenters() }
            </section>
        );
    }

}

export default Centers;
import React, { Component } from "react";

import Center from "./center";

class Centers extends Component{

    constructor(props){
        super(props);

    }
    renderCenters(){
        let isMobile = this.props.isMobile,
            centers = this.props.centers;

        return centers.map((center) => <Center key={center.id} center={center} isMobile={ isMobile } />);
    }
    render(){
        return(
            <section class="container home-centers-holder">
                <ul>
                    { this.renderCenters() }
                </ul>
            </section>
        );
    }

}

export default Centers;
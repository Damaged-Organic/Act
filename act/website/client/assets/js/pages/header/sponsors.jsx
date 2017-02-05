import React, { Component } from "react";

import Sponsor from "./sponsor";

class Sponsors extends Component{

    constructor(props){
        super(props);
        
    }
    renderSponsor(){
        return this.props.sponsors.map((sponsor) => <Sponsor key={ sponsor.id } sponsor={ sponsor } />);
    }
    render(){
        
        return(
            <ul class="sponsors">
                { this.renderSponsor() }
            </ul>
        );
    }

}

export default Sponsors;
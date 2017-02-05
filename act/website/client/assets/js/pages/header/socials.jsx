import React, { Component } from "react";

import Social from "./social";

class Socials extends Component{

    constructor(props){
        super(props);
    }
    renderSocials(){
        return this.props.socials.map((social) => <Social key={ social.id } social={ social } />);
    }
    render(){
        return(
            <ul class="socials">
                { this.renderSocials() }
            </ul>
        );
    }

}

export default Socials;
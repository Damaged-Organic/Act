import React, { Component } from "react";

class Sponsor extends Component{

    constructor(props){
        super(props);
        
    }
    render(){
        let sponsor = this.props.sponsor;
        
        return(
            <li key={ sponsor.id }>
                <a href={ sponsor.link } target="_blank">
                    <img src={ sponsor.logo } alt={ sponsor.title } />
                </a>
            </li>
        );
    }

}

export default Sponsor;
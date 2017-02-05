import React, { Component } from "react";

class Disclaimer extends Component{

    constructor(props){
        super(props);
        
    }
    render(){
        let disclaimer = this.props.disclaimer;

        return(
            <div class="disclaimer-holder">
                <p>{ disclaimer.text_uk }</p>
                <p>{ disclaimer.text_en }</p>
            </div>
        );
    }

}

export default Disclaimer;
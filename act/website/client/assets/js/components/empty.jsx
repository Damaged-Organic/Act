import React, { Component } from "react";

class Empty extends Component{

    constructor(props){
        super(props);
        
    }
    render(){
        return(
            <div class="empty-holder">
                <p>{ this.props.message }</p>
            </div>
        );
    }

}

export default Empty;
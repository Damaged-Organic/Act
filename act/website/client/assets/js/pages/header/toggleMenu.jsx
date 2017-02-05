import React, { Component } from "react";

class ToggleMenu extends Component{

    constructor(props){
        super(props);
        
    }
    render(){
        let onToggle = this.props.onToggle;

        return(
            <div class="toggle-menu" onTouchStart={ (e) => onToggle(e) }>
                <span class="line"></span>
                <span class="line"></span>
                <span class="line"></span>
            </div>
        );
    }

}

export default ToggleMenu;
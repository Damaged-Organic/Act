import React, { Component } from "react";
import { Link } from "react-router";

import generateUrl from "Router/generateUrl";

class BackButton extends Component{

    constructor(props){
        super(props);
        
    }
    render(){
        let center = this.props.center || {},
            city = center.city || {},
            photoObj = city.photo || {},
            url = generateUrl("center", {id: center.id});

        return(
            <div class="back-holder">
                <Link to={ url }>
                    <span class="icon icon-arrow-left"></span>
                    <figure data-title={ city.name }>
                        <img src={ photoObj.square } alt={ city.name } />
                    </figure>
                </Link>
            </div>
        );
    }

}

export default BackButton;
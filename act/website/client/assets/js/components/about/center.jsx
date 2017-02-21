import React, { Component } from "react";
import { Link } from "react-router";

import generateUrl from "Router/generateUrl";

class Center extends Component{

    constructor(props){
        super(props);
        
    }
    render(){
        let isMobile = this.props.isMobile,
            center = this.props.center,
            city = center.city || {},
            photoSquare = city.photo_square || {},
            url = generateUrl("center", {id: center.id});

        return(
            <div class="center-holder">
                <Link to={ url }>
                    <figure>
                        {
                            isMobile
                                ? <img src={ photoSquare.square } alt={ city.name } />
                                : <img src={ photoSquare.original } alt={ city.name } />
                        }
                    </figure>
                    <h3>{ city.name }</h3>
                </Link>
            </div>
        );
    }

}

export default Center;
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
            photoObj = city.photo || {},
            url = generateUrl("center", {id: center.id});

        return(
            <div class="center-holder">
                <Link to={ url }>
                    <figure>
                        {
                            isMobile
                                ? <img src={ photoObj.square } alt={ city.name } />
                                : <img src={ photoObj.original } alt={ city.name } />
                        }
                    </figure>
                    <h3>{ city.name }</h3>
                </Link>
            </div>
        );
    }

}

export default Center;
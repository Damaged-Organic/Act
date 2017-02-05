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
            <li>
                <Link to={ url }>
                    <figure>
                        {  
                            !isMobile
                                ? <img src={ photoObj.square } alt={ city.name } />
                                : <img src={ photoObj.original } alt={ city.name } />
                        }
                    </figure>
                    <div class="inner">
                        <span class="upper-divider"></span>
                        <h2>{ city.name }</h2>
                    </div>
                </Link>
            </li>
        );
    }

}

export default Center;
import React, { Component } from "react";
import { Link } from "react-router";

import generateUrl from "Router/generateUrl";

class SubPage extends Component{

    constructor(props){
        super(props);
        
    }
    render(){
        let subPage = this.props.subPage,
            centerId = this.props.centerId,
            url = generateUrl("centerSubPage", {centerId: centerId, subPageId: subPage.id});

        return(
            <li>
                <Link to={ url }>{ subPage.headline }</Link>
            </li>
        );
    }

}

export default SubPage;
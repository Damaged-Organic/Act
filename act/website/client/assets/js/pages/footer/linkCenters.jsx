import React, { Component } from "react";
import { Link } from "react-router";
import { translate } from "react-i18next";

import generateUrl from "Router/generateUrl";

@translate(["headlines"], {wait: true})
class LinkCenters extends Component{

    constructor(props){
        super(props);
        
    }
    renderCity(){
        let centers = this.props.centers;

        return centers.map((center) => {
            let city = center.city;

            return <li key={ center.id }><Link to={ generateUrl("center", {id: center.id}) }>{ city.name }</Link></li>;
        });
    }
    render(){
        return(
            <div class="item">
                <span class="upper-divider"></span>
                <h3>{ this.props.t("headlines:footer.centers") }</h3>
                <ul>
                    { this.renderCity() }
                </ul>
            </div>
        );
    }

}

export default LinkCenters;
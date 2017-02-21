import React, { Component } from "react";
import { Link } from "react-router";
import { translate } from "react-i18next";

import generateUrl from "Router/generateUrl";

@translate(["buttons"], {wait: true})
class Center extends Component{

    constructor(props){
        super(props);
    }
    render(){
        let isMobile = this.props.isMobile,
            center = this.props.center,
            city = center.city || {},
            photoHigh = city.photo_high || {},
            photo = !isMobile ? photoHigh.high : photoHigh.original,
            styles = {};

        styles = {
            "backgroundImage": "url("+ photo +")",
            "backgroundRepeat": "no-repeat",
            "backgroundPosition": "50% 50%",
            "backgroundSize": "cover"
        }

        return(
            <div class="item">
                <Link to={ generateUrl("center", {id: center.id}) } style={ styles }>
                    <div class="inner">
                        <span class="upper-divider"></span>
                        <h2>{ city.name }</h2>
                        <span class="detail">{ this.props.t("buttons:detail") }</span>
                    </div>
                </Link>
            </div>
        );
    }
}

export default Center;
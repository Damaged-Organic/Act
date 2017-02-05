import React, { Component } from "react";
import { Link } from "react-router";
import { translate } from "react-i18next";

import generateUrl from "Router/generateUrl";

@translate(["menu", "headlines"], {wait: true})
class LinkMenu extends Component{

    constructor(props){
        super(props);
        
    }
    render(){
        return(
            <div class="item">
                <span class="upper-divider"></span>
                <h3>{ this.props.t("headlines:footer.navigation") }</h3>
                <ul>
                    <li><Link to={ generateUrl("about") }>{ this.props.t("menu:about") }</Link></li>
                    <li><Link to={ generateUrl("centers") }>{ this.props.t("menu:centers") }</Link></li>
                    <li><Link to={ generateUrl("projects") }>{ this.props.t("menu:projects") }</Link></li>
                    <li><Link to={ generateUrl("events") }>{ this.props.t("menu:events") }</Link></li>
                </ul>
            </div>
        );
    }

}

export default LinkMenu;
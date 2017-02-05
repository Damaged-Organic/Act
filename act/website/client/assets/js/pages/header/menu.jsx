import React, { Component } from "react";
import { Link } from "react-router";
import { translate } from "react-i18next";

import generateUrl from "Router/generateUrl";

@translate(["menu"], {wait: true})
class Menu extends Component{

    constructor(props){
        super(props);

    }
    render(){
        let isActive = this.props.isActive,
            location = this.props.location,
            ActiveClassNames = {};

        ActiveClassNames.home = /^\/$/gi.test(location.pathname) ? "active" : "";
        ActiveClassNames.about = /about/gi.test(location.pathname) ? "active" : "";
        ActiveClassNames.centers = /centers|center/gi.test(location.pathname) ? "active" : "";
        ActiveClassNames.projects = /projects|project/gi.test(location.pathname) ? "active" : "";
        ActiveClassNames.events = /events|event/gi.test(location.pathname) ? "active" : "";

        return(
            <nav id="menu" class={ isActive ? "active" : "" }>
                <ul>
                    <li class={ ActiveClassNames.about }>
                        <Link to={ generateUrl("about") }>
                            <span>{ this.props.t("menu:about") }</span>
                        </Link>
                    </li>
                    <li class={ ActiveClassNames.centers }>
                        <Link to={ generateUrl("centers") }>
                            <span>{ this.props.t("menu:centers") }</span>
                        </Link>
                    </li>
                    <li class={ ActiveClassNames.projects }>
                        <Link to={ generateUrl("projects") }>
                            <span>{ this.props.t("menu:projects") }</span>
                        </Link>
                    </li>
                    <li class={ ActiveClassNames.events }>
                        <Link to={ generateUrl("events") }>
                            <span>{ this.props.t("menu:events") }</span>
                        </Link>
                    </li>
                </ul>
            </nav>
        );
    }

}

export default Menu;
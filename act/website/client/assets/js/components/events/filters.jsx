import React, { Component } from "react";
import { Link } from "react-router";
import { translate } from "react-i18next";

import generateUrl from "Router/generateUrl";

@translate(["filters"])
class Filters extends Component{

    constructor(props){
        super(props);
    }
    shouldComponentUpdate(nextProps, nextState){
        if(nextProps.centers.length > 0){
            return true;
        }
        return false;
    }
    renderItem(centers, query, url){
        return centers.map((center) => {

            let activeClassName = (query.centres == center.id) ? "active" : "",
                params = {};

            params = {
                centres: center.id,
                event_category: query.event_category
            }

            return(
                <li key={ center.id } class={ activeClassName }>
                    <Link to={{ pathname: url, query: params }}>{ center.city.name }</Link>
                </li>
            );
        });
    }
    render(){
        let centers = this.props.centers,
            query = this.props.location.query,
            url = generateUrl("events"),
            activeClassName = !query.centres ? "active" : "";

        return(
            <div class="filters-holder">
                <ul>
                    <li class={ activeClassName }>
                        <Link to={{ pathname: url, query: { event_category: query.event_category } }}>
                            { this.props.t("filters:allProjects") }
                        </Link>
                    </li>
                    { this.renderItem(centers, query, url) }
                </ul>
            </div>
        );
    }

}

export default Filters;
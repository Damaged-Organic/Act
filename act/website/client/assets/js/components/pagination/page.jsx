import React, { Component } from "react";
import { Link } from "react-router";
import autoBind from "autobind-decorator";

import generateUrl from "Router/generateUrl";

@autoBind
class Page extends Component{

    constructor(props){
        super(props);
        
    }
    getActiveClassName(num){
        let pageNum = this.props.location.query.page || 1;

        return (pageNum == num) ? "active" : "";
    }
    handlePageClick(e){
        window.scrollTo(0, 0);
    }
    render(){
        let number = this.props.number,
            url = this.props.url,
            query = this.props.location.query,
            activeClassName = this.getActiveClassName(number),
            queryParams = {};

        if(url === "projects"){

            queryParams = {
                project_area: query.project_area,
                centres: query.centres,
                page: number
            }

        } else{

            queryParams = {
                event_category: query.event_category,
                centres: query.centres,
                page: number
            }

        }

        return(
            <li class={ activeClassName } onClick={ this.handlePageClick }>
                <Link to={{ pathname: url, query: queryParams }}>{ number }</Link>
            </li>
        );
    }

}
export default Page;
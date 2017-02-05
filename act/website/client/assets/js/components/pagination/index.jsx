import React, { Component } from "react";

import Page from "./page";

class Pagination extends Component{

    constructor(props){
        super(props);
        
    }
    getPageCount(quantity, splitBy){
        return (quantity > 0) ? Math.ceil(quantity / splitBy) : 0;
    }
    renderPages(pageCount){
        let pages = [];

        for(let i = 1; i <= pageCount; i++){
            pages[i] = <Page key={ i } number={ i } url={ this.props.url } location={ this.props.location } />;
        }

        return pages;
    }
    render(){
        let quantity = this.props.quantity || 0,
            splitBy = this.props.splitBy,
            pageCount = this.getPageCount(quantity, splitBy);

        return(
            <div class="pagination-holder">
                <ul>
                    { this.renderPages(pageCount) }
                </ul>
            </div>
        );
    }

}
export default Pagination;
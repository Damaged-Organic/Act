import React, { Component } from "react";

import SubPage from "./subPage";

class CenterSubPages extends Component{

    constructor(props){
        super(props);
        
    }
    renderSubPages(){
        let subPages = this.props.subPages,
            centerId = this.props.centerId;

        return subPages.map((subPage) => <SubPage key={ subPage.id } subPage={ subPage } centerId={ centerId } />);
    }
    render(){
        return(
            <div class="container sub-pages-holder">
                <div class="inner">
                    <ul>{ this.renderSubPages() }</ul>
                </div>
            </div>
        );
    }

}

export default CenterSubPages;
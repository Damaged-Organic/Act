import React, { Component } from "react";

import BackButton from "./backButton";

class SubPageComponent extends Component{

    constructor(props){
        super(props);
        
    }
    render(){
        let subPage = this.props.subPage;

        return(
            <section class="container sub-page-holder extra-padding-top">
                <div class="inner">
                    <BackButton center={ subPage.centre } />
                    <span class="upper-divider"></span>
                    <h1>{ subPage.headline }</h1>
                    <div class="content-holder" dangerouslySetInnerHTML={{__html: subPage.content }}></div>
                </div>
            </section>
        );
    }

}

export default SubPageComponent;
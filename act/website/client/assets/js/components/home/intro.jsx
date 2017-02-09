import React, { Component } from "react";
import { Link } from "react-router";
import { translate } from "react-i18next";

import { staticPath } from "Settings";
import generateUrl from "Router/generateUrl";

@translate(["buttons"], {wait: true})
class Intro extends React.Component{

    constructor(props){
        super(props);

    }
    shouldComponentUpdate(nextProps, nextState){
        if(Object.keys(nextProps.intro).length > 0){
            return true;
        }
        return false;
    }
    render(){
        let intro = this.props.intro;

        return(
            <section class="container home-intro-holder extra-padding-top">
                <div class="photo-holder">
                    <figure>
                        <img src={ staticPath("/images/intro-background.jpg") } alt={ intro.headline } />
                    </figure>
                </div>
                <div class="inner entitled-holder">
                    <span class="upper-divider"></span>
                    <h1>{ intro.headline }</h1>
                    <div class="buttons-holder">
                        <div class="btn-detailed bordered">
                            <Link to={ generateUrl("about") }>{ this.props.t("buttons:detail") }</Link>
                        </div>
                        <div class="btn-connect red">
                            <Link to={ generateUrl("connect") }>{ this.props.t("buttons:connect") }</Link>
                        </div>
                    </div>
                </div>
            </section>
        );
    }

}

export default Intro;

import React, { Component } from "react";
import { translate } from "react-i18next";

@translate(["headlines"])
class Intro extends Component{

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
            <section class="container intro-holder">
                <span class="upper-divider"></span>
                <h1>{ this.props.t("headlines:about.intro") }</h1>
                <p>{ intro.text }</p>
            </section>
        );
    }

}

export default Intro;
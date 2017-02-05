import React, { Component } from "react";
import { translate } from "react-i18next";

@translate(["headlines"])
class Partners extends Component{

    constructor(props){
        super(props);
        
    }
    shouldComponentUpdate(nextProps, nextState){
        return (nextProps.partners.length > 0) ? true : false;
    }
    renderPartner(){
        return this.props.partners.map((partner) => {
            return(
                <li key={ partner.id }>
                    <a href={ partner.link } target="_blank">
                        <figure>
                            <img src={ partner.logo.original } alt={ partner.name } />
                        </figure>
                    </a>
                </li>
            );
        });
    }
    render(){
        if(this.props.partners.length <= 0) return null;

        return(
            <section class="container partners-holder">
                <span class="upper-divider"></span>
                <h2>{ this.props.t("headlines:about.partners") }</h2>
                <ul>{ this.renderPartner() }</ul>
            </section>
        );
    }

}

export default Partners;
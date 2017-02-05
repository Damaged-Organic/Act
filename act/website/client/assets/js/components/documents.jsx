import React, { Component } from "react";
import { translate } from "react-i18next";

@translate(["buttons"])
class Documents extends Component{

    constructor(props){
        super(props);
    }
    shouldComponentUpdate(nextProps, nextState){
        if(nextProps.documents.length){
            return true;
        }
        return false;
    }
    renderDocument(){
        let documents = this.props.documents || [];

        return documents.map((doc) => {
            return(
                <div class="document" key={ doc.id }>
                    <span class="icon icon-document"></span>
                    <p>{ doc.description }</p>
                    <a href={ doc.document } target="_blank">{ this.props.t("buttons:download") }</a>
                </div>
            );
        });
    }
    render(){
        return(
            <div class="document-holder">
                { this.renderDocument() }
            </div>
        );
    }

}

export default Documents;
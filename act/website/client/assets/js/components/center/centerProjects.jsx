import React, { Component } from "react";
import { translate } from "react-i18next";
import { Link } from "react-router";

import generateUrl from "Router/generateUrl";

import ProjectItem from "Components/projectItem";

@translate(["center"], {wait: true})
class CenterProjects extends Component{

    constructor(props){
        super(props);
        
    }
    shouldComponentUpdate(nextProps, nextState){
        return nextProps.projects.length > 0 ? true : false;
    }
    renderProjects(projects){
        return projects.map((project) => <ProjectItem key={ project.id } project={ project } />);
    }
    render(){
        let projects = this.props.projects.slice(0, 3),
            centerId = this.props.centerId,
            url = generateUrl("projects"),
            query = { centres: centerId };

        if(projects.length <= 0) return null;

        return(
            <section class="container projects-holder">
                <div class="inner">
                    <span class="upper-divider"></span>
                    <h2>{ this.props.t("center:headlines.projects") }</h2>
                    { this.renderProjects(projects) }
                    <div class="btn">
                        <Link to={{ pathname: url, query: query  }}>{ this.props.t("center:buttons.allProjects") }</Link>
                    </div>
                </div>
            </section>
        );
    }

}

export default CenterProjects;
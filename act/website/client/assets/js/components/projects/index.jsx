import React, { Component } from "react";
import { translate } from "react-i18next";

import Filters from "./filters";
import Categories from "./categories";

import ProjectItem from "Components/projectItem";
import Pagination from "Components/pagination/";
import Empty from "Components/empty";

@translate(["common"], {wait: true})
class ProjectsComponent extends Component{

    constructor(props){
        super(props);
        
    }
    shouldComponentUpdate(nextProps, nextState){
        if(nextProps.centers.length > 0 || nextProps.categories.length > 0 || nextProps.projects.count > 0){
            return true;
        }
        return false;
    }
    renderProject(projects){
        let items = projects.results || [];

        return items.map((item) => <ProjectItem key={ item.id } project={ item } />);
    }
    render(){
        let isMobile = this.props.isMobile,
            centers = this.props.centers,
            categories = this.props.categories,
            projects = this.props.projects,
            location = this.props.location;

        return(
            <div class="inner">
                <Filters centers={ centers } location={ location } isMobile={ isMobile } />
                <Categories categories={ categories } location={ location } />
                <section class="projects">
                    {projects.count > 0 ? this.renderProject(projects) : <Empty message={ this.props.t("empty") } />}
                </section>
                <Pagination quantity={ projects.count } splitBy={ 5 } url="projects" location={ location } />
            </div>
        );
    }

}

export default ProjectsComponent;
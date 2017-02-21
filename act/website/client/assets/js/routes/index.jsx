import React, { Component } from "react";
import { Router, Route, IndexRoute, browserHistory } from "react-router";

import RouterUrls from "./routerUrls";

import Layout from "Pages/layout";

import Home from "Pages/home";
import About from "Pages/about";
import Centers from "Pages/centers";
import Center from "Pages/center";
import SubPage from "Pages/subPage";
import Projects from "Pages/projects";
import Project from "Pages/project";
import Events from "Pages/events";
import Event from "Pages/event";
import Connect from "Pages/connect";
import Subscribe from "Pages/subscribe";
import Unsubscribe from "Pages/unsubscribe";

import NotFound from "Pages/notFound";

class Routes extends Component{

    constructor(){
        super();
    }
    render(){
        return(
            <Router onUpdate={() => window.scrollTo(0, 0)} history={ browserHistory }>
                <Route path={ RouterUrls.home } component={ Layout }>
                    <IndexRoute component={ Home } />
                    <Route path={ RouterUrls.about } component={ About } />
                    <Route path={ RouterUrls.centers } component={ Centers } />
                    <Route path={ RouterUrls.center } component={ Center } />
                    <Route path={ RouterUrls.centerSubPage } component={ SubPage } />
                    <Route path={ RouterUrls.projects } component={ Projects } />
                    <Route path={ RouterUrls.project } component={ Project } />
                    <Route path={ RouterUrls.events } component={ Events } />
                    <Route path={ RouterUrls.event } component={ Event } />
                    <Route path={ RouterUrls.connect } component={ Connect } />
                    <Route path={ RouterUrls.subscribe } component={ Subscribe } />
                    <Route path={ RouterUrls.unsubscribe } component={ Unsubscribe } />
                    <Route path="*" component={ NotFound } />
                </Route>
            </Router>
        );
    }

}

export default Routes;
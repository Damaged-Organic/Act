import React, { Component } from "react";
import autoBind from "autobind-decorator";

import PageMeta from "Meta/";

import * as scrapingsActions from "Actions/scrapingsActions";

import * as centerActions from "Actions/centerActions";
import CenterStore from "Stores/centerStore";

import Header from "Pages/header/";
import Footer from "Pages/footer/";

import CenterSubPages from "Components/center/centerSubPages";
import CenterIntro from "Components/center/centerIntro";
import CenterProjects from "Components/center/centerProjects";
import CenterEvents from "Components/center/centerEvents";
import CenterParticipants from "Components/center/centerParticipants";

import Loader from "Components/loader";

import isMobile from "Utils/isMobile";

@autoBind
class Center extends Component{

    constructor(props){
        super(props);

        this.state = {
            isLoading: true,
            isMobile: isMobile(),
            metadata: CenterStore.getMetaData(),
            sponsors: CenterStore.getSponsors(),
            socials: CenterStore.getSocials(),
            center: CenterStore.getCenter(),
            cities: CenterStore.getCities(),
            disclaimer: CenterStore.getDisclaimer(),
            contacts: CenterStore.getContacts()
        }
    }
    componentWillMount(){
        CenterStore.on("change", this.handleStoreChange);
    }
    componentDidMount(){
        let centerId = parseInt(this.props.routeParams.id);

        if(centerId) centerActions.loadData(centerId);
    }
    componentDidUpdate(prevProps, prevStates){
        if(this.state.isLoading) return;

        let path = this.props.location.pathname,
            head = document.querySelector("head").innerHTML;

        scrapingsActions.scrap(path, head);
    }
    shouldComponentUpdate(nextProps, nextState){
        return !nextState.isLoading ? true : false;
    }
    componentWillUnmount(){
        CenterStore.removeListener("change", this.handleStoreChange);
    }
    handleStoreChange(){
        if(CenterStore.isLoading()) return;

        this.setState({
            isLoading: CenterStore.isLoading(),
            metadata: CenterStore.getMetaData(),
            sponsors: CenterStore.getSponsors(),
            socials: CenterStore.getSocials(),
            center: CenterStore.getCenter(),
            cities: CenterStore.getCities(),
            disclaimer: CenterStore.getDisclaimer(),
            contacts: CenterStore.getContacts()
        });
    }
    render(){
        let isLoading = this.state.isLoading,
            isMobile = this.state.isMobile,
            metadata = this.state.metadata,
            sponsors = this.state.sponsors,
            socials = this.state.socials,
            center = this.state.center,
            subPages = center.centres_subpages || [],
            centerProjects = center.projects || [],
            topEvent = center.top_event || {},
            centerEvents = center.events || [],
            centerParticipants = center.participants || [],
            cities = this.state.cities,
            disclaimer = this.state.disclaimer,
            contacts = this.state.contacts;

        return(
            <div id="page" class="__center">
                <PageMeta metadata={ metadata } />
                <Header sponsors={ sponsors } socials={ socials } location={ this.props.location } isMobile={ isMobile } />
                <main id="content">
                    <CenterIntro center={ center } isMobile={ isMobile } />
                    <CenterSubPages subPages={ subPages } centerId={ center.id } />
                    <CenterEvents events={ centerEvents } topEvent={ topEvent } centerId={ center.id } />
                    <CenterProjects projects={ centerProjects } centerId={ center.id } />
                    <CenterParticipants participants={ centerParticipants } />
                    <Footer
                        centers={ cities }
                        socials={ socials }
                        contacts={ contacts }
                        disclaimer={ disclaimer }
                    />
                </main>
                <Loader isLoading={ isLoading }/>
            </div>
        );
    }

}

export default Center;

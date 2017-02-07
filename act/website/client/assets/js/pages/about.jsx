import React, { Component } from "react";
import autoBind from "autobind-decorator";

import PageMeta from "Meta/";

import * as scrapingsActions from "Actions/scrapingsActions";

import * as aboutActions from "Actions/aboutActions";
import AboutStore from "Stores/aboutStore";

import Header from "Pages/header/";
import Footer from "Pages/footer/";

import AboutComponent from "Components/about/";
import Loader from "Components/loader";

import isMobile from "Utils/isMobile";

@autoBind
class About extends Component{

    constructor(props){
        super(props);

        this.state = {
            isLoading: true,
            isMobile: isMobile(),
            metadata: AboutStore.getMetaData(),
            sponsors: AboutStore.getSponsors(),
            socials: AboutStore.getSocials(),
            activities: AboutStore.getActivities(),
            aboutContent: AboutStore.getAboutContent(),
            centers: AboutStore.getCenters(),
            contacts: AboutStore.getContacts(),
            participants: AboutStore.getParticipants(),
            partners: AboutStore.getPartners(),
            disclaimer: AboutStore.getDisclaimer()
        }
    }
    componentWillMount(){
        AboutStore.on("change", this.handleStoreChange);
    }
    componentDidMount(){
        aboutActions.loadData();
    }
    shouldComponentUpdate(nextProps, nextState){
        return !nextState.isLoading ? true : false;
    }
    componentDidUpdate(prevProps, prevStates){
        if(this.state.isLoading) return;

        let path = this.props.location.pathname,
            head = document.querySelector("head").innerHTML;

        scrapingsActions.scrap(path, head);
    }
    componentWillUnmount(){
        AboutStore.removeListener("change", this.handleStoreChange);
    }
    handleStoreChange(){
        if(AboutStore.isLoading()) return;

        this.setState({
            isLoading: AboutStore.isLoading(),
            metadata: AboutStore.getMetaData(),
            sponsors: AboutStore.getSponsors(),
            socials: AboutStore.getSocials(),
            activities: AboutStore.getActivities(),
            aboutContent: AboutStore.getAboutContent(),
            centers: AboutStore.getCenters(),
            contacts: AboutStore.getContacts(),
            participants: AboutStore.getParticipants(),
            partners: AboutStore.getPartners(),
            disclaimer: AboutStore.getDisclaimer()
        });
    }
    render(){
        let isLoading = this.state.isLoading,
            isMobile = this.state.isMobile,
            metadata = this.state.metadata,
            sponsors = this.state.sponsors,
            socials = this.state.socials,
            activities = this.state.activities,
            aboutContent = this.state.aboutContent,
            centers = this.state.centers,
            contacts = this.state.contacts,
            participants = this.state.participants,
            partners = this.state.partners,
            disclaimer = this.state.disclaimer;

        return(
            <div id="page" class="__about">
                <PageMeta metadata={ metadata } />
                <Header sponsors={ sponsors } socials={ socials } location={ this.props.location } isMobile={ isMobile } />
                <main id="content">
                    <AboutComponent
                        contacts={ contacts }
                        centers={ centers }
                        activities={ activities }
                        aboutContent={ aboutContent }
                        participants={ participants }
                        partners={ partners }
                        location={ this.props.location }
                        isMobile={ isMobile }
                    />
                    <Footer
                        centers={ centers }
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

export default About;

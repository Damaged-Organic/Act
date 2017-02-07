import React, { Component } from "react";
import autoBind from "autobind-decorator";

import PageMeta from "Meta/";

import * as scrapingsActions from "Actions/scrapingsActions";

import * as connectActions from "Actions/connectActions";
import ConnectStore from "Stores/connectStore";

import Header from "Pages/header/";
import Footer from "Pages/footer";

import ConnectComponent from "Components/connect/";
import Loader from "Components/loader";

import isMobile from "Utils/isMobile";

@autoBind
class Connect extends Component{

    constructor(props){
        super(props);

        this.state = {
            isLoading: true,
            isMobile: isMobile(),
            metadata: ConnectStore.getMetaData(),
            sponsors: ConnectStore.getSponsors(),
            socials: ConnectStore.getSocials(),
            centers: ConnectStore.getCenters(),
            contacts: ConnectStore.getContacts(),
            disclaimer: ConnectStore.getDisclaimer()
        }
    }
    componentWillMount(){
        ConnectStore.on("change", this.handleStoreChange);
    }
    componentDidMount(){
        connectActions.loadData();
    }
    componentDidUpdate(prevProps, prevStates){
        if(this.state.isLoading) return;

        let path = this.props.location.pathname,
            head = document.querySelector("head").innerHTML;

        scrapingsActions.scrap(path, head);
    }
    shouldComponentUpdate(nextProps, nextState){
        if(!nextState.loading){
            return true;
        }
        return false;
    }
    componentWillUnmount(){
        ConnectStore.removeListener("change", this.handleStoreChange);
    }
    handleStoreChange(){
        this.setState({
            isLoading: ConnectStore.isLoading(),
            metadata: ConnectStore.getMetaData(),
            sponsors: ConnectStore.getSponsors(),
            socials: ConnectStore.getSocials(),
            centers: ConnectStore.getCenters(),
            contacts: ConnectStore.getContacts(),
            disclaimer: ConnectStore.getDisclaimer()
        });
    }
    render(){
        let isLoading = this.state.isLoading,
            isMobile = this.state.isMobile,
            metadata = this.state.metadata,
            sponsors = this.state.sponsors,
            socials = this.state.socials,
            centers = this.state.centers,
            contacts = this.state.contacts,
            disclaimer = this.state.disclaimer;

        return(
            <div id="page" class="__connect">
                <PageMeta metadata={ metadata } />
                <Header sponsors={ sponsors } socials={ socials } location={ this.props.location } isMobile={ isMobile } />
                <main id="content">
                    <ConnectComponent />
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

export default Connect;

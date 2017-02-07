import React, { Component } from "react";
import autoBind from "autobind-decorator";

import PageMeta from "Meta/";

import * as scrapingsActions from "Actions/scrapingsActions";

import * as subPageActions from "Actions/subPageActions";
import SubPageStore from "Stores/subPageStore";

import Header from "Pages/header/";
import Footer from "Pages/footer/";

import SubPageComponent from "Components/subPage/";

import Loader from "Components/loader";

import isMobile from "Utils/isMobile";

@autoBind
class SubPage extends Component{

    constructor(props){
        super(props);

        this.state = {
            isLoading: true,
            isMobile: isMobile(),
            metadata: SubPageStore.getMetaData(),
            sponsors: SubPageStore.getSponsors(),
            socials: SubPageStore.getSocials(),
            subPage: SubPageStore.getSubPage(),
            centers: SubPageStore.getCenters(),
            contacts: SubPageStore.getContacts(),
            disclaimer: SubPageStore.getDisclaimer()
        }
    }
    componentWillMount(){
        SubPageStore.on("change", this.handleStoreChange);
    }
    componentDidMount(){
        subPageActions.loadData(this.props.params.subPageId);
    }
    componentDidUpdate(prevProps, prevStates){
        if(this.state.isLoading) return;

        let path = this.props.location.pathname,
            head = document.querySelector("head").innerHTML;

        scrapingsActions.scrap(path, head);
    }
    componentWillUnmount(){
        SubPageStore.removeListener("change", this.handleStoreChange);
    }
    handleStoreChange(){
        this.setState({
            isLoading: SubPageStore.isLoading(),
            metadata: SubPageStore.getMetaData(),
            sponsors: SubPageStore.getSponsors(),
            socials: SubPageStore.getSocials(),
            subPage: SubPageStore.getSubPage(),
            centers: SubPageStore.getCenters(),
            contacts: SubPageStore.getContacts(),
            disclaimer: SubPageStore.getDisclaimer()
        });
    }
    render(){
        let isLoading = this.state.isLoading,
            isMobile = this.state.isMobile,
            metadata = this.state.metadata,
            sponsors = this.state.sponsors,
            socials = this.state.socials,
            subPage = this.state.subPage,
            centers = this.state.centers,
            contacts = this.state.contacts,
            disclaimer = this.state.disclaimer;

        return(
            <div id="page" class="__sub-page">
                <PageMeta metadata={ metadata } />
                <Header sponsors={ sponsors } socials={ socials } location={ this.props.location } isMobile={ isMobile } />
                <main id="content">
                    <SubPageComponent subPage={ subPage } />
                    <Footer
                        centers={ centers }
                        socials={ socials }
                        contacts={ contacts }
                        disclaimer={ disclaimer }
                    />
                </main>
                <Loader isLoading={ isLoading } />
            </div>
        );
    }

}

export default SubPage;

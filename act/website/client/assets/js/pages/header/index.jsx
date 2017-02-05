import React, { Component } from "react";

import Sponsors from "./sponsors";
import Socials from "./socials";
import Logo from "./logo";
import ConnectButton from "./connectButton";
import Menu from "./menu";
import ToggleMenu from "./toggleMenu";

class Header extends Component{

    constructor(props){
        super(props);

        this.state = {
            isActive: false
        }
    }
    onToggle(e){
        this.setState({ isActive: !this.state.isActive });
    }
    renderMobileHeader(){
        let isActive = this.state.isActive,
            socials = this.props.socials;

        return(
            <header id="header" class={ isActive ? "active" : "" }>
                <Logo />
                <ToggleMenu onToggle={ this.onToggle.bind(this) } />
                <Menu location={ location } />
                <Socials socials={ socials } />
                <ConnectButton />
            </header>
        );
    }
    renderHeader(){
        let sponsors = this.props.sponsors,
            socials = this.props.socials,
            location = this.props.location;

        return(
            <header id="header">
                <div class="social-links-holder">
                    <Sponsors sponsors={ sponsors } />
                    <Socials socials={ socials } />
                </div>
                <div class="head-holder">
                    <Logo />
                    <ConnectButton />
                    <Menu location={ location } />
                </div>
            </header>
        );
    }
    render(){
        let isMobile = this.props.isMobile;

        return isMobile ? this.renderMobileHeader() : this.renderHeader();
    }

}

export default Header;
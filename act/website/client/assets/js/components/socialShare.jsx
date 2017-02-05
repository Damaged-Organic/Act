import React, { Component } from "react";
import { ShareButtons } from "react-share";

const FacebookShare = ShareButtons.FacebookShareButton;
const TwitterShare = ShareButtons.TwitterShareButton;
const VKShare = ShareButtons.VKShareButton;

class SocialShare extends Component{

    constructor(props){
        super(props);
        
    }
    render(){
        let location = this.props.location;

        return(
            <ul class="socials-holder">
                <li>
                    <FacebookShare url={ location.pathname }>
                        <span class="icon icon-facebook"></span>
                    </FacebookShare>
                </li>
                <li>
                    <VKShare url={ location.pathname }>
                        <span class="icon icon-vk"></span>
                    </VKShare>
                </li>
                <li>
                    <TwitterShare url={ location.pathname }>
                        <span class="icon icon-twitter"></span>
                    </TwitterShare>
                </li>
            </ul>
        );
    }

}

export default SocialShare;
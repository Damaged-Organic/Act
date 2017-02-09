import React, { Component } from "react";
import { ShareButtons } from "react-share";

const FacebookShare = ShareButtons.FacebookShareButton;
const TwitterShare = ShareButtons.TwitterShareButton;
const VKShare = ShareButtons.VKShareButton;

class Socials extends Component{

    constructor(props){
        super(props);
        
    }
    render(){
        let metadata = this.props.metadata,
            og = metadata.open_graph || {};

        return(
            <ul class="socials-holder">
                <li>
                    <FacebookShare url={ og.url } title={ og.title } description={ og.description } picture={ og.image }>
                        <span class="icon icon-facebook"></span>
                    </FacebookShare>
                </li>
                <li>
                    <VKShare url={ og.url } title={ og.title } description={ og.description } picture={ og.image }>
                        <span class="icon icon-vk"></span>
                    </VKShare>
                </li>
                <li>
                    <TwitterShare url={ og.url } title={ og.title }>
                        <span class="icon icon-twitter"></span>
                    </TwitterShare>
                </li>
            </ul>
        );
    }

}

export default Socials;
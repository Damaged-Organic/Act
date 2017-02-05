import Promise from "promise-polyfill";

if(!window.Promise){
    window.Promise = Promise;
}

class Http{

    constructor(){
        this.isOriginal = ("withCredentials" in new XMLHttpRequest()) ? true : false;

        this.isPOST = false;
    }
    request(options){
        let xhr = this.isOriginal ? new XMLHttpRequest() : new XDomainRequest(),
            method = options.method,
            url = options.url,
            headers = options.headers || {},
            data = options.data || {};

        if(!(data instanceof FormData)){
            data = this._convertData(data);
            url = this._generateUrl(url, data);
        }

        return new Promise((resolve, reject) => {
            
            xhr.open(method, url, true);
            
            if(Object.keys(headers).length > 0) this.setHeaders(xhr, headers);

            xhr.onreadystatechange = () => {
                if(xhr.readyState !== 4) return;

                if(xhr.status >= 200 && xhr.status < 300){

                    let response = {
                        status: "success",
                        data: xhr.response
                    }
                    resolve(response);

                } else{
                    
                    let error = {
                        status: "fail",
                        data: xhr.responseText
                    }
                    reject(error);
                    
                }
            }
            xhr.send(this.isPOST ? data : "");

        });
    }
    get(options = {}){
        this.isPOST = false;
        if(!this._checkOptions(options)) return;

        return this.request(options);
    }
    post(options = {}){
        this.isPOST = true;

        if(!this._checkOptions(options)) return;

        return this.request(options);
    }
    setHeaders(xhr, headers){
        for(let type in headers){
            xhr.setRequestHeader(type, headers[type]);
        }
    }
    setWithCredentials(credentials){
        this.xhr.withCredentials = credentials;
    }
    _params(data){
        let paramsString = "";

        for(let key in data){
            if(paramsString.length > 0) paramsString += "&";
            paramsString += encodeURI(`${key}=${data[key]}`);
        }
        return paramsString;
    }
    _checkOptions(options){
        let isCorrect = false;

        if(!options.method){
            console.error("HTTP: No method provided");
            return;
        }
        if(!options.url){
            console.error("HTTP: Such endpoint doesn't exist");
            return;
        }

        isCorrect = true;

        return isCorrect;
    }
    _convertData(data){
        let convertedData = "";

        if(this.isPOST){

            convertedData = this._params(data);

        } else if(!this.isPOST && Object.keys(data).length > 0){

            convertedData = "?" + this._params(data);
        }
        return convertedData;
    }
    _generateUrl(url, data){
        return this.isPOST ? url : url + data;
    }
}

export default new Http;
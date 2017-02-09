import cfg from "../../diu.config.js";

export function staticPath(path = ""){
    return cfg.build + path;
}
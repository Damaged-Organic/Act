const MONTHS = [
    "січня",
    "лютого",
    "березня",
    "квітня",
    "травня",
    "червня",
    "липня",
    "серпня",
    "вересня",
    "жовтня",
    "листопада",
    "грудня"
];

const DAYS = 1000 * 60 * 60 * 24;
const HOURS = 1000 * 60 * 60;
const MINUTES = 1000 * 60;

function splitDate(date){
    date = new Date(date);

    return {
        day: ("0" + date.getDate()).slice(-2),
        month: ("0" + (date.getMonth() + 1)).slice(-2),
        year: date.getFullYear()
    };
}

export function toNamedMonth(date){
    date = new Date(date);

    let day = date.getDate(),
        month = date.getMonth(),
        year = date.getFullYear();

    return `${ ("0" + day).slice(-2) } ${ MONTHS[month] } ${ year }`;
}

export function separateBySlashes(date){
    date = splitDate(date);

    return `${ date.day }/${ date.month }/${ date.year }`;
}

export function timeHasPassedFromNow(date){
    let dateNow = Date.now(),
        timeDiff = 0,
        days = 0,
        hours = 0,
        minutes = 0;

    date = new Date(date);

    timeDiff = dateNow - date;

    days = Math.floor(timeDiff / DAYS);
    timeDiff -= days * DAYS;
    
    hours = Math.floor(timeDiff / HOURS);
    timeDiff -= hours * HOURS;

    minutes = Math.floor(timeDiff / MINUTES);
    timeDiff -= minutes * MINUTES;

    if(days > 0 || hours >= 2){
        date = splitDate(date);

        return `${ date.day }/${ date.month }/${ date.year }`;
    }
    if(days <= 0 && hours > 0) return hours + " год. тому"; 
    if(days <= 0 && hours <= 0 && minutes > 0) return minutes +" хв. тому";
}


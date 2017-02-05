export default function clearPhone(phone = ""){
    return phone.replace(/([\+\)\(\-\s])/gi, "");
}
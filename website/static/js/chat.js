function openPopup(){
    var popup = document.getElementById("pop-up-add")
    var popupCover = document.getElementById("pop-up-add-background")
    popup.style.visibility="visible"
    popupCover.style.visibility="visible"
}
function closePopup(){
    var popup = document.getElementById("pop-up-add")
    var popupCover = document.getElementById("pop-up-add-background")
    popup.style.visibility="hidden"
    popupCover.style.visibility="hidden"
}
function displayImage(){
    var src = document.forms["chat-add"]["chat-profile-add"].value
    var part = src.slice(0,2)
    if(part == ".."){
        document.getElementById("chat-profile-show").src = src
    }    
}
function openDelete(){
    var popup = document.getElementById("pop-up-del")
    var popupCover = document.getElementById("pop-up-del-background")
    popup.style.visibility="visible"
    popupCover.style.visibility="visible"
}
function closeDelete(){
    var popup = document.getElementById("pop-up-del")
    var popupCover = document.getElementById("pop-up-del-background")
    popup.style.visibility="hidden"
    popupCover.style.visibility="hidden"
}
function openSetting(){
    var popup = document.getElementById("pop-up-setting")
    var popupCover = document.getElementById("pop-up-setting-background")
    popup.style.visibility="visible"
    popupCover.style.visibility="visible"
    var choice = document.forms["chat-setting"]["chat-setting-img"].value
    document.getElementById("chat-profile-show-setting").src = choice
}
function closeSetting(){
    var popup = document.getElementById("pop-up-setting")
    var popupCover = document.getElementById("pop-up-setting-background")
    popup.style.visibility="hidden"
    popupCover.style.visibility="hidden"
}
function displayImageSetting(){
    var src = document.forms["chat-setting"]["chat-profile-setting"].value
    var part = src.slice(0,2)
    if(part == ".."){
        document.getElementById("chat-profile-show-setting").src = src
    }    
}
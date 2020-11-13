// {#  {#Auth#}* #}
// var ANGULAR_IP = 'http://192.168.2.103:4200/';
var ANGULAR_IP = 'http://178.218.200.63:80/';
var CMS_IP = 'http://178.218.200.63:8001/';
var DJANGO_IP = 'http://178.218.200.63:8000/';
var TOKEN_TITLE = 'token';

// {#let token2 = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJxd2VAd2QucnUiLCJyb2xlcyI6IlVTRVIiLCJpc3MiOiJldGlja2V0LnV6cmFpbHdheS51eiIsImV4cCI6MTU1Mzc2ODEyNSwidXNlcklkIjoiZDAwZWIxMTItNzI1YS00NzFjLWJhMmQtOGY5ZWQzYTNkY2Y2In0.PzL5R0txI1eD2rcJ1hPW56WRfhCJnD0IL2JmIr0pjbk";#}
// {#sessionStorage.setItem('tk_1', token2);#}
let token;
let query = document.URL;
// {#console.log(query);#}
let a = window.document.createElement('a');
a.href = query;
let params = new URLSearchParams(a.search);
token = params.get(TOKEN_TITLE);
let isLogged = null;
console.log('tok = ' + !token);
console.log("tok = " + (token === "false"));

if (!token || token === "false") {
    console.log('if token === false => ' + (token === "false"));
    token = sessionStorage.getItem(TOKEN_TITLE);
    if (!token || token === "false" || !getCookie('token')) {
        console.log("cookie get inner");
        token = getCookie('token');
    }
} else {
    sessionStorage.setItem(TOKEN_TITLE, token);
    if (!getCookie('token')) {
        console.log("cookie save");
        setCookie("token", token, 1);
    }

}

var dropDown = document.getElementById("userIdDropDown");
if (token) {
    //save to session storage
    getMenuItems();
    let userId = parseJwt(token)['sub'];
    document.getElementById("login").style.display = "none";
    document.getElementById("loggedIn").style.display = "inline";
    document.getElementById("userIdPlace").innerHTML = userId;
    dropDown.style.visibility = 'visible';
    dropDown.style.position = 'relative';
    isLogged = true;
} else {
    console.log(">> hide");
    isLogged = false;
    document.getElementById("loggedIn").style.display = "none";
    dropDown.style.visibility = 'hidden';
    dropDown.style.position = 'absolute';
}

if ((!token || token === "false") && getCSRFToken()) {
    // logOut()
}


function goLogin() {
    window.location.href = ANGULAR_IP + 'auth/login?next=cms';
    // {#window.location.reload();#}
    // {#console.log("login pushed");#}

}

function logOut() {
    localStorage.clear();
    console.log('logout');
    token = params.delete(TOKEN_TITLE);
    sessionStorage.removeItem(TOKEN_TITLE);
    console.log(token);
    window.location.href = CMS_IP + "auth/logout";
    deleteCookie("csrftoken");
    deleteCookie("token");
}


function parseJwt(token) {
    let base64Url = token.split('.')[1];
    let base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    return JSON.parse(window.atob(base64));
}

function goToDirection() {
    let from = document.getElementById('input-from').value;
    let to = document.getElementById('input-to').value;
    let date = document.getElementById('datepicker-inp').value;
    console.log(from);
    console.log(to);
    console.log(date);
}

function to_admin_panel() {
    console.log('to admin panel');
    token = sessionStorage.getItem(TOKEN_TITLE);
    if (token) {
        console.log('forwarding');
        window.location.href = DJANGO_IP + '?token=' + token;
    } else {
        alert("Please login as administrator");
    }
}

function to_cms_panel() {
    // # todo
    console.log('to to_cms_panel panel');
    token = sessionStorage.getItem(TOKEN_TITLE);
    if (token) {
        console.log('forwarding');
        window.location.href = CMS_IP + 'auth?token=' + token;
    } else {
        alert("Please login as administrator");
    }
}

function saveData(data) {
    localStorage.clear();
    for (var prop in data) {
        var item = data[prop];
        localStorage[prop] = JSON.stringify(data[prop]);
    }
}

function displayData() {
    // console.log("data.keys() " + localStorage['ru']);
    console.log("data.keys() " + localStorage['url']);
    lang = window.location.pathname.slice(1, 3);

    if (localStorage['url'] && localStorage[lang]) {
        let url_stored = JSON.parse(localStorage.getItem("url"));
        let lang_stored = JSON.parse(localStorage.getItem(lang));
        let len = url_stored.length;
        let tkn = "?token=" + token;

        var ul = document.getElementById("userAccessPages");
        for (var i = 0; i < len; i++) {
            let li = window.document.createElement('li');
            let a = window.document.createElement('a');
            li.innerText = lang_stored[i];
            a.appendChild(li);
            ul.appendChild(a);
            if (i === 0) {
                li.className = "dropdown-item bottom-bordered-item";
            } else if (i === len - 1) {
                li.className = "dropdown-item top-bordered-item";
                a.setAttribute('onclick', 'outter_logout()');
                continue;
            } else {
                li.className = "dropdown-item";
            }
            a.href = url_stored[i] + tkn;
        }
    } else {
        alert('Something went wrong please try to reload!');
    }
}

function outter_logout() {
    var out = logOut();
    return out;
}

function getMenuItems() {
    lang = window.location.pathname.slice(1, -1);

    if (!localStorage || (!localStorage['url'] && !localStorage[lang])) {
        console.log("getMenuItems");
        header = {
            'lang': lang
        };
        console.log(">>>> " + jQuery.param(header));
        $.ajax({
            type: "GET",
            url: CMS_IP + 'auth/check?' + jQuery.param(header),
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': 'Bearer ' + getCookie('token'),
                'X-CSRFToken': getCookie("csrftoken")
            },
            data: JSON.stringify({}),
            traditional: true,
            success: function (data) {
                console.log("data received");
                saveData(data);
                displayData();
            },
            error: function (jqXHR, textStatus, errorThrown) {
                alert('>>> Internal Server Error!')
            }
        });
    } else {
        displayData();
    }
}

function getCSRFToken() {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, 10) === ('csrftoken' + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(10));
                break;
            }
        }
    }
    return cookieValue;
}

function getCookie(name) {
    if (!document.cookie) {
        return null;
    }

    const xsrfCookies = document.cookie.split(';')
        .map(c => c.trim())
        .filter(c => c.startsWith(name + '='));

    if (xsrfCookies.length === 0) {
        return null;
    }

    return decodeURIComponent(xsrfCookies[0].split('=')[1]);
}

function setCookie(c_name, value, exdays) {
    var exdate = new Date();
    exdate.setDate(exdate.getDate() + exdays);
    var c_value = escape(value) + ((exdays == null) ? "" : "; expires=" + exdate.toUTCString());
    document.cookie = c_name + "=" + c_value;
}

function deleteCookie(name) {
    document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
}

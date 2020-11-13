function StationSearch(type) {
    let request = null;
    const input = document.getElementById('input-' + type);
    const loader = document.getElementById('loader-' + type);
    const result = document.getElementById('result-' + type);
    let timer = null;

    updateLoader(false);

    this.search = function () {
        searchFunction();
    };

    this.setSearchValue = function (value) {
        input.value = value;
        searchFunction();
    };

    function updateLoader(loading) {
        loader.style.display = (loading ? ('block') : ('none'));
    }

    function searchFunction() {
        const value = input.value;
        if (value.length > 2) {
            updateLoader(true);

            // ajax
            clearTimeout(timer);
            timer = setTimeout(function () {
                request = $.ajax({
                    url: "http://178.218.200.63:8080/api/v1/station/list",
                    type: "post",
                    dataType: "json",
                    contentType: "application/json",
                    data: JSON.stringify({
                        'nameFull': value
                    }),
                    success: function (returnData) {
                        updateLoader(false);
                        console.log(returnData);
                        result.innerHTML = '';
                        if (returnData['station'].length) {
                            returnData['station'].forEach(function(value) {
                                const el = document.createElement('li');
                                el.innerText = value['nameFull'];
                                el.className = 'list-group-item list-group-item-action';
                                el.onclick = function () {
                                    input.value = value['nameFull'];
                                    sessionStorage.setItem(type, value['code']);
                                    result.innerHTML = '';
                                };
                                result.appendChild(el);
                            });
                        }
                        request = null;
                    }
                });
            }, 500);
        } else {
            updateLoader(false);
            if (request !== null) {
                request.abort();
            }
        }
    }
}

const from = new StationSearch('from');
const to = new StationSearch('to');

// datepicker
let sdVal1 = 'КОГДА';
let sdVal2 = '';

let onlyForward = true;

const datepickerInput = $('#datepicker-input');
const datepickerWrapper = $('.datepicker');
const datepicker = $("#datepicker");
const datepickerMulti = $("#datepicker-multi");
const buttons = $('.btn-outline-accent');

const date = new Date();
const today = (date.getMonth() + 1);
const newDate = new Date(date.setDate(date.getDate() + 40));
let after = (newDate.getMonth() + 1);
if ((after < today)) {
    after += 12;
}
const numberOfMonths = (after - today) + 1;

datepicker.datepicker({
    numberOfMonths: numberOfMonths,
    showButtonPanel: false,
    showOtherMonths: true,
    minDate: 0,
    maxDate: '+40D',
    onSelect: function (sd_value) {
        sessionStorage.setItem('value', sd_value);
        sessionStorage.removeItem('value2');
        const split = sd_value.split('/');
        sdVal1 = split[1] + '/' + split[0] + '/' + split[2];
        datepickerInput.val(sdVal1);
        datepickerWrapper.hide();
    },
});
datepicker.datepicker("option", $.datepicker.regional["ru"]);
datepicker.datepicker("option", "showAnim", 'None');
datepicker.datepicker("option", "dateFormat", 'mm/dd/yy');

datepickerMulti.datepicker({
    range: 'period',
    numberOfMonths: numberOfMonths,
    showButtonPanel: false,
    showOtherMonths: true,
    minDate: 0,
    maxDate: '+40D',
    onSelect: function (dateText, inst, extensionRange) {
        const split1 = extensionRange.startDateText.split('/');
        sdVal1 = split1[1] + '/' + split1[0] + '/' + split1[2];
        const split2 = extensionRange.endDateText.split('/');
        sdVal2 = split2[1] + '/' + split2[0] + '/' + split2[2];
        sessionStorage.setItem('value', sdVal1);
        sessionStorage.setItem('value2', sdVal2);
        datepickerInput.val(sdVal1 + ' - ' + sdVal2);
        if (sdVal1 !== sdVal2) {
            datepickerWrapper.hide();
        }
    },
});
datepickerMulti.datepicker("option", $.datepicker.regional["ru"]);
datepickerMulti.datepicker("option", "showAnim", 'None');
datepickerMulti.datepicker("option", "dateFormat", 'mm/dd/yy');
datepickerMulti.hide();

// clickOutside
$(document).on('click', function () {
    datepickerWrapper.hide();
});

datepickerInput.on('click', eventInput);

function eventInput() {
    event.stopPropagation();
    if (datepickerWrapper.is(':hidden')) {
        datepickerWrapper.show();
    } else {
        datepickerWrapper.hide();
    }
}

function forward(el) {
    event.stopPropagation();
    onlyForward = true;
    buttons.removeClass('active');
    if (el.classList) {
        el.classList.add('active');
    } else {
        el.className += ' active';
    }
    datepickerMulti.hide();
    datepicker.show();
}

function backward(el) {
    event.stopPropagation();
    onlyForward = false;
    buttons.removeClass('active');
    if (el.classList) {
        el.classList.add('active');
    } else {
        el.className += ' active';
    }
    datepickerMulti.show();
    datepicker.hide();
}

function exchange() {
    const from = $('input-from');
    const to = $('input-to');

    const tmp = from.val();
    from.val(to.val());
    to.val(tmp);
}

function gotoNext() {
    const from = +sessionStorage.getItem('from') || 0;
    const to = +sessionStorage.getItem('to') || 0;
    const date = sessionStorage.getItem('value') || '';
    const date2 = sessionStorage.getItem('value2') || '';

    if (from !== 0 && to !== 0) {
        const cms_ip = 'http://178.218.200.63:80/';
        let token_param = '';
        let token = sessionStorage.getItem('token');
        if (!token) {
            token = getCookie('token')
        }
        if (token) {
            console.log("token");
            token_param = "&token=" + token;
        }
        if (onlyForward === true) {
            if (date.length) {
                const tmp = date.split('/');
                const newDate = tmp[1] + '.' + tmp[0] + '.' + tmp[2];
                console.log(cms_ip + 'process/train/?f=' + from + '&t=' + to + '&date=' + newDate + token_param);
                window.location.href = cms_ip + 'process/train/?f=' + from + '&t=' + to + '&date=' + newDate + token_param;
            }
        } else {
            if (date.length && date2.length) {
                const newDate = date.replace(/\//g, '.');

                const newDate2 = date2.replace(/\//g, '.');
                window.location.href = cms_ip + 'process/train/?f=' + from + '&t=' + to + '&date=' + newDate + '&date2=' + newDate2 + token_param;
            }
        }
    }
}

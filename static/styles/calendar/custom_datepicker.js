// {# Custom datepicker-Nurlan #}

const datepickerInp = $('#datepicker-inp');
const datepickerWrapper = $('.datepicker');
const btnForward = $('#forwardBtn');
const btnBackward = $('#backwardBtn');
const dp = $('#datepicker-multi');
const dpRange = $('#datepicker-multi-range');
let onlyForward = true;

let sdVal1 = 'КОГДА';
let sdVal2 = '';

$(function () {
    // preparing the datepicker data
    const date = new Date();
    const today = (date.getMonth() + 1);
    const newDate = new Date(date.setDate(date.getDate() + 40));
    let after = (newDate.getMonth() + 1);
    if ((after < today)) {
        after += 12;
    }
    const numberOfMonths = (after - today) + 1;

    datepickerInp.val(sdVal1);

    // hide
    datepickerWrapper.hide();
    dpRange.hide();


    $(document).on('click', () => {
        datepickerWrapper.hide();
    });
    datepickerInp.on('click', eventInput);
    // datepickerInp.on('focus', eventInput);

    btnForward.addClass('active');
    btnBackward.removeClass('active');

    btnForward.on('click', () => {
        event.stopPropagation();
        onlyForward = true;
        btnForward.addClass('active');
        btnBackward.removeClass('active');
        dpRange.hide();
        dp.show();
    });

    btnBackward.on('click', () => {
        event.stopPropagation();
        onlyForward = false;
        btnForward.removeClass('active');
        btnBackward.addClass('active');
        dpRange.show();
        dp.hide();
    });

    // datepicker's options
    dp.datepicker({
        numberOfMonths: numberOfMonths,
        showButtonPanel: false,
        showOtherMonths: true,
        minDate: 0,
        maxDate: '+40D',
        onSelect: function (sd_value) {
            sessionStorage.setItem('sd-value', sd_value);
            sessionStorage.removeItem('sd-value2');
            const split = sd_value.split('/');
            sdVal1 = split[1] + '/' + split[0] + '/' + split[2];
            datepickerInp.val(sdVal1);
            datepickerWrapper.hide();
        },
    });

    dpRange.datepicker({
        range: 'period', // режим - выбор периода
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
            sessionStorage.setItem('sd-value', sdVal1);
            sessionStorage.setItem('sd-value2', sdVal2);
            datepickerInp.val(sdVal1 + ' - ' + sdVal2);
            if (sdVal1 !== sdVal2) {
                datepickerWrapper.hide();
            }
        },
    });

});

function eventInput() {
    event.stopPropagation();
    if (datepickerWrapper.is(':hidden')) {
        datepickerWrapper.show();
    } else {
        // {#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#}
        datepickerWrapper.hide();
    }
}

function gotoNext() {
    const from = +sessionStorage.getItem('sf-code') || 0;
    const to = +sessionStorage.getItem('st-code') || 0;
    const date = sessionStorage.getItem('sd-value') || '';
    const date2 = sessionStorage.getItem('sd-value2') || '';

    if (from !== 0 && to !== 0) {
        var cms_ip = 'http://178.218.200.63:80/';
        var token_param = '';
        var token = sessionStorage.getItem(TOKEN_TITLE);
        if(!token){
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
                // {#https://nulledbb.com/thread-vBulletin-Connect-5-4-5-Nulled#}
                console.log(cms_ip + 'process/train/?f=' + from + '&t=' + to + '&date=' + newDate + token_param);
                window.location.href = cms_ip + 'process/train/?f=' + from + '&t=' + to + '&date=' + newDate + token_param;
            }
        } else {
            if (date.length && date2.length) {
                const newDate = date.replace(/\//g, '.');
                // const tmp = date.split('/');
                // const newDate = tmp[1] + '.' + tmp[0] + '.' + tmp[2];

                const newDate2 = date2.replace(/\//g, '.');
                // const tmp2 = date2.split('/');
                // const newDate2 = tmp2[1] + '.' + tmp2[0] + '.' + tmp2[2];
                window.location.href = cms_ip + 'process/train/?f=' + from + '&t=' + to + '&date=' + newDate + '&date2=' + newDate2 + token_param;
            }
        }
    }
}

/* search */
for (let i = 1; i <= 2; i++) {
    const search = $('#search' + i);
    const result = $('#result' + i);
    const loading = $('#loading' + i);
    let timer = [null, null];
    loading.hide();
    search.keyup(function () {
        const minlength = 3;
        let searchRequest = [null, null];
        clearTimeout(timer[i - 1]);
        timer[i - 1] = setTimeout(() => {
            const that = this, value = $(this).val();
            if (value.length >= minlength) {
                loading.show();
                if (searchRequest[i - 1] != null) {
                    searchRequest[i - 1].abort();
                }
                searchRequest[i - 1] = $.ajax({
                    url: "http://178.218.200.63:8080/api/v1/station/list",
                    type: "post",
                    dataType: "json",
                    contentType: "application/json",
                    data: JSON.stringify({
                        'nameFull': value
                    }),
                    success: function (msg) {
                        //we need to check if the value is the same
                        if (value === $(that).val()) {
                            result.html('');
                            if (msg['station'].length) {
                                //Receiving the result of search here
                                msg['station'].forEach(value => {
                                    result.append('<li class="list-group-item" onclick="listClicked(' + i + ', ' + value['code'] + ', \'' + value['nameFull'] + '\')">' + value['nameFull'] + '</li>');
                                });
                            } else {
                                // {#result.append('<a href="#" class="list-group-item text-muted">По Вашему запросу ничего не найдено.</a>');#}
                            }
                        }
                    }
                }).done(function () {
                    loading.hide();
                });
            } else {
                loading.hide();
                if (searchRequest[i - 1] != null) {
                    searchRequest[i - 1].abort();
                }
                result.html('');
            }
        }, 500);
    });
    search.click(function () {
        const minlength = 3;
        let searchRequest = [null, null];
        clearTimeout(timer[i - 1]);
        timer[i - 1] = setTimeout(() => {
            const that = this, value = $(this).val();
            if (value.length >= minlength) {
                loading.show();
                if (searchRequest[i - 1] != null) {
                    searchRequest[i - 1].abort();
                }
                searchRequest[i - 1] = $.ajax({
                    type: "POST",
                    url: "http://178.218.200.63:8080/api/v1/station/list",
                    data: JSON.stringify({
                        'nameFull': value
                    }),
                    contentType: 'application/json',
                    dataType: 'json',
                    success: function (msg) {
                        //we need to check if the value is the same
                        if (value === $(that).val()) {
                            result.html('');
                            if (msg['station'].length) {
                                //Receiving the result of search here
                                msg['station'].forEach(value => {
                                    result.append('<li class="list-group-item" onclick="listClicked(' + i + ', ' + value['code'] + ', \'' + value['nameFull'] + '\')">' + value['nameFull'] + '</li>');
                                });
                            } else {
                                // {#result.append('<a href="#" class="list-group-item text-muted">По Вашему запросу ничего не найдено.</a>');#}
                            }
                        }
                    }
                }).done(function () {
                    loading.hide();
                });
            } else {
                loading.hide();
                if (searchRequest[i - 1] != null) {
                    searchRequest[i - 1].abort();
                }
                result.html('');
            }
        }, 500);
    });
    $(document).click(function (event) {
        $target = $(event.target);
        if (!$target.closest('#search').length && $('#result> a').is(":visible")) {
            result.html('');
        }
    });
}

function listClicked(index, code, value) {
    const search = $('#search' + index);
    const result = $('#result' + index);
    search.val(value);
    result.html('');
    if (index === 1) {
        sessionStorage.setItem('sf-code', code);
    } else if (index === 2) {
        sessionStorage.setItem('st-code', code);
    }
}

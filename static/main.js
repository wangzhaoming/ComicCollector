$(function () {
    $('body').height($(window).height());

    $('.js-fetch-comic').click(function () {
        let url = $(this).data('url');
        let div = $(this).parent().next();
        $.getJSON(url, function (data) {
            let ul = $('<ul></ul>');
            $.each(data.list, function (i, item) {
                let li = $('<li>' + item.name + '</li>');
                li.data('pages', item.pages);
                li.click(function () {
                    let page = $(this).data('pages')[0];
                    $('.container>img').attr('src', page['href']);

                    $('#prev').data('url', '');
                    $('#next').data('url', '');
                    $('#prev').data('cur', 0);
                    $('#next').data('cur', 0);
                    $('#prev').data('pages', $(this).data('pages'));
                    $('#next').data('pages', $(this).data('pages'));
                    let next = $(this).data('pages')[1];
                    if (next) {
                        $('#next').data('url', next['href']);
                    }
                });
                ul.append(li);
            });
            div.empty().append(ul);
        });
    });

    $('#next').click(function () {
        let url = $(this).data('url');
        if (url) {
            $('#prev').data('url', $('.container>img').attr('src'));
            $('.container>img').attr('src', url);

            let cur = $(this).data('cur');
            $('#prev').data('cur', cur + 1);
            $('#next').data('cur', cur + 1);

            let pages = $(this).data('pages');

            $('#next').data('url', '');
            let next = pages[$(this).data('cur')];
            if (next) {
                $('#next').data('url', next['href']);
            }
        }
    });

    $('#prev').click(function () {
        let url = $(this).data('url');
        if (url) {
            $('#next').data('url', $('.container>img').attr('src'));
            $('.container>img').attr('src', url);

            let cur = $(this).data('cur');
            $('#prev').data('cur', cur - 1);
            $('#next').data('cur', cur - 1);
            let pages = $(this).data('pages');

            $('#prev').data('url', '');
            let prev = pages[$(this).data('cur')];
            if (prev) {
                $('#prev').data('url', prev['href']);
            }
        }
    });
});
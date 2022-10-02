/* 
    =================================
    Dropdown Filters
    =================================
*/

    $('.dropdown .title').click(function () {
        if($(this).parent().find('.dropdown-menu').height() > 0) {
            closeMenu(this);
        } else {
            openMenu(this);
        }
    });

    $('.dropdown-menu li').click(function () {
        closeMenu(this);
    });

    function closeMenu(el) {
        $(el).closest('.dropdown').toggleClass('closed').find('.title').text($(el).text());
        $(el).parent().find('.dropdown-menu').css('height', 0);
    }

    function openMenu(el) {
        var numberOfItems = $(el).parent().find('li').length;
        var listLineHeight = parseInt($('.dropdown-menu li').css('line-height'));
        var bottomPadding = 40;

        $(el).parent().toggleClass('closed');

        $(el).parent().find('.dropdown-menu').css({
            height: numberOfItems * listLineHeight + bottomPadding
        });
    }
const $headerElem = $('header');
const $divRedheader = $('div#red_header');

$divRedheader.on('click', function () {
    $headerElem.addClass('red');
});

const $headerElem = $('header');
const $divRedheader = $('div#red_header');

$divRedheader.on('click', function () {
    $headerElem.css('color', '#FF0000');
});

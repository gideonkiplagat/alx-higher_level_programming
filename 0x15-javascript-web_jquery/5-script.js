const $listElem = $('ul.my_list');
const $addItemElem = $('div#add_item');

$addItemElem.om('click', () => {
    $listElem.append('<li>Item</li>');
});

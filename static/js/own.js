/**
 * Created by Abc on 11.03.2016.
 */

// Adding items to form

$(document).ready(function () {
    $('.add-item').click(function (ev) {
        ev.preventDefault();
        var count = $('.items').children().length;
        var itemMarkup = $('.items div:last-child')[0].outerHTML;
        $('div.items').append(itemMarkup);
        var item = $('.items div:last-child');
        var str = item[0].outerHTML;
        var regex = /-\d+/gi;
        item.replaceWith(str.replace(regex, "-"+count.toString()));
        $('#id_item_set-TOTAL_FORMS').attr('value', count + 1);
    });
});


// Deleting items from form

$(document).ready(function () {
    $(document).on('change', 'input[id$="DELETE"]', function(event){
        event.preventDefault();
        var items = $('.items');
        var count = items.children().length;
        var deletedItem = $(this).parents('div[id^="item"]');
        var itemNumber = deletedItem.index();
        items.slice(itemNumber).each(function(){
            var str = this[0].outerHTML;
            var regex = /-\d+/gi;
            this.replaceWith(str.replace(regex, "-"+$(".items").index(this).toString()));
        });
        deletedItem.remove();
        $('#id_item_set-TOTAL_FORMS').attr('value', count - 1);

    });
});


// Making archived items grey in admin table

$(document).ready(function () {
   $('tr td:last-child').each(function(){
           var archived = $(this).find('img').attr('alt') == 'True';
            if (archived) {
                $(this).parents('tr').css('background-color', '#BFB8B8');
            }
   })
});


// dynamic update of total cost

$(document).ready(function(){
  $(document).on('keyup', 'input[id$="cost"]', function(){
      var currentCost = $('#total-cost');
      var total = parseFloat(currentCost.text());
      var current = parseFloat($(this).val());
      var res = total + current;
     if (!isNaN(res))
        currentCost.text(ress.toString());
  });
});
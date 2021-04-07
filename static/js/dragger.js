// JavaScript Document
$('.draggable').draggable({
  revert: "invalid",
  stack: ".draggable",
  helper: 'clone'
});
$('.droppable').droppable({
  accept: ".draggable",
  drop: function(event, ui) {
    var droppable = $(this);
    var draggable = ui.draggable;
    // Move draggable into droppable
    draggable.clone().appendTo(droppable);
    draggable.css({float:'left'});
  }
});
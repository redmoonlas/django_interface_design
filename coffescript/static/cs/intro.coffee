class RensonsiveCanvas
  constructor: (selector) ->
    @canvas_ref = $(selector)
    @canvas = @canvas_ref.get(0)
    @context = @canvas.getContext('2d')
    @resize()
    window.addEventListener 'resize', @resize
  resize: () =>
    container = $(@canvas_ref).parent()
    @canvas_ref.attr 'width', $(container).width()
    @canvas_ref.attr 'height', $(container).height()

class Game extends RensonsiveCanvas
  constructor: () ->
    super '#chart'
    @context.font = "20px Calibri";
    @context.textAlign = "center"
    @loopindex = 0
    window.setInterval @mainloop, 200
  updateCanvas: () ->
    @loopindex = @loopindex + 1
  drawCanvas: () ->
    @context.fillStyle = if @loopindex % 2 then 'yellow' else 'blue'
    @context.fillRect 0, 0, @canvas.width, @canvas.height
    @context.fillStyle = "#333333"
    @context.fillText "Canvas width: #{@canvas.width} px", (@canvas.width/2), (@canvas.height/2)
  mainloop: () =>
    @updateCanvas()
    @drawCanvas()

startGame = () ->
  new Game

document.addEventListener('DOMContentLoaded', startGame)
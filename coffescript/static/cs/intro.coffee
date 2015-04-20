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

class Balloon
  constructor: (static_root) ->
      @sprite = new Image()
      @sprite.src = static_root
      @sprite.width = 76
      @sprite.height = 213
      @x = 0
      @y = 0
  updatePosition: () ->
      @x = @x + 3
      @y = 10 * Math.sin(@x)

class Game extends RensonsiveCanvas
  constructor: (static_root) ->
    super '#chart'
    @context.font = "20px Calibri";
    @context.textAlign = "center"
    @loopindex = 0
    @balloon = new Balloon(static_root)
    window.setInterval @mainloop, 200
  updateCanvas: () ->
    @loopindex = @loopindex + 1
    @balloon.updatePosition()
  drawBackgroud: () ->
#    @context.fillStyle = if @loopindex % 2 then 'yellow' else 'blue'
    @context.fillStyle = 'yellow'
    @context.fillRect 0, 0, @canvas.width, @canvas.height
  drawBalloon: () ->
    @context.save()
    @context.translate @balloon.x, @balloon.y
    sprite = @balloon.sprite
    @context.drawImage sprite, 0, 0, sprite.width, sprite.height, 0, 0, sprite.width, sprite.height
    @context.restore()
  drawCanvas: () ->
    @drawBackgroud()
    @drawBalloon()
#    @context.fillStyle = "#333333"
#    @context.fillText "Canvas width: #{@canvas.width} px", (@canvas.width/2), (@canvas.height/2)
  mainloop: () =>
    @updateCanvas()
    @drawCanvas()

@game = Game
#startGame = () ->
#  new Game
#
#document.addEventListener('DOMContentLoaded', startGame)
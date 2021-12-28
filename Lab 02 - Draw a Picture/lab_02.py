import arcade

arcade.open_window(600, 600, "Drawing for lab 2")

arcade.set_background_color((255, 255, 255))

arcade.start_render()

arcade.draw_circle_filled(300, 300, 200, arcade.color.YELLOW)
arcade.draw_circle_filled(220, 350, 5, arcade.color.BLACK)
arcade.draw_circle_filled(380, 350, 5, arcade.color.BLACK)
arcade.draw_arc_outline(300, 200, 130, 75, arcade.color.BLACK, 190, 350, 10)
arcade.draw_arc_filled(200, 375, 125, 125, arcade.color.BLACK, 180, 360)
arcade.draw_arc_filled(400, 375, 125, 125, arcade.color.BLACK, 180, 360)
arcade.draw_line(250, 370, 350, 370, arcade.color.BLACK, 10)

arcade.finish_render()

arcade.run()
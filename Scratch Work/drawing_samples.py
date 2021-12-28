import arcade

arcade.open_window(1000, 1000, "Drawing Example")

arcade.set_background_color((77, 221, 240))

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 999, 500, 0, arcade.csscolor.GREEN)
arcade.draw_rectangle_filled(100, 512, 20, 60, arcade.csscolor.SADDLE_BROWN)
arcade.draw_circle_filled(100, 560, 30, arcade.csscolor.FOREST_GREEN)
arcade.draw_rectangle_filled(192, 515, 20, 60, arcade.csscolor.SADDLE_BROWN)
arcade.draw_ellipse_filled(192, 567, 60, 80, arcade.csscolor.FOREST_GREEN)
arcade.draw_rectangle_filled(300, 520, 20, 60, arcade.csscolor.SADDLE_BROWN)
arcade.draw_arc_filled(298, 540, 60, 100, arcade.csscolor.FOREST_GREEN, -10, 190)
arcade.draw_rectangle_filled(400, 520, 20, 60, arcade.csscolor.SADDLE_BROWN)
arcade.draw_triangle_filled(400, 600, 370, 520, 430, 520, arcade.csscolor.FOREST_GREEN)
arcade.draw_rectangle_filled(500, 500, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500, 600),
                            (480, 568),
                            (470, 520),
                            (530, 520),
                            (520, 568)
                            ),
                           arcade.csscolor.FOREST_GREEN)
arcade.draw_circle_filled(800, 850, 50, arcade.color.YELLOW)
arcade.draw_line(800, 850, 700, 850, arcade.color.YELLOW, 3)
arcade.draw_line(800, 850, 900, 850, arcade.color.YELLOW, 3)
arcade.draw_line(800, 850, 800, 750, arcade.color.YELLOW, 3)
arcade.draw_line(800, 850, 800, 950, arcade.color.YELLOW, 3)

arcade.draw_line(800, 850, 850, 900, arcade.color.YELLOW, 3)
arcade.draw_line(800, 850, 850, 800, arcade.color.YELLOW, 3)
arcade.draw_line(800, 850, 750, 900, arcade.color.YELLOW, 3)
arcade.draw_line(800, 850, 750, 800, arcade.color.YELLOW, 3)

arcade.draw_text("Plant some trees!",
                 300, 380,
                 arcade.color.BLACK, 24)

arcade.finish_render()

arcade.run()
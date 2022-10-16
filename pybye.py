#!/bin/python3
from create_config import *
import subprocess
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

# Functions used to change cursor.
def switch_to_watch_cursor():
    watch_cursor = Gdk.Cursor(Gdk.CursorType.WATCH)
    win.get_window().set_cursor(watch_cursor)


def switch_to_arrow_cursor():
    arrow_cursor = Gdk.Cursor(Gdk.CursorType.ARROW)
    win.get_window().set_cursor(arrow_cursor)

# Runs a command and displays an error if there is one.
def run_command(shell_command):
    try:
        click = subprocess.check_output((shell_command), shell=True)
    except subprocess.CalledProcessError as error:
        dialog = Gtk.MessageDialog(
            transient_for=MainWindow(),
            flags=0,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.CLOSE,
            text="There's been an error while running the command",
        )
        dialog.format_secondary_text(
            str(error)
        )
        response = dialog.run()
        dialog.destroy()
        if response == Gtk.ResponseType.CLOSE:
            switch_to_arrow_cursor()
    else:
        switch_to_arrow_cursor()
        Gtk.main_quit()


class ConfirmAction(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(title=status,
                         transient_for=parent,
                         modal=True,
                         name="dialog"
                         )
        self.set_default_size(150, 120)
        self.set_resizable(False)
        self.connect('key-press-event', self.on_escape_pressed)

        cancel = self.add_button(Gtk.STOCK_NO, Gtk.ResponseType.CANCEL)
        yes = self.add_button(Gtk.STOCK_YES, Gtk.ResponseType.YES)

        label = Gtk.Label(label=f"\n\nDo you want to {status.lower()}?")
        box = self.get_content_area()
        box.add(label)
        self.show_all()

    def on_escape_pressed(self, widget, event):
        pressed_key = Gdk.keyval_name(event.keyval)
        alt = (event.state & Gdk.ModifierType.MOD1_MASK)
        if pressed_key == "Escape":
            switch_to_arrow_cursor()
            self.hide()

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,
                            title="PyBye",
                            name="main_window"
                            )
        Gtk.Window.set_default_size(self, width, height)
        self.set_border_width(border_width)
        self.set_decorated(False)
        self.connect('key-press-event', self.on_key_pressed)

        # Get CSS style for GTK+3 from a file.
        path_to_css = os.path.dirname(os.path.abspath(__file__)) + "/gtk_style.css"
        style_provider = Gtk.CssProvider()
        style_provider.load_from_path(path_to_css)
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
    # First button.
        label1 = Gtk.Label(label=button_one)
        label1.set_selectable(False)
        button1 = Gtk.Button.new_from_icon_name(icon_name=button_one_icon,
                                                size=icon_size
                                                )
        button1.connect("clicked", self.on_button1_clicked)
    # Second button.
        label2 = Gtk.Label(label=button_two)
        label2.set_selectable(False)
        button2 = Gtk.Button.new_from_icon_name(icon_name=button_two_icon,
                                                size=icon_size
                                                )
        button2.connect("clicked", self.on_button2_clicked)
    # Third button.
        label3 = Gtk.Label(label=button_three)
        label3.set_selectable(False)
        button3 = Gtk.Button.new_from_icon_name(icon_name=button_three_icon,
                                                size=icon_size
                                                )
        button3.connect("clicked", self.on_button3_clicked)
    # Fourth button.
        label4 = Gtk.Label(label=button_four)
        label4.set_selectable(False)
        button4 = Gtk.Button.new_from_icon_name(icon_name=button_four_icon,
                                                size=icon_size)
        button4.connect("clicked", self.on_button4_clicked)
    # Fifth button.
        label5 = Gtk.Label(label=button_five)
        label5.set_selectable(False)
        button5 = Gtk.Button.new_from_icon_name(icon_name=button_five_icon,
                                                size=icon_size
                                                )
        button5.connect("clicked", self.on_button5_clicked)

    # Add buttons and labels to the grid.
        grid = Gtk.Grid()
        grid.add(button1)
        grid.attach_next_to(label1, button1,
                            Gtk.PositionType.BOTTOM,
                            1, 1
                            )
        grid.add(button2)
        grid.attach_next_to(label2, button2,
                            Gtk.PositionType.BOTTOM,
                            1, 1
                            )
        grid.add(button3)
        grid.attach_next_to(label3, button3,
                            Gtk.PositionType.BOTTOM,
                            1, 1
                            )
        grid.add(button4)
        grid.attach_next_to(label4,
                            button4,
                            Gtk.PositionType.BOTTOM, 
                            1, 1
                            )
        grid.add(button5)
        grid.attach_next_to(label5, button5,
                            Gtk.PositionType.BOTTOM, 
                            1, 1
                            )
        grid.set_row_spacing(row_spacing)
        grid.set_row_homogeneous(False)
        grid.set_column_homogeneous(True)
        grid.set_column_spacing(column_spacing)
        self.add(grid)

    # Button functions.
    def on_button1_clicked(self, widget):
        switch_to_watch_cursor()
        if confirmation == "True":
            global status
            status = button_one
            dialog = ConfirmAction(self)
            response = dialog.run()
            if response == Gtk.ResponseType.YES:
                run_command(button_one_command)
            switch_to_arrow_cursor()
            dialog.hide()
        elif confirmation == "False":
            run_command(button_one_command)

    def on_button2_clicked(self, widget):
        switch_to_watch_cursor()
        if confirmation == "True":
            global status
            status = button_two
            dialog = ConfirmAction(self)
            response = dialog.run()
            if response == Gtk.ResponseType.YES:
                run_command(button_two_command)
            switch_to_arrow_cursor()
            dialog.hide()
        elif confirmation == "False":
            run_command(button_two_command)

    def on_button3_clicked(self, widget):
        switch_to_watch_cursor()
        if confirmation == "True":
            global status
            status = button_three
            dialog = ConfirmAction(self)
            response = dialog.run()
            if response == Gtk.ResponseType.YES:
                run_command(button_three_command)
            switch_to_arrow_cursor()
            dialog.hide()
        elif confirmation == "False":
            run_command(button_three_command)

    def on_button4_clicked(self, widget):
        switch_to_watch_cursor()
        if confirmation == "True":
            global status
            status = button_four
            dialog = ConfirmAction(self)
            response = dialog.run()
            if response == Gtk.ResponseType.YES:
                run_command(button_four_command)
            switch_to_arrow_cursor()
            dialog.hide()
        elif confirmation == "False":
            run_command(button_four_command)
    
    def on_button5_clicked(self, widget):
        switch_to_watch_cursor()
        if confirmation == "True":
            global status
            status = button_five
            dialog = ConfirmAction(self)
            response = dialog.run()
            if response == Gtk.ResponseType.YES:
                run_command(button_five_command)
            switch_to_arrow_cursor()
            dialog.hide()
        elif confirmation == "False":
            run_command(button_five_command)
            
    # Key press function.
    def on_key_pressed(self, widget, event):
        pressed_key = Gdk.keyval_name(event.keyval)
        alt = (event.state & Gdk.ModifierType.MOD1_MASK)
        if pressed_key == "Escape":
            Gtk.main_quit()
        if enable_shortcuts == "True":
            if alt and pressed_key == "1":
                but1 = os.system(button_one_command)
            elif alt and pressed_key == "2":
                but2 = os.system(button_two_command)
            elif alt and pressed_key == "3":
                but3 = os.system(button_three_command)
            elif alt and pressed_key == "4":
                but4 = os.system(button_four_command)
            elif alt and pressed_key == "5":
                but5 = os.system(button_five_command)


if __name__ == "__main__":
    win = MainWindow()
    screen = win.get_screen()
    visual = screen.get_rgba_visual()
    win.set_visual(visual)
    win.connect("destroy", Gtk.main_quit)
    win.show_all()

    if fullscreen_mode == "True":
        win.fullscreen()
    Gtk.main()

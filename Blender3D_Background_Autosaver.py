import bpy
from datetime import datetime
import os

bl_info = {
    "name": "Auto Save with Timer",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "Window",
    "description": "Auto save every 30 minutes without freezing the UI",
    "warning": "",
    "wiki_url": "",
    "category": "System",
}

class AutoSaveOperator(bpy.types.Operator):
    """This operator auto saves the .blend file"""
    bl_idname = "wm.auto_save_operator"
    bl_label = "Auto Save Operator"

    _timer = None
    _cycles = 0

    def modal(self, context, event):
        if event.type == 'TIMER':
            self._cycles += 1
            if self._cycles > 60:  # 30 minutes
                filepath = bpy.data.filepath
                if filepath:  # Check if the file has been saved before
                    directory = os.path.dirname(filepath)
                else:  # If not, set a default directory
                    directory = "C:/temp"  # Replace this with your desired directory
                filename = bpy.path.basename(bpy.data.filepath) if filepath else "untitled"
                filename_without_extension = os.path.splitext(filename)[0]
                timestamp_str = datetime.now().strftime("%Y%m%d-%H%M%S")
                new_filename = "{}_{}.blend".format(filename_without_extension, timestamp_str)
                new_filepath = os.path.join(directory, new_filename)
                bpy.ops.wm.save_as_mainfile(filepath=new_filepath, copy=True)

                self._cycles = 0
        return {'PASS_THROUGH'}

    def execute(self, context):
        wm = context.window_manager
        self._timer = wm.event_timer_add(30.0, window=context.window)  # Set the timer to 30 seconds
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)


def register():
    bpy.utils.register_class(AutoSaveOperator)


def unregister():
    bpy.utils.unregister_class(AutoSaveOperator)


if __name__ == "__main__":
    register()

    # Test run
    bpy.ops.wm.auto_save_operator()

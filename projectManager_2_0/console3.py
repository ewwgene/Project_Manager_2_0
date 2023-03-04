...
import sys, os
import tempfile as tmpf
...
        else:

            #save a reference to the Python Console of QGIS before reassignment
            oldstdout = sys.stdout

            #creating a temporary file
            file = tmpf.NamedTemporaryFile(delete=False)

            file_name = file.name

            #reassigning the standard output to temporary file
            sys.stdout = file

            #printing to temporary file
            help(QgsVectorLayer.geometryType)

            #force the flush to temporary file
            sys.stdout.flush()

            file.close()

            #reassigning the standard output to the Python Console
            sys.stdout = oldstdout

            #opening temporary file
            tmp_file = open(file_name, 'r')

            data = tmp_file.read()

            #writing to QTextBrowser
            txtBox = self.dlg.textFeedback
            txtBox.setText(data)

            tmp_file.close()

            #erasing temporary file
            os.unlink(file.name)

    def run(self):
        """Run method that performs all the real work"""
...
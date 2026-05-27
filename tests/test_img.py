import os
from unittest import TestCase
from reptile.bands import Report, DataBand, DataSource, Text, Page, Band, Image, SizeMode
from reptile.exports import pdf


DIR_NAME: str = os.path.dirname(__file__)


class ImageTestCase(TestCase):
    def test_img(self):
        rep = Report()
        page: Page = rep.new_page()
        band = Band()
        page.add_band(band)
        with open(os.path.join(DIR_NAME, 'test_img.png'), 'rb') as f:
            img_buf = f.read()
        # normal size mode
        img = Image()
        img.size_mode = SizeMode.NORMAL
        img.left = 0
        img.top = 0
        img.height = 100
        img.width = 100
        img.picture = img_buf
        band.add_object(img)
        img = Image()
        img.size_mode = SizeMode.AUTO
        img.left = 0
        img.top = 150
        img.height = 100
        img.width = 100
        img.picture = img_buf
        band.add_object(img)
        img = Image()
        img.size_mode = SizeMode.CENTER
        img.left = 0
        img.top = 300
        img.height = 100
        img.width = 100
        img.picture = img_buf
        band.add_object(img)
        img = Image()
        img.size_mode = SizeMode.STRETCH
        img.left = 0
        img.top = 450
        img.height = 100
        img.width = 100
        img.picture = img_buf
        band.add_object(img)
        img = Image()
        img.size_mode = SizeMode.ZOOM
        img.left = 0
        img.top = 600
        img.height = 100
        img.width = 100
        img.picture = img_buf
        band.add_object(img)

        doc = rep.prepare()
        pdf.PDF(doc).export(os.path.join(DIR_NAME, 'reports', 'test_img.pdf'))

    def test_img_field(self):
        rep = Report()
        rep.variables['media_dir'] = DIR_NAME
        page: Page = rep.add_page()
        band = page.add_band(Band())
        ds = DataSource({'test_img': 'test_img.png'}, name='ds1')
        rep.register_datasource(ds)
        img = Image()
        img.left = 0
        img.top = 0
        img.width = 100
        img.height = 100
        img.field = 'test_img'
        img.datasource = ds
        band.add_object(img)
        doc = rep.prepare()
        pdf.PDF(doc).export(os.path.join(DIR_NAME, 'reports', 'test2.pdf'))

from reptile.runtime import PreparedPage
from reptile.bands import Page, GroupHeader, GroupFooter, DataBand
from reptile.bands.widgets import BandObject


class SubReport(BandObject):
    page_name: str = None
    _page = None
    _overlapped = False
    _x = _y = 0

    def __init__(self, page: Page = None):
        self.page = page

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value: Page):
        if self._page:
            self._page.subreport = None
        self._page = value
        if value:
            self.page_name = value.name
            value.subreport = self

    @property
    def bands(self):
        return self.report_page.bands

    @property
    def report_page(self) -> Page:
        if self._page:
            return self._page
        return self.report.pages.get(self.page_name)

    @report_page.setter
    def report_page(self, value: Page):
        self.page_name = value.name
        value.subreport = self

    def prepare(self, page: PreparedPage, context):
        # preserve original pos
        _x, _y = page.x, page.y
        try:
            page.x = self.left + _x + self.left
            page.y = self.top + _y + self.top
            for b in self.bands:
                b.prepare_objects(page, context)
        finally:
            page.x, page.y = _x, _y



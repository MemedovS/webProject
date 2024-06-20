import csv
from django.http import HttpResponse

from django.db.models.options import Options


class ExportAsCSVMixin:

    def export_csv(self, request, queryset):
        meta: Options = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv;charset=windows-1251')  # для руской кодировки
        response['Content-Disposition'] = 'attachment; filename={}-export.csv'.format(meta)
        data = csv.writer(response)
        data.writerow(field_names)
        for obj in queryset:
            data.writerow([getattr(obj, field) for field in field_names])
        return response

    export_csv.short_description = 'Export as CSV'

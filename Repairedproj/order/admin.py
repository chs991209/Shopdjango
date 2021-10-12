from django.contrib import admin
from django.db import transaction
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from django.template.response import TemplateResponse
from django.contrib.admin.models import LogEntry, CHANGE
from django.urls import path
from .models import Order
from django.utils.html import format_html


# Register your models here.


def refund(modeladmin, request, queryset):
    
    with transaction.atomic():

        qs = queryset.filter(~Q(status='환불'))
        ct = ContentType.objects.get_for_model(queryset.model)

        for obj in qs:
            obj.product.stock += obj.quantity
            obj.product.save()
        
            LogEntry.objects.log_action(
                user_id=request.user.id,
                content_type_id=ct.pk,
                object_id=obj.pk,
                object_repr='주문 환불',
                action_flag=CHANGE,
                change_message='주문 환불'
            )
        qs.update(status='환불')


refund.short_description = '환불'


class OrderAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('customer', 'product', 'styled_status')

    change_list_template = 'admin/order_change_list.html'

    change_form_template = 'admin/order_change_form.html'

    actions = [
        refund
    ]

    def action(self, obj):
        if obj.status != '환불':
            return format_html('<input type="button" value="환불"'
                               'onclick="order_refund_submit({obj.id}) class="btn btn-primary btn-sm>')

    def styled_status(self, obj):
        if obj.status == 'REFUNDED':
            return format_html(f'<b><span style="color:red">{obj.status}</b>')
        if obj.status == 'STANDBY':
            return format_html(f'<b><span style="color:blue">{obj.status}</b>')
        if obj.status == 'PAID':
            return format_html(f'<b><span style="color:green">{obj.status}</b>')
        if obj.status == 'PROCESSING':
            return format_html(f'<b><span style="color:brown">{obj.status}</b>') #f>>바로 입력

        return obj.status
    
    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'OrderList'}

        if request.method == 'POST':
            obj_id = request.POST.get('obj_id')
            if obj_id:
                qs = Order.objects.filter(pk=obj_id)
                ct = ContentType.objects.get_for_model(qs.model)
                for obj in qs:
                    obj.product.stock += obj.quantity
                    obj.product.save()

                    LogEntry.objects.log_action(
                        user_id=request.user.id,
                        content_type_id=ct.pk,
                        object_id=obj.pk,
                        object_repr='주문 환불',
                        action_flag=CHANGE,
                        change_message='주문 환불'
                    )
                qs.update(status='환불')

        return super().changelist_view(request, extra_context)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        order = Order.objects.get(pk=object_id)
        extra_context = { 'title': f"'{order.customer.email}'의 '{order.product.name}' 주문 수정하기'"}
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_and_continue'] = False
        return super().changeform_view(request, object_id, form_url, extra_context)

    def get_urls(self):
        urls = super().get_urls()
        date_urls = [
            path('date_view/', self.date_view)
        ]
        return date_urls + urls

    def date_view(self, request):
        context = dict(
            self.admin_site.each_context(request),
        )

        return TemplateResponse(request, 'admin/order_date_view.html', context)

    styled_status.short_description = 'STATUS'


admin.site.register(Order, OrderAdmin)
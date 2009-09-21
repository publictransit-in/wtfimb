from models import Stage
from django.contrib import admin
from routes.models import RouteStage

class RouteStageInline(admin.TabularInline):
    model = RouteStage 
    extra = 1 
    ordering = ['stage__display_name']

class StageAdmin(admin.ModelAdmin):
    list_display = ('display_name',
                    'view_stage_link',
                    'latitude', 
                    'longitude', 
                    )
    def view_stage_link(self, obj):
        return '<a href="/chennai/stage/%s">View</a>' % obj.id

    view_stage_link.allow_tags = True
    view_stage_link.short_description = "Link to Site"

    inlines = (RouteStageInline, )

    search_fields = ['display_name']

    def save_model(self, request, obj, form, change):
        obj.save(user=request.user)


admin.site.register(Stage, StageAdmin)
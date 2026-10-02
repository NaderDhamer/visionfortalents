from django.contrib import admin
from .models import WorkPackage, SABMember, ConsortiumPartner, TrainingProgram, ContactSubmission

@admin.register(WorkPackage)
class WorkPackageAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'coordinator')
    ordering = ('number',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'coordinator')


@admin.register(SABMember)
class SABMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'affiliation', 'order')
    ordering = ('order', 'name')
    search_fields = ('name', 'affiliation')


@admin.register(ConsortiumPartner)
class ConsortiumPartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'order')
    ordering = ('order', 'name')
    search_fields = ('name', 'country')



@admin.register(TrainingProgram)
class TrainingProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    ordering = ('-date',)
    search_fields = ('title',)    

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'created_at')
    ordering = ('-created_at',)
    search_fields = ('name', 'email', 'subject')
    readonly_fields = ('created_at',)
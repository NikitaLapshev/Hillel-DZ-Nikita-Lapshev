from django.contrib import admin
from core.models import Citizen,PublicService,ServiceUsage,Infrastructure,SocialProgram,ProgramEnrollment,GovEmployee

admin.site.register(Citizen)
admin.site.register(PublicService)
admin.site.register(ServiceUsage)
admin.site.register(Infrastructure)
admin.site.register(SocialProgram)
admin.site.register(ProgramEnrollment)
admin.site.register(GovEmployee)

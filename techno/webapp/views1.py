from django.http import JsonResponse
from .models import Tool


def get_tool_names(request):
    job_id = request.GET.get('job_id', None)
    if job_id:
        try:
            # Retrieve tool names for the given job_id
            tools = Tool.objects.filter(job_id=job_id)
            tool_names = [tool.tool_name for tool in tools]
            return JsonResponse({'tool_names': tool_names})
        except Tool.DoesNotExist:
            return JsonResponse({'error': 'Tools not found for the given job ID'})
    else:
        return JsonResponse({'error': 'Job ID not provided'})

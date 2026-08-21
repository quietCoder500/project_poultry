from django.shortcuts import render

from growth.generators import ALL_GENERATORS


def progress_report_view(request):
    return render(
        request, "growth/progress_report.html", context={"models": ALL_GENERATORS}
    )

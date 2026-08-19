from django.shortcuts import render

from growth.generators import ALL_GENERATORS


# Create your views here.


def progress_report_view(request):
    print(ALL_GENERATORS)
    return render(
        request, "growth/progress_report.html", context={"models": ALL_GENERATORS}
    )

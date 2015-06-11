from bs4 import beautifulsoup

activityServiceURI = "https://connect.garmin.com/proxy/activity-service-1.1/tcx/activity/{}?full=true"

# activityIds = $('.activityNameLink').map(function() {
#         return this.href.substr(this.href.lastIndexOf('/') + 1)
# });
# urls = activityIds.map(function() {
#         return activityServiceUrl + this + ".tcx";
# });

# urls.map(function() { downloadURI(this); } )


# function downloadURI(uri, name)
# {
#         var link = document.createElement("a");
#         link.download = name;
#         link.href = uri;
#         link.click();
# }

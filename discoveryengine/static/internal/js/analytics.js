/*******************
**** SETUP AJAX ****
*******************/
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            var csrftoken = Cookies.get('csrftoken');
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
/*******************
***** END SETUP ****
*******************/

/*******************
*** USER COUNTS ****
*******************/
function getUserCounts(startDate, endDate) {
    url = "/api/internal/analytics/count-users/";
    url += "?start_date="+startDate;
    url += "&end_date="+endDate;
    $.get(url, function(data, status, xhr) {
        if (status=="success") {
            buildUserChart(data);
        } else {
            console.log(status);
        }
    });
}

function buildUserChart(data) {
    // GENERATE CHART DATA
    var chartData = {
        x: 'Dates',
        axes: {
            Daily: 'y',
            Total: 'y2'
        },
        // types: {
        //     Daily: 'area',
        //     Total: 'area'
        // },
    };
    var axisData = {
        x: {
            type: 'timeseries',
            tick: {
                format: '%Y-%m-%d'
            }
        },
        y: {
            show: true,
            label: {
                text: 'Daily Sign Ups',
                position: 'outer-middle'
            }
        },
        y2: {
            show: true,
            label: {
                text: 'Total Users',
                position: 'outer-middle'
            }
        }
    };

    var dates = ['Dates'];
    var dalies = ['Daily'];
    var totals = ['Total'];
    for (var idx in data) {
        var datum = data[idx];
        var date = moment.unix(datum['timestamp']);
        dates.push(date.format('YYYY-MM-DD'));
        dalies.push(datum['daily_users']);
        totals.push(datum['total_users']);
    }
    chartData['columns'] = [
        dates,
        dalies,
        totals
    ];

    // BUILD ACTUAL CHART
    var userCountsChart = c3.generate({
        bindto: '#userCounts',
        data: chartData,
        axis: axisData,
    });
}

getUserCounts(moment().subtract(30, 'days').unix(), moment().unix());

function getTodayUserCounts() {
    url = "/api/internal/analytics/count-users/";
    $.get(url, function(data, status, xhr) {
        if (status=="success") {
            parseTodayUserCounts(data);
        } else {
            console.log(status);
        }
    });}

function parseTodayUserCounts(data) {
    var daily = data[0]['daily_users'];
    var total = data[0]['total_users'];
    $('#today-signUps').text(daily);
    $('#today-totalUsers').text(total);
}

getTodayUserCounts();

/*******************
** END USER COUNTS *
*******************/
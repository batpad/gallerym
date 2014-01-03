function getTileLayer(zoomable) {
    //console.log(zoomable);
    return L.tileLayer(zoomable.tms_url, {
        minZoom: 2,
        maxZoom: 6,
        continuousWorld: true,
        noWrap: true,
        attribution: 'gdal2tiles and coffee :-)',
        tms: true                
    })
}


var map = L.map('map').setView(getCenter(ZOOMABLES[0]), 2);
var activeLayer = getTileLayer(ZOOMABLES[0]);
activeLayer.addTo(map);

function getCenter(zoomable) {
    var width = zoomable.width;
    var height = zoomable.height;
    if (width > height) {
        return [-75, -100];
    } else {
        return [-50, -100];
    }
}

$(function() {
    $('.thumbLi').click(function() {
        $('.currentZoomThumb').removeClass('currentZoomThumb');
        $(this).addClass("currentZoomThumb");
        var index = $(this).index();
        map.removeLayer(activeLayer);
        activeLayer = getTileLayer(ZOOMABLES[index]);
        activeLayer.addTo(map);
        var center = getCenter(ZOOMABLES[index]);
        map.setView(center, 2);
    });
});

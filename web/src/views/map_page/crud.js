import L from 'leaflet';


export default {
  methods: {
    initMap() {
      // 初始化地图
      this.map = L.map('map').setView([51.505, -0.09], 13);

      // 添加图层
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
      }).addTo(this.map);
      

      // 添加标记点
      L.marker([51.5, -0.09]).addTo(this.map)
        .bindPopup('A UAV is here!');

      // 添加图形
      const latlngs = [
        [51.5, -0.09],
        [51.51, -0.1],
        [51.52, -0.08]
      ];
      const polygon = L.polygon(latlngs, {color: 'red'}).addTo(this.map);
      polygon.bindPopup('Mission Area');

      // 添加交互
      this.map.on('click', function(e) {
        alert("You clicked the map at " + e.latlng);
      });
    },
    updateMarkerPosition(lat, lng) {
      // 更新标记点位置信息
      const newLatLng = new L.LatLng(lat, lng);
      this.marker.setLatLng(newLatLng);
    }
  },
  mounted() {
    // 初始化地图
    this.initMap();
  }
}

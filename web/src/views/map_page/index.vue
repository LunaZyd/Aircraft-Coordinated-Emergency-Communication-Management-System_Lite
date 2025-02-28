
<template>
  <div class="command-center">
    
    <div class="myMap" id="myMap"></div>
    <div class="option-div">
      <el-row :gutter="20"     justify="space-around"  class="btn-row">
        <el-col :span="24">
          <el-button type="primary" icon="el-icon-map-location" @click="showMarkers">显示标记</el-button>
          <el-button type="primary" icon="el-icon-view" @click="hideMarkers">隐藏标记</el-button>
          <el-button type="primary" icon="el-icon-picture" @click="handlerPaint">画笔</el-button>
          <el-button type="primary" icon="el-icon-delete" @click="handler.clear()">清空画布</el-button>
          <el-button type="primary" icon="el-icon-edit-outline" @click="startCustomMarkerMode">开始标记</el-button>
          <el-button type="primary" icon="el-icon-circle-check" @click="stopCustomMarkerMode">停止标记</el-button>
          <el-button type="primary" icon="el-icon-check" @click="setBounds">设置边界</el-button>
          <el-button type="primary" icon="el-icon-refresh" @click="resetMaxBounds">重置边界</el-button>
          <el-button type="primary" size="small"  @click="drawLineBetweenPoints">绘制路线</el-button>
          <el-button type="primary" style="margin-top: 10px;" size="small" @click="removeDrawnLine">清除路线</el-button>
        </el-col>
      </el-row>
      <el-table :data="points" style="width: 100%" >
        <el-table-column prop="lng" label="经度"></el-table-column>
        <el-table-column prop="lat" label="纬度"></el-table-column>
        <el-table-column label="操作">
          <template v-slot="scope">
            <el-button size="mini" @click="deleteMarker(scope.row.id)">删除</el-button>
            <el-button size="mini" @click="addMapClick(1, scope.row.id)">起始点</el-button>
            <el-button size="mini" @click="addMapClick(3, scope.row.id)">途径</el-button>
            <el-button size="mini" @click="addMapClick(2, scope.row.id)">目的地</el-button>

          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>



<script>
const TITANITE_API_KEY = 'e453f5c7e906439cedc1ae8495cfa531';
import { ref, onMounted } from 'vue'
import { response } from "@/api/tools";
import { AddObj, GetList, UpdateObj,DelObj } from "../satellite/api"; // 查询添加修改删除的http请求接口
export default {
  name: 'MapPage',
  data() {
    return {
      drawnLines: [], // 存储所有绘制的直线
      boundsValue: '', // 添加这行来定义 boundsValue
      points: [], // 存储标记点的经纬度和ID
      markersVisible: false, // 表示标记是否已经展示
      customMarkerMode: false ,// 表示是否开启自定义标记模式
      markerRefs: {}, // 存储标记对象的引用
      defaultBounds: [123.44719, 41.97034, 123.34685, 41.8725], // 预定义的边界值
      midLngLat: null,  // 用于存储中间点的经纬度


      drawnLine: null, // 用于保存直线的引用
      mapClickEnabled: false, // 控制地图点击事件监听器是否激活
      mapClickHandler: null, // 存储地图点击事件处理函数的引用
      // control: null,
      // handler: null,
      isPaint: false,
      startIcon: "http://lbs.tianditu.gov.cn/images/bus/start.png",	//起点图标
      endIcon: "http://lbs.tianditu.gov.cn/images/bus/end.png",		//终点图标
      actionMarker: 0, // 标注操作 0-普通标注 1-起点 2-终点
      drivingRoute: null,
      startLngLat: '', // 起点
      startLngLatArr: [], // 起点数组
      endLngLat: '', // 终点
      lineColors: ["#2dcbf3", "#dd3efa", "#27ea46", "#f6351b"],
      currentColor: -1,
      // markerTool: null, // 标注工具对象
      // handlerMarkerTool: null,
    };
  },
  mounted() {
    this.loadTiandituMap().then(() => {
    this.initMapEvent(); // 初始化地图事件
    });
  },
  methods: {
    loadTiandituMap() {
      return new Promise((resolve, reject) => {
      // 检查是否已经加载了天地图API
      if (typeof window.T === 'undefined') {
        const script = document.createElement('script');
        script.src = `http://api.tianditu.gov.cn/api?v=4.0&tk=${TITANITE_API_KEY}`;
        script.onload = () => {
          this.initMap(); // 确保在加载完成后初始化地图
          resolve(); // 加载和初始化完成后解析Promise
        }
        document.head.appendChild(script);
      } else {
        this.initMap(); // 如果已加载，直接初始化地图
        resolve();
      }
    });
    },
    
    deleteMarker(markerId) {
  DelObj(markerId).then(response => {
    if (response.code === 2000) {
      // 删除成功，执行相应操作，例如移除地图上的标记
      this.points = this.points.filter(point => point.id !== markerId);

      // 如果地图上有对应的标记，则移除它
      if (this.markerRefs[markerId]) {
        this.map.removeOverLay(this.markerRefs[markerId]); // 从地图上移除标记
        delete this.markerRefs[markerId]; // 从引用存储中删除标记的引用
      }

      alert("删除成功");
    } else if (response.data) {
      // 删除失败，显示错误信息
      alert("删除失败：" + response.data.message);
    }
  }).catch(error => {
    console.error('删除数据失败：', error);
    alert("删除数据失败：" + error.message);
  });
}, 


    setBounds() {
      // var bounds = document.getElementById("bounds").value.split(",");
      this.map.setMaxBounds(new T.LngLatBounds(
      new T.LngLat(this.defaultBounds[0], this.defaultBounds[1]),
      new T.LngLat(this.defaultBounds[2], this.defaultBounds[3])
    ));
    },
    resetMaxBounds() {
      // 清除地图拖动范围限制
      if (this.map) {
        this.map.setMaxBounds(null);
      }
    },

    //初始化地图
    initMap() {
      // 确保T对象可用
      if (typeof window.T !== 'undefined') {
    // 地图初始化代码
    this.map = new window.T.Map('myMap');
    // 设置显示地图的中心点和级别
    this.map.centerAndZoom(new window.T.LngLat(123.39852, 41.92447), 16);
    // 创建地图类型控件对象
    var mapTypeControl = new window.T.Control.MapType();

    // 将地图类型控件添加到地图上
    this.map.addControl(mapTypeControl);
      this.polygonTool = new T.PolygonTool(this.map);
    
    this.addPolygons(); // 添加多边形到地图上

     // 画笔工具
     this.isPaint = false
      this.handler = new window.T.PaintBrushTool(this.map, {
        keepdrawing: true,
        style: {
          weight: 3
        }
      })

      //创建\添加缩放平移控件, 设置控件位置
      this.control = new window.T.Control.Zoom()
      this.map.addControl(this.control)
      //创建\添加比例尺控件
      let scale = new window.T.Control.Scale()
      this.map.addControl(scale)
    }
  },

// 添加到 methods 中
addMapClick(actionMarker, pointId) {
  // 从 points 数组中查找对应的点
  const point = this.points.find(p => p.id === pointId);
  if (!point) {
    console.error('未找到点的信息');
    return;
  }

  // 根据 actionMarker 的值设置起始点或目的地
  if (actionMarker === 1) {
    // 设置起始点
    this.startLngLat = new window.T.LngLat(point.lng, point.lat);
  } else if (actionMarker === 2) {
    // 设置目的地
    this.endLngLat = new window.T.LngLat(point.lng, point.lat);
  }

  // 新增的部分
  else if (actionMarker === 3) {
    // 设置中间点
    this.midLngLat = new window.T.LngLat(point.lng, point.lat);
  }
},
     MapClick(e) {
      if (!this.mapClickEnabled|| !this.currentPoint) return;
       // 使用保存的点坐标添加标记
        const lnglat = new window.T.LngLat(this.currentPoint.lng, this.currentPoint.lat);
         this.addLocalMarker(e, lnglat, this.actionMarker);

       // this.addLocalMarker(e, new window.T.LngLat(e.lnglat.getLng(), e.lnglat.getLat()), this.actionMarker)

       switch (this.actionMarker) {
         case 0:
           this.startLngLat = ''
           this.endLngLat = ''
           break;
         case 1:
           this.startLngLat = new window.T.LngLat(e.lnglat.getLng(), e.lnglat.getLat())
           this.startLngLatArr.push(this.startLngLat)
           // this.removeMapClick()
           break;
         case 2:
           this.endLngLat = new window.T.LngLat(e.lnglat.getLng(), e.lnglat.getLat())
           this.removeMapClick()
           break;
     }
    },



  drawLine(path) {
    // 创建折线对象
    const polyline = new window.T.Polyline(path, {
      color: "red", // 线颜色
      weight: 3, // 线宽
      opacity: 0.5, // 透明度
    });

    // 将折线添加到地图上
    this.map.addOverLay(polyline);
    return polyline;
  },
//画一条直线
drawLineBetweenPoints() {
    if (!this.startLngLat || !this.endLngLat) {
      alert('起始点或目的地未设置');
      return;
    }

      // 新增的部分：确保中间点已设置
  if (!this.midLngLat) {
    alert('中间点未设置');
    return;
  }

  // 创建包含起点、中间点、终点的路径
  const path = [this.startLngLat, this.midLngLat, this.endLngLat];



    // 创建两点之间的直线路径
    // const path = [this.startLngLat, this.endLngLat];

    // 创建折线对象
    // 确保在使用 polyline 变量之前，已经正确创建了这个变量
    const polyline = new window.T.Polyline(path, {
      color: "red", // 线颜色
      weight: 3, // 线宽
      opacity: 0.5, // 透明度
    });

    // 将折线添加到地图上
    this.map.addOverLay(polyline);

    // 假设 polyline 是你创建的直线对象
    this.drawnLine = polyline; // 保存直线引用
  },


removeDrawnLine() {
  if (this.drawnLine) {
    this.map.removeOverLay(this.drawnLine); // 移除直线
    this.drawnLine = null; // 清除引用
  }
},
 
   // 画笔功能开启关闭
   handlerPaint () {
      this.isPaint = !this.isPaint
      if(this.isPaint) {
        this.handler.open()
      }else {
        this.handler.close()
      }
    },
    //标注工具
    getOverlays () {
      alert(this.map.getOverlays().length)

    },
    initMapEvent() {
    // 绑定MapClick函数到地图点击事件
    this.mapClickHandler = (e) => this.MapClick(e);
    this.map.on('click', this.mapClickHandler);
  },
  // 在组件销毁前移除事件
  beforeDestroy() {
    this.map.off('click', this.mapClickHandler); // 移除地图点击事件监听器
  },
     // 多边形绘制工具
  addPolygons() {
    const polygonsData = [
      {
        id: 'polygon1',
        vertices: [{ lat: 41.91909, lng: 123.40998}, { lat: 41.9152, lng: 123.40932}, { lat: 41.91469, lng: 123.41457}, { lat: 41.91864, lng: 123.41526 }]
      },
      {
        id:'polygon12',
        vertices:[{lng:123.40007	,lat:41.92327	},{  lng: 123.40005,lat:	41.92228	},{lng:123.40054,lat:	41.92233},{lng:123.40118,lat:41.92227	},{lng:123.40178,lat:41.92236},
        {lng:123.4024,lat:	41.92261},{lng:123.40266,lat:41.92295},{lng:123.40276,lat:	41.92332}]
      }
      // 可以继续添加更多多边形数据
    ];
    polygonsData.forEach(polygonData => {
      const vertices = polygonData.vertices.map(vertex => new window.T.LngLat(vertex.lng, vertex.lat));
      const polygon = new window.T.Polygon(vertices, {
        color: "blue", // 边线颜色
        weight: 3, // 线宽
        opacity: 0.5, // 边线透明度
        fillColor: "#FFFFFF", // 填充颜色
        fillOpacity: 0.5 // 填充透明度
      });
      this.map.addOverLay(polygon);
    });

  },
  //显示标记
  showMarkers() {
      GetList().then(res => {
      if (res.code === 2000) {
      // 清空当前地图上的所有标记
      // if (this.map) {
      //   this.map.clearOverLays();
      // }
      // 清空之前保存的点
      this.points = [];
      const satelliteInfo = res.data.data;
      // 遍历数据，为每个数据点创建并添加标记
      satelliteInfo.forEach(info => {
        const point = { lat: info.latitude, lng: info.longitude, id: info.id };
        this.points.push(point); // 保存点到本地状态，以便显示在表格中
        this.addMarkerToMap(point.lng, point.lat,point.id); // 调用方法添加标记
      });
      this.markersVisible = true; // 标记已加载
    }
  }).catch(error => {
    console.error('获取数据失败：', error);
  });
  this.addPolygons(); // 添加多边形到地图上

},
    //开启自定义标记模式
    startCustomMarkerMode() {
      if (this.markersVisible) {
        if (!this.customMarkerMode) {
          this.customMarkerMode = true; // 开启自定义标记模式
          this.map.addEventListener('click', this.handleMapClick); // 添加地图点击事件监听器
        } else {
          console.log('自定义标记模式已经开启');
        }
      }else{
            // 如果标记未展示，弹出提示对话框
            alert('请先展示标记，然后再添加新的标记。');
      }
    },
    //添加标记到地图上
    addMarkerToMap(lng, lat,id) {

      const marker = new window.T.Marker(new window.T.LngLat(lng, lat)); // 创建标记

      this.map.addOverLay(marker); // 将标记添加到地图上
      this.markerRefs[id] = marker; // 保存标记对象的引用，使用标记的ID作为键

      // 添加标记的点击事件，弹出坐标信息
      marker.addEventListener('click', () => {
        alert(`经度：${lng}，纬度：${lat}`);
      });
    },
    //隐藏标记
    hideMarkers() {
    if (this.map && this.markersVisible) {
      this.map.clearOverLays(); // 假设这个方法可以清除地图上的所有标记
      this.markersVisible = false; // 更新状态为未显示
      this.customMarkerMode = false; // 也关闭自定义标记模式
      // 如果需要，可以清空本地保存的标记点信息
      this.points = [];
    } else {
      console.log('标记已经是隐藏状态');
    }
  },
  //停止自定义标记
  stopCustomMarkerMode() {
      this.customMarkerMode = false; // 关闭自定义标记模式
      this.map.removeEventListener('click', this.handleMapClick); // 移除地图点击事件
    },
    //操作地图点击事件
  handleMapClick(event) {
  const { lng, lat } = event.lnglat; // 获取点击位置的经纬度
  const point = { lng, lat };
  this.points.push(point); // 将新的经纬度点添加到数组中

  // 创建并添加新的标记
  const marker = new window.T.Marker(new window.T.LngLat(lng, lat));

  this.map.addOverLay(marker);

  // 添加标记的点击事件，弹出坐标信息
  marker.addEventListener('click', () => {
    alert(`经度：${lng}，纬度：${lat}`);
  });

  // 调用后端接口保存新标记点数据
  const row = {
    "longitude": lng,
    "latitude": lat,
    "message_content": "位置点",
    "signal_strength": 3,
    "device_id": "sel",
    "communication_channel": "12",
    "description": "自动"
  };
  AddObj(row).then(res => {
    if (res.code === 2000) {
      console.log('标记保存成功');
    }
  }).catch(error => {
    console.error('保存标记失败：', error);
  });
},

  },

};    
</script>

<style scoped>
.command-center {
  position: relative;
  width: 100%;
  height: 100%; /* 使用视口高度确保填充整个屏幕 */
  display: flex;
  flex-direction: column; /* 垂直排列 */
}

.option-div {
  position: absolute; /* 设置为绝对定位 */
  top: 10px; /* 距离地图顶部10像素 */
  left: 60px; /* 距离地图左侧10像素 */
  z-index: 1000; /* z-index设置得比地图的z-index高，确保浮动在地图之上 */
  background-color: rgba(255, 255, 255, 0.8); /* 背景色设置为半透明白色 */
  padding: 10px; /* 内边距 */
  border-radius: 5px; /* 边框圆角 */
  box-shadow: 0 2px 4px rgba(0,0,0,0.2); /* 设置阴影效果 */
  width: auto; /* 宽度根据内容自动调整 */
  max-width: 87%; /*87%; 最大宽度限制，避免占满整个地图 */
  box-sizing: border-box; /* 盒子模型设置，防止边框和内边距影响宽度 */
}
.myMap {
  flex-grow: 1; /* 填充剩余空间 */
  height: 100vh; /* 防止直接设置高度，而是通过flex-grow来填充 */
  position: relative;
}
</style>
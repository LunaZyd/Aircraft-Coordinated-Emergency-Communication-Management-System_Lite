import { request, downloadFile } from '@/api/service';

// 设置后端接口地址前缀
const urlPrefix = '/api/map-app/';

// 获取地图数据列表
export function GetMapDataList(query) {
  return request({
    url: `${urlPrefix}map-data/`,
    method: 'get',
    params: query
  });
}

// 添加地图数据
export function AddMapData(data) {
  return request({
    url: `${urlPrefix}map-data/`,
    method: 'post',
    data
  });
}

// 更新地图数据
export function UpdateMapData(id, data) {
  return request({
    url: `${urlPrefix}map-data/${id}/`,
    method: 'put',
    data
  });
}

// 删除地图数据
export function DeleteMapData(id) {
  return request({
    url: `${urlPrefix}map-data/${id}/`,
    method: 'delete'
  });
}

// 导出地图数据
export function ExportMapData(params) {
  return downloadFile({
    url: `${urlPrefix}map-data/export/`,
    params,
    method: 'get'
  });
}
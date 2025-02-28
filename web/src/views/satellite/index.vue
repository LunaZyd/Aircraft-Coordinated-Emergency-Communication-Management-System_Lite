<template>
  <d2-container :class="{ 'page-compact': crud.pageOptions.compact }">
    <d2-crud-x ref="d2Crud" v-bind="_crudProps" v-on="_crudListeners">
      <div slot="header">
        <crud-search
          ref="search"
          :options="crud.searchOptions"
          @submit="handleSearch"
        />
        <el-button-group>
          <el-button size="small" type="primary" @click="addRow"
            ><i class="el-icon-plus" /> 新增</el-button
          >
        </el-button-group>
        <el-button
            size="small"
            type="warning"
            @click="onExport"
            ><i class="el-icon-download" /> 导出
          </el-button>
        <crud-toolbar
          v-bind="_crudToolbarProps"
          v-on="_crudToolbarListeners"
          @columns-filter-changed="handleColumnsFilterChanged"
          :columns="crud.columns"
          :compact.sync="crud.pageOptions.compact"
          :search.sync="crud.searchOptions.show"
        />
      </div>
    </d2-crud-x>
  </d2-container>
</template>

<script>
import { satelliteCrudOptions } from "./crud"; // 上文的 satelliteCrudOptions 配置
import { d2CrudPlus } from "d2-crud-plus";
import * as api from './api'

export default {
  name: "satellite_data",
  mixins: [d2CrudPlus.crud],
  methods: {
    getCrudOptions() {
      return satelliteCrudOptions(this);
    },
    pageRequest(query) {
      return api.GetList(query);
    },
    addRequest(row) {
      return api.AddObj(row);
    },
    updateRequest(row) {
      return api.UpdateObj(row);
    },
    delRequest(row) {
      return api.DelObj(row.id);
    },
    onExport() {
      const that = this;
      this.$confirm('是否确认导出所有数据项?', '警告', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(function () {
        const query = that.getSearch().getForm();
        return api.exportData({ ...query });
      });
    },
  },
};
</script>

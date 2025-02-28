export const satelliteCrudOptions = vm => {
  return {
    pageOptions: {
      compact: true
    },
    options: {
      tableType: 'vxe-table',
      stripe: false,
      rowKey: true,
      rowId: 'id',
      height: '100%',
      highlightCurrentRow: false,
      defaultExpandAll: true,
      resizable: true,
    },
    rowHandle: {
      width: 140,
      edit: {
        thin: true,
        text: "编辑",
        disabled() {
          return !vm.hasPermissions("Update");
        }
      },
      remove: {
        thin: true,
        text: "删除",
        disabled() {
          return !vm.hasPermissions("Delete");
        }
      }
    },
    indexRow: {
      title: "序号",
      align: "center",
      width: 100
    },
    viewOptions: {
      componentType: "form"
    },
    formOptions: {
      defaultSpan: 10,
      width: "65%"
    },
    columns: [ 
          {
          title: "ID",
          key: "id",
          show: false,
          disabled: true,
          form: {
            disabled: true
          }
        },
        {
        title: "经度",
        key: "longitude",
        sortable: true,
        search: {
          component: {
            props: {
              clearable: true
            }
          }
        },
        type: "number",
        form: {
          rules: [{
            required: true,
            message: "经度必填"
          }],
          component: {
            span: 12,
            props: {
              clearable: true
            },
            placeholder: "请输入经度"
          }
        }
      },
      {
        title: "纬度",
        key: "latitude",
        sortable: true,
        search: {
          component: {
            props: {
              clearable: true
            }
          }
        },
        type: "number",
        form: {
          rules: [{
            required: true,
            message: "纬度必填"
          }],
          component: {
            span: 12,
            props: {
              clearable: true
            },
            placeholder: "请输入纬度"
          }
        }
  },

          {
          title: "消息内容",
          key: "message_content",
          sortable: true,
          search: {
            component: {
              props: {
                clearable: true
              }
            }
          },
        type: "input",
        form: {
          rules: [{
            required: true,
            message: "消息内容必填"
          }],
          component: {
            props: {
              clearable: true
            },
            placeholder: "请输入消息内容"
          }
        }
      },
      {
        title: "信号强度",
        key: "signal_strength",
        sortable: true,
        search: {
          component: {
            props: {
              clearable: true
            }
          }
        },
        type: "number",
        form: {
          rules: [{
            required: false,
            message: "信号强度"
          }],
          component: {
            props: {
              clearable: true
            },
            placeholder: "请输入信号强度"
          }
        }
      },
      {
        title: "设备ID",
        key: "device_id",
        sortable: true,
        search: {
          component: {
            props: {
              clearable: true
            }
          }
        },
        type: "input",
        form: {
          rules: [{
            required: true,
            message: "设备ID必填"
          }],
          component: {
            props: {
              clearable: true
            },
            placeholder: "请输入设备ID"
          }
        }
      },
      {
        title: "通信信道",
        key: "communication_channel",
        sortable: true,
        search: {
          component: {
            props: {
              clearable: true
            }
          }
        },
        type: "input",
        form: {
          rules: [{
            required: false,
            message: "通信信道"
          }],
          component: {
            props: {
              clearable: true
            },
            placeholder: "请输入通信信道"
          }
        }
      }
    ].concat(vm.commonEndColumns())
  };
};

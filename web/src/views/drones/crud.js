export const crudOptions = vm => {
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
      view: {
        thin: true,
        text: "",
        disabled() {
          return !vm.hasPermissions("Retrieve");
        }
      },
      edit: {
        thin: true,
        text: "",
        disabled() {
          return !vm.hasPermissions("Update");
        }
      },
      remove: {
        thin: true,
        text: "",
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
        title: "名称",
        key: "name",
        sortable: true,
        search: {
          component: {
            props: {
              clearable: true
            }
          }
        },
        type: "input",
        align: "center",
        form: {
          editDisabled: false,
          rules: [
            {
              required: true,
              message: "名称必填"
            }
          ],
          component: {
            span: 12,
            props: {
              clearable: true
            },
            placeholder: "请输入名称"
          },
          itemProps: {
            class: {
              yxtInput: true
            }
          }
        }
      },
      {
        title: "注册号",
        key: "registration_number",
        sortable: true,
        search: {
          component: {
            props: {
              clearable: true
            }
          }
        },
        type: "input",
        align: "center",
        form: {
          editDisabled: false,
          rules: [
            {
              required: true,
              message: "注册号必填"
            }
          ],
          component: {
            span: 12,
            props: {
              clearable: true
            },
            placeholder: "请输入注册号"
          },
          itemProps: {
            class: {
              yxtInput: true
            }
          }
        }
      },
      {
        title: "生产厂家",
        key: "manufacturer",
        sortable: true,
        search: {
          component: {
            props: {
              clearable: true
            }
          }
        },
        type: "input",
        align: "center",
        form: {
          editDisabled: false,
          rules: [
            {
              required: true,
              message: "生产厂家必填"
            }
          ],
          component: {
            span: 12,
            props: {
              clearable: true
            },
            placeholder: "请输入生产厂家"
          },
          itemProps: {
            class: {
              yxtInput: true
            }
          }
        }
      },
      {
        title: "型号",
        key: "model",
        sortable: true,
        search: {
          component: {
            props: {
              clearable: true
            }
          }
        },
        type: "input",
        align: "center",
        form: {
          editDisabled: false,
          rules: [
            {
              required: true,
              message: "型号必填"
            }
          ],
          component: {
            span: 12,
            props: {
              clearable: true
            },
            placeholder: "请输入型号"
          },
          itemProps: {
            class: {
              yxtInput: true
            }
          }
        }
      },
      {
        title: "最大飞行高度（米）",
        key: "max_flight_altitude",
        sortable: true,
        search: {
          component: {
            props: {
              clearable: true
            }
          }
        },
        type: "number",
        align: "center",
        form: {
          editDisabled: false,
          rules: [
            {
              required: true,
              message: "最大飞行高度必填"
            }
          ],
          component: {
            span: 12,
            props: {
              clearable: true
            },
            placeholder: "请输入最大飞行高度（米）"
          },
          itemProps: {
            class: {
              yxtInput: true
            }
          }
        }
      },
      {
        title: "最大飞行速度（m/s）",
        key: "max_flight_speed",
        sortable: true,
        search: {
          component: {
            props: {
              clearable: true
            }
          }
        },
        type: "number",
        align: "center",
        form: {
          editDisabled: false,
          rules: [
            {
              required: true,
              message: "最大飞行速度必填"
            }
          ],
          component: {
            span: 12,
            props: {
              clearable: true
            },
            placeholder: "请输入最大飞行速度（m/s）"
          },
          itemProps: {
            class: {
              yxtInput: true
            }
          }
        }
      },
      {
        title: "最大飞行时间（分钟）",
        key: "max_flight_time",
        sortable: true,
        search: {
          component: {
            props: {
              clearable: true
            }
          }
        },
        type: "number",
        align: "center",
        form: {
          editDisabled: false,
          rules: [
            {
              required: true,
              message: "最大飞行时间必填"
            }
          ],
          component: {
            span: 12,
            props: {
              clearable: true
            },
            placeholder: "请输入最大飞行时间"
          },
          itemProps: {
            class: {
              yxtInput: true
            }
          }
        }
      },
      {
        title: "航程范围（公里）",
        key: "range",
        sortable: true,
        search: {
          component: {
            props: {
              clearable: true
            }
          }
        },
        type: "number",
        align: "center",
        form: {
          editDisabled: false,
          rules: [
            {
              required: true,
              message: "航程范围必填"
            }
          ],
          component: {
            span: 12,
            props: {
              clearable: true
            },
            placeholder: "请输入航程范围"
          },
          itemProps: {
            class: {
              yxtInput: true
            }
          }
        }
      },
      {
        title: "最大起飞重量",
        key: "max_takeoff_weight",
        sortable: true,
        search: {
          component: {
            props: {
              clearable: true
            }
          }
        },
        type: "number",
        align: "center",
        form: {
          editDisabled: false,
          rules: [
            {
              required: true,
              message: "最大起飞重量必填"
            }
          ],
          component: {
            span: 12,
            props: {
              clearable: true
            },
            placeholder: "请输入最大起飞重量"
          },
          itemProps: {
            class: {
              yxtInput: true
            }
          }
        }
      },
      {
        title: "负载能力",
        key: "payload_capacity",
        sortable: true,
        search: {
          component: {
            props: {
              clearable: true
            }
          }
        },
        type: "number",
        align: "center",
        form: {
          editDisabled: false,
          rules: [
            {
              required: true,
              message: "负载能力必填"
            }
          ],
          component: {
            span: 12,
            props: {
              clearable: true
            },
            placeholder: "请输入负载能力"
          },
          itemProps: {
            class: {
              yxtInput: true
            }
          }
        }
      },
      {
        title: "电池类型（毫安）",
        key: "battery_type",
        sortable: true,
        search: {
          component: {
            props: {
              clearable: true
            }
          }
        },
        type: "input",
        align: "center",
        form: {
          editDisabled: false,
          rules: [
            {
              required: true,
              message: "电池类型必填"
            }
          ],
          component: {
            span: 12,
            props: {
              clearable: true
            },
            placeholder: "请输入电池类型"
          },
          itemProps: {
            class: {
              yxtInput: true
            }
          }
        }
      },
      {
        title: "GPS系统",
        key: "gps_system",
        sortable: true,
        search: {
          component: {
            props: {
              clearable: true
            }
          }
        },
        type: "input",
        align: "center",
        form: {
          editDisabled: false,
          rules: [
            {
              required: true,
              message: "GPS系统必填"
            }
          ],
          component: {
            span: 12,
            props: {
              clearable: true
            },
            placeholder: "请输入GPS系统"
          },
          itemProps: {
            class: {
              yxtInput: true
            }
          }
        }
      },
      {
        title: "通信设备",
        key: "communication_device",
        sortable: true,
        search: {
          component: {
            props: {
              clearable: true
            }
          }
        },
        type: "input",
        align: "center",
        form: {
          editDisabled: false,
          rules: [
            {
              required: true,
              message: "通信设备必填"
            }
          ],
          component: {
            span: 12,
            props: {
              clearable: true
            },
            placeholder: "请输入通信设备"
          },
          itemProps: {
            class: {
              yxtInput: true
            }
          }
        }
      }
    ].concat(vm.commonEndColumns())
  };
};

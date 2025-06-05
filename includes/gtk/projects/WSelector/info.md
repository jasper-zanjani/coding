[WSelector](https://github.com/Cookiiieee/WSelector) disposes of UI definition files and is built entirely in code (1).
{: .annotate }

1.  
    
    ```blueprint title="Draft UI layout for Gradia"
    ApplicationWindow {
      title: "WSelector";
      default-width: 800;
      default-height: 650;

      Adw.ToastOverlay {

        [titlebar]
        HeaderBar {
          show-title-buttons: true; // ?
        }

        Box main_box {
          orientation: vertical;
        }

        ScrolledWindow scroll {
          hexpand: true;
          vexpand: true;

          Overlay overlay {
            FlowBox flowbox {
              valign: start;
              homogeneous: true;
              selection-mode: none;
              column-spacing: 12;
              row-spacing: 12;
              margin-top: 12;
              margin-bottom: 12;
              margin-start: 12;
              margin-end: 12;
              hexpand: true;
              vexpand: true;
            }
          }
        }
        
      }
    }
    ```

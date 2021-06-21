import React, { Component } from "react";
import DragAndDrop from "./DragAndDrop";
class FileList extends Component {
  constructor() {
    super();
    this.state = {
      fileSelected: null,
    };
  }

  handleDrop = (files) => {
    this.setState({
      fileSelected: files[0],
    });
  };

  render() {
    return (
      <DragAndDrop handleDrop={this.handleDrop}>
        <div style={{ height: 300, width: 250 }}></div>
      </DragAndDrop>
    );
  }
}
export default FileList;

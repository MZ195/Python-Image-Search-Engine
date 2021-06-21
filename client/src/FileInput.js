import React, { Component } from "react";
import axios from "axios";

class FileInput extends Component {
  constructor() {
    super();
    this.state = {
      fileSelected: null,
      images: [],
    };
  }
  render() {
    const fileUploadHandler = () => {
      const fd = new FormData();
      fd.append("image", this.state.fileSelected, this.state.fileSelected.name);

      axios.post("http://127.0.0.1:7070/upload/", fd).then((res) => {
        this.setState({
          images: res.data.result,
        });
      });
    };

    const fileSelectHandler = (event) => {
      this.setState({
        fileSelected: event.target.files[0],
      });
    };

    const newData = this.state.images.map((data, index) => (
      <div key={index}>
        <img alt="" src={}></img>
      </div>
    ));

    return (
      <div className="div">
        <input type="file" onChange={fileSelectHandler} />
        <button onClick={fileUploadHandler}>upload</button>
        {newData}
      </div>
    );
  }
}

export default FileInput;

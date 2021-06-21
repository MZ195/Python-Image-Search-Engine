import React, { Component } from "react";
import axios from "axios";

class FileInput extends Component {
  constructor() {
    super();
    this.state = {
      fileSelected: null,
      images: [],
      isLoading: false,
    };
  }
  render() {
    const fileUploadHandler = () => {
      const fd = new FormData();
      fd.append("image", this.state.fileSelected, this.state.fileSelected.name);

      this.setState({
        isLoading: true,
      });

      axios.post("http://127.0.0.1:7070/upload/", fd).then((res) => {
        this.setState({
          images: res.data.result,
          isLoading: false,
        });
      });
    };

    const fileSelectHandler = (event) => {
      this.setState({
        fileSelected: event.target.files[0],
      });
    };

    const newData = this.state.images.map((data, index) => (
      <div className="col m-3 pb-3" key={index}>
        <img
          className="result-image mx-auto img-thumbnail"
          alt=""
          src={window.location.origin + "/images/" + data.image}
        ></img>
      </div>
    ));

    return this.state.isLoading ? (
      <div className="row loading-view">
        <p>Loading...</p>
      </div>
    ) : (
      <div>
        <div className="row">
          <div className="col">
            <div className="row m-3 mx-auto pb-3">
              <img
                className="result-image mx-auto img-thumbnail"
                alt=""
                src={
                  this.state.fileSelected
                    ? window.location.origin +
                      "/images/" +
                      this.state.fileSelected.name
                    : window.location.origin + "/images/generic.png"
                }
              />
            </div>
            <div className="row mx-auto m-3 pb-3">
              <div className="col">
                <input
                  type="file"
                  class="form-control"
                  onChange={fileSelectHandler}
                />
              </div>
            </div>
            <div className="row m-3 mx-auto pb-3">
              <div className="col">
                <button
                  class="btn btn-primary mx-auto btn-block"
                  onClick={fileUploadHandler}
                >
                  upload
                </button>
              </div>
            </div>
          </div>
        </div>
        <div className="row">{newData}</div>
      </div>
    );
  }
}

export default FileInput;

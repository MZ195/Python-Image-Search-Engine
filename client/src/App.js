import "./App.css";
import FileInput from "./FileInput";

import "antd/dist/antd.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { Container } from "react-bootstrap";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Container fluid className="content">
          <div className="row">
            <div className="col">
              <FileInput />
            </div>
          </div>
        </Container>
      </header>
    </div>
  );
}

export default App;

import "./App.css";
import FileInput from "./FileInput";
import NavBar from "./NavBar";

import "bootstrap/dist/css/bootstrap.min.css";
import { Container } from "react-bootstrap";

function App() {
  return (
    <div className="App">
      <NavBar />
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

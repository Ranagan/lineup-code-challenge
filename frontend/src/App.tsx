import "./App.css";
import {
  BrowserRouter as Router,
  Route,
  Routes,
  useParams,
} from "react-router-dom";
import UserDetails from "./User";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/:userID" element={<User></User>}></Route>
      </Routes>
    </Router>
  );
}

function User() {
  let { userID } = useParams();
  console.log(userID);

  const userDetails = UserDetails(parseInt(userID!));

  return <div>{userDetails}</div>;
}

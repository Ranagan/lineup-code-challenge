import { useEffect, useState } from "react";
import { UserData } from "./interfaces/User";
import { getUserDetails } from "./services/userAPI";

const UserDetails = (userID: number) => {
  const [userDetails, setUserDetails] = useState<UserData | null>(null);

  const loadUser = async () => {
    // Fetch the user details for the given userID
    const user = await getUserDetails(userID);
    setUserDetails(user);
    console.log(user);
  };

  useEffect(() => {
    loadUser();
  }, []);

  return (
    <div>
      <h1>User</h1>
      {userDetails ? (
        <table>
          <tr>
            <th>ID</th>
            <th>Email</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>avatar</th>
          </tr>
          <tr>
            <td>{userDetails.id}</td>
            <td>{userDetails.email}</td>
            <td>{userDetails.first_name}</td>
            <td>{userDetails.last_name}</td>
            <td>{userDetails.avatar}</td>
          </tr>
        </table>
      ) : (
        <></>
      )}
    </div>
  );
};

export default UserDetails;

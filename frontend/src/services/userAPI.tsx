const rootUrl = 'http://localhost:8000/user/'

export const getUserDetails = (id: number) => {
    return fetch(`${rootUrl}${id}`)
    .then(res => res.json()).
    catch(error => {
        console.error('Failed to fetch user: ', console.error);
    });
};
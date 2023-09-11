import { get, post, put } from "../utils/request";

export const getEvents = async(id) => {
    const route = "/allevents/";
    return await get(route);
}


export const createEvent = (data) => {
    const route = "/events/";
    return post(route, data);
}

export const getEvent = (id) => {
    const route = `/event/${id}/`;
    return get(route);
}

export const editEvent = (id, data) => {
    const route = `/event/${id}/`;
    return put(route, data);

}
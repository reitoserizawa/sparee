import { useEffect } from 'react';

import { useAppDispatch, useAppSelector } from '../store/hooks';
import { selectLocation } from '../store/features/user/userSelector';
import { setLocation } from '../store/features/user/userSlice';

const useUserLocation = () => {
    const { lng, lat } = useAppSelector(selectLocation);
    const dispatch = useAppDispatch();

    useEffect(() => {
        if (lng || lat) return;
        if (!navigator.geolocation) return;

        navigator.geolocation.getCurrentPosition(
            position => {
                const { latitude, longitude } = position.coords;
                dispatch(setLocation({ lat: latitude, lng: longitude }));
            },
            error => {
                console.error('Error get user location: ', error);
            },
        );
    }, [lng, lat, dispatch]);
};

export default useUserLocation;
